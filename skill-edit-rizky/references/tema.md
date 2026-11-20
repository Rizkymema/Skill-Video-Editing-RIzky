# Katalog tema — pilih tampilan untuk topik apa pun

Satu video = satu tema (`KONFIG.tema`). Tema mengatur **grade warna, 2 warna aksen, warna stabilo, musik sintesis**, dan (tema baru) **latar + gaya huruf bawaan**. Semua bisa ditimpa per video (`grade`, `palet`, `gayaTeks`, `latar` per adegan). Ditanya di dialog setup (pertanyaan **Tema**); bawaan "Otomatis dari topik".

| Tema | Tampilan | Cocok untuk | Latar & benda khas | Huruf | Contoh |
|---|---|---|---|---|---|
| `arsip` | kertas krem, tint hangat, halftone, debu | sejarah 1900–1990, Indonesia yang terlupakan | koran + stabilo, kartu foto, dokumen | `judul` putih, `tahun` serif merah | `contoh/n250` |
| `dosir` | teal gelap kontras | misteri, kriminal, kasus, kebijakan kontroversial | dokumen + cap merah, kartu foto ditempel | `judul`, `elegan` | video "Kenapa Rokok Masih Legal" |
| `pasar` | hangat, aksen hijau + jingga | uang, bisnis, harga, saham | grafik, label harga, papan kapur | `padat`, `judul` | — |
| `teknologi` | biru dingin, cyan | gadget, internet, AI (versi gelap) | layar, cetak biru, grid biru | `judul` | `contoh/ai-mikir` versi pertama |
| `tv` | garis layar, ceria | budaya pop, iklan, tren | TV kayu, stiker | `judul`, `stiker` | video "Siaran TV Pertama" |
| `modern` | warna pekat tanpa halftone | kejadian 2005–kini, berita, tokoh publik | HP, kartu foto, grafik | `judul` | video "Wapres Gibran Mundur" |
| `perang` | pudar berdebu | perang, bencana, tragedi | peta, dokumen rahasia | `judul`, `elegan` | — |
| `alam` | hangat natural | alam, hewan, sains, lingkungan | lanskap, grafik | `judul`, `elegan` | video "Efek Domino Hutan Bakau" |
| **`editorial`** (baru) | abu-putih bervinyet, monokrom + merah | penjelasan cerdas, opini, teknologi elegan, self-improvement | latar `editorial` (lengkungan + garis putus-putus) otomatis, kartu putih bersudut bulat, kotak sorot hitam | `serif` kecil di atas `tebal` besar; `judul` otomatis jadi Inter tebal hitam | `contoh/ai-mikir` (acuan pengguna 20 Nov 2026) |
| **`kartu`** (baru) | navy #051D40 bergrid + kartu kertas retro | tips, tutorial, produktivitas, seri edukasi bertokoh | latar navy grid otomatis, kartu kertas berselotip, mockup chat/UI, tokoh 3D | `judul`, `stiker` merah, `label`, `tangan` | `contoh/prompt-ai` (seri prompt AI, tokoh Raka 3D) |
| **ikut acuan** | sesuai video/gambar yang pengguna kirim | apa saja | dibedah `scripts/bedah_acuan.py` → `acuan.md` | sesuai acuan | — |

## Aturan pakai
- **Otomatis**: pilih dari kolom "Cocok untuk", lalu cek `riwayat.py lihat` supaya tidak sama dengan video terakhir (kecuali pengguna memilih tema sendiri atau sedang membuat seri).
- **Seri** (beberapa video satu tokoh/tema, mis. seri prompt AI): tema dan aset tokoh dipakai ulang dengan sengaja; aturan "beda dari video terakhir" tidak berlaku. Simpan aset seri di `aset/<seri>/` repo skill (gambar saja, tanpa video/audio).
- Tema baru yang dipakai berulang: tambahkan ke `TEMA` + `GRADE_DASAR` di `assets/templat.html` (boleh dengan `latar` dan `gayaTeks`), lalu ke tabel ini.
- Tema hanya tampilan: data tetap wajib bersumber, teks tetap ditulis mesin.
