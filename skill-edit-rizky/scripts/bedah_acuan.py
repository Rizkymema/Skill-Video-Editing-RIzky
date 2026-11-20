"""Bedah acuan visual dari pengguna (video dan/atau gambar) -> bahan untuk meniru GAYA-nya pada topik apa pun.

Pakai:
  python -X utf8 -I scripts/bedah_acuan.py <_kerja> <berkas1> [berkas2 ...] [--fps 2] [--lebar 270]

Hasil di <_kerja>/acuan/:
  asal/<berkas>            salinan acuan (tidak dikirim ke mana pun)
  lembar-NN.jpg            lembar bingkai (video: 2 bingkai/dtk, 8x6 per lembar, berlabel detik)
  potongan.jpg             satu bingkai tiap potongan/perpindahan yang terdeteksi (berlabel detik)
  ringkasan.json           angka: durasi, potongan, rata-rata panjang bidikan, kecerahan, saturasi, palet, kontras teks
  gaya-acuan.md            kartu gaya acuan (angka sudah terisi; bagian pengamatan diisi Claude setelah MELIHAT lembar)
Langkah berikutnya: references/acuan.md.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

GAMBAR = {'.jpg', '.jpeg', '.png', '.webp', '.bmp'}
VIDEO = {'.mp4', '.mov', '.webm', '.mkv', '.m4v', '.avi', '.gif'}


def ffmpeg_exe():
    for c in ('ffmpeg',):
        if shutil.which(c):
            return shutil.which(c)
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        sys.exit('ffmpeg tidak ditemukan (pasang imageio-ffmpeg atau tambahkan ffmpeg ke PATH)')


def info_video(ff, p):
    r = subprocess.run([ff, '-hide_banner', '-i', str(p)], capture_output=True, text=True, errors='replace')
    import re
    d = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r.stderr)
    dur = int(d.group(1)) * 3600 + int(d.group(2)) * 60 + float(d.group(3)) if d else 0
    s = re.search(r'Video:.*?(\d{2,5})x(\d{2,5})', r.stderr)
    w, h = (int(s.group(1)), int(s.group(2))) if s else (0, 0)
    f = re.search(r'([\d.]+) fps', r.stderr)
    return {'durasi': round(dur, 2), 'lebar': w, 'tinggi': h, 'fps': float(f.group(1)) if f else 0, 'audio': 'Audio:' in r.stderr}


def bingkai(ff, p, fps, lebar):
    """[(detik, PIL.Image RGB)] pada fps tertentu, lebar tetap"""
    w0, h0 = info_video(ff, p)['lebar'], info_video(ff, p)['tinggi']
    h = int(round(lebar * h0 / max(1, w0) / 2) * 2) if w0 else int(lebar * 16 / 9)
    cmd = [ff, '-v', 'error', '-i', str(p), '-vf', f'fps={fps},scale={lebar}:{h}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    raw = subprocess.run(cmd, capture_output=True).stdout
    n = len(raw) // (lebar * h * 3)
    arr = np.frombuffer(raw[:n * lebar * h * 3], np.uint8).reshape(n, h, lebar, 3)
    return [(i / fps, Image.fromarray(arr[i])) for i in range(n)]


def huruf(uk):
    for f in ('arialbd.ttf', 'DejaVuSans-Bold.ttf', 'Arial.ttf'):
        try:
            return ImageFont.truetype(f, uk)
        except Exception:
            pass
    return ImageFont.load_default()


def lembar(frames, keluar, awalan, kolom=8, baris=6):
    if not frames:
        return []
    w, h = frames[0][1].size
    per = kolom * baris; hasil = []; f = huruf(max(12, w // 14))
    for k in range(0, len(frames), per):
        sh = Image.new('RGB', (kolom * w, baris * h), (0, 0, 0)); d = ImageDraw.Draw(sh)
        for i, (t, im) in enumerate(frames[k:k + per]):
            x, y = (i % kolom) * w, (i // kolom) * h
            sh.paste(im.resize((w, h)), (x, y)); d.rectangle([x, y, x + w * .38, y + w * .1], fill=(0, 0, 0)); d.text((x + 4, y + 2), f'{t:.1f}s', fill=(255, 255, 0), font=f)
        nama = keluar / f'{awalan}-{k // per + 1:02d}.jpg'; sh.save(nama, quality=86); hasil.append(nama.name)
    return hasil


def palet(frames, n=6):
    if not frames:
        return []
    sampel = Image.new('RGB', (64 * min(len(frames), 40), 114))
    step = max(1, len(frames) // 40)
    for i, (t, im) in enumerate(frames[::step][:40]):
        sampel.paste(im.resize((64, 114)), (i * 64, 0))
    q = sampel.quantize(colors=n, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()[:n * 3]; cnt = sorted(q.getcolors(), reverse=True)
    out = []
    for c, idx in cnt:
        r, g, b = pal[idx * 3:idx * 3 + 3]; out.append({'hex': '#%02x%02x%02x' % (r, g, b), 'porsi': round(c / (sampel.width * sampel.height), 3)})
    return out


def statistik(frames):
    if not frames:
        return {}
    arr = np.stack([np.asarray(im.resize((90, 160)), np.float32) / 255 for _, im in frames])
    lum = arr @ np.array([.299, .587, .114], np.float32)
    mx, mn = arr.max(-1), arr.min(-1); sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    tepi = lum[:, :, :8].mean() * .25 + lum[:, :, -8:].mean() * .25 + lum[:, :8, :].mean() * .25 + lum[:, -8:, :].mean() * .25
    return {'kecerahan': round(float(lum.mean()), 3), 'kecerahan_tepi': round(float(tepi), 3), 'kecerahan_tengah': round(float(lum[:, 50:110, 25:65].mean()), 3),
            'saturasi': round(float(sat.mean()), 3), 'kontras': round(float(lum.std()), 3),
            'kesan': ('terang' if lum.mean() > .6 else 'gelap' if lum.mean() < .35 else 'sedang') + (' monokrom' if sat.mean() < .12 else ' berwarna lembut' if sat.mean() < .3 else ' berwarna kuat') + (' + vinyet' if float(lum[:, 50:110, 25:65].mean()) - tepi > .12 else '')}


def potongan(ff, p, keluar):
    """deteksi potongan/perpindahan: beda bingkai 10 fps di atas ambang adaptif"""
    fr = bingkai(ff, p, 10, 96)
    if len(fr) < 3:
        return [], []
    g = np.stack([np.asarray(im.convert('L'), np.float32) for _, im in fr])
    d = np.abs(np.diff(g, axis=0)).mean(axis=(1, 2))
    amb = max(10.0, float(np.median(d) * 4))
    idx = [i + 1 for i in range(len(d)) if d[i] > amb and (i == 0 or d[i] >= d[i - 1]) and (i + 1 >= len(d) or d[i] >= d[i + 1])]
    rapat = []
    for i in idx:
        if not rapat or i - rapat[-1] >= 4:
            rapat.append(i)
    waktu = [round(fr[i][0], 2) for i in rapat]
    besar = bingkai(ff, p, 10, 180)
    pilih = [(t, besar[min(len(besar) - 1, int(round(t * 10)))][1]) for t in waktu]
    if pilih:
        lembar(pilih, keluar, 'potongan', kolom=8, baris=max(1, min(8, (len(pilih) + 7) // 8)))
    return waktu, [round(float(d[i - 1]), 1) for i in rapat]


def main():
    arg = sys.argv[1:]
    fps = float(arg[arg.index('--fps') + 1]) if '--fps' in arg else 2.0
    lebar = int(arg[arg.index('--lebar') + 1]) if '--lebar' in arg else 270
    pos = [a for i, a in enumerate(arg) if not a.startswith('--') and (i == 0 or arg[i - 1] not in ('--fps', '--lebar'))]
    if len(pos) < 2:
        sys.exit(__doc__)
    kerja, berkas = Path(pos[0]), [Path(x) for x in pos[1:]]
    keluar = kerja / 'acuan'; (keluar / 'asal').mkdir(parents=True, exist_ok=True)
    ff = ffmpeg_exe(); ring = {'berkas': [], 'video': [], 'gambar': []}
    semua = []
    for b in berkas:
        if not b.exists():
            print('LEWATI (tidak ada):', b); continue
        tujuan = keluar / 'asal' / b.name
        if b.resolve() != tujuan.resolve():
            shutil.copy2(b, tujuan)
        ring['berkas'].append(b.name); ext = b.suffix.lower()
        if ext in VIDEO:
            inf = info_video(ff, tujuan); fr = bingkai(ff, tujuan, fps, lebar); semua += fr
            sh = lembar(fr, keluar, f'lembar-{tujuan.stem[:20]}')
            waktu, kuat = potongan(ff, tujuan, keluar)
            bid = np.diff([0] + waktu + [inf['durasi']]) if inf['durasi'] else []
            inf.update({'lembar': sh, 'potongan_detik': waktu, 'jumlah_potongan': len(waktu), 'rata_bidikan_dtk': round(float(np.mean(bid)), 2) if len(bid) else None,
                        'statistik': statistik(fr), 'palet': palet(fr)})
            ring['video'].append({'nama': b.name, **inf})
        elif ext in GAMBAR:
            im = Image.open(tujuan).convert('RGB'); im.thumbnail((lebar * 2, lebar * 4)); semua.append((0, im))
            ring['gambar'].append({'nama': b.name, 'ukuran': Image.open(tujuan).size, 'statistik': statistik([(0, im)]), 'palet': palet([(0, im)])})
        else:
            print('LEWATI (jenis tidak dikenal):', b)
    if ring['gambar']:
        lembar([(0, im) for t, im in semua if t == 0][:48], keluar, 'lembar-gambar', kolom=4, baris=3)
    ring['gabungan'] = {'statistik': statistik(semua), 'palet': palet(semua)}
    (keluar / 'ringkasan.json').write_text(json.dumps(ring, ensure_ascii=False, indent=1), encoding='utf-8')
    st, pl = ring['gabungan']['statistik'], ring['gabungan']['palet']
    v0 = ring['video'][0] if ring['video'] else {}
    kartu = f"""# Kartu gaya acuan — {', '.join(ring['berkas'])}
