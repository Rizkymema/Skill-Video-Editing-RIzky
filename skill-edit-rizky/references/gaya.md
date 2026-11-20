# Gaya kolase retro (dari bedah @earn.edits, 18 Nov 2026)

Laporan lengkap + 26 lembar bingkai: `D:\automation\Video AI\Video Refrensi\earn.edits\`. Ringkasnya: gambar diam realistis bernuansa arsip, dipotong jadi lapisan, dihidupkan kamera; **perpindahan dibawa gerak benda/kamera**, bukan potong biasa; informasi ditulis di benda (koran, dokumen, papan).

## 0. Menyesuaikan topik (supaya tiap video beda)
**Acuan visual dari pengguna menang** (sejak 20 Nov 2026): bila pengguna mengirim video/gambar acuan, tampilan mengikuti acuan itu (`acuan.md`), bukan tabel tema di bawah, dan aturan §0.4 tidak berlaku untuk tampilan; pola cerita tetap dipilih dari topik.

Permintaan pengguna 18 Nov 2026: skill ini dipakai untuk **topik apa saja** dan hasilnya **tidak boleh selalu sama**. Yang tetap hanya tekniknya (lapisan, kamera, perpindahan bermotivasi, data bersumber). Tampilan, alur cerita, benda, dan transisi khas dipilih dari topik, lalu dicek dengan riwayat video sebelumnya.

### 0.1 Tema (`KONFIG.tema`)
| Tema | Topik | Latar/pola yang cocok | Benda khas | Transisi tanda tangan | Musik bawaan |
|---|---|---|---|---|---|
| `arsip` | sejarah 1900–1990, Indonesia yang terlupakan | kertas krem, koran, meja kayu | koran + stabilo kuning, kartu foto, dokumen | `tutup` koran, `bingkai` ke foto, `kartu` | dokumenter |
| `dosir` | misteri, kriminal, konspirasi, kasus tak terpecahkan | dinding gelap bertekstur, meja interogasi, papan petunjuk | dokumen + cap merah, kartu foto ditempel, `bingkai` bentuk `kunci`/`peti` | `fokus`, `bingkai`, `tarik` pelan | misteri |
| `pasar` | uang, bisnis, harga, saham, merek | grid, meja kantor, `sinar` hijau | grafik, label harga berayun, papan kapur angka, stabilo hijau | `jatuh` (uang/angka), `kartu` struk, `sentak` | dokumenter cepat |
| `teknologi` | gadget, internet, AI, penemuan modern | grid biru (blueprint), ruang gelap bercahaya layar | TV/layar, grafik progres, cetak biru | `dorong` ke layar, `bingkai` ke layar TV, `strip` | pulsa |
| `tv` | budaya pop, iklan, hiburan, tren 70–2000an | ruang keluarga, studio, `spiral`/`sinar` | TV kayu, stiker, label | `bingkai` ke TV, `kilat`, `putar` | ceria |
| `modern` | kejadian 2005–sekarang, viral, tokoh publik (tanpa wajah AI) | warna pekat, kota, kantor kaca | HP/layar, grafik, kartu foto | `dorong`, `sentak`, `fokus` | dokumenter |
| `perang` | perang, bencana, tragedi | abu-abu berdebu, peta, puing | peta, dokumen rahasia, cap, angka korban (hati-hati, bersumber) | `kilat`, `sentak`, `tarik` | tegang |
| `alam` | alam, hewan, geografi, sains, luar angkasa | lanskap, langit, kertas grid hijau | kartu foto spesimen, grafik, papan | `tarik` (dekat → bentang alam), `bingkai` bulat (lensa), `fokus` | pad |
| `editorial` | penjelasan cerdas, opini, teknologi elegan, self-improvement | latar `editorial` otomatis (abu-putih, lengkungan, garis putus-putus) | kartu putih bersudut bulat, kotak sorot hitam, `kustom` UI | `geser`, `fokus`, `cocok` | pad |
| `kartu` | tips, tutorial, produktivitas, seri edukasi bertokoh | navy #051D40 bergrid otomatis | kartu kertas retro berselotip, mockup chat/tabel, tokoh 3D (`aset/raka-3d/`) | `pop`, `kartu`, `sentak` | ceria |

Ringkasan lengkap tiap tema (tampilan, huruf, contoh, aturan seri) ada di `tema.md`. Tema dipilih pengguna di dialog setup (pertanyaan **Tema**) atau otomatis dari kolom Topik.

Topik di luar tabel: pilih tema terdekat, lalu sesuaikan `palet` (dua warna aksen yang punya arti di topik itu: hijau uang, biru teknologi, merah bahaya) dan pola latar. Satu video = satu tema; warna aksen hanya dua.

### 0.2 Pola cerita (tulis `# pola: <nama>` di `naskah.txt`)
| Pola | Cocok untuk | Urutan |
|---|---|---|
| `balik` (bawaan, §2) | sejarah terlupakan, "ternyata sudah ada" | dunia dikenal → pembalik → pengenalan + 3 fakta → masalah → konsekuensi → hari ini + vonis |
| `misteri` | kriminal, kejadian aneh | pertanyaan/kejadian ganjil → petunjuk 1–2–3 (tiap petunjuk = benda) → pembalik → jawaban (atau "sampai hari ini belum terjawab" bila memang begitu) |
| `angka` | uang, bisnis, statistik | satu angka besar di detik 0 → dari mana asalnya → 3 pecahan angka → artinya buat penonton → vonis |
| `kronologi` | bencana, peristiwa satu hari, penemuan | tanggal/jam di layar demi tanggal (hitung mundur/maju) → titik balik → akibat → hari ini |
| `duel` | persaingan merek/negara/tokoh | A vs B diperkenalkan → 3 ronde (tiap ronde satu fakta + skor) → pemenang tak terduga → pelajaran |
| `mitos` | sains, kesehatan, kepercayaan umum | yang dipercaya banyak orang → bukti 1–2 → fakta sebenarnya (bersumber) → cara mengingatnya |

