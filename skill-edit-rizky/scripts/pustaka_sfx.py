"""Pustaka SFX Edit Rizky: folder `sfx/` per kategori + `katalog.json` (sejak 28 Nov 2026).

Sumber utama SFX untuk semua video skill ini. `jalankan.py rakit` memakainya OTOMATIS (tanpa --sfx):
bunyi bawaan mesin (whoosh, swish, kertas, stempel, gulir, ...) diganti berkas pustaka lewat `peta`, dan
nama pustaka (mis. 'hit-bersih') atau judul Epidemic aslinya bisa ditulis langsung di konfig.

Letak pustaka (yang pertama ada): --pustaka-sfx DIR · env EDIT_RIZKY_SFX · D:\\automation\\Skill-Video-Editing-Rizky\\sfx
· <skill>/sfx (salinan terpasang) · <repo>/sfx.

Pakai:
  python -X utf8 scripts/pustaka_sfx.py lihat [kata]            daftar SFX (saring nama/kategori/kegunaan)
  python -X utf8 scripts/pustaka_sfx.py cek                     katalog vs berkas, peta, keras
  python -X utf8 scripts/pustaka_sfx.py tambah <berkas.mp3> --kategori transisi --nama whoosh-baru --kapan "…"
          [--judul "judul Epidemic"] [--loop] [--target -14] [--potong 0 2.5] [--peta whoosh|masuk.sapu]
      SFX baru (mis. unduhan Epidemic karena belum ada yang cocok): dipotong hening, disamakan keras per kategori
      (puncak ≤ −1 dBFS), disimpan ke <pustaka>/<kategori>/<nama>.mp3 dan dicatat di katalog.json.
Kategori: transisi · muncul · kertas · ui · angka · tekanan · latar.
"""
import argparse, json, os, re, subprocess, sys
from pathlib import Path

AKAR_SKILL = Path(__file__).resolve().parent.parent
KATEGORI = {'transisi': -14, 'muncul': -16, 'kertas': -16, 'ui': -17, 'angka': -16, 'tekanan': -9, 'latar': -20}
AUDIO = ('.mp3', '.wav', '.ogg', '.m4a')
SR = 48000


def cari_pustaka(arg=None):
    calon = [arg, os.environ.get('EDIT_RIZKY_SFX'), r'D:\automation\Skill-Video-Editing-Rizky\sfx', AKAR_SKILL / 'sfx', AKAR_SKILL.parent / 'sfx']
    for c in calon:
        if c and (Path(c) / 'katalog.json').exists():
            return Path(c)
    return None


def muat(pustaka):
    return json.loads((Path(pustaka) / 'katalog.json').read_text(encoding='utf-8'))


def nama_peta(v):
    return v['berkas'] if isinstance(v, dict) else v


def untuk_rakit(konfig, pustaka, tambahan=(), data_uri=None):
    """→ dict untuk data-suara: sfxBerkas (hanya yang dipakai), sfxInfo, sfxPetaBawaan, bunyiMunculBawaan."""
    berkas, info, alias, peta, bm, cocok = {}, {}, {}, {}, {}, {}
    if pustaka:
        kat = muat(pustaka)
        for n, e in kat['sfx'].items():
            f = Path(pustaka) / e['berkas']
            if f.exists():
                berkas[n] = f; info[n] = {'puncak': e['puncak'], 'durasi': e['durasi']}; alias[e['judul']] = n
        peta = {k: v for k, v in kat['peta'].items() if nama_peta(v) in berkas}
        bm = {k: v for k, v in kat['bunyiMuncul'].items() if k == 'vol' or v in berkas}
        cocok = {k: v for k, v in kat.get('muncul', {}).items() if not k.startswith('_') and nama_peta(v) in berkas}
    proyek = {}
    for d in tambahan or []:
        for f in sorted(Path(d).rglob('*')):
            if f.suffix.lower() in AUDIO:
                proyek[f.stem] = f
    dipakai = {nama_peta(v) for v in peta.values()}
    if not re.search(r'sfxPeta\s*:\s*false', konfig) and re.search(r'bunyiMuncul\s*:\s*true', konfig):
        dipakai |= {v for k, v in bm.items() if k != 'vol'}
    if re.search(r'sfxPeta\s*:\s*false', konfig):
        dipakai = set()
    if not re.search(r'bunyiMuncul\s*:\s*false', konfig):
        dipakai |= {nama_peta(v) for v in cocok.values()}
    else:
        cocok = {}
    teks = set(re.findall(r"'([^'\n]{2,120})'", konfig)) | set(re.findall(r'"([^"\n]{2,120})"', konfig))
    keluar, inf = {}, {}
    for s in teks:
        if s in proyek:
            continue
        if s in berkas:
            dipakai.add(s)
        elif s in alias:  # judul Epidemic lama ditulis di konfig → ditanam dengan judul itu
            keluar[s] = data_uri(berkas[alias[s]]); inf[s] = info[alias[s]]
    for n in sorted(dipakai):
        keluar[n] = data_uri(berkas[n]); inf[n] = info[n]
    for n, f in proyek.items():  # berkas proyek (--sfx DIR) selalu ditanam dan menang atas pustaka
        keluar[n] = data_uri(f); inf.pop(n, None)
    return {'sfxBerkas': keluar, 'sfxInfo': inf, 'sfxPetaBawaan': peta, 'bunyiMunculBawaan': bm, 'bunyiMunculCocok': cocok}


