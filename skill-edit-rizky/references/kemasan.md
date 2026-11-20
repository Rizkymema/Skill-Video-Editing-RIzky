# Kemasan + unggah

## 1. Judul dan deskripsi
- 3 judul, 4–8 kata, menyebut **benda/tokoh + keanehannya**, tanpa membocorkan akhir. Contoh: "Indonesia Pernah Bikin Pesawat Sendiri", "Pesawat Indonesia yang Dihentikan IMF", "Kenapa N250 Cuma Jadi Museum?". Terkuat dipakai, dua cadangan di laporan.
- Deskripsi pendek (±5 baris): satu kalimat pembuka cerita, satu kalimat konteks, **"Sumber: …"** (1–3 sumber utama dari `KONFIG.sumber`, nama situs + tahun cukup), satu pertanyaan untuk komentar, ajakan follow satu baris. Tanpa menyebut alat pembuat (AI, Flow, ElevenLabs, Claude).
- 3–5 tagar topik (#sejarah #indonesia #pesawat …), bukan tagar alat.
- Komentar sematan: pertanyaan lanjutan ("Menurutmu, kalau tidak ada krisis 1998, N250 bakal laku?").
- `synthetic`: `true` (gambar realistis buatan AI tentang kejadian nyata wajib dilabel konten sintetis di YouTube).

## 2. Thumbnail
Mesin bersama `_thumbnail` (`D:\automation\Video AI\_thumbnail\PANDUAN.md`): subjek = gambar Flow terkuat (pelat atau potongan, mis. `gambar/pesawat.png`), teks dari mesin. Tata letak `dosir` atau `kertas` paling cocok dengan gaya arsip. Hasil `thumbnail.png` 16:9 + `thumbnail_short.png` 9:16.

## 3. Unggah
Lewat skill `unggah-youtube` ke `D:\automation\Video AI\Hasil Video\Edit Rizky\Umum\<tanggal> <Judul>\`: MP4 final + `thumbnail.png` + `youtube.json` (+ `"channel"` pilihan Tahap 2, `categoryId` `27` atau `25`) + `info YouTube.md` + `<Judul>.html`. `_kerja\` dibuang ke Recycle Bin setelah terunggah (kecuali saya bilang mau revisi/sekuel). Kiriman ke saya: MP4 final + HTML.