### 0.3 Kartu identitas visual (wajib di Tahap 2, sebelum aset Flow)
Tulis 6 baris di chat dan di kepala `konfig.js`: **tema** · **pola cerita** · **2 warna aksen** · **benda khas topik** (1–2 benda bertulisan yang jadi "wajah" video, mis. struk belanja untuk harga, peta untuk perang) · **transisi tanda tangan** (satu perpindahan khas yang muncul di momen terpenting, mis. `bingkai` ke layar TV untuk topik siaran) · **beda dari video terakhir** (apa yang diganti, dari `riwayat.py lihat`). Gaya prompt Flow ikut tema (`flow.md`: `arsip`/`modern`/`gelap` + suasana tema).

### 0.4 Aturan beda dari video sebelumnya
1. Awal Tahap 2: `python -X utf8 scripts/riwayat.py lihat` (riwayat di `Hasil Video\_seri\edit-rizky\riwayat.json`).
2. Jangan mengulang dari video terakhir: tema (kecuali topik menuntut; maka ganti aksen + pola latar), pola cerita, perpindahan pembuka (adegan ke-2), perpindahan penutup, transisi tanda tangan, bentuk hook (kalimat pertama), benda khas utama.
3. Dalam satu video: satu jenis perpindahan maks 3 kali, tidak dua kali berturut-turut (cek memberi saran), ≥ 6 jenis.
4. Variasikan juga: posisi teks (atas/tengah/bawah zona aman), gaya teks utama (`judul` · `padat` · `elegan` · `tangan`), preset kamera, warna latar pola.
5. Musik sintesis otomatis berbeda per judul (`benih`); tetap ganti jenis musik bila tema sama dengan video sebelumnya.
6. Setelah video jadi (Tahap 5): `python -X utf8 scripts/riwayat.py catat <_kerja>`.

## 1. Contoh topik dari akun acuan (topik lain tetap boleh, lihat §0)
| Kategori | Contoh pola |
|---|---|
| Teknologi yang datang terlalu cepat | "Sebelum X, sudah ada Y tahun 19xx" (IBM Simon 1994, N250 1995) |
| Sejarah aneh tapi nyata | pengadilan mayat (Cadaver Synod), mumi Ötzi, D. B. Cooper |
| Uang/bisnis besar | uang tunai Buffett, krisis 1998, harga yang meledak |
| Benda/merek dengan kisah tersembunyi | lukisan The Scream, roket jadi mobil |
| Indonesia yang terlupakan | proyek, penemuan, kejadian dengan angka dan tanggal jelas |

