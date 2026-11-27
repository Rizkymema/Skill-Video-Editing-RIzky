"""Identifikasi elemen yang bisa dihidupkan di dalam SATU gambar (Kolase 1.5, references/gerak-elemen.md).

Pakai:
  python -X utf8 -I scripts/elemen.py kisi  <gambar> [--keluar kisi.jpg]
      gambar + kisi koordinat 0–1 (garis tiap 0,05, label tiap 0,1) → baca wilayah elemen dengan tepat saat MELIHAT gambarnya
  python -X utf8 -I scripts/elemen.py saran <gambar> [--keluar saran.json]
      deteksi otomatis sederhana: titik cahaya/jendela menyala (→ kedip/terang), pita langit (→ arus awan),
      bagian terpisah di PNG transparan (→ elemen sendiri). Hasil = usulan; tetap dilihat dan dipilih manual.
      Juga menulis <gambar>_saran.jpg (kotak bernomor).
  python -X utf8 -I scripts/elemen.py uji   <gambar> <elemen.json> [--keluar uji.jpg]
      gambar + wilayah (kotak/bulat/titik) + poros tiap elemen dari elemen.json (daftar objek seperti `elemen: [...]` di konfig)

Format elemen (sama dengan konfig): {"nama": "roda-depan", "bulat": [u, v, ru], "poros": [u, v], "putaran": 360}
  wilayah: "kotak": [u0, v0, u1, v1] · "bulat": [u, v, ru(, rv)] · "titik": [[u, v], ...]  (pecahan 0–1 lebar/tinggi gambar)
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def huruf(uk):
    for f in ('arialbd.ttf', 'arial.ttf', 'DejaVuSans-Bold.ttf'):
        try:
            return ImageFont.truetype(f, uk)
        except OSError:
            pass
    return ImageFont.load_default()


def buka(p, maks=1600):
    im = Image.open(p)
    alfa = im.convert('RGBA').split()[-1] if im.mode in ('RGBA', 'LA', 'P') else None
    rgb = im.convert('RGB')
    if alfa is not None:  # tampilkan potongan transparan di atas kotak-kotak abu
        bg = Image.new('RGB', rgb.size, (128, 128, 128)); d = ImageDraw.Draw(bg); s = 32
        for y in range(0, rgb.size[1], s):
            for x in range(0, rgb.size[0], s):
                if (x // s + y // s) % 2: d.rectangle([x, y, x + s, y + s], fill=(160, 160, 160))
        bg.paste(rgb, mask=alfa); rgb = bg
    k = min(1.0, maks / max(rgb.size))
    if k < 1:
        rgb = rgb.resize((round(rgb.width * k), round(rgb.height * k)), Image.LANCZOS)
    return rgb, im


def kisi(p, keluar):
    im, _ = buka(p); w, h = im.size; d = ImageDraw.Draw(im, 'RGBA'); f = huruf(max(14, w // 55))
    for i in range(1, 20):
        q = i / 20; tebal = 3 if i % 2 == 0 else 1; warna = (255, 230, 0, 210) if i % 2 == 0 else (255, 255, 255, 110)
        d.line([(q * w, 0), (q * w, h)], fill=warna, width=tebal); d.line([(0, q * h), (w, q * h)], fill=warna, width=tebal)
        if i % 2 == 0:
            for (x, y, t) in ((q * w + 4, 4, f'{q:.1f}'), (4, q * h + 2, f'{q:.1f}')):
                d.rectangle([x - 2, y - 1, x + f.size * 1.9, y + f.size + 3], fill=(0, 0, 0, 170)); d.text((x, y), t, fill=(255, 230, 0), font=f)
    im.save(keluar, quality=90); print('kisi:', keluar)


def saran(p, keluar):
    im, asli = buka(p, 900); a = np.asarray(im).astype(np.float32); h, w = a.shape[:2]
    from scipy import ndimage
    hasil = []
    lum = .299 * a[..., 0] + .587 * a[..., 1] + .114 * a[..., 2]
    amb = max(200.0, float(np.percentile(lum, 98.5)))
    lab, n = ndimage.label(ndimage.binary_closing(lum >= amb, iterations=2))
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        if sl is None: continue
        luas = (lab[sl] == i).sum() / (w * h)
        if .0004 <= luas <= .03:
            y0, y1, x0, x1 = sl[0].start / h, sl[0].stop / h, sl[1].start / w, sl[1].stop / w
            hasil.append({'nama': f'cahaya-{len(hasil) + 1}', 'kotak': [round(x0, 3), round(y0, 3), round(x1, 3), round(y1, 3)],
                          'saran': 'titik terang (lampu/jendela/layar): kedip {kuat:.25} atau gerak terang (menyala)'})
    biru = (a[..., 2] > a[..., 0] + 15) & (a[..., 2] >= a[..., 1]) & (lum > 90)
    baris = biru.mean(axis=1); v = 0
    while v < h and baris[v] > .6: v += 1
    if v / h > .08:
        hasil.append({'nama': 'langit', 'kotak': [0, 0, 1, round(v / h, 3)], 'saran': 'pita langit: arus {x: 6} pelan (awan), atau elemen awan terpisah dengan ombak'})
    if asli.mode in ('RGBA', 'LA', 'P'):
        al = np.asarray(asli.convert('RGBA').resize((w, h)))[..., 3] > 40
        lab2, n2 = ndimage.label(al)
        bagian = [(i, sl) for i, sl in enumerate(ndimage.find_objects(lab2), 1) if sl is not None and (lab2[sl] == i).sum() / (w * h) > .01]
        if len(bagian) > 1:
            for i, sl in bagian:
                hasil.append({'nama': f'bagian-{i}', 'kotak': [round(sl[1].start / w, 3), round(sl[0].start / h, 3), round(sl[1].stop / w, 3), round(sl[0].stop / h, 3)],
                              'saran': 'bagian terpisah potongan: elemen sendiri (goyang/ombak/putaran sesuai benda)'})
    Path(keluar).write_text(json.dumps(hasil, ensure_ascii=False, indent=1), encoding='utf-8')
    gb = Path(keluar).with_suffix('.jpg'); uji_gambar(im, hasil, gb)
    print(f'{len(hasil)} usulan -> {keluar} + {gb}')
    for e in hasil: print(' ', e['nama'], e['kotak'], '·', e['saran'])


def uji_gambar(im, daftar, keluar):
    im = im.copy(); w, h = im.size; d = ImageDraw.Draw(im, 'RGBA'); f = huruf(max(14, w // 50))
    warna = [(255, 60, 60), (60, 200, 255), (255, 210, 0), (120, 255, 120), (255, 120, 255), (255, 160, 60)]
    for i, el in enumerate(daftar):
        c = warna[i % len(warna)]
        if 'titik' in el: d.polygon([(u * w, v * h) for u, v in el['titik']], outline=c + (255,), fill=c + (50,))
        elif 'bulat' in el:
            u, v, ru = el['bulat'][:3]; rv = el['bulat'][3] * h if len(el['bulat']) > 3 else ru * w
            d.ellipse([u * w - ru * w, v * h - rv, u * w + ru * w, v * h + rv], outline=c + (255,), fill=c + (50,), width=3)
        else:
            u0, v0, u1, v1 = el.get('kotak', [0, 0, 1, 1]); d.rectangle([u0 * w, v0 * h, u1 * w, v1 * h], outline=c + (255,), fill=c + (40,), width=3)
        if el.get('poros'):
            pu, pv = el['poros']; r = max(5, w // 120); d.ellipse([pu * w - r, pv * h - r, pu * w + r, pv * h + r], fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=2)
        nm = f"{i + 1}. {el.get('nama', '')}"
        x, y = (el['kotak'][0] * w if 'kotak' in el else (el['bulat'][0] * w if 'bulat' in el else el['titik'][0][0] * w)), (el['kotak'][1] * h if 'kotak' in el else (el['bulat'][1] * h if 'bulat' in el else el['titik'][0][1] * h))
        d.rectangle([x, y - f.size - 6, x + len(nm) * f.size * .62, y], fill=(0, 0, 0, 190)); d.text((x + 3, y - f.size - 4), nm, fill=c, font=f)
    im.save(keluar, quality=90)


def main():
    arg = sys.argv[1:]
    if len(arg) < 2: sys.exit(__doc__)
    cmd, gb = arg[0], Path(arg[1])
    keluar = arg[arg.index('--keluar') + 1] if '--keluar' in arg else None
    if cmd == 'kisi':
        kisi(gb, keluar or str(gb.with_name(gb.stem + '_kisi.jpg')))
    elif cmd == 'saran':
        saran(gb, keluar or str(gb.with_name(gb.stem + '_saran.json')))
    elif cmd == 'uji':
        if len(arg) < 3: sys.exit(__doc__)
        daftar = json.loads(Path(arg[2]).read_text(encoding='utf-8'))
        im, _ = buka(gb); out = keluar or str(gb.with_name(gb.stem + '_uji.jpg')); uji_gambar(im, daftar, out); print('uji:', out)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
