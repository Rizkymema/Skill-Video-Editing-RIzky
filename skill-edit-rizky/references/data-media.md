# Data dan media nyata (foto + video asli)

Sejak 18 Nov 2026 (permintaan pengguna: "ketika saya membahas topik yang ada datanya bantu ambil langsung datanya seperti contoh gambar atau video"). Topik yang punya data nyata (tokoh, pesawat/kendaraan, gedung, peristiwa, produk, tempat) **tidak hanya memakai ilustrasi Flow**: foto/video asli diambil, dicek lisensinya, ditanam sebagai lapisan, dan kreditnya tampil di layar.

## 1. Kapan
- Topik menyebut **benda/tokoh/tempat/peristiwa yang benar-benar ada** → cari minimal 2–4 media asli di Tahap 2 (bersamaan dengan riset angka). Topik fiksi/umum (kebiasaan, konsep) cukup Flow.
- Ilustrasi Flow tetap dipakai untuk suasana, tempat umum, dan potongan yang perlu latar hijau. Media asli untuk **bukti**: rupa benda/tokoh asli, dokumen, siaran, cuplikan kejadian.
- Wajah tokoh nyata **hanya** dari foto/video asli (atau kiriman pengguna), tidak pernah digambar Flow.

## 2. Alur (Tahap 2, sebelum storyboard final)
```
python -X utf8 -I scripts/ambil_media.py cari "<benda/tokoh/peristiwa>" [--di wiki|commons|nasa|youtube] [--jenis video]
python -X utf8 -I scripts/ambil_media.py ambil <url> <_kerja>                    # unduh ke _calon (+ lembar bingkai video) untuk dilihat
python -X utf8 -I scripts/ambil_media.py ambil <url> <_kerja> --kode <kode> [--mulai 12 --sampai 17] [--potong]
python -X utf8 -I scripts/ambil_media.py daftar <_kerja>                         # kredit untuk deskripsi
```
- Urutan sumber: **Wikipedia/Commons** (lisensi bebas, atribusi) → **NASA** (domain publik) → **YouTube Creative Commons** (`--cc`) → **kutipan berita/kanal resmi** (3–8 dtk per klip, total ≤ 20 dtk per video, kredit kanal + tanggal di layar) → **kiriman pengguna** (path lokal).
- Izin: permintaan pengguna 18 Nov 2026 ("bantu ambil langsung datanya") = izin tetap untuk mengunduh foto/video berlisensi bebas (Wikipedia, Commons, NASA) di Tahap 2 tanpa bertanya lagi. Kutipan YouTube/berita disebutkan di pesan Tahap 2 (judul, kanal, detik yang dipakai) dan ikut disetujui di klik 2; bila pengguna menolak, ganti dengan ilustrasi.
- YouTube/Instagram sering menolak unduhan tanpa login ("confirm you're not a bot"). **Jangan memakai cookie/login browser pengguna.** Minta pengguna mengunduh MP4-nya sendiri, lalu `ambil <berkas.mp4>`.
- Lisensi bertanda `NON-BEBAS` (fair use Wikipedia, logo, "all rights reserved") tidak dipakai, kecuali kutipan berita pendek dengan kredit.
- Poin penting dari video panjang tanpa mengunduh: subtitle otomatis di browser Claude (`flow.md` §7).

## 3. Cara tampil (supaya berlapis, bukan ditempel datar)
`ambil` mencetak lapisan siap tempel. Pilihan:
| Media | Lapisan | Kapan |
|---|---|---|
| foto | `benda: { jenis: 'kartu', gambar, keterangan }` + `putar`, `bayangan`, `masuk: 'terbang'` | bukti rupa benda/tokoh; bisa pindah antar-adegan dengan `cocok` |
| foto | `benda: koran { foto }` / `benda: tv { gambar }` | foto di berita / siaran |
| foto | `{ gambar }` pelat penuh | foto lanskap tajam ≥ 1600 px yang memang jadi tempat adegan |
| foto `--potong` | potongan transparan (rembg, bila terpasang) + `jangkar`/`rig` | tokoh/benda dikeluarkan dari fotonya (hanya bila tepinya bersih) |
| video | `{ urutan: kode, lebar: 940, putar: -1.5, bayangan: true }` + `rakit --klip kode=klip/kode.mp4@12` | cuplikan kejadian, pernyataan resmi |

Selalu tambahkan **label kredit** (`gaya: 'label'`, ±1330 px) selama media tampil, entri `KONFIG.sumber` (dicetak `ambil`), dan baris kredit di deskripsi (`daftar`). Grade mesin menyatukan warna foto asli dengan ilustrasi Flow; foto hitam-putih (`hitamPutih: true`) cocok untuk tema arsip.

## 4. Catatan
- `media.json` di `_kerja` = asal-usul tiap media (judul, pembuat, tanggal, tautan, lisensi, segmen, kredit).
- Gambar ≤ 2400 px (`rakit --maks` memperkecil lagi saat ditanam); klip bisu H.264 ≤ 1080 px.
- `--potong` butuh `rembg` (belum terpasang di PC ini; memasangnya mengunduh model ±170 MB, tanya dulu). Tanpa itu pakai kartu/bingkai, jangan memotong foto setengah jadi.