Syarat: ada **angka/tanggal/nama yang bisa dicek** (lihat `riset.md`) dan ada **benda yang bisa difoto** (pesawat, koran, gedung, uang).

## 2. Naskah: pola `balik` 6 ketukan (±100–110 kata untuk 45 dtk; pola lain di §0.2)
| Ketukan | Fungsi | Contoh N250 |
|---|---|---|
| 1 Dunia dikenal (hook, ≤ 3 dtk) | hal yang penonton alami hari ini | "Pesawat yang kamu naiki mudik, hampir pasti buatan luar negeri." |
| 2 Pembalik | "padahal / sebelum itu" + tahun | "Padahal tahun 1995, Indonesia sudah terbang dengan pesawat buatannya sendiri." |
| 3 Pengenalan + 3 fakta | nama + tempat, lalu tiga ketukan angka | nama/IPTN · 10 Agustus 55 menit · 50 penumpang fly-by-wire · prototipe kedua |
| 4 Masalah | kalimat pendek sendiri ("Tapi lalu, …") → kartu teks | "Tapi lalu, krisis datang." |
| 5 Konsekuensi | angka + benda (dokumen, cap, grafik) | LoI IMF, US$43 miliar, dana dihentikan, separuh uji terbang |
| 6 Hari ini + vonis | keadaan sekarang + satu kalimat pendek yang membalik | "Pesawatnya sudah jadi. Yang tidak siap, zamannya." |

Kalimat pendek (≤ 14 kata), angka ditulis angka, tanpa salam/"tahukah kamu", tanpa ajakan follow di narasi. Vonis jangan meniru kalimat mereka ("Sometimes the future arrives too early").

## 3. Storyboard dan tempo
- **Satu adegan ±2–3 dtk** (N250: 17 adegan / 46,5 dtk). Ganti adegan di awal kalimat atau di kata kunci (`'L05.w4'`).
- Dalam adegan: **sesuatu baru tiap ±1–1,5 dtk** (teks meluncur, benda masuk, sorot stabilo, angka bergulir, cap).
- Kamera tidak pernah diam (preset bawaan `dorong`; ganti-ganti `dorong-kuat`, `mundur`, `naik`, `turun`, `kiri`, `kanan`, `guling`, atau keyframe).
- **Perpindahan berganti-ganti, ≥ 6 jenis per video**, potong keras ≤ 3 (hanya lompatan zaman).
- Tabel storyboard: `# · waktu · gambar/latar · teks layar · benda · masuk · kamera`.

## 4. Katalog perpindahan (`masuk` di adegan)
**Tata bahasa** (bedah ulang 18 Nov 2026, video wabah @earn.edits, 20 perpindahan dalam 42,7 dtk, lembar bingkai di scratchpad sesi; ringkasannya di sini):
1. **Momentum, bukan efek.** Gerak adegan lama dipercepat sampai titik potong (zoom, tilt, putar, benda keluar bawah), dipotong di puncak kecepatan, adegan baru melanjutkan kecepatan itu lalu melambat ±0,4–0,7 dtk. Tidak ada silang pudar.
2. **Kedalaman.** Saat kamera melesat, lapisan depan (kepala penonton, mik, tangan) bergerak paling jauh dan paling kabur; adegan baru mulai tidak fokus lalu menajam.
3. **Subjek datang dari dekat lensa.** Tokoh/benda utama masuk besar dan kabur dari tepi, lalu melayang mundur ke tempatnya (`masuk: 'terbang'`). Latar sering tampil kosong ±0,3 dtk dulu.
4. **Adegan berubah jadi benda di adegan berikut.** Lab mundur jadi foto berbingkai di koran; berita koran → layar TV; ruang → lubang kunci (`bingkai`).
5. **Panel.** Adegan baru naik sebagai panel bersudut bulat, isinya menyusul belakangan (`tutup`).

