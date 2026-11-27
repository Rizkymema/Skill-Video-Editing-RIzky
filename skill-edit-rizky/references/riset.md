# Riset data: setiap angka benar dan bersumber

Video gaya ini hidup dari angka, tanggal, dan nama. Satu angka salah = komentar "hoaks" dan kredibilitas channel hilang. Aturan:

## 1. Cara riset
1. Sebelum menawarkan ide (Tahap 1): satu pencarian web per ide untuk memastikan inti faktanya ada.
2. Tahap 2: untuk **setiap** angka/tanggal/nama/kejadian di naskah dan di layar, cari minimal **2 sumber** (WebSearch, lalu WebFetch halaman yang paling kuat). Urutan kekuatan: dokumen resmi/lembaga > ensiklopedia dengan rujukan (Wikipedia) > media besar > blog/situs penggemar.
3. Sumber beda angka/tanggal: pakai yang paling kuat, atau tulis rentang/"±", atau hindari angka itu. Contoh N250: prototipe kedua "Agustus 1996" (roll-out) vs "19 Desember 1996" (terbang) → yang dipakai tanggal terbang, sesuai kalimat "ikut mengudara".
4. Perkiraan tetap perkiraan: "separuh dari ±1.400 jam" ditampilkan sebagai **±50%**, bukan "700 JAM".
5. Catat di `naskah.txt`:
   ```
   # sumber: <url> — <fakta persis yang dipakai>
   # dramatisasi: <apa yang fiktif: nama koran, adegan, kalimat pembuka umum>
   ```
   dan di `KONFIG.sumber = [{ fakta, url }]` (mesin menolak bila kosong atau url tidak sah; `KONFIG.data: false` hanya untuk video tanpa klaim fakta).
6. Laporan Tahap 2 dan deskripsi YouTube menyebut sumber utama.

## 2. Yang boleh didramatisasi
- Nama media di layar **fiktif** (Harian Nusantara, bukan Kompas/Tempo); kejadian dan tanggalnya tetap nyata.
- Dokumen di layar adalah **catatan ringkas** ("CATATAN · 15 Jan 1998"), bukan replika dokumen asli.
- Gambar Flow adalah ilustrasi suasana (hangar, kerumunan, kabin), bukan foto arsip asli; jangan menulis "foto asli".
- Kalimat pembuka umum ("hampir pasti buatan luar negeri") boleh tanpa angka, asal tidak menyesatkan.

## 3. Tokoh nyata dan merek
- Wajah tokoh terkenal tidak dibuat Flow. Pilihan: foto berlisensi (Wikimedia Commons, domain publik, NASA; `scripts/ambil_media.py` skill ini, lisensi tercatat di `media.json`, lihat `data-media.md`), orang dari belakang/siluet, atau benda yang mewakili (pesawat, dokumen).
- Logo merek/media nyata tidak digambar; nama merek boleh disebut di narasi.
- Topik tragedi: korban tidak jadi bahan lelucon; vonis menghormati.

## 4. Angka di narasi
- Tulis angka sebagai angka di naskah ("1995", "55", "43", "1.400"); Edge/ElevenLabs membacanya benar, dan penyelaras kata menangani token gabungan ("Agustus 1995").
- Satuan mata uang: "43 miliar dolar" di narasi, "US$43 miliar" di layar.
