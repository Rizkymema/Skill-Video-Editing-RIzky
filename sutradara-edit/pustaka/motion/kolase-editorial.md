# Kolase dan animasi editorial: gambar diam jadi hidup

> MOTION · dipakai di langkah 6–8 dan 14 · terkait: `../cinematic/kamera.md` (parallax), `transisi.md`, `prinsip-animasi.md`, `../visual/komposisi.md`, `../style/gaya-visual.md` (Collage, Newspaper/Magazine, Handcrafted, Grunge), `../style/bahasa-earnedits.md` · implementasi mesin: `skill-edit-rizky/references/gaya.md` §4a, `flow.md`, `klip.md`

Prinsip inti:
1. **Lapisan, bukan gambar.** Satu adegan kolase = latar + subjek + (benda/teks) + (depan). Tiap lapisan punya kedalaman sendiri; kedalaman itulah yang membuat foto diam terasa ruang.
2. **Benda fisik punya hukum fisik.** Kertas punya bayangan, tebal, tekstur, sedikit miring, jatuh dengan memantul pelan, tidak melayang sempurna. Kolase yang terlalu bersih terlihat seperti templat.
3. **Satu fokus per bingkai.** Kolase mudah ramai. Maks 3–5 unsur yang terlihat bersamaan; satu paling besar/tajam/terang.
4. **Gerak kecil terus-menerus, gerak besar jarang.** Napas, ayun, kamera pelan sepanjang waktu; masuk/keluar besar hanya di kata kunci.
5. **Tidak ada yang terpotong di tengah layar.** Potongan utuh dengan margin, atau sengaja masuk dari tepi layar.

## 1. Bahan: dua jenis aset
| Jenis | Isi | Fungsi | Di mesin Kolase |
|---|---|---|---|
| Pelat | latar penuh 9:16, ruang kosong sepertiga atas untuk judul | tempat/suasana | `{ gambar: 'kode' }` tanpa ukuran = pelat penuh (lebih 1,16 untuk kamera) |
| Potongan | satu subjek di latar hijau polos → PNG transparan | tokoh, tangan, benda, kerumunan | `{ gambar: 'kode', x, y, lebar, z, bayangan }`; buat di Flow (`skill-edit-rizky/references/flow.md` §2) |
| Foto nyata | foto berlisensi (Commons/NASA) atau kiriman pengguna | bukti rupa asli | `benda: { jenis: 'kartu', gambar }` (`data-media.md` §3) |
| Benda bertulisan | koran, dokumen, kartu, papan, label, cap, stiker | informasi yang ditulis mesin (selalu benar) | `benda: { jenis: 'koran'\|'dokumen'\|'kartu'\|'papan'\|'label'\|'cap' }` |

Patokan satu video 45 dtk: 9–12 pelat/foto + 4–8 potongan + 4–8 benda bertulisan.

## 2. Teknik
### Kolase foto (photo collage)
- **Kapan**: membandingkan beberapa hal, memperkenalkan banyak tokoh/benda, "dunia" sebuah topik dalam satu bingkai.
- **Kenapa**: satu bingkai bercerita lebih padat daripada tiga potongan berturut-turut; penonton melihat hubungan.
- **Cara**: susun 3–5 unsur dengan ukuran berbeda nyata (1 besar, 2 sedang, 1–2 kecil), miring berbeda (−6° s/d +6°), saling tumpang 10–25%, z berbeda (0,8 · 1,2 · 1,7). Masuk bergiliran 0,12–0,25 dtk, dari unsur terbesar.
- **Hindari**: semua unsur sama ukuran (grid rapi = slideshow); semua masuk bersamaan; lebih dari 5 unsur.
- **Di mesin Kolase**: beberapa lapisan `gambar`/`benda: kartu` dengan `putar`, `z`, `bayangan: .35–.5`, `masuk: 'lempar'` atau `{ gaya: 'jatuh', guncang: .3 }`, `t` bergiliran.

