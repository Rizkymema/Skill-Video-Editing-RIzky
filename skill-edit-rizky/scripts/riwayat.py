"""Riwayat pilihan visual skill-edit-rizky supaya tiap video beda (gaya.md §0.4).

  python -X utf8 riwayat.py lihat [--n 5] [--akar "D:\\automation\\Video AI\\Hasil Video"]
      Tampilkan pilihan N video terakhir + daftar "hindari" untuk video berikutnya.
  python -X utf8 riwayat.py catat <_kerja>
      Baca _kerja/konfig.js (+ naskah.txt) lalu simpan/perbarui satu baris riwayat (kunci = judul).

Riwayat: Hasil Video/_seri/edit-rizky/riwayat.json (data tetap, tidak di-commit, jangan dibuang).
Di naskah.txt boleh ada baris `# pola: misteri` (pola cerita, gaya.md §0.2).
"""
import argparse, json, os, re, sys
from collections import Counter
from datetime import date

GAYA_TEKS = {'judul', 'padat', 'tahun', 'kutip', 'mesin', 'stiker', 'label', 'tangan', 'gelap', 'elegan'}
BENDA = {'koran', 'dokumen', 'kartu', 'papan', 'label', 'cap', 'grafik', 'tv'}
TANDA = {'bingkai', 'kartu', 'iris', 'jatuh', 'strip', 'lempar', 'putar', 'kilat'}


def cari_akar(mulai):
    p = os.path.abspath(mulai)
    while True:
        if os.path.basename(p).lower() == 'hasil video':
            return p
        q = os.path.dirname(p)
        if q == p:
            return None
        p = q


def akar_bawaan():
    for k in [os.getcwd(), os.path.dirname(os.path.abspath(__file__))]:
        a = cari_akar(k)
        if a:
            return a
    for k in [r'D:\automation\Video AI\Hasil Video', os.path.join(os.getcwd(), 'Hasil Video')]:
        if os.path.isdir(k):
            return k
    return os.path.join(os.getcwd(), 'Hasil Video')


def berkas(akar):
    d = os.path.join(akar, '_seri', 'edit-rizky')
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, 'riwayat.json')


def muat(akar):
    f = berkas(akar)
    if os.path.exists(f):
        with open(f, encoding='utf-8') as h:
            return json.load(h)
    return []


def baca_konfig(kerja):
    with open(os.path.join(kerja, 'konfig.js'), encoding='utf-8') as h:
        s = h.read()
    g = lambda pola, bawaan=None: (re.search(pola, s).group(1) if re.search(pola, s) else bawaan)
    adegan = re.findall(r"\{\s*id:\s*'([\w-]+)',\s*((?:mulai|akhir|durasi|masuk|latar|kamera)\b[^\n]*)", s)
    urut = []
    for i, (aid, sisa) in enumerate(adegan):
        m = re.search(r"\bmasuk:\s*'(\w+)'", sisa)
        urut.append((aid, m.group(1) if m else ('-' if i == 0 else 'potong')))
    trans = [m for _, m in urut[1:]]
    benda = Counter(x for x in re.findall(r"jenis:\s*'(\w+)'", s) if x in BENDA)
    gaya = sorted({x for x in re.findall(r"gaya:\s*'(\w+)'", s) if x in GAYA_TEKS})
    latar = sorted(set(re.findall(r"pola:\s*'(\w+)'", s)))
    kamera = Counter(re.findall(r"kamera:\s*'([\w-]+)'", s))
    pola, hook = None, None
    nsk = os.path.join(kerja, 'naskah.txt')
    if os.path.exists(nsk):
        with open(nsk, encoding='utf-8') as h:
            for b in h:
                if b.lower().startswith('# pola:') and not pola:
                    pola = re.split(r'[\s(]', b.split(':', 1)[1].strip())[0]
                m = re.match(r'L0*1\s*\|\s*(.+)', b)
                if m and not hook:
                    hook = m.group(1).strip()
    return {
        'judul': g(r"judul:\s*'([^']*)'", os.path.basename(os.path.dirname(os.path.abspath(kerja)))),
        'tanggal': date.today().isoformat(),
        'folder': os.path.dirname(os.path.abspath(kerja)),
        'tema': g(r"\btema:\s*'(\w+)'", 'arsip'),
        'grade': g(r"\bgrade:\s*'(\w+)'"),
        'musik': g(r"sintesis:\s*'(\w+)'"),
        'pola_cerita': pola or 'balik',
        'hook': hook,
        'pembuka': trans[0] if trans else None,
        'penutup': trans[-1] if trans else None,
        'transisi': trans,
        'tanda_tangan': sorted({t for t in trans if t in TANDA}),
        'benda': [k for k, _ in benda.most_common()],
        'gaya_teks': gaya,
        'latar': latar,
        'kamera': [k for k, _ in kamera.most_common(4)],
        'adegan': len(urut),
    }