# ---------------------------------------------------------------- olah audio (sama dengan perapian 28 Nov 2026)
def _ff():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return 'ffmpeg'


def _baca(p):
    import numpy as np
    r = subprocess.run([_ff(), '-v', 'error', '-i', str(p), '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32).reshape(-1, 2).copy()


def _tulis(x, p):
    import numpy as np
    p.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([_ff(), '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', '-c:a', 'libmp3lame', '-q:a', '2', str(p)],
                   input=np.ascontiguousarray(x, np.float32).tobytes(), check=True)


def _env(x, win):
    import numpy as np
    win = max(1, min(win, len(x))); m = len(x) // win; mono = x[:m * win].mean(1)
    return 20 * np.log10(np.sqrt((mono.reshape(m, win) ** 2).mean(1)) + 1e-9)


def olah(x, target, loop=False, potong=None):
    import numpy as np
    if potong:
        x = x[int(potong[0] * SR):int(potong[1] * SR)]
    if not loop:
        w5 = int(.005 * SR); e = _env(x, w5); mx = e.max()
        aktif = np.where(e > mx - 40)[0]; a = max(0, aktif[0] * w5 - int(.006 * SR))
        ekor = np.where(e > mx - 50)[0]; b = min(len(x), (ekor[-1] + 1) * w5 + int(.03 * SR))
        x = x[a:b]
        n = min(len(x) // 4, int(.03 * SR))
        if n > 0: x[-n:] *= np.linspace(1, 0, n)[:, None]
        n2 = min(len(x) // 8, int(.004 * SR))
        if a > 0 and n2 > 0: x[:n2] *= np.linspace(0, 1, n2)[:, None]
    elif potong:
        n = int(.3 * SR); x[-n:] *= np.linspace(1, 0, n)[:, None]
    g = 10 ** ((target - _env(x, int(.05 * SR)).max()) / 20)
    pk = np.abs(x).max() * g
    if pk > 10 ** (-1 / 20): g *= 10 ** (-1 / 20) / pk
    return x * g


def ukur(x):
    import numpy as np
    e = _env(x, int(.01 * SR)); i = int(e.argmax())
    return {'durasi': round(len(x) / SR, 2), 'puncak': round(i * .01 + .005, 2), 'puncakDb': round(float(20 * np.log10(np.abs(x).max() + 1e-9)), 1),
            'rmsMaks': round(float(_env(x, int(.05 * SR)).max()), 1)}


# ---------------------------------------------------------------- perintah
def lihat(a):
    p = cari_pustaka(a.pustaka_sfx) or sys.exit('pustaka SFX tidak ditemukan')
    kat = muat(p); kata = (a.kata or '').lower()
    peran = {}
    for k, v in kat['peta'].items(): peran.setdefault(nama_peta(v), []).append(k)
    for k, v in kat['bunyiMuncul'].items():
        if k != 'vol': peran.setdefault(v, []).append('muncul.' + k)
    print(f'pustaka: {p}')
    for n, e in kat['sfx'].items():
        baris = f"{e['kategori']:8} {n:18} {e['durasi']:5.2f} dtk  {e['kapan']}" + (f"  [bawaan: {', '.join(peran[n])}]" if n in peran else '')
        if not kata or kata in baris.lower() or kata in e['judul'].lower():
            print(baris)


def cek(a):
    p = cari_pustaka(a.pustaka_sfx) or sys.exit('pustaka SFX tidak ditemukan')
    kat = muat(p); salah = []
    ada = {f.relative_to(p).as_posix() for f in p.rglob('*') if f.suffix.lower() in AUDIO}
    tercatat = {e['berkas'] for e in kat['sfx'].values()}
    salah += [f'berkas tidak ada: {b}' for b in sorted(tercatat - ada)]
    salah += [f'berkas belum dicatat (pakai tambah): {b}' for b in sorted(ada - tercatat)]
    for k, v in list(kat['peta'].items()) + [(k, v) for k, v in kat['bunyiMuncul'].items() if k != 'vol'] + [(k, v) for k, v in kat.get('muncul', {}).items() if not k.startswith('_')]:
        if nama_peta(v) not in kat['sfx']: salah.append(f'peta {k} → {nama_peta(v)} tidak ada di katalog')
    for n, e in kat['sfx'].items():
        if e['puncakDb'] > -0.5: salah.append(f'{n}: puncak {e["puncakDb"]} dBFS (maks −1)')
    print(f'pustaka: {p} · {len(kat["sfx"])} SFX · {len(kat["peta"])} peta bawaan')
    print('\n'.join(salah) if salah else 'BERES')
    sys.exit(1 if salah else 0)


def tambah(a):
    p = cari_pustaka(a.pustaka_sfx) or sys.exit('pustaka SFX tidak ditemukan')
    if a.kategori not in KATEGORI: sys.exit(f'kategori: {", ".join(KATEGORI)}')
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', a.nama): sys.exit('nama: huruf kecil + tanda hubung, mis. whoosh-kain')
    kat = muat(p)
    if a.nama in kat['sfx'] and not a.timpa: sys.exit(f'{a.nama} sudah ada (pakai --timpa untuk mengganti)')
    x = olah(_baca(a.berkas), a.target if a.target is not None else KATEGORI[a.kategori], a.loop, a.potong)
    out = p / a.kategori / f'{a.nama}.mp3'; _tulis(x, out); h = ukur(_baca(out))
    judul = a.judul or re.sub(r'^ES_|\s*-\s*Epidemic Sound$', '', Path(a.berkas).stem)
    kat['sfx'][a.nama] = dict(kategori=a.kategori, berkas=f'{a.kategori}/{a.nama}.mp3', judul=judul, kapan=a.kapan, **h,
                              **({'ulang': True} if a.loop else {}), sumber=a.sumber)
    kat['sfx'] = dict(sorted(kat['sfx'].items(), key=lambda kv: (kv[1]['kategori'], kv[0])))
    for k in a.peta or []:
        kat['peta'][k] = {'berkas': a.nama, 'ulang': True} if a.loop else a.nama
    (p / 'katalog.json').write_text(json.dumps(kat, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f"ok {out} · {h['durasi']} dtk · puncak@{h['puncak']} · {h['puncakDb']} dBFS" + (f" · bawaan untuk {', '.join(a.peta)}" if a.peta else ''))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pustaka-sfx')
    sub = ap.add_subparsers(dest='perintah', required=True)
    q = sub.add_parser('lihat'); q.add_argument('kata', nargs='?'); q.set_defaults(f=lihat)
    q = sub.add_parser('cek'); q.set_defaults(f=cek)
    q = sub.add_parser('tambah'); q.add_argument('berkas'); q.add_argument('--kategori', required=True); q.add_argument('--nama', required=True)
    q.add_argument('--kapan', required=True); q.add_argument('--judul'); q.add_argument('--loop', action='store_true'); q.add_argument('--target', type=float)
    q.add_argument('--potong', type=float, nargs=2); q.add_argument('--peta', action='append'); q.add_argument('--timpa', action='store_true')
    q.add_argument('--sumber', default='Epidemic Sound'); q.set_defaults(f=tambah)
    a = ap.parse_args(); a.f(a)


if __name__ == '__main__':
    main()
