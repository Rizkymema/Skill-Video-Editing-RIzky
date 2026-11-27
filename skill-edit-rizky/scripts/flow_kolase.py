#!/usr/bin/env python3
"""Aset gambar Google Flow untuk skill skill-edit-rizky: aset.json -> prompt bergaya arsip -> (Claude memanggil Flow) -> gambar/ siap tanam.

Prinsip (bedah @earn.edits, 18 Nov 2026): video = gambar diam realistis bernuansa arsip yang DIPOTONG JADI LAPISAN,
lalu digerakkan mesin. Jadi ada dua jenis aset:
  pelat    = latar penuh (ruangan, jalan, langit, hangar …) dengan ruang kosong di sepertiga atas untuk judul
  potongan = satu subjek/benda di latar HIJAU polos (#00FF00) -> dibuang otomatis jadi PNG transparan (potong_latar.py)
Teks (koran, dokumen, angka, label) TIDAK digambar Flow: ditulis mesin supaya datanya benar. Prompt selalu melarang teks.

Pakai (folder proyek = ..._kerja):
  python -X utf8 -I flow_kolase.py rencana <_kerja> [--hanya kode1,kode2]
      baca _kerja/aset.json, tulis _kerja/flow_batch.json (argumen siap pakai flow_agent_images: project, aspect_ratio,
      scenes, references, scene_references) + _kerja/prompt_flow.md. Claude lalu memanggil flow_agent_images persis
      dengan argumen itu (maks 50 adegan per panggilan; 0 kredit) dan flow_wait sampai selesai.
  python -X utf8 -I flow_kolase.py ambil <_kerja> [--proyek <folder Flow, mis. kolase-n250-2k>] [--flow C:\\Users\\ASUS\\flow-mcp-out] [--toleransi 1.0]
      salin scene-NN / clip-NN (unduhan 2K) dari folder Flow ke _kerja/gambar/<kode>.jpg (pelat) atau _kerja/gambar/potong/<kode>.jpg (potongan),
      buang latar hijau -> _kerja/gambar/<kode>.png, lalu _kerja/gambar/_kontak.jpg (lembar periksa semua aset).

Klip gerak (opsional, BERBAYAR kredit Flow; hanya di momen yang memang butuh gerak, references/klip.md):
  python -X utf8 -I flow_kolase.py klip <_kerja> [--hanya kode]      aset.json["klip"] -> flow_klip.json + perkiraan kredit
      Claude MENANYAKAN kreditnya dulu (dialog persetujuan Tahap 2), lalu memanggil flow_generate dengan project/scenes
      dari berkas itu dan flow_wait.
  python -X utf8 -I flow_kolase.py ambil-klip <_kerja> [--flow DIR]   scene-NN.mp4 -> _kerja/klip/<kode>.mp4 + _cek-<kode>.jpg
      + argumen rakit --klip siap salin (":hijau" untuk klip dari potongan berlatar hijau = potongan bergerak).
  "klip": [{"kode": "nelayan-hidup", "dari": "nelayan", "gerak": "the fisherman slowly lifts the heavy net, water drips",
            "kamera": "slow push-in", "lama": 4, "model": "Omni 1.1 Flash", "fps": 15}]
      dari  = kode aset yang sudah dibuat (pelat -> klip penuh / foto hidup; potongan -> klip berlatar hijau)
      lama  = 4/6/8/10 dtk (Omni); Veo selalu 8 dtk. Kredit: Omni 4 dtk ±7, 8 dtk ±12; Veo Lite 10, Fast 20.

aset.json:
{
  "proyek": "kolase-n250",              # nama folder hasil Flow (flow-mcp-out/<proyek>); unik per video
  "rasio": "9:16",
  "era": "1990s Indonesia",             # zaman + tempat cerita: masuk ke setiap prompt
  "gaya": "arsip",                      # arsip (foto film 35 mm pudar) | modern (foto dokumenter kini) | gelap (malam, dramatis) | studio3d (render 3D krom, kaca-gradien)
  "acuan": {"pesawat": "C:/.../n250.png"},   # opsional: gambar acuan (tokoh/benda yang harus sama di beberapa aset)
  "aset": [
    {"kode": "hangar", "jenis": "pelat", "isi": "inside a bright aircraft assembly hangar, a white turboprop airliner ..."},
    {"kode": "pesawat", "jenis": "potongan", "isi": "side view of a white twin-engine turboprop airliner in flight", "acuan": ["pesawat"]},
    {"kode": "awan", "jenis": "potongan", "isi": "one big fluffy white cumulus cloud", "gaya": "modern"}
  ]
}
Orang nyata (tokoh terkenal) jangan dibuat wajahnya dengan Flow: pakai foto berlisensi (Wikimedia Commons / domain publik)
atau tampilkan dari belakang/siluet. Butuh: Pillow, numpy (potong_latar.py di folder yang sama).
"""
import glob, json, os, shutil, subprocess, sys