def lihat(akar, n):
    r = muat(akar)
    if not r:
        print('Belum ada riwayat (video pertama: bebas memilih, tetap sesuaikan topik).')
        return
    akhir = r[-n:]
    print(f'Riwayat {len(r)} video, {len(akhir)} terakhir:')
    for v in akhir:
        print(f"- {v['tanggal']} · {v['judul']} · tema {v['tema']} · pola {v['pola_cerita']} · musik {v.get('musik')}")
        print(f"    pembuka {v['pembuka']} · penutup {v['penutup']} · tanda tangan {', '.join(v['tanda_tangan']) or '-'} · benda {', '.join(v['benda'][:4]) or '-'}")
        if v.get('hook'):
            print(f"    hook: {v['hook']}")
    t, d2 = akhir[-1], akhir[-2:]
    hit = Counter(x for v in akhir[-3:] for x in v['transisi'])
    print('\nHINDARI di video berikutnya (kecuali topik benar-benar menuntut, lalu ubah aksen/pola lain):')
    print(f"- tema sama dengan video terakhir: {t['tema']}")
    print(f"- pola cerita video terakhir: {t['pola_cerita']}")
    print(f"- perpindahan pembuka: {', '.join(sorted({v['pembuka'] for v in d2 if v['pembuka']}))}")
    print(f"- perpindahan penutup: {', '.join(sorted({v['penutup'] for v in d2 if v['penutup']}))}")
    print(f"- transisi tanda tangan: {', '.join(sorted({x for v in d2 for x in v['tanda_tangan']})) or '-'}")
    print(f"- paling sering (3 video): {', '.join(f'{k} ×{c}' for k, c in hit.most_common(3))} → kurangi")
    if t.get('hook'):
        print(f"- bentuk hook yang sama dengan: \"{' '.join(t['hook'].split()[:4])} …\"")
    print(f"- musik {t.get('musik')} (benih otomatis dari judul sudah membedakan melodi; ganti jenis bila tema sama)")


def catat(kerja, akar):
    v = baca_konfig(kerja)
    r = [x for x in muat(akar) if x['judul'] != v['judul']] + [v]
    with open(berkas(akar), 'w', encoding='utf-8') as h:
        json.dump(r, h, ensure_ascii=False, indent=1)
    print(f"tercatat: {v['judul']} · tema {v['tema']} · pola {v['pola_cerita']} · {v['adegan']} adegan · {len(set(v['transisi']))} jenis perpindahan")
    print(berkas(akar))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('lihat'); a.add_argument('--n', type=int, default=5); a.add_argument('--akar')
    b = sub.add_parser('catat'); b.add_argument('kerja'); b.add_argument('--akar')
    x = ap.parse_args()
    if x.cmd == 'lihat':
        lihat(x.akar or akar_bawaan(), x.n)
    else:
        if not os.path.exists(os.path.join(x.kerja, 'konfig.js')):
            sys.exit(f'konfig.js tidak ada di {x.kerja}')
        catat(x.kerja, x.akar or cari_akar(x.kerja) or akar_bawaan())


if __name__ == '__main__':
    main()