(diisi otomatis: angka; diisi Claude setelah melihat lembar-*.jpg dan potongan-*.jpg: semua bagian bertanda »)

## Angka
- kesan: **{st.get('kesan', '-')}** · kecerahan {st.get('kecerahan')} (tengah {st.get('kecerahan_tengah')}, tepi {st.get('kecerahan_tepi')}) · saturasi {st.get('saturasi')} · kontras {st.get('kontras')}
- palet: {' '.join(p['hex'] + f" ({int(p['porsi'] * 100)}%)" for p in pl)}
- video: {v0.get('durasi', '-')} dtk · {v0.get('lebar', '-')}×{v0.get('tinggi', '-')} · potongan/perpindahan {v0.get('jumlah_potongan', '-')} · rata-rata bidikan {v0.get('rata_bidikan_dtk', '-')} dtk · audio {'ada' if v0.get('audio') else '-'}

## Pengamatan (» isi)
- » latar (warna, tekstur, bentuk dekoratif yang bergerak):
- » huruf (berapa gaya, ukuran relatif, serif/sans, miring/tebal, kapital?, letak, cara muncul per kata):
- » penekanan (kotak sorot, warna aksen, garis bawah, coretan):
- » gambar/benda (foto realistis, potongan, ikon 3D, kartu bersudut bulat, polaroid, lingkaran):
- » gerak kamera + perpindahan (jenis dan kapan):
- » efek (glitch, vinyet, grain, blur, cahaya):
- » ritme (adegan per detik, kapan teks berganti):
- » bunyi (musik, efek; dengarkan bila perlu: jangan disalin, cari yang senada di Epidemic):
- » yang TIDAK boleh ditiru (logo/watermark/nama akun/footage/tokoh/kalimat mereka):

## Terjemahan ke mesin (» isi; lihat references/acuan.md §3)
- KONFIG.grade / palet / gayaTeks:
- latar per adegan:
- gaya teks:
- benda/kartu:
- perpindahan tanda tangan:
- musik + SFX:
"""
    (keluar / 'gaya-acuan.md').write_text(kartu, encoding='utf-8')
    print(f"ok {keluar} · {st.get('kesan')} · palet {' '.join(p['hex'] for p in pl[:4])}" + (f" · {v0.get('jumlah_potongan')} potongan, bidikan ±{v0.get('rata_bidikan_dtk')} dtk" if v0 else ''))
    print('lihat:', ', '.join(sorted(p.name for p in keluar.glob('*.jpg'))))


if __name__ == '__main__':
    main()