from PIL import Image, ImageDraw

SINI = os.path.dirname(os.path.abspath(__file__))
GAYA = {
    'arsip': 'Authentic {era} documentary photograph shot on 35mm film, warm faded colors, soft film grain, natural light, realistic',
    'modern': 'Contemporary documentary photograph, natural colors, realistic, sharp',
    'gelap': 'Dramatic {era} documentary photograph at night, low-key lighting, deep shadows, film grain, realistic',
    'studio3d': 'Premium 3D product render, soft diffused studio lighting, glossy and chrome materials with subtle iridescent highlights, clean, high detail',  # gaya kaca-gradien / benda 3D (28 Nov 2026)
}
LARANG = 'no text, no letters, no numbers, no logos, no signage, no watermark'
PELAT = 'Vertical {rasio} photo: {isi}. {gaya}, generous empty space in the upper third of the frame, {larang}.'
POTONG = ('{isi}, the whole subject visible with a generous margin, isolated on a perfectly flat pure green background (#00FF00), '
          'no shadow on the background, no floor, {gaya}, {larang}.')


def prompt(a, cfg):
    gaya = GAYA.get(a.get('gaya') or cfg.get('gaya', 'arsip'), GAYA['arsip']).format(era=cfg.get('era', '1990s'))
    if a['jenis'] == 'pelat':
        return PELAT.format(rasio=cfg.get('rasio', '9:16'), isi=a['isi'].rstrip('.'), gaya=gaya, larang=LARANG)
    return POTONG.format(isi=a['isi'].rstrip('.')[0].upper() + a['isi'].rstrip('.')[1:], gaya=gaya, larang=LARANG)