| Jenis | Kapan | Bukti di acuan |
|---|---|---|
| `dorong` (+`titikMasuk`) | menyelam ke detail di adegan lama (foto koran, layar, jendela) lalu mendarat di tempatnya | ruang TV → dinding foto (23,7 dtk) |
| `tarik` | mundur dari detail ke gambaran besar; adegan baru terus mundur | peti → rumah sakit + kerumunan (3,0 dtk) |
| `sentak` (+`arahMasuk`) | whip ke kartu teks/angka atau tempat baru | teks → gedung + bendera (29,3 dtk) |
| `putar` | kekacauan, krisis, "dunia terbalik" | koran keluar berputar → grid biru (14,6 dtk) |
| `bingkai` (+`bingkai.lapis`) | **transisi tanda tangan**: adegan jadi foto/layar/lubang kunci di adegan berikut | lab → foto heksagon di koran (11,0 dtk), lubang kunci (35,5 dtk) |
| `tutup` (+`arahMasuk`) | adegan baru naik menutupi (koran, dokumen, layar) | kerja lab naik menutupi teks tanggal (8,7 dtk), ruang retro (39,0 dtk) |
| `buka` | benda lama tergeser keluar, adegan baru sudah di belakang | koran turun keluar (14,0 dtk) |
| `fokus` | ganti tempat dengan tenang, "membuka mata" | koran kabur → TV (21,4 dtk), merah (34,2 dtk) |
| `geser` (+`arahMasuk`) | dua adegan bergeser bersama | tilt langit → penggali kubur |
| `jatuh` | adegan baru menghantam dari atas (dramatis) | HP ke timbangan |
| `lempar` | adegan lama dilempar ke samping | kartu potret paus |
| `kartu` | adegan lama mengecil jadi foto lalu tergeser ("arsip") | sidang → foto di kertas |
| `strip` | membuka gambar teknis/peluncuran | roket (Tesla) |
| `iris` | penutup / fokus satu hal | lensa bulat (Buffett) |
| `kilat` | potong di ketukan dengan kilatan | "YOU ARE GUILTY" |
| `cocok` (+`cocok: { dari, ke }`) | **benda yang sama bertahan saat dunia berganti**: amplop di tangan berpindah jadi surat di meja, foto di koran jadi foto di dinding, bulan tetap di langit saat latar berganti. Benda melayang dari tempatnya di adegan lama ke tempatnya di adegan baru (bila gambarnya beda, saling melebur di jalan); latar lama kabur, latar baru menajam | reel DffBJweOo9e (benda tetap, dunia berganti); bulan + roket di acuan wabah |
| `zoom`, `lebur` | hanya bila tak ada yang lain cocok | — |

Di dalam adegan, lapisan sendiri punya `masuk`: `terbang` (dari dekat lensa, besar + kabur → tajam), `geser` (dari tepi + blur gerak), `jatuh` (memantul + guncang), `lempar` (berputar), `pop`, `tumbuh`, `kabur`, `naik`, `sapu`, `cap`. Lapisan depan (mik, kepala penonton, tangan) diberi `z` 1,6–2,4 supaya ikut melesat saat perpindahan.

## 4a. Lapisan yang hidup dan utuh (Kolase 1.2, permintaan pengguna 18 Nov 2026 + reel acuan DffBJweOo9e)
Masalah yang diperbaiki: potongan tangan berlengan terlihat terpotong di tengah layar, foto berganti datar, potongan diam seperti stiker.

**1. Tidak ada objek yang terpotong di tengah layar.** Potongan yang di gambar aslinya terpotong di satu sisi (tangan + lengan baju, badan setengah, kerumunan, mobil yang keluar bingkai) harus menempel ke tepi layar di sisi itu. Mesin mendeteksinya sendiri (`potong` dari piksel tepi gambar) dan **menggeser lapisan sampai garis potongnya di luar layar** (`jangkar`), juga selama kamera bergerak/berputar. Sisi yang terlalu jauh dari tepi (> 45% layar, mis. lengan menunjuk ke kiri padahal tangannya di kanan) tidak menyeret lapisan keluar layar; sisi itu dipudarkan halus. Tulis `jangkar: 'bawah'` (atau `['bawah', 'kiri']`) untuk memaksa, `jangkar: false` untuk mematikan. Cek memberi saran bila geserannya > 140 px atau ada sisi yang dipudarkan: atur `x`/`y`/`putar`/`lebar` supaya potongan memang keluar dari tepi itu. Benda utuh (amplop, palu, kursi) dibuat **utuh di Flow** dengan ruang hijau di semua sisinya (`flow.md`).