### Animasi cutout (cutout animation)
- **Kapan**: tokoh/benda harus "berakting" tanpa klip video: mengangguk, menunjuk, bernapas, bendera berkibar, tangan menyerahkan amplop.
- **Kenapa**: potongan diam terasa stiker; gerak sendi kecil membuatnya makhluk hidup.
- **Cara**: potongan dengan sendi terlihat (pergelangan, leher, pinggang), pose netral. Gerak sendi kecil: napas ±1–2%, angguk ±2–4°, tekuk pergelangan ±3–6°. Gerak sekali (menyerahkan) memakai keyframe dengan antisipasi (mundur sedikit dulu, lalu maju, lalu settle; `prinsip-animasi.md`).
- **Hindari**: memutar seluruh potongan tokoh seperti jarum jam; gerak sendi yang besar (rig membengkokkan gambar, lebih dari ±8° terlihat karet).
- **Di mesin Kolase**: `rig: 'napas' | 'goyang' | 'tekuk' | 'angguk' | 'kibar'` atau objek `{ jenis, poros, sudut, amp, periode }`, keyframe sudut `[[t, derajat, ease], …]` (`gaya.md` §4a.2). Tidak untuk `urutan`.

### Animasi kertas (paper animation)
- **Kapan**: gaya Handcrafted, Collage, Newspaper; topik arsip, sekolah, catatan, perencanaan.
- **Kenapa**: kertas langsung terbaca "buatan tangan", hangat, nyata; lawan dari tampilan AI yang licin.
- **Cara**: kertas krem/putih tidak murni (#ece2c8, #f3ead6), serat + noda halus, bayangan jatuh lembut (offset 10–20 px, blur 30–50), sudut sedikit melengkung, selotip/klip/peniti sebagai pengait. Gerak: jatuh dengan memantul kecil, bergeser dengan sedikit putar, kibar ujung bila tertiup.
- **Hindari**: kertas putih bersih #ffffff dengan bayangan hitam pekat; kertas yang melayang tanpa bayangan.
- **Di mesin Kolase**: `latar: { pola: 'kertas', tua: .4 }` / `'garis'` / `'grid'`; `benda: kartu`/`dokumen`; `rig: { jenis: 'kibar', dari: 'kiri', amp: .02 }` untuk ujung kertas; kartu kertas berselotip lewat benda `kustom` (contoh `pKertas` di `contoh/prompt-ai.konfig.js`).

### Tata letak majalah (magazine layout)
- **Kapan**: gaya Luxury Editorial, Cinematic Editorial, Newspaper/Magazine; profil tokoh, kutipan, angka besar.
- **Kenapa**: kisi majalah memberi hierarki instan dan kesan "dikurasi".
- **Cara**: kisi 6 kolom 9:16 (margin 60–80 px), judul besar menembus kolom, foto boleh keluar batas (bleed) di satu sisi, teks kecil sejajar kisi, satu warna aksen. Huruf: serif besar + sans kecil (`../type/tipografi-kinetik.md` §Editorial). Ruang kosong ≥ 30% bingkai.
- **Hindari**: semua di tengah; lebih dari 2 keluarga huruf; teks kecil yang tak terbaca di HP (< 34 px pada 1080 lebar).
- **Di mesin Kolase**: gaya teks `serif` di atas `tebal`, `sorot` untuk kata penting, `rata: 'kiri'`, latar `editorial` atau `polos`; foto `benda: kartu` atau `gambar` dengan `x` dekat tepi supaya bleed (`jangkar` otomatis bila potongan menyentuh tepi).

### Komposisi koran (newspaper composition)
- **Kapan**: kejadian bersejarah, berita, "dunia tahu tentang ini pada tanggal…".
- **Kenapa**: koran adalah bukti zaman: tanggal + judul + foto dalam satu benda.
- **Cara**: kop fiktif, tanggal nyata, judul 2–5 kata, foto hitam-putih, kolom isi samar. Kamera mendorong dari koran utuh ke judul/foto, stabilo menyapu judul saat diucapkan, lalu `bingkai`/`dorong` masuk ke foto koran.
- **Hindari**: nama koran nyata (Kompas, Tempo); judul panjang; isi kolom yang terbaca sebagai teks salah.
- **Di mesin Kolase**: `benda: { jenis: 'koran', nama, tanggal, judul, foto, isi, sorot: [{ baris: 'judul', t }] }` + `masuk: 'tutup'`/`'jatuh'`; transisi `bingkai` (adegan lama jadi foto di koran) atau `dorong` dengan `titikMasuk` di foto koran.

### Fotografi berlapis (layered photography) dan parallax foto
- **Kapan**: hampir setiap adegan kolase.
- **Kenapa**: parallax (lapisan dekat bergerak lebih jauh daripada lapisan jauh) adalah ilusi kedalaman termurah dan paling meyakinkan.
- **Cara**: pisahkan latar (z 0,2–0,4), subjek (z 1), depan (z 1,6–2,4: tangan, mik, kepala penonton, daun). Kamera bergerak terus pelan (zoom 3–9% per adegan, atau geser 60–120 px). Lapisan depan boleh kabur sedikit.
- **Hindari**: kamera diam; semua lapisan z sama (gerak datar seperti satu gambar); parallax terlalu kuat sampai tepi potongan terlihat.
- **Di mesin Kolase**: `z` per lapisan + preset `kamera` (`'dorong'`, `'kiri'`, `'naik'`…), lihat `../cinematic/kamera.md` §Parallax 2,5D. Kerumunan bertingkat: 2–3 potongan `z` 0,8 · 1,3 · 1,9 naik dari bawah bergiliran 0,15 dtk, `jangkar: 'bawah'`.

### Foto hidup (animated photographs)
- **Kapan**: momen aksi yang memang butuh gerak nyata (orang beraksi, air, api, kendaraan, kerumunan), tepat di kata kunci.
- **Kenapa**: foto diam yang tiba-tiba bergerak menarik perhatian lebih kuat daripada video yang bergerak sejak awal (pattern interrupt kecil).
- **Cara**: klip dibuat dari foto itu sendiri (first frame) sehingga peralihan tak terlihat; foto diam dulu 0,5–2 dtk, mulai bergerak di kata kunci, 2–4 dtk saja. Foto berlapis tetap ≥ 70% video.
- **Hindari**: klip yang wajah/tangannya berubah bentuk; klip yang kamera-nya melompat (periksa 8 bingkai/dtk).
- **Di mesin Kolase**: `{ gambar: 'nelayan', klip: { kode: 'nelayan-hidup', t: 'L08.w9', lebur: .25 } }`, `klip: { tahan: true }` untuk berhenti dan kembali jadi foto (`klip.md` §3). Berbayar (Flow), ditanya di dialog persetujuan.

### Elemen hidup di dalam satu foto (Kolase 1.5)
- **Kapan**: hampir setiap foto utama, terutama bila anggaran Flow/klip terbatas. **Kenapa**: acuan @earn.edits `Del7Vohuw9D` hampir tidak punya foto yang benar-benar diam: lampu menyala satu-satu, layar berkedip, daun bergoyang, sementara kamera pelan; satu foto terasa seperti dunia hidup, gratis dan tanpa risiko bentuk berubah seperti klip AI.
- **Cara**: baca isi gambar (`skill-edit-rizky/scripts/elemen.py saran` + `kisi`), pilih 2–5 bagian yang bisa bergerak di tempat (roda, layar, lampu, jendela, daun, kain, asap), satu jadi pusat perhatian, sejenis beda fase. Gerak besar yang memperlihatkan belakang benda tetap butuh potongan terpisah/klip.
- **Hindari**: semua bagian bergerak sekaligus; amplitudo besar (terlihat efek tempelan); bayangan ganda (pakai `tambal`).
- **Di mesin Kolase**: `{ gambar: 'lab', elemen: [{ bulat: [.28, .57, .06], kedip: { kuat: .45, laju: 7 } }, { kotak: [.6, 0, 1, .4], poros: [.92, .42], goyang: { sudut: 1.6, periode: 3.4 }, tambal: true }] }`; panduan lengkap `skill-edit-rizky/references/gerak-elemen.md`.

### Benda melayang (floating objects)
- **Kapan**: ikon/benda simbol yang menemani penjelasan (bohlam, koin, jam, kunci), benda kunci yang berpindah antar-adegan.
- **Kenapa**: gerak melayang halus membuat bingkai terasa hidup tanpa mencuri perhatian.
- **Cara**: amplitudo 4–10 px, periode 2,5–4,5 dtk, fase berbeda tiap benda; putar ±1–2°. Benda kunci yang muncul di dua adegan **dipindahkan**, bukan dimunculkan ulang.
- **Hindari**: semua benda melayang dengan fase sama (seperti satu papan bergoyang); amplitudo besar yang mengganggu baca teks.
- **Di mesin Kolase**: `hidup: 6` (px) atau `ayun: { sudut: 6, periode: 2.4 }`; pindah antar-adegan dengan `masuk: 'cocok'` + `cocok: { dari, ke }`.

### Tekstur kertas (paper texture)
- **Kapan**: semua gaya fisik/analog; juga untuk mengikat foto AI yang terlalu licin.
- **Kenapa**: tekstur menyatukan aset dari sumber berbeda (Flow, foto nyata, teks mesin) menjadi satu dunia.
- **Cara**: tekstur di latar + grain halus di atas semua; noda/serat diam (tidak berkedip) di benda kertas, grain bergerak di seluruh bingkai. Satu jenis tekstur per video (`../style/warna-tekstur.md` §Anggaran tekstur).
- **Hindari**: tekstur kertas di atas UI digital; tekstur yang menutupi teks kecil.
- **Di mesin Kolase**: `pola: 'kertas'` (+`tua`), grade `halftone`/`grain`/`debu`; `hitamPutih` + `campur: 'multiply'` untuk foto yang "dicetak" di kertas.

### Transisi sobek kertas (ripped-paper transition)
- **Kapan**: pergantian babak di gaya Collage/Grunge/Handcrafted; "membuka" fakta di balik permukaan.
- **Kenapa**: transisi bermotivasi dari bahan dunia itu sendiri (`transisi.md` §Motivasi).
- **Cara**: tepi sobek tidak beraturan dengan serat putih, sobekan bergerak 0,35–0,6 dtk outQuart, adegan baru sudah terlihat di belakang; bunyi kertas sobek dengan transient di awal gerak.
- **Hindari**: sobek berulang lebih dari 2 kali per video; tepi sobek yang terlalu rapi (gergaji beraturan).
- **Di mesin Kolase**: *Celah mesin* (tidak ada perpindahan sobek). Akali: (a) perpindahan `buka` (adegan lama terdorong keluar) dengan pelat atasnya berupa PNG kertas bertepi sobek (Flow latar hijau: "torn paper sheet, ragged fibrous edge") sebagai lapisan depan yang keluar dengan `keluar: { gaya: 'geser', ke: 'atas' }`; (b) benda `kustom` yang menggambar poligon bergerigi acak (`K.acak`) sebagai topeng kertas.

### Animasi ala scrapbook
- **Kapan**: kisah pribadi, perjalanan, kenangan, tutorial santai, seri bertokoh.
- **Kenapa**: kesan dibuat tangan oleh seseorang, bukan mesin; akrab.
- **Cara**: foto polaroid miring + selotip, stiker bertepi putih, coretan spidol (lingkar, panah), tulisan tangan untuk catatan pinggir, label. Gerak: tempel (pop kecil + bunyi selotip/klik), coretan tergambar bertahap 0,4–0,6 dtk.
- **Hindari**: terlalu banyak stiker (≤ 3 per bingkai); tulisan tangan untuk informasi utama (sulit dibaca).
- **Di mesin Kolase**: `tepi: true` (garis putih stiker), `benda: kartu` + `putar`, `coret: 'lingkar'|'panah'|'centang'`, gaya teks `tangan`, `label`, `stiker`.

### Komposisi editorial
- **Kapan**: penjelasan cerdas, opini, analisis, tema `editorial`.
- **Kenapa**: ruang kosong dan hierarki tegas terasa percaya diri dan mahal.
- **Cara**: satu gambar kuat + satu baris judul + satu baris pengantar; ruang kosong ≥ 35%; aksen satu warna; garis/bentuk dekoratif bergerak sangat pelan.
- **Hindari**: mengisi ruang kosong "karena terasa sepi".
- **Di mesin Kolase**: tema `editorial` (latar lengkungan + garis putus-putus), gaya teks `serif`/`tebal`/`sorot` (`acuan.md` §3).

## 3. Resep adegan kolase (urutan lapisan)
1. Pelat/pola latar (z 0–0,3), kamera bergerak pelan.
2. Teks judul **di belakang** potongan subjek bila subjek menutupi sebagian teks dengan elegan (teks di antara lapisan).
3. Potongan subjek (z 1), `bayangan`, `rig`.
4. Benda bertulisan/kartu bukti (z 1,1–1,4), sedikit miring.
5. Lapisan depan (z 1,6–2,4), kabur ringan, masuk `terbang`.
6. Efek 0–1 (cahaya bocor, partikel debu) + grade tema.

## Teknik modern
- **Teks di belakang subjek (text-behind-subject)**: judul besar ditaruh di antara latar dan potongan subjek. Manfaat: kedalaman editorial instan, kesan majalah premium. Kapan: hook, kartu judul, profil tokoh. Alur: urutan `lapis` latar → teks → potongan (mesin menggambar urut).
- **Garis luar stiker + bayangan lunak (sticker cutout)**: potongan diberi tepi putih 8–14 px dan bayangan jatuh. Manfaat: gaya kolase media sosial yang terbaca jelas di layar kecil. Alur: `tepi: true, bayangan: .4`.
- **Kartu foto miring 3D**: kartu berputar di sumbu Y seperti dipegang. Manfaat: foto diam terasa benda fisik. Alur: `rig: { jenis: 'miring', y: [[0, -20], [2.4, 12, 'inOutSine']] }` (`klip.md` §4).

## Cek cepat
- [ ] Tiap adegan ≥ 2 lapisan bergerak dengan z berbeda; kamera tidak pernah diam.
- [ ] Maks 3–5 unsur terlihat bersamaan, satu unsur jelas dominan.
- [ ] Potongan berbayangan, utuh atau menempel ke tepi layar (tidak ada garis gunting di tengah layar).
- [ ] Potongan makhluk hidup/benda lentur diberi `rig`; benda kunci antar-adegan pindah dengan `cocok`.
- [ ] Tekstur satu jenis dan konsisten; tidak menutupi teks.
- [ ] Nama media di layar fiktif; data/tanggal di benda bertulisan sama dengan sumber.

## Celah mesin
- **Sobek kertas** sebagai perpindahan belum ada. Akali: PNG kertas bertepi sobek sebagai lapisan depan + `buka`/`keluar`, atau benda `kustom` poligon bergerigi. Usulan mesin: `masuk: 'sobek'` (topeng tepi bergerigi berderau + serat putih, arah `arahMasuk`).
- **Lipat kertas (paper fold)** belum ada. Akali: `rig: { jenis: 'miring', x: [[0, 70], [.5, 0, 'outBack']] }` pada kartu (membuka dari terlipat 70°), atau dua potongan setengah kertas.
- **Stop-motion "on twos"** (gerak patah 12–15 fps) belum ada sebagai opsi. Akali: easing berupa fungsi tangga di keyframe `gerak` — `gerak: [[0, { x: 300 }], [1.2, { x: 700 }, x => Math.floor(x * 8) / 8]]` — dan kamera fungsi `kamera: t => ({ x: Math.floor(t * 12) % 2 * 3, y: 0, zoom: 1.04, putar: Math.floor(t * 12) % 3 * .2 - .2 })`. Usulan mesin: `KONFIG.patah: 12` (sampel posisi lapisan dibulatkan ke 12 fps).