def rencana(folder, hanya=None):
    cfg = json.load(open(os.path.join(folder, 'aset.json'), encoding='utf-8'))
    aset = [a for a in cfg['aset'] if not hanya or a['kode'] in hanya]
    acuan = cfg.get('acuan', {})
    batch = {'project': cfg.get('proyek', 'kolase') + ('-ulang-' + '-'.join(hanya)[:30] if hanya else ''),
             'aspect_ratio': cfg.get('rasio', '9:16'), 'scenes': [prompt(a, cfg) for a in aset], 'kode': [a['kode'] for a in aset]}
    if acuan:
        batch['references'] = [{'image': os.path.abspath(v), 'name': k} for k, v in acuan.items()]
        batch['scene_references'] = [a.get('acuan', []) for a in aset]
    json.dump(batch, open(os.path.join(folder, 'flow_batch.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(folder, 'prompt_flow.md'), 'w', encoding='utf-8') as f:
        f.write(f"# Prompt Flow · {batch['project']} · {batch['aspect_ratio']}\n\n")
        for i, (a, p) in enumerate(zip(aset, batch['scenes']), 1):
            f.write(f"{i:02d}. **{a['kode']}** ({a['jenis']})\n    {p}\n\n")
    print(f"ok {len(aset)} aset -> flow_batch.json (panggil flow_agent_images dengan project/aspect_ratio/scenes"
          f"{'/references/scene_references' if acuan else ''} dari berkas itu)")


def ambil(folder, root, tol, proyek=None):
    cfg = json.load(open(os.path.join(folder, 'aset.json'), encoding='utf-8'))
    batch = json.load(open(os.path.join(folder, 'flow_batch.json'), encoding='utf-8'))
    src = os.path.join(root, proyek or batch['project'])
    gb = os.path.join(folder, 'gambar'); pt = os.path.join(gb, 'potong')
    os.makedirs(pt, exist_ok=True)
    jenis = {a['kode']: a['jenis'] for a in cfg['aset']}
    hilang, potongan = [], []
    for i, kode in enumerate(batch['kode'], 1):
        cocok = sorted(glob.glob(os.path.join(src, f'scene-{i:02d}.*')) + glob.glob(os.path.join(src, f'clip-{i:02d}.*'))
                       + glob.glob(os.path.join(src, f'*-scene-{i:02d}.*')))
        if not cocok:
            hilang.append(kode); continue
        if jenis.get(kode) == 'pelat':
            Image.open(cocok[-1]).convert('RGB').save(os.path.join(gb, kode + '.jpg'), quality=92)
        else:
            tujuan = os.path.join(pt, kode + '.jpg'); Image.open(cocok[-1]).convert('RGB').save(tujuan, quality=95); potongan.append(tujuan)
    if potongan:
        subprocess.run([sys.executable, '-X', 'utf8', '-I', os.path.join(SINI, 'potong_latar.py'), *potongan, '--toleransi', str(tol), '--cek'], check=False)
        if os.path.exists(os.path.join(gb, 'potong_cek.jpg')):   # lembar periksa jangan ikut ditanam sebagai gambar
            shutil.move(os.path.join(gb, 'potong_cek.jpg'), os.path.join(pt, 'potong_cek.jpg'))
    # lembar kontak semua aset (potongan di atas kotak-kotak)
    berkas = sorted(f for f in os.listdir(gb) if f.lower().endswith(('.jpg', '.png')) and not f.startswith('_'))
    if berkas:
        tw, th = 220, 390; kol = 6; bar = (len(berkas) + kol - 1) // kol
        L = Image.new('RGB', (kol * tw, bar * (th + 26)), (30, 30, 30)); d = ImageDraw.Draw(L)
        kotak = Image.new('RGB', (tw, th), (200, 200, 200)); kd = ImageDraw.Draw(kotak)
        for y in range(0, th, 20):
            for x in range(0, tw, 20):
                if (x // 20 + y // 20) % 2: kd.rectangle([x, y, x + 19, y + 19], fill=(160, 160, 160))
        for i, f in enumerate(berkas):
            im = Image.open(os.path.join(gb, f)).convert('RGBA'); im.thumbnail((tw, th))
            sel = kotak.copy().convert('RGBA'); sel.alpha_composite(im, ((tw - im.width) // 2, (th - im.height) // 2))
            L.paste(sel.convert('RGB'), ((i % kol) * tw, (i // kol) * (th + 26) + 26)); d.text(((i % kol) * tw + 6, (i // kol) * (th + 26) + 6), f, fill=(255, 220, 80))
        L.save(os.path.join(gb, '_kontak.jpg'), quality=85)
    print(f'ok {len(batch["kode"]) - len(hilang)} aset -> {gb}' + (f'; BELUM ADA: {", ".join(hilang)} (flow_retry atau rencana --hanya)' if hilang else ''))
    print('periksa', os.path.join(gb, '_kontak.jpg'), '+ gambar/potong/potong_cek.jpg')


# ---------------------------------------------------------------- klip gerak Flow (berbayar; references/klip.md)
KREDIT = {'Omni 1.1 Flash': {4: 7, 6: 10, 8: 12, 10: 15}, 'Veo 3.1 - Lite': 10, 'Veo 3.1 - Fast': 20, 'Veo 3.1 - Quality': 100}
KLIP = ('{gerak}. {kamera}. Continue exactly from the first frame: same place, same people, same objects, same light and colors; '
        'one continuous shot, natural realistic motion, documentary footage, no new objects appear, no text, no subtitles, no logos.')
KLIP_HIJAU = (' The subject stays isolated on the perfectly flat pure green (#00FF00) background for the whole clip: the background never '
              'changes, no shadows, no floor, the whole subject stays inside the frame, camera locked off.')


def kredit_klip(k):
    m = k.get('model', 'Omni 1.1 Flash'); v = KREDIT.get(m, 20)
    return v.get(int(k.get('lama', 4)), 12) if isinstance(v, dict) else v


def rencana_klip(folder, hanya=None):
    """aset.json["klip"] -> flow_klip.json (argumen siap pakai flow_generate) + perkiraan kredit. Klip dibuat dari gambar
    yang sudah ada (pelat 2K atau potongan berlatar hijau) sebagai first_frame, jadi awal klip = gambar diam di video."""
    cfg = json.load(open(os.path.join(folder, 'aset.json'), encoding='utf-8'))
    klip = [k for k in cfg.get('klip', []) if not hanya or k['kode'] in hanya]
    if not klip:
        sys.exit('aset.json belum punya "klip": [...] (lihat references/klip.md)')
    jenis = {a['kode']: a['jenis'] for a in cfg['aset']}
    gb = os.path.join(folder, 'gambar')
    scenes, total, kurang = [], 0, []
    for k in klip:
        dari = k['dari']
        ff = os.path.join(gb, 'potong', dari + '.jpg') if jenis.get(dari) == 'potongan' or k.get('hijau') else os.path.join(gb, dari + '.jpg')
        if not os.path.exists(ff):
            kurang.append(f"{k['kode']}: {ff}")
        model = k.get('model', 'Omni 1.1 Flash')
        p = KLIP.format(gerak=k['gerak'].rstrip('.'), kamera=(k.get('kamera') or 'Static locked-off camera').rstrip('.'))
        if k.get('hijau') or jenis.get(dari) == 'potongan':
            p += KLIP_HIJAU
        s = {'prompt': p, 'first_frame': os.path.abspath(ff), 'aspect_ratio': cfg.get('rasio', '9:16'), 'model': model,
             'download_quality': 'upscaled', 'max_credits': kredit_klip(k) + 3}
        if model.startswith('Omni'):
            s['duration'] = int(k.get('lama', 4)); s['resolution'] = '720p'
        scenes.append(s); total += kredit_klip(k)
    batch = {'project': cfg.get('proyek', 'kolase') + '-klip' + ('-' + '-'.join(hanya)[:30] if hanya else ''), 'scenes': scenes,
             'kode': [k['kode'] for k in klip], 'hijau': [bool(k.get('hijau') or jenis.get(k['dari']) == 'potongan') for k in klip],
             'fps': [int(k.get('fps', 15)) for k in klip], 'kredit': total}
    json.dump(batch, open(os.path.join(folder, 'flow_klip.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for k, s in zip(klip, scenes):
        print(f"- {k['kode']}: {s['model']} {k.get('lama', 4) if s['model'].startswith('Omni') else 8} dtk ±{kredit_klip(k)} kredit · dari {k['dari']}")
    print(f"ok {len(klip)} klip -> flow_klip.json · perkiraan total ±{total} kredit (TANYA DULU sebelum flow_generate)")
    if kurang:
        print('PERINGATAN gambar awal belum ada: ' + '; '.join(kurang))


def ambil_klip(folder, root):
    """Hasil flow_generate (scene-NN*.mp4) -> _kerja/klip/<kode>.mp4 + lembar periksa 8 fps per klip (cari wajah/benda yang berubah)."""
    import imageio_ffmpeg, tempfile
    batch = json.load(open(os.path.join(folder, 'flow_klip.json'), encoding='utf-8'))
    src = os.path.join(root, batch['project']); tj = os.path.join(folder, 'klip'); os.makedirs(tj, exist_ok=True)
    ff = imageio_ffmpeg.get_ffmpeg_exe(); arg_rakit = []
    for i, (kode, hijau, fps) in enumerate(zip(batch['kode'], batch['hijau'], batch['fps']), 1):
        cocok = sorted(glob.glob(os.path.join(src, f'scene-{i:02d}*.mp4')) + glob.glob(os.path.join(src, f'*-scene-{i:02d}*.mp4')))
        if not cocok:
            print(f'BELUM ADA: {kode} (scene-{i:02d}.mp4 di {src})'); continue
        tujuan = os.path.join(tj, kode + '.mp4'); shutil.copyfile(cocok[-1], tujuan)
        with tempfile.TemporaryDirectory() as d:
            subprocess.run([ff, '-v', 'error', '-y', '-i', tujuan, '-vf', 'fps=8,scale=200:-2', os.path.join(d, 'b%03d.jpg')], check=True)
            bb = sorted(glob.glob(os.path.join(d, 'b*.jpg')))
            if bb:
                w, h = Image.open(bb[0]).size; kol = 8; bar = (len(bb) + kol - 1) // kol
                L = Image.new('RGB', (kol * w, bar * h), (0, 0, 0))
                for j, f in enumerate(bb):
                    L.paste(Image.open(f), ((j % kol) * w, (j // kol) * h))
                L.save(os.path.join(tj, f'_cek-{kode}.jpg'), quality=82)
        arg_rakit.append(f'--klip {kode}=klip/{kode}.mp4@{fps}' + (':hijau' if hijau else ''))
        print(f'ok {kode} -> klip/{kode}.mp4 · periksa klip/_cek-{kode}.jpg (8 bingkai/dtk)')
    if arg_rakit:
        print('rakit: ' + ' '.join(arg_rakit))


if __name__ == '__main__':
    if len(sys.argv) < 3 or sys.argv[1] not in ('rencana', 'ambil', 'klip', 'ambil-klip'):
        sys.exit(__doc__)
    f = sys.argv[2]
    if sys.argv[1] == 'klip':
        rencana_klip(f, sys.argv[sys.argv.index('--hanya') + 1].split(',') if '--hanya' in sys.argv else None)
    elif sys.argv[1] == 'ambil-klip':
        ambil_klip(f, sys.argv[sys.argv.index('--flow') + 1] if '--flow' in sys.argv else os.path.join(os.path.expanduser('~'), 'flow-mcp-out'))
    elif sys.argv[1] == 'rencana':
        rencana(f, sys.argv[sys.argv.index('--hanya') + 1].split(',') if '--hanya' in sys.argv else None)
    else:
        ambil(f, sys.argv[sys.argv.index('--flow') + 1] if '--flow' in sys.argv else os.path.join(os.path.expanduser('~'), 'flow-mcp-out'),
              float(sys.argv[sys.argv.index('--toleransi') + 1]) if '--toleransi' in sys.argv else 1.0,
              sys.argv[sys.argv.index('--proyek') + 1] if '--proyek' in sys.argv else None)