**2. Rig: potongan bergerak seperti hidup, bukan stiker.** `rig` membengkokkan gambar dengan jaring segitiga (seperti Puppet Pin di After Effects), jadi bagian yang menempel tetap diam dan ujungnya bergerak:
| Rig | Untuk | Contoh |
|---|---|---|
| `'napas'` | tokoh/siluet berdiri, dada naik-turun halus | `rig: 'napas'` |
| `'goyang'` | tanaman, tiang bendera, tokoh berdiri bergoyang dari kaki (`poros` bawah) | `rig: { jenis: 'goyang', sudut: { amp: 1.3, periode: 4.2 } }` |
| `'tekuk'` | tangan memegang benda: pergelangan menekuk dari `poros`, lengan diam | `rig: { jenis: 'tekuk', poros: [.5, .62], sudut: { amp: 4, periode: 2.6 } }` |
| `'angguk'` | kepala mengangguk (poros di leher) | `rig: 'angguk'` |
| `'kibar'` | bendera, kain, kertas tertiup | `rig: { jenis: 'kibar', dari: 'kiri', amp: .03 }` |
Gabungkan dengan daftar (`rig: ['napas', { jenis: 'goyang', fase: .3 }]`). Sudut boleh keyframe `[[t, derajat, ease], ...]` untuk gerak sekali (tangan menyerahkan amplop). Rig tidak dipakai pada `urutan` (klip video sudah bergerak). Pakai pada **setiap potongan makhluk hidup** dan benda lentur; benda keras cukup `hidup`/`ayun`.

**3. Pola berlapis dari reel acuan** (foto realistis ditumpuk, bukan diganti):
- **Kerumunan bertingkat**: 2–3 potongan kerumunan/penonton di `z` berbeda (0,8 · 1,3 · 1,9) yang naik dari bawah satu per satu (`masuk: { gaya: 'geser', dari: 'bawah' }`, jeda 0,15 dtk), semuanya `jangkar: 'bawah'`; baris depan paling besar dan paling kabur saat kamera bergerak.
- **Benda tetap, dunia berganti**: benda kunci (amplop, foto, koin, kursi) dipindah antar-adegan dengan `masuk: 'cocok'`, bukan dimunculkan ulang.
- **Kilau di puncak**: kata kunci/benda yang "menyala" (palu diketuk, keputusan, angka puncak) diberi `efek: [{ jenis: 'kilau', t, titik: [x, y] }]` (sinar + cahaya, bunyi boom otomatis).
- **Kartu foto asli di atas ilustrasi**: foto/video nyata (dari `ambil_media.py`) tampil sebagai kartu/layar miring berbayangan di atas pelat ilustrasi, dengan label kredit di bawahnya, lalu pindah dengan `cocok`/`bingkai`.
- **Teks di antara lapisan**: judul diletakkan di belakang potongan depan (urutan `lapis`: latar → teks → potongan) supaya terlihat bertumpuk dalam ruang.

## 4b. Klip gerak dan efek ala After Effects (Kolase 1.3)
Rincian di `klip.md`. Ringkasnya:
- **Foto dulu, klip hanya bumbu.** Acuan ±90% gambar diam; klip Flow (mode Foto + klip) hanya di 1–4 momen aksi (orang beraksi, air/api bergerak, kendaraan, kerumunan), ≤ 30% durasi. Teknik paling mirip acuan: **foto hidup** (foto diam tiba-tiba bergerak tepat di kata kunci).
- **Potongan bergerak**: tokoh/benda dari klip berlatar hijau di atas foto latar diam, berbayangan, ditempel ke tepi bila terpotong.
- **Efek bermakna, bukan hiasan**: cahaya bocor (kenangan/pembuka), film terbakar (akhir babak, lompatan zaman), glitch (berita/fakta mengejutkan/teknologi), garis gerak (angka mendarat), partikel (debu arsip, hujan, bawah air, konfeti/koin uang), sorot (menunjuk tokoh), coretan spidol (menandai bukti di foto), kilap (kartu/HP/koin), miring 3D (kartu foto berputar), HP/notifikasi/balon (berita viral, chat, kutipan). 1–2 per adegan; satu efek tanda tangan per video, dicatat di kartu identitas visual.

