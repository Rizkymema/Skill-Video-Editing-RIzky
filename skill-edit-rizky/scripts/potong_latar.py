#!/usr/bin/env python3
"""Buang latar polos (hijau, biru, atau magenta) dari gambar Flow jadi PNG transparan untuk "lapisan" potongan di mesin.

Pakai:
  python3 potong_latar.py gambar\\potong\\K03-virus.jpg [file lain ...] [--keluar folder] [--toleransi 1.0] [--cek]
  python3 potong_latar.py gambar\\potong [--cek]          # semua gambar di folder itu

Gambar sumber (latar polos dari Flow) disimpan di gambar\\potong\\; hasilnya gambar\\<nama>.png (folder induk "potong"),
jadi nama lapisan di film.json = nama file tanpa ekstensi. Warna kunci dibaca otomatis dari tepi gambar, jadi latar
hijau (bawaan), biru (untuk subjek yang berwarna hijau), atau magenta sama-sama bisa. Tepi dibersihkan dari pantulan
warna latar (unmix + despill), bintik kecil dibuang, lalu gambar dipangkas ke isinya.
--toleransi  > 1 membuang lebih banyak (latar kotor/bergradasi), < 1 lebih hati-hati (subjek mirip warna latar).
--cek        lembar periksa potong_cek.jpg: tiap potongan di atas kotak-kotak dan di atas latar gelap.

Lembar ikon: banyak ikon/elemen kecil dibuat dalam SATU gambar Flow (kisi, latar hijau, jarak lebar antar-ikon), lalu
dipisah otomatis. Nama file sumber diawali "lembar-" (mis. gambar\\potong\\lembar-ikon.jpg). Nama tiap potongan diambil
dari gambar\\potong\\lembar-ikon.txt (satu nama per baris, urut baca: kiri→kanan, atas→bawah) atau --nama a,b,c;
tanpa nama = lembar-ikon-1, -2, … Lembar cek memberi nomor + nama tiap potongan: kalau urutan Flow berbeda, susun
ulang baris di .txt lalu jalankan lagi. Bagian satu ikon yang terpisah sedikit (kilau, garis gerak) ikut ikonnya.
Butuh: Pillow, numpy (scipy opsional untuk membuang bintik).
"""
import os
import sys

import numpy as np
from PIL import Image, ImageFilter

EKS = (".jpg", ".jpeg", ".png", ".webp")


def arg(nama, bawaan, tipe=float):
    if nama in sys.argv:
        return tipe(sys.argv[sys.argv.index(nama) + 1])
    return bawaan


