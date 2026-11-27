# Katalog tema — pilih tampilan untuk topik apa pun

Satu video = satu tema (`KONFIG.tema`). Tema mengatur **grade warna, 2 warna aksen, warna stabilo, musik sintesis**, dan (tema baru) **latar + gaya huruf bawaan**. Semua bisa ditimpa per video (`grade`, `palet`, `gayaTeks`, `latar` per adegan). Ditanya di dialog setup (pertanyaan **Tema**); bawaan "Otomatis dari topik".

| Tema | Tampilan | Cocok untuk | Latar & benda khas | Transisi tanda tangan | Musik bawaan | Huruf | Contoh |
|---|---|---|---|---|---|---|---|
| `arsip` | kertas krem, tint hangat, halftone, debu | sejarah 1900–1990, Indonesia yang terlupakan | kertas krem, koran + stabilo kuning, kartu foto, dokumen, meja kayu | `tutup` koran, `bingkai` ke foto, `kartu` | dokumenter | `judul` putih, `tahun` serif merah | `contoh/n250` |
| `dosir` | teal gelap kontras | misteri, kriminal, konspirasi, kebijakan kontroversial | dinding gelap bertekstur, meja interogasi, dokumen + cap merah, kartu foto ditempel, `bingkai` bentuk `kunci`/`peti` | `fokus`, `bingkai`, `tarik` pelan | misteri | `judul`, `elegan` | video "Kenapa Rokok Masih Legal" |
| `pasar` | hangat, aksen hijau + jingga | uang, bisnis, harga, saham, merek | grid, meja kantor, `sinar` hijau, grafik, label harga berayun, papan kapur | `jatuh` (uang/angka), `kartu` struk, `sentak` | dokumenter cepat | `padat`, `judul` | — |
| `teknologi` | biru dingin, cyan | gadget, internet, AI (versi gelap) | grid biru (blueprint), ruang gelap bercahaya layar, TV/layar, grafik progres | `dorong` ke layar, `bingkai` ke layar TV, `strip` | pulsa | `judul` | `contoh/ai-mikir` versi pertama |
| `tv` | garis layar, ceria | budaya pop, iklan, hiburan, tren 70–2000an | ruang keluarga, studio, `spiral`/`sinar`, TV kayu, stiker, label | `bingkai` ke TV, `kilat`, `putar` | ceria | `judul`, `stiker` | video "Siaran TV Pertama" |
| `modern` | warna pekat tanpa halftone | kejadian 2005–kini, berita, viral, tokoh publik (tanpa wajah AI) | kota, kantor kaca, HP/layar, kartu foto, grafik | `dorong`, `sentak`, `fokus` | dokumenter | `judul` | video "Wapres Gibran Mundur" |
| `perang` | pudar berdebu | perang, bencana, tragedi | abu-abu berdebu, peta, puing, dokumen rahasia, cap, angka korban (hati-hati, bersumber) | `kilat`, `sentak`, `tarik` | tegang | `judul`, `elegan` | — |
| `alam` | hangat natural | alam, hewan, geografi, sains, luar angkasa | lanskap, langit, kertas grid hijau, kartu foto spesimen, grafik | `tarik` (dekat → bentang alam), `bingkai` bulat (lensa), `fokus` | pad | `judul`, `elegan` | video "Efek Domino Hutan Bakau" |
| **`editorial`** | abu-putih bervinyet, monokrom + merah | penjelasan cerdas, opini, teknologi elegan, self-improvement | latar `editorial` (lengkungan + garis putus-putus) otomatis, kartu putih bersudut bulat, kotak sorot hitam, `kustom` UI | `geser`, `fokus`, `cocok` | pad | `serif` kecil di atas `tebal` besar; `judul` otomatis jadi Inter tebal hitam | `contoh/ai-mikir` (acuan pengguna 20 Nov 2026) |
| **`kartu`** | navy #051D40 bergrid + kartu kertas retro | tips, tutorial, produktivitas, seri edukasi bertokoh | latar navy grid otomatis, kartu kertas berselotip, mockup chat/UI, tokoh 3D (`aset/raka-3d/`) | `pop`, `kartu`, `sentak` | ceria | `judul`, `stiker` merah, `label`, `tangan` | `contoh/prompt-ai` (seri prompt AI, tokoh Raka 3D) |
| **ikut acuan** | sesuai video/gambar yang pengguna kirim | apa saja | dibedah `scripts/bedah_acuan.py` → `acuan.md` | sesuai acuan | sesuai acuan | sesuai acuan | — |

## Resep gaya dan 20 gaya → tema dasar
Resep (`sutradara-edit/pustaka/style/resep/`) memakai tema di atas sebagai dasar lalu menimpa `grade`, `palet`, `gayaTeks`, `latar`, dan `musik`:
| Resep | Tema dasar | Inti tampilan |
|---|---|---|
| Sinema Kasus | `modern` | malam biru dingin + satu merah, layar di dalam adegan, kartu tersangka |
| Legenda Gelap | `dosir` | api jingga vs bulan biru, papan kapur, polaroid bertali merah |
| Piksel Kertas | `kartu` | kertas zaitun, potongan kertas, huruf 8-bit, pita merah |
| Panggung Emas | `modern` | hijau botol + emas, serif raksasa di belakang subjek, konfeti |
| Arsip Pop | `tv` | warna selektif, label sobek, halaman warna datar, koran fiktif |
| Kaca Gradien | `editorial` | kisi putih, benda krom, tombol kaca, biru listrik |
| Panggung Korporat | `modern` | dunia abu + warna kuasa, grafik batang di kertas grafik, dokumen dicoret |
| Diorama Kreator | `modern` | dunia mainan voxel, benda di bawah sorot, layar chat biru, kartu krem berangka, satu benda kunci berpindah adegan |
20 gaya visual lain beserta tema dasarnya: `sutradara-edit/pustaka/style/gaya-visual.md`.

## Aturan pakai
- **Otomatis**: pilih dari kolom "Cocok untuk", lalu cek `riwayat.py lihat` supaya tidak sama dengan video terakhir (kecuali pengguna memilih tema sendiri atau sedang membuat seri).
- **Seri** (beberapa video satu tokoh/tema, mis. seri prompt AI): tema dan aset tokoh dipakai ulang dengan sengaja; aturan "beda dari video terakhir" tidak berlaku. Simpan aset seri di `aset/<seri>/` repo skill (gambar saja, tanpa video/audio).
- Tema baru yang dipakai berulang: tambahkan ke `TEMA` + `GRADE_DASAR` di `assets/templat.html` (boleh dengan `latar` dan `gayaTeks`), lalu ke tabel ini.
- Tema hanya tampilan: data tetap wajib bersumber, teks tetap ditulis mesin.