## 5. Teks dan benda
| Unsur | Gaya | Pakai untuk |
|---|---|---|
| Judul `gaya: 'judul'`, `anim: 'luncur'`, `ikut: true` | Archivo Black kapital putih berbayang, kata meluncur saat diucapkan; `*kata*` = kuning, `^kata^` = besar | kalimat kunci, kartu "TAPI…" |
| Tahun `gaya: 'padat'`, `anim: 'jatuh'` | Anton besar, huruf jatuh memantul | 1995, 1998 |
| `gaya: 'tahun'` | serif miring merah tua | tanggal di kertas krem |
| `angka: { dari, ke }` | odometer bergulir, digit baru beraksen | 55 MENIT, 50, 381 |
| `gaya: 'stiker'` / `'label'` | kotak merah bertepi putih / pil hitam | IPTN · BANDUNG, FLY-BY-WIRE, nama tempat |
| `benda: koran` | kop + tanggal + judul + foto (hitam-putih) + kolom isi dari naskah; `sorot` stabilo | headline kejadian |
| `benda: dokumen` | ketikan mesin, `sorot` per baris (kuning/merah) | perjanjian, catatan, syarat |
| `benda: cap` (`masuk: 'cap'`) | stempel merah bertekstur | DIHENTIKAN, DITOLAK |
| `benda: kartu` | foto berbingkai + pita keterangan | prototipe, tokoh, tanggal |
| `benda: grafik` | batang / progres di kertas grafik | perbandingan, persen |
| `benda: papan` | papan tulis kapur ditulis huruf demi huruf | angka pasar |
| `benda: label` (+`ayun`) | label harga berayun | harga, biaya |
| `benda: tv` | TV kayu, gambar di layar bergaris | arsip siaran |

**Tanpa subtitle di bawah** (bawaan sejak 18 Nov 2026, permintaan pengguna): kata kunci sudah tampil sebagai teks kinetik di layar. Subtitle pil hanya bila pengguna memintanya (`subtitle: { gaya: 'pil' }`, ±62% tinggi). Teks judul di 15–45% tinggi.

## 6. Checklist lembar kontak
1. Bingkai 0–1 dtk sudah memperlihatkan tempat + satu teks/benda (hook terbaca tanpa suara).
2. Tiap adegan punya ≥ 2 lapisan bergerak berbeda (latar + subjek/teks), potongan berbayangan.
3. Tidak ada teks terpotong tepi, tidak ada teks di bawah 70% atau di kanan bawah (tombol).
4. Angka/tanggal di layar sama persis dengan sumber (`KONFIG.sumber`).
5. Perpindahan terlihat bergerak (bingkai tengahnya kabur/miring), bukan potong.
6. Warna seragam (grade dari tema), hanya dua warna aksen tema.
7. Gambar Flow tidak aneh (tangan, wajah, teks tak sengaja). Bila aneh: buat ulang aset itu saja.
8. Bingkai tengah perpindahan bermomentum kabur/miring searah gerak, lapisan depan paling kabur; adegan baru mulai tidak fokus.
9. Kartu identitas visual (§0.3) terlihat di hasil: benda khas dan transisi tanda tangan muncul, berbeda dari video terakhir.
10. Tidak ada potongan yang ujungnya terpotong lurus di tengah layar (lengan, badan, kerumunan menempel ke tepi; §4a).
11. Potongan makhluk hidup/benda lentur bergerak dengan `rig`; tidak ada subtitle di bawah kecuali diminta.
12. Foto/video nyata punya label kredit di layar selama tampil dan tercatat di `media.json`.
13. Klip Flow (bila ada) mulus dari fotonya, tanpa wajah/tangan berubah bentuk; efek tidak menutupi teks/data.