def kroma(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return -0.168736 * r - 0.331264 * g + 0.5 * b, 0.5 * r - 0.418688 * g - 0.081312 * b


def potong(src, keluar, tol, nama_lembar=None):
    a = np.asarray(Image.open(src).convert("RGB"), dtype=np.float32) / 255.0
    h, w, _ = a.shape
    t = max(3, min(h, w) // 200)
    tepi = np.concatenate([a[:t].reshape(-1, 3), a[-t:].reshape(-1, 3), a[:, :t].reshape(-1, 3), a[:, -t:].reshape(-1, 3)])
    kunci = np.median(tepi, axis=0)
    kcb, kcr = kroma(kunci)
    km = float(np.hypot(kcb, kcr))
    peringatan = []
    if km < 0.12:
        peringatan.append("latar tidak berwarna jelas (bukan hijau/biru/magenta); hasil bisa memakan subjek")
    cb, cr = kroma(a)
    d = np.hypot(cb - kcb, cr - kcr)
    d0, d1 = 0.2 * km * tol, 0.4 * km * tol
    alpha = np.clip((d - d0) / max(1e-6, d1 - d0), 0, 1)
    alpha = alpha * alpha * (3 - 2 * alpha)
    # dominasi kanal kunci (hijau/biru): pendar atau tepi yang bercampur latar (mis. cahaya kuning di atas hijau)
    # kroma-nya jauh dari kunci tapi kanal kuncinya masih menonjol, jadi dibuat semi-transparan lalu di-unmix
    kc = int(np.argmax(kunci))
    lain = [i for i in range(3) if i != kc]
    ek = float(kunci[kc] - max(kunci[lain[0]], kunci[lain[1]]))
    if ek > 0.3:
        lebih = a[..., kc] - np.maximum(a[..., lain[0]], a[..., lain[1]])
        e0, e1 = 0.12 / tol, 0.55 * ek / tol
        ax = 1 - np.clip((lebih - e0) / max(1e-6, e1 - e0), 0, 1)
        alpha = np.minimum(alpha, ax * ax * (3 - 2 * ax))
    alpha[alpha < 0.03] = 0
    try:                                                    # buang bintik kecil yang lolos (pulau < 0,05% gambar)
        from scipy import ndimage
        lab, n = ndimage.label(alpha > 0.5)
        if n > 1:
            luas = ndimage.sum(np.ones_like(alpha), lab, range(1, n + 1))
            ambang = 0.00005 if nama_lembar is not None else 0.0005           # lembar ikon: kilau kecil jangan terbuang
            kecil = np.isin(lab, [i + 1 for i, v in enumerate(luas) if v < ambang * h * w])
            alpha[kecil] = 0
        sekitar = ndimage.binary_dilation(alpha < 0.98, iterations=3)   # pita tepi untuk despill
    except ImportError:
        sekitar = np.asarray(Image.fromarray(((alpha < 0.98) * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(7))) > 0
    # unmix: warna tepi semi-transparan dikurangi campuran warna latar
    tm = (alpha > 0.02) & (alpha < 0.98)
    am = np.maximum(alpha[tm], 0.08)[:, None]
    a[tm] = np.clip((a[tm] - (1 - am) * kunci) / am, 0, 1)
    # despill: di pita tepi, kanal warna kunci tidak boleh melebihi dua kanal lain (hanya piksel yang masih mirip latar)
    mirip = sekitar & ((d < d1 * 1.8) | (alpha < 0.98))
    batas = np.maximum(a[..., lain[0]], a[..., lain[1]])
    a[..., kc] = np.where(mirip, np.minimum(a[..., kc], batas + 0.02), a[..., kc])
    al = Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
    rgba = Image.fromarray((a * 255).astype(np.uint8), "RGB")
    rgba.putalpha(al)
    aa = np.asarray(al)
    ys, xs = np.nonzero(aa > 5)
    if not len(xs):
        return None, ["semua piksel terbuang; cek warna latar atau turunkan --toleransi"], kunci
    tb = np.r_[aa[:t].ravel(), aa[-t:].ravel(), aa[:, :t].ravel(), aa[:, -t:].ravel()]
    if (tb > 128).mean() > 0.02:
        peringatan.append("subjek menyentuh tepi gambar (terpotong); buat ulang dengan ruang kosong di sekeliling subjek")
    isi = (aa > 128).mean()
    if isi > 0.85:
        peringatan.append(f"latar hampir tidak terbuang (isi {isi:.0%}); latar Flow tidak polos?")
    pad = int(0.015 * max(h, w))
    if nama_lembar is not None:
        return pisah_lembar(rgba, aa, keluar, nama_lembar, peringatan), peringatan, kunci
    kotak = (max(0, xs.min() - pad), max(0, ys.min() - pad), min(w, xs.max() + pad + 1), min(h, ys.max() + pad + 1))
    hasil = rgba.crop(kotak)
    hasil.save(keluar, optimize=True)
    return hasil, peringatan, kunci


def pisah_lembar(rgba, aa, keluar, nama, peringatan):
    """Pisah lembar ikon: pulau-pulau isi (yang berdekatan digabung) diurutkan per baris lalu kiri→kanan."""
    from scipy import ndimage
    h, w = aa.shape
    isi = aa > 128
    gabung = ndimage.binary_dilation(isi, iterations=max(2, int(0.012 * max(h, w))))   # kilau/garis kecil ikut ikonnya
    lab, n = ndimage.label(gabung)
    pulau = []
    for i, sl in enumerate(ndimage.find_objects(lab), 1):
        bagian = isi[sl] & (lab[sl] == i)
        if bagian.sum():
            ys, xs = np.nonzero(bagian)
            pulau.append((sl[0].start + ys.min(), sl[1].start + xs.min(), sl[0].start + ys.max(), sl[1].start + xs.max(), i, int(bagian.sum())))
    if not pulau:
        return []
    besar = np.median([p[5] for p in pulau])
    utama = [list(p) for p in pulau if p[5] > 0.12 * besar]
    jangkau = 0.06 * max(h, w)
    for p in pulau:                                                         # pulau kecil (kilau, garis gerak) ikut ikon terdekat
        if p[5] > 0.12 * besar or not utama:
            continue
        jarak = [max(q[0] - p[2], p[0] - q[2], 0) + max(q[1] - p[3], p[1] - q[3], 0) for q in utama]
        j = int(np.argmin(jarak))
        if jarak[j] <= jangkau:
            q = utama[j]
            lab[lab == p[4]] = q[4]
            q[0], q[1], q[2], q[3] = min(q[0], p[0]), min(q[1], p[1]), max(q[2], p[2]), max(q[3], p[3])
    pulau = [tuple(q) for q in utama]
    tinggi_m = np.median([p[2] - p[0] for p in pulau])
    pulau.sort(key=lambda p: (p[0] + p[2]) / 2)
    baris, sekarang = [], []
    for p in pulau:                                                         # kelompokkan per baris (pusat y berdekatan)
        if sekarang and (p[0] + p[2]) / 2 - np.mean([(q[0] + q[2]) / 2 for q in sekarang]) > 0.5 * tinggi_m:
            baris.append(sekarang)
            sekarang = []
        sekarang.append(p)
    baris.append(sekarang)
    urut = [p for b in baris for p in sorted(b, key=lambda q: q[1])]
    dasar = os.path.splitext(keluar)[0]
    if nama and len(nama) != len(urut):
        peringatan.append(f"{len(urut)} potongan tetapi {len(nama)} nama; cek lembar periksa dan susun ulang daftar nama")
    pad = int(0.012 * max(h, w))
    data = np.asarray(rgba).copy()
    hasil = []
    for k, (y0, x0, y1, x1, i, _) in enumerate(urut):
        y0, x0, y1, x1 = max(0, y0 - pad), max(0, x0 - pad), min(h, y1 + pad + 1), min(w, x1 + pad + 1)
        kotak = data[y0:y1, x0:x1].copy()
        kotak[..., 3] = np.where(lab[y0:y1, x0:x1] == i, kotak[..., 3], 0)    # buang bagian ikon tetangga di dalam kotak
        nm = nama[k] if nama and k < len(nama) else f"{os.path.basename(dasar)}-{k + 1}"
        im = Image.fromarray(kotak, "RGBA")
        im.save(os.path.join(os.path.dirname(keluar), nm + ".png"), optimize=True)
        hasil.append((f"{k + 1} {nm}", im))
    return hasil


def lembar_cek(hasil, keluar):
    from PIL import ImageDraw, ImageFont
    tinggi = 420
    kartu = []
    for nama, im in hasil:
        k = tinggi / im.height
        im = im.resize((max(1, int(im.width * k)), tinggi))
        for latar in ("kotak", "gelap"):
            bg = Image.new("RGB", im.size, (22, 18, 74))
            if latar == "kotak":
                bg = Image.new("RGB", im.size, (235, 235, 235))
                px = 20
                for y in range(0, im.height, px):
                    for x in range((y // px % 2) * px, im.width, 2 * px):
                        bg.paste((200, 200, 200), (x, y, x + px, y + px))
            bg.paste(im, (0, 0), im)
            if latar == "kotak":
                try:
                    huruf = ImageFont.load_default(size=26)
                except TypeError:
                    huruf = ImageFont.load_default()
                ImageDraw.Draw(bg).text((8, 6), nama, fill=(200, 0, 90), font=huruf, stroke_width=3, stroke_fill=(255, 255, 255))
            kartu.append(bg)
    lebar_maks, baris, x = 6000, [[]], 0                                   # banyak potongan (lembar ikon): beberapa baris
    for c in kartu:
        if x + c.width > lebar_maks and baris[-1]:
            baris.append([])
            x = 0
        baris[-1].append(c)
        x += c.width + 10
    lembar = Image.new("RGB", (min(lebar_maks, max(sum(c.width + 10 for c in b) for b in baris)), (tinggi + 10) * len(baris)), (255, 255, 255))
    for j, b in enumerate(baris):
        x = 0
        for c in b:
            lembar.paste(c, (x, j * (tinggi + 10)))
            x += c.width + 10
    lembar.save(keluar, quality=88)
    return keluar


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    nilai = {sys.argv[i + 1] for i, a in enumerate(sys.argv[:-1]) if a in ("--keluar", "--toleransi", "--nama")}
    masukan = [a for a in sys.argv[1:] if not a.startswith("--") and a not in nilai]
    if not masukan:
        sys.exit(__doc__)
    tol = arg("--toleransi", 1.0)
    file = []
    for m in masukan:
        if os.path.isdir(m):
            file += [os.path.join(m, f) for f in sorted(os.listdir(m)) if f.lower().endswith(EKS)]
        else:
            file.append(m)
    hasil, gagal = [], 0
    for src in file:
        folder = os.path.dirname(os.path.abspath(src))
        tujuan = arg("--keluar", os.path.dirname(folder) if os.path.basename(folder).lower() == "potong" else folder, str)
        os.makedirs(tujuan, exist_ok=True)
        keluar = os.path.join(tujuan, os.path.splitext(os.path.basename(src))[0] + ".png")
        if os.path.abspath(keluar) == os.path.abspath(src):
            print(f"lewati {src}: hasil akan menimpa sumbernya (taruh sumber di gambar\\potong\\)")
            gagal += 1
            continue
        lembar = os.path.basename(src).lower().startswith("lembar-")
        nama = None
        if lembar:
            txt = os.path.splitext(src)[0] + ".txt"
            nama = [x.strip() for x in arg("--nama", "", str).split(",") if x.strip()] if "--nama" in sys.argv else \
                [x.strip() for x in open(txt, encoding="utf-8") if x.strip()] if os.path.exists(txt) else []
        im, catatan, kunci = potong(src, keluar, tol, nama if lembar else None)
        hx = "#%02X%02X%02X" % tuple(int(v * 255) for v in kunci)
        if im is None or (lembar and not im):
            print(f"GAGAL {os.path.basename(src)} (kunci {hx}): {catatan[0] if catatan else 'tidak ada potongan'}")
            gagal += 1
            continue
        if lembar:
            hasil += im
            print(f"{'PERIKSA' if catatan else 'BERES'}  {os.path.basename(src)} → {len(im)} potongan: {', '.join(n.split(' ', 1)[1] for n, _ in im)}"
                  + (f"  — {'; '.join(catatan)}" if catatan else ""))
            continue
        hasil.append((os.path.basename(keluar), im))
        print(f"{'PERIKSA' if catatan else 'BERES'}  {os.path.basename(keluar)}  {im.width}x{im.height}  kunci {hx}"
              + (f"  — {'; '.join(catatan)}" if catatan else ""))
    if "--cek" in sys.argv and hasil:
        print("lembar periksa:", lembar_cek(hasil, os.path.join(os.path.dirname(keluar), "potong_cek.jpg")))
    if gagal:
        sys.exit(1)


if __name__ == "__main__":
    main()
