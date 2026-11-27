# Katalog tema — pilih tampilan untuk topik apa pun (10 tema dasar + 8 tema gaya dari reel acuan)

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

## 8 tema gaya dari reel acuan (sejak 27 Nov 2026, tertanam di mesin)
Hasil bedah reel @earn.edits dan @t1mline (permintaan pengguna: "skill saya diupdate agar ada beberapa style"). **Satu kata** di konfig, mis. `tema: 'panggung-korporat'`, langsung memasang grade, warna aksen kata (`*…*`), warna stiker/cap, latar bawaan (adegan tanpa `latar`), dan gaya huruf. Musik tidak otomatis: tulis `musik: { sintesis: '<musik bawaan>' }` atau pakai berkas Epidemic. Semua tetap bisa ditimpa (`grade`, `palet`, `gayaTeks`, `latar` per adegan).

| Tema | Tampilan | Cocok untuk | Latar bawaan | Huruf | Transisi tanda tangan | Musik bawaan | Rincian resep |
|---|---|---|---|---|---|---|---|
| `sinema-kasus` | malam biru dingin, satu aksen merah, layar di dalam adegan | kriminal siber, skandal, penipuan, kasus viral | polos biru-hitam | judul Inter tipis putih, angka abu, label tanpa kotak | `dorong` ke layar, bentuk/`iris`, adegan masuk ke TV (`bingkai`) | pulsa 96 | `sinema-kasus.md` |
| `legenda-gelap` | api jingga vs bulan biru, papan kapur, polaroid bertali merah | mitos, legenda Nusantara, asal-usul tradisi, sejarah kelam | kertas arang | judul kuning api, serif krem, tulisan tangan krem | lensa `bingkai` bulat, lingkungan sama musim berganti (`fokus`), `tutup` | misteri 76 | `legenda-gelap.md` |
| `piksel-kertas` | kertas zaitun, potongan kertas, pita merah, metafora benda | produktivitas, karier, kesehatan mental kerja, tips, gaming | kertas zaitun | judul krem kapital, pita merah | `strip`/`glitch` pendek, benda turun berayun, `cocok` layar | jenaka 92 | `piksel-kertas.md` |
| `panggung-emas` | hijau botol + emas, serif raksasa di belakang subjek | pengumuman, peringkat, giveaway, prestasi, peluncuran | polos hijau botol | serif kapital (elegan), Inter tipis (judul) | `sentak`, `terbang`, `kilau` di payoff | tegang 104 | `panggung-emas.md` |
| `arsip-pop` | iklan majalah lama: warna selektif, label sobek, halaman warna datar | penemuan aneh, rekor, sejarah produk, kuliner, sains populer | polos merah | judul putih tidak kapital, label biru | `cocok` benda tetap zaman berganti, `iris` ke tekstur bahan | ceria 124 | `arsip-pop.md` |
| `kaca-gradien` | kisi putih, benda krom, tombol kaca, biru listrik | aplikasi, AI, fitur produk, fintech, tutorial alat | kisi putih | Inter sedang gelap, label kaca | `cocok`/`kartu` tukar, `iris` dari tombol | pulsa 96 | `kaca-gradien.md` |
| `panggung-korporat` | dunia abu + warna kuasa, grafik di kertas grafik, panggung pesaing | naik-turun perusahaan, persaingan, ekonomi, karier tokoh | polos panggung gelap (adegan data: `latar: { pola: 'grid', warna: '#ece6d6', warnaGaris: 'rgba(40,60,90,.10)', jarak: 44 }` + teks `gaya: 'serif'`/`'tebal'` gelap) | pita jingga Anton, angka kuning, kesimpulan Inter tipis | `cocok` benda kuasa, `tarik`, warna hilang (`hitamPutih`) | dokumenter 84 | `panggung-korporat.md` |
| `diorama-kreator` | dunia mainan voxel, benda di bawah sorot, layar chat biru, kartu krem berangka | alat AI, proses kreatif, mitos "tombol ajaib", produk digital sendiri | polos panggung gelap | Inter tipis putih, kata tulisan tangan merah | `dorong` menembus lensa, `cocok` benda kunci, `bingkai` masuk ke layar | pulsa 118 | `diorama-kreator.md` |

Rincian resep (urutan adegan khas, contoh lapisan konfig, penerapan untuk topik lain, yang tidak boleh disalin) ada di `sutradara-edit/pustaka/style/resep/<nama>.md`; contoh video jadi: Kodak (27 Nov 2026, Panggung Korporat). 20 gaya visual umum lain beserta tema dasarnya: `sutradara-edit/pustaka/style/gaya-visual.md`.

## Aturan pakai
- **Otomatis**: pilih dari kolom "Cocok untuk", lalu cek `riwayat.py lihat` supaya tidak sama dengan video terakhir (kecuali pengguna memilih tema sendiri atau sedang membuat seri).
- **Seri** (beberapa video satu tokoh/tema, mis. seri prompt AI): tema dan aset tokoh dipakai ulang dengan sengaja; aturan "beda dari video terakhir" tidak berlaku. Simpan aset seri di `aset/<seri>/` repo skill (gambar saja, tanpa video/audio).
- Tema baru yang dipakai berulang: tambahkan ke `TEMA` + `GRADE_DASAR` di `assets/templat.html` (boleh dengan `latar` dan `gayaTeks`), lalu ke tabel ini.
- Tema hanya tampilan: data tetap wajib bersumber, teks tetap ditulis mesin.
