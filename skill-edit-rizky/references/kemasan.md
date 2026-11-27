# Kemasan + unggah

## 1. Judul dan deskripsi
- 3 judul, 4–8 kata, menyebut **benda/tokoh + keanehannya**, tanpa membocorkan akhir. Contoh: "Indonesia Pernah Bikin Pesawat Sendiri", "Pesawat Indonesia yang Dihentikan IMF", "Kenapa N250 Cuma Jadi Museum?". Terkuat dipakai, dua cadangan di laporan.
- Deskripsi pendek (±5 baris): satu kalimat pembuka cerita, satu kalimat konteks, **"Sumber: …"** (1–3 sumber utama dari `KONFIG.sumber`, nama situs + tahun cukup), satu pertanyaan untuk komentar, ajakan follow satu baris. Tanpa menyebut alat pembuat (AI, Flow, ElevenLabs, Claude).
- 3–5 tagar topik (#sejarah #indonesia #pesawat …), bukan tagar alat.
- Komentar sematan: pertanyaan lanjutan ("Menurutmu, kalau tidak ada krisis 1998, N250 bakal laku?").
- `synthetic`: `true` (gambar realistis buatan AI tentang kejadian nyata wajib dilabel konten sintetis di YouTube).

## 2. Sampul
**Utama (sejak 28 Nov 2026): Google Flow, `references/sampul.md`.** Satu sampul dengan rasio yang sama dengan video (9:16 → `sampul.jpg` 1080×1920; 16:9 → 1280×720), desain poster mengikuti style video (`scripts/sampul.py`). Di cloud: kirim prompt `prompt-sampul.md` ke pengguna.
Cadangan (Flow gagal / ejaan judul terus salah): mesin bersama `_thumbnail` (`D:\automation\Video AI\_thumbnail\PANDUAN.md`) dengan latar = varian Flow tanpa teks; tetap satu rasio sesuai video.

## 3. Simpan, unggah, kirim
- Semua hasil di `D:\automation\Skill-Video-Editing-Rizky\Hasil Video\<tanggal> <Judul>\` (permintaan pengguna 28 Nov 2026): `<Judul>.mp4` + `<Judul>.html` + `sampul.jpg` + `prompt-sampul.md` + `info YouTube.md` (+ `youtube.json` bila diunggah: `"thumbnail": "sampul.jpg"`, `"channel"` pilihan Tahap 2, `categoryId` `27` atau `25`). `Hasil Video/` tidak di-commit.
- Unggah hanya bila dipilih: lewat skill `unggah-youtube` (skill itu menyalin berkas ke foldernya sendiri). `_kerja\` dibuang ke Recycle Bin setelah terunggah (kecuali saya bilang mau revisi/sekuel).
- **Kiriman ke saya sesudah video jadi**: MP4 final (+ 720p) + HTML + `sampul.jpg` + di chat: 3 judul (terkuat ditandai) + deskripsi siap tempel + tagar. Di cloud: prompt sampul di chat menggantikan `sampul.jpg`.
