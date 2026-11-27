# Pustaka gaya visual: 20 gaya + resep dari reel

> STYLE · dipakai di langkah 4 (pilih gaya), 8–10 (gerak, huruf, transisi), 14 (polish) · terkait: `campur-gaya.md`, `warna-tekstur.md`, `bahasa-earnedits.md`, `resep/`, `../type/tipografi-kinetik.md`, `../motion/transisi.md`, `../cinematic/kamera.md`, `../audio/sound-design.md`, `../polish/qc.md`

Prinsip inti:
- **Gaya dipilih dari cerita, bukan dari selera hari itu.** Pertanyaannya: emosi apa yang harus dirasakan penonton, dan dunia visual apa yang membuat topik ini dipercaya?
- **Satu gaya = sepuluh keputusan yang saling mengunci** (huruf, warna, transisi, tekstur, kamera, animasi, bunyi, tempo, komposisi, kegunaan). Mengganti satu tanpa yang lain membuat video terasa "tempelan".
- **Gaya bukan efek.** Retro VHS bukan "pasang overlay VHS"; ia juga tempo, bunyi pita, huruf cap waktu, dan cara kamera bergerak.
- **Jangan semua video sama.** Rotasi gaya per topik, catat di riwayat (`skill-edit-rizky` `riwayat.py`), kecuali sedang membuat seri.
- Setiap gaya punya cara gagal yang khas (baris **Hindari**). Baca itu sebelum membangun, karena di situlah video berubah dari "dibuat editor" menjadi "dibuat AI" (`../polish/qc.md` §6).

Singkatan huruf (tulis di kepala `konfig.js`, karena `HURUF` mesin belum terdefinisi saat konfig dibaca):
```js
const F = { judul: '"KR Archivo","Archivo Black",sans-serif', padat: '"KR Anton","Anton",sans-serif',
  teks: '"KR Inter","Inter",sans-serif', tangan: '"KR Caveat","Caveat",cursive',
  serif: 'Georgia,"Times New Roman",serif', mesin: '"Courier New",monospace' };
```
`KONFIG.gayaTeks` menimpa gaya teks bawaan (`judul`, `padat`, `tahun`, `kutip`, `mesin`, `stiker`, `label`, `tangan`, `gelap`, `elegan`, `serif`, `tebal`, `sorot`) dengan `{ font, gaya, uk, warna, kapital, bayang, kotak, tepiKotak }`. `palet.kuning` = warna kata `*aksen*`, `palet.merah` = stiker/label/cap, `palet.stabilo` = sorot.

## Pilih cepat
Topik/emosi → 2 gaya yang disarankan (pertama = Rekomendasi). Resep reel (`resep/`) ditulis miring bila lebih cocok daripada gaya umum.

| Topik / emosi | Gaya 1 (Rekomendasi) | Gaya 2 |
|---|---|---|
| Sejarah terlupakan, "ternyata sudah ada" | Newspaper/Magazine | Cinematic Documentary |
| Sejarah besar, tragedi, perang (hormat) | Cinematic Documentary | Analog Film |
| Misteri, kriminal, kasus | *Sinema Kasus* | Psychological/Dark |
| Skandal siber, peretasan, kebocoran data | *Sinema Kasus* | Dark Tech |
| Bisnis besar, naik-turun merek | *Panggung Korporat* | Cinematic Editorial |
| Uang, harga, inflasi, saham | Corporate Premium | Newspaper/Magazine |
| Finansial pribadi, menabung, utang | Minimalist | Handcrafted/Organic |
| Teknologi, AI, aplikasi | *Kaca Gradien* | Dark Tech |
| Cara memakai alat AI, proses kreatif di balik layar, mitos "tombol ajaib" | *Diorama Kreator* | *Kaca Gradien* |
| Masa depan, robot, kota pintar | Futuristic UI | Cyberpunk |
| Tips produktivitas, kebiasaan | *Piksel Kertas* | Minimalist |
| Karier, kerja, kesepian kerja | *Piksel Kertas* | Corporate Premium |
| Psikologi, overthinking, kecemasan | Psychological/Dark | Minimalist |
| Kesehatan, tubuh, gizi | Documentary | Handcrafted/Organic |
| Sains, fakta aneh tapi nyata | *Arsip Pop* | Experimental Motion Graphics |
| Penemuan, rekor, eksperimen nyeleneh | *Arsip Pop* | Vintage Commercial |
| Budaya pop, film, musik, tren | Collage | Y2K |
| Nostalgia 90an–2000an, HP lama, internet lama | Retro VHS | Y2K |
| Berita terkini (netral) | Documentary | Corporate Premium |
| Politik (netral, berdata) | Documentary | Newspaper/Magazine |
| Motivasi, kisah underdog | Cinematic Editorial | Grunge |
| Pengumuman, kompetisi, giveaway, peringkat | *Panggung Emas* | Social Media Viral |
| Produk, promosi, peluncuran | *Kaca Gradien* | Luxury Editorial |
| Merek mewah, properti, kekayaan | Luxury Editorial | Cinematic Editorial |
| Edukasi anak, keluarga | Handcrafted/Organic | Collage |
| Horor, legenda, asal-usul tradisi | *Legenda Gelap* | Psychological/Dark |
| Olahraga, kompetisi fisik | Social Media Viral | *Panggung Emas* |
| Kuliner, resep, UMKM | Handcrafted/Organic | Vintage Commercial |
| Sejarah merek/iklan jadul | Vintage Commercial | Newspaper/Magazine |
| Luar angkasa, alam semesta | Cinematic Documentary | Futuristic UI |
| Alam, hewan, lingkungan | Cinematic Documentary | Documentary |
| Konsep abstrak, intro seri, musik | Experimental Motion Graphics | Collage |
| Fakta cepat / listicle 15–30 dtk | Social Media Viral | *Arsip Pop* |

## Peta ke tema mesin (`KONFIG.tema`)
Tema mesin = titik awal (grade + aksen + stabilo + musik, kadang latar + huruf). Gaya = keputusan lengkap di atasnya. Tulis `grade`/`palet`/`gayaTeks` sendiri untuk menimpa.

| Tema mesin | Gaya yang paling dekat |
|---|---|
| `arsip` | Newspaper/Magazine, Collage (versi kertas), Grunge (dengan kontras dinaikkan) |
| `dosir` | Psychological/Dark, Grunge (gelap), *Legenda Gelap* |
| `pasar` | Corporate Premium (hangat), Vintage Commercial (versi uang) |
| `teknologi` | Dark Tech, Futuristic UI, Cyberpunk (palet diganti) |
| `tv` | Retro VHS, Y2K, Vintage Commercial |
| `modern` | Cinematic Editorial, Social Media Viral, *Panggung Korporat* |
| `perang` | Cinematic Documentary (tragedi), Analog Film (kelam) |
| `alam` | Cinematic Documentary, Documentary, Analog Film (hangat), Handcrafted/Organic |
| `editorial` | Minimalist, Luxury Editorial (terang), Corporate Premium (terang), *Kaca Gradien* |
| `kartu` | Collage, Handcrafted/Organic, *Piksel Kertas* (palet hijau zaitun) |
| (belum ada) | Experimental Motion Graphics → `modern` + latar `sinar`/`spiral` |

## Cara membaca blok gaya
Tiap gaya memakai blok yang sama: **Rasa** (satu kalimat) · **Tipografi** · **Warna** (hex latar/teks/aksen + arti) · **Transisi** · **Tekstur** · **Kamera** · **Animasi** · **Bunyi** · **Tempo** (rata-rata bidikan) · **Komposisi** · **Kegunaan** · **Hindari** · **Di mesin Kolase**. Angka tempo untuk video 30–60 dtk bernarasi; tanpa narasi, turunkan ±20%.

---

### 1. Cinematic Editorial
- **Rasa**: majalah besar bertemu film; tenang, percaya diri, mahal tanpa pamer.
- **Tipografi**: pasangan serif miring kecil (pengantar) + sans tebal besar (inti); maksimal 1 kata beraksen per baris; label kecil kapital dengan jarak huruf lebar.
- **Warna**: latar `#0E0F11` · teks `#F2EEE6` · aksen `#C8A24A` (nilai/penting) atau `#D7261E` (bahaya). Hitam pekat tapi tidak hancur (hitam ±8%).
- **Transisi**: potong bermomentum (`dorong`, `tarik`), `fokus`, `cocok` untuk benda kunci, `bingkai` sekali di momen terpenting.
- **Tekstur**: grain halus, vinyet sedang, tanpa halftone.
- **Kamera**: satu gerak per adegan, dorong pelan 1,00→1,06 dalam 3 dtk; kadang statis untuk kalimat berat.
- **Animasi**: outQuart/outExpo; overshoot 0–4%; teks melayang masuk, tidak memantul.
- **Bunyi**: drone rendah, sub-hit di kalimat kunci, foley kertas/kain, whoosh lembut; musik pad/piano jarang.
- **Tempo**: 2,5–3,5 dtk; satu "napas" 1 dtk sebelum vonis.
- **Komposisi**: sepertiga, subjek kecil dalam ruang besar, teks di ruang kosong, teks di belakang subjek.
- **Kegunaan**: esai visual, bisnis besar, tokoh, opini cerdas, sejarah modern.
- **Hindari**: lens flare di mana-mana, letterbox palsu tanpa alasan, gelap sampai wajah hilang, emas di semua teks.
- **Di mesin Kolase**: `tema: 'modern'`; `grade: { tint: '#e8dcc8', kuat: .06, saturasi: .85, halftone: 0, grain: .05, vinyet: .48, debu: .05, garis: 0, kontras: .16 }`; `palet: { kuning: '#C8A24A', merah: '#D7261E' }`; `gayaTeks: { elegan: { font: F.serif, warna: '#F2EEE6' }, tebal: { font: F.teks, gaya: '800', warna: '#F2EEE6' } }`; latar = pelat foto gelap Flow; `musik: { sintesis: 'pad' }`; masuk favorit `dorong`, `fokus`, `cocok`, `bingkai`; efek `berkas` 1×, `kabut` rendah.

### 2. Documentary
- **Rasa**: jujur, berdata, tenang; penonton percaya karena tidak dibujuk.
- **Tipografi**: sans 600–800 (Inter) untuk lower-third dan label; angka besar Anton hanya untuk data kunci; kredit sumber kecil.
- **Warna**: warna alami foto; teks `#FFFFFF` · panel `rgba(15,15,15,.86)` · aksen `#FFD23F` (penanda data). Saturasi normal.
- **Transisi**: potong biasa dominan (≥ 70%), `fokus`, `geser`, `kartu` untuk foto arsip, J/L-cut di audio.
- **Tekstur**: grain sangat halus, vinyet ringan.
- **Kamera**: Ken Burns 3–6% per bidikan, arah konsisten; footage boleh handheld asli.
- **Animasi**: outCubic, tanpa overshoot atau ≤ 3%; label geser masuk 0,3 dtk.
- **Bunyi**: ambience/room tone asli, foley nyata, musik rendah (pad/piano) −24 dB di bawah narasi.
- **Tempo**: 3–5 dtk.
- **Komposisi**: subjek setinggi mata, foto asli sebagai kartu berlabel kredit, peta, grafik bersumber.
- **Kegunaan**: berita, sains, kesehatan, politik netral, sejarah berdata.
- **Hindari**: glitch dramatis, "BREAKING" palsu, musik emosional berlebihan, menyebut "foto asli" untuk gambar AI.
- **Di mesin Kolase**: `tema: 'modern'` atau `'alam'`; `grade: { tint: '#ffffff', kuat: 0, saturasi: .95, halftone: 0, grain: .03, vinyet: .25, debu: 0, garis: 0, kontras: .08 }`; media nyata `ambil_media.py` + label kredit (`gaya: 'label'`); `benda: grafik`, `angka`; `musik: { sintesis: 'pad' }`; masuk `potong`/`fokus`/`geser`/`kartu`.

### 3. Dark Tech
- **Rasa**: ruang server jam 2 pagi; dingin, presisi, sedikit mengancam.
- **Tipografi**: Inter 700 untuk judul, Courier untuk data/log/kode; label kecil kapital; satu kata aksen cyan.
- **Warna**: latar `#07080A` (grafit) · teks `#E8EEF4` · aksen `#38E1FF` (sinyal) + opsional `#7CFF6B` (terminal, maks 10% layar).
- **Transisi**: `dorong` ke layar, `bingkai` ke monitor, `strip`, `sentak`; `glitch` maks 2 per video.
- **Tekstur**: grain halus, garis layar tipis, vinyet kuat.
- **Kamera**: dolly pelan, dorong menembus layar, parallax panel UI (z 0,6–1,6).
- **Animasi**: outExpo 150–300 md untuk UI, stagger 40 md, ketikan per karakter, kursor berkedip.
- **Bunyi**: tik UI, dengung data, sub-boom, glitch pendek, ketikan keyboard.
- **Tempo**: 2–3 dtk.
- **Komposisi**: panel UI terpusat, garis tipis, ruang gelap luas, satu sumber cahaya layar.
- **Kegunaan**: AI, siber, privasi data, startup teknologi, cara kerja algoritma.
- **Hindari**: neon di semua tepi, hujan kode ala film, glow di semua teks, hoodie hacker tanpa fungsi.
- **Di mesin Kolase**: `tema: 'teknologi'`; `grade: { tint: '#9fb6d8', kuat: .08, saturasi: .8, halftone: 0, grain: .04, vinyet: .52, debu: .05, garis: .04, kontras: .18 }`; `latar: { pola: 'grid', warna: '#07080A', warnaGaris: 'rgba(56,225,255,.08)', jarak: 64 }`; teks `mesin` dengan `gayaTeks: { mesin: { warna: '#7CFF6B' } }`; `benda: hp` + `kustom` (terminal, progres); `musik: { sintesis: 'pulsa' }`. *Celah mesin*: teks bercahaya neon (akali: `kustom` dengan `shadowColor` cyan + `shadowBlur` 18, reset sesudahnya).

### 4. Retro VHS
- **Rasa**: kaset rumahan 1990an yang diputar ulang; nostalgia dengan sedikit bahaya.
- **Tipografi**: cap waktu Courier (`PLAY 00:12`, `SEP 2022`), judul Anton kapital, satu kata merah menyala.
- **Warna**: latar `#10131C` (biru gelap) · teks `#F4F1E8` · aksen `#FF3B3B` + bayangan `#3BD1FF` (pisah warna).
- **Transisi**: `kilat`, `glitch` (tracking), potong keras dengan derau pita, `strip`; layar CRT (`bingkai` ke `tv`).
- **Tekstur**: garis layar jelas, grain tinggi, pisah warna 2–4 px, sedikit lembek; derau di pembuka.
- **Kamera**: handheld halus, zoom kejut (`dorong-kuat`), kadang statis seperti kamera tripod rumahan.
- **Animasi**: tangga (stepped) dan patah; tanpa overshoot; teks muncul instan atau diketik.
- **Bunyi**: desis pita, klak mekanis play/stop, musik sedikit goyah nadanya, dengung CRT.
- **Tempo**: 2–3 dtk; kartu "BEBERAPA HARI KEMUDIAN" sebagai jeda.
- **Komposisi**: subjek di tengah (aman 4:3), cap waktu di sudut atas, TV tabung sebagai bingkai.
- **Kegunaan**: nostalgia 90an, kasus lama, sejarah game/internet, true crime.
- **Hindari**: overlay VHS 100% yang membuat teks tak terbaca, glitch tiap detik, VHS untuk data modern yang butuh ketajaman.
- **Di mesin Kolase**: `tema: 'tv'`; `grade: { tint: '#d6c3d9', kuat: .1, saturasi: .85, halftone: 0, grain: .09, vinyet: .5, debu: .15, garis: .12, kontras: .14 }`; `palet: { kuning: '#FF3B3B', merah: '#FF3B3B' }`; `benda: tv` (warna: true); teks `mesin` untuk cap waktu; efek `glitch` ≤ 2, `kilat`; `musik: { sintesis: 'tegang' }`. *Celah mesin*: pisah warna per bingkai, pita tracking bergulir, goyang nada musik (akali: `glitch` 0,3 dtk di sambungan; `kustom` lapisan atas berupa pita derau tipis bergeser `cek: false`; musik berkas yang sudah di-*warp* ffmpeg).

### 5. Analog Film
- **Rasa**: seluloid 16/35 mm; hangat, intim, sedikit rapuh.
- **Tipografi**: serif (Georgia) miring untuk judul, ketikan Courier untuk tanggal; huruf kecil, banyak ruang.
- **Warna**: latar `#1A1410` · teks `#F3E9D2` · aksen `#E0782F` (amber). Highlight krem, bayangan cokelat, bukan hitam murni.
- **Transisi**: `bakar` (maks 2, akhir babak), `cahaya` bocor, `fokus`, potong biasa; `lebur` hanya untuk lompatan waktu.
- **Tekstur**: grain tinggi bergerak, debu, vinyet, kedip halus.
- **Kamera**: handheld lambat, dorong lembut, rack focus.
- **Animasi**: inOutSine, lambat, tanpa overshoot.
- **Bunyi**: dengung proyektor, kresek, piano/senar hangat, room tone.
- **Tempo**: 3–5 dtk.
- **Komposisi**: sepertiga, cahaya jendela, jarak dekat yang intim.
- **Kegunaan**: kenangan, keluarga, biografi, budaya, kuliner tradisional, sejarah kampung.
- **Hindari**: sepia total, goresan di seluruh video, film terbakar di setiap sambungan.
- **Di mesin Kolase**: `tema: 'alam'` atau `'arsip'`; `grade: { tint: '#f0c27a', kuat: .14, saturasi: .9, halftone: 0, grain: .08, vinyet: .45, debu: .4, garis: 0, kontras: .1 }`; efek `cahaya` (pembuka), `bakar` (penutup babak); SFX `proyektor`; `musik: { sintesis: 'dokumenter' }`. *Celah mesin*: halation, gate weave, kedip (akali: `cahaya` kuat .25; `kamera` keyframe ±2 px acak; efek `gelap` kuat .05 berkedip pendek).

### 6. Grunge
- **Rasa**: fotokopi poster jalanan; kasar, jujur, melawan.
- **Tipografi**: Anton kapital rapat, kesan tercetak kasar; anotasi tangan Caveat; stiker merah.
- **Warna**: latar `#1C1B19` (gelap) atau `#D9D2C3` (kertas) · teks `#111111`/`#F2EFE8` · aksen `#D7261E`.
- **Transisi**: `tutup` (lembar kertas), `buka`, `jatuh`, `sentak`, `kartu`; gerak patah ala stop-motion.
- **Tekstur**: kertas tua, halftone tinggi, kontras fotokopi, debu, tepi sobek.
- **Kamera**: sedikit goyang, lompatan bingkai kecil (jump reframe).
- **Animasi**: on twos (patah), overshoot 8–12% dengan settle cepat, cap mendarat keras.
- **Bunyi**: sobek kertas, staples, stempel, selotip, spidol, drum kasar.
- **Tempo**: 1,5–2,5 dtk.
- **Komposisi**: tidak simetris, potongan bertumpuk, selotip, coretan.
- **Kegunaan**: musik, budaya jalanan, kisah underdog, opini keras (berimbang), tekanan mental.
- **Hindari**: tekstur menutupi teks, 3 tekstur ditumpuk, cipratan acak tanpa arti.
- **Di mesin Kolase**: `tema: 'arsip'` (terang) atau `'dosir'` (gelap); `grade: { tint: '#d9cfb8', kuat: .08, saturasi: .7, halftone: .14, grain: .09, vinyet: .45, debu: .5, garis: 0, kontras: .22 }`; `latar: { pola: 'kertas', tua: .8 }`; teks `padat` + `tangan`; `coret`, `benda: cap`, `masuk: 'cap'`; masuk `tutup`/`jatuh`. *Celah mesin*: huruf rusak (distressed), ambang fotokopi, displacement (akali: potongan kertas bertulisan dari Flow sebagai gambar; halftone .16 + kontras .24; `kustom` dengan pola titik putih menggerus huruf).

### 7. Minimalist
- **Rasa**: satu gagasan, satu bingkai, banyak napas.
- **Tipografi**: satu keluarga (Inter) 600–800 besar; label kecil berjarak huruf lebar; tanpa bayangan.
- **Warna**: latar `#F5F5F2` · teks `#121212` · aksen tunggal `#FF4D00` (hanya untuk kata/angka terpenting).
- **Transisi**: `geser`, `fokus`, `cocok`, potong biasa.
- **Tekstur**: nyaris tidak ada (grain sangat halus).
- **Kamera**: hampir statis (`tenang`), satu dorongan pelan di kalimat kunci.
- **Animasi**: outQuart; overshoot 2–4%; tahan lama sesudah muncul.
- **Bunyi**: sedikit dan presisi: klik, whoosh lembut, hening; piano/pad minimal.
- **Tempo**: 3–4 dtk.
- **Komposisi**: satu benda di tengah/sepertiga, 60–70% ruang kosong.
- **Kegunaan**: produktivitas, finansial pribadi, filosofi, kesehatan mental yang tenang.
- **Hindari**: kosong tanpa gagasan (jadi membosankan), teks terlalu kecil, terlalu banyak abu-abu.
- **Di mesin Kolase**: `tema: 'editorial'`; `grade: { tint: '#ffffff', kuat: 0, saturasi: .95, halftone: 0, grain: .02, vinyet: .18, debu: 0, garis: 0, kontras: .06 }`; `latar: { pola: 'polos', warna: '#F5F5F2' }` atau `{ pola: 'editorial', sabit: false, putus: false }`; `gayaTeks: { tebal: { warna: '#121212' } }`, `palet: { kuning: '#FF4D00' }`; `kamera: 'tenang'`; `musik: { sintesis: 'pad' }`.

### 8. Luxury Editorial
- **Rasa**: katalog rumah mode; pelan, sunyi, mahal.
- **Tipografi**: serif besar kontras tinggi (Georgia, miring untuk kata emosi), label sans kecil kapital berjarak lebar.
- **Warna**: latar `#0B0B0B` atau krem `#EFE8DC` · teks `#F5EFE3` / `#1A1612` · aksen `#C9A45C` (champagne, bukan emas kuning).
- **Transisi**: `fokus`, `geser` lambat, `cocok`, `lebur` lambat sesekali; `bingkai` ke foto produk.
- **Tekstur**: grain halus, vinyet sedang, kilap di permukaan produk.
- **Kamera**: dolly pelan 1,00→1,04 dalam 4 dtk (inOutSine), kesan orbit lewat miring 3D.
- **Animasi**: outQuint lambat, tanpa overshoot; muncul dengan pudar + naik 12 px.
- **Bunyi**: cello/senar, piano lembut, whoosh berudara, denting kaca; banyak hening.
- **Tempo**: 3,5–5 dtk.
- **Komposisi**: simetris, margin lebar, produk sebagai pahlawan.
- **Kegunaan**: merek mewah, properti, kekayaan, kopi spesialti, fashion.
- **Hindari**: gradien emas murahan, partikel kilau, teks banyak, kontras berlebih.
- **Di mesin Kolase**: `tema: 'editorial'` (`latar: { pola: 'editorial', gelap: true }`) atau `'modern'`; `grade: { tint: '#f3e6cf', kuat: .05, saturasi: .85, halftone: 0, grain: .03, vinyet: .4, debu: 0, garis: 0, kontras: .12 }`; `gayaTeks: { elegan: { font: F.serif, warna: '#F5EFE3' }, label: { font: F.teks, gaya: '600', kotak: 'rgba(0,0,0,0)' } }`, `palet: { kuning: '#C9A45C' }`; `kilap` pada produk; `rig: { jenis: 'miring', y: [[0, -12], [4, 8, 'inOutSine']] }`. *Celah mesin*: teks emas metalik, jarak huruf (tracking) (akali: `kustom` dengan `createLinearGradient` emas tiga titik; tracking dengan `c.letterSpacing` di `kustom`).

### 9. Futuristic UI
- **Rasa**: antarmuka dari lima tahun ke depan; bersih, ringan, cerdas.
- **Tipografi**: Inter 500–700, angka monospace, garis tipis; label kapital kecil.
- **Warna**: latar `#05070D` · teks `#DDE7FF` · aksen `#5B8CFF` + `#9B6BFF` (maks dua, saling bergradasi).
- **Transisi**: `dorong` ke panel, `geser` panel, `cocok` (shared element), `iris`, `strip`.
- **Tekstur**: grain halus, garis layar sangat tipis, bokeh lembut di latar.
- **Kamera**: parallax lapisan UI, drift lambat, panel miring 3D.
- **Animasi**: outExpo 150–300 md (mikro), 300–500 md (layar), stagger 40 md, overshoot 2–6%.
- **Bunyi**: bip UI lembut, kicau sinus, dengung, riser tipis.
- **Tempo**: 2–3 dtk.
- **Komposisi**: HUD terpusat, cincin data, panel bertingkat, garis tipis 1–2 px.
- **Kegunaan**: AI, masa depan, luar angkasa, teknologi medis, kota pintar.
- **Hindari**: HUD penuh hiasan tanpa data, cincin berputar tanpa makna, biru menyala berlebihan.
- **Di mesin Kolase**: `tema: 'teknologi'`; `grade: { tint: '#b8c6ff', kuat: .06, saturasi: .9, halftone: 0, grain: .03, vinyet: .5, debu: 0, garis: .03, kontras: .15 }`; `benda: { jenis: 'kustom' }` untuk cincin/panel, `hp` + `lukis`; `rig: 'miring'`; efek `bokeh`, `berkas`; `musik: { sintesis: 'pulsa' }`. *Celah mesin*: kaca buram (backdrop blur), garis gradien bercahaya (akali: isi semi-transparan + tepi gradien di `kustom`, bokeh di belakangnya agar terasa kaca).

### 10. Newspaper / Magazine
- **Rasa**: arsip redaksi; bukti di atas kertas.
- **Tipografi**: judul serif tebal (Georgia), stiker Archivo, mesin ketik untuk catatan; kolom isi.
- **Warna**: latar `#ECE2C8` (kertas) · teks `#1B1712` · aksen `#D7261E` + stabilo `#FFE200`.
- **Transisi**: `tutup` (halaman), `buka`, `kartu`, `bingkai` (adegan menjadi foto di koran), `dorong` ke foto.
- **Tekstur**: halftone, grain, debu, serat kertas.
- **Kamera**: tilt menyusuri halaman, dorong ke judul, putar kecil.
- **Animasi**: kertas geser outCubic, cap overshoot 10%, stabilo menyapu kiri ke kanan 0,4 dtk.
- **Bunyi**: gemerisik kertas, balik halaman, mesin ketik, stempel, decit stabilo.
- **Tempo**: 2–3 dtk.
- **Komposisi**: kolom, judul di atas, foto + keterangan, kliping bertumpuk.
- **Kegunaan**: sejarah, kronologi, skandal lama, "ternyata sudah ada".
- **Hindari**: logo koran nyata, tulisan palsu terbaca jelas di close-up, semua adegan kertas tanpa jeda tempat.
- **Di mesin Kolase**: `tema: 'arsip'` (grade bawaan); `benda: koran` (nama fiktif) + `sorot`, `benda: dokumen`, `benda: cap`; masuk `tutup`/`bingkai`/`kartu`; contoh lengkap `skill-edit-rizky/contoh/n250.konfig.js`.

### 11. Collage
- **Rasa**: buku tempel yang hidup; bermain tapi tertata.
- **Tipografi**: campuran terkendali: Anton untuk judul, serif untuk kutipan, tangan untuk anotasi; label di kertas sobek.
- **Warna**: latar `#EDE6D6` · teks `#141414` · aksen `#FF5A36` + `#2F6BFF`.
- **Transisi**: `tutup`, `jatuh`, `lempar`, `cocok`, lapisan `terbang`; gerak patah.
- **Tekstur**: kertas, halftone sedang, selotip, bayangan potongan.
- **Kamera**: parallax 2,5D jelas (z 0,3 / 1 / 1,8), dorong pelan.
- **Animasi**: on twos untuk potongan, overshoot 8–12%, goyang rig halus.
- **Bunyi**: kertas, gunting, selotip, pop, foley meja.
- **Tempo**: 2–2,5 dtk.
- **Komposisi**: berlapis, sengaja tidak di grid, potongan bertepi putih.
- **Kegunaan**: budaya pop, sejarah ringan, explainer, musik, edukasi.
- **Hindari**: stiker acak tanpa makna, potongan terlalu banyak sampai tanpa hierarki.
- **Di mesin Kolase**: `tema: 'kartu'` (palet diganti) atau `'arsip'`; potongan Flow + `tepi: true` + `bayangan`; `rig`; masuk `terbang`/`jatuh`/`lempar`; lihat `../motion/kolase-editorial.md`.

### 12. Cyberpunk
- **Rasa**: kota hujan malam bertanda neon; teknologi tanpa harapan.
- **Tipografi**: Archivo/Anton rapat, mono untuk sistem; papan tanda fiktif.
- **Warna**: latar `#0A0612` · teks `#F2F2F2` · aksen dominan `#FF2E88` (magenta), pendamping `#19F0FF` (cyan) ≤ 20%.
- **Transisi**: `glitch`, `sentak`, `kilat`, `strip`.
- **Tekstur**: garis layar, grain, hujan, kabut.
- **Kamera**: sudut rendah, dorong pelan, miring (`guling`).
- **Animasi**: outExpo cepat, tangga glitch.
- **Bunyi**: synth bass, hujan, dengung neon, glitch.
- **Tempo**: 1,5–2,5 dtk.
- **Komposisi**: sudut rendah, garis menuju titik hilang, papan tanda.
- **Kegunaan**: distopia teknologi, AI gelap, game, masa depan kota.
- **Hindari**: magenta-cyan merata di semua benda (tampilan "AI" paling klise). Pilih satu warna dominan.
- **Di mesin Kolase**: `tema: 'teknologi'` + `palet: { kuning: '#FF2E88', merah: '#19F0FF' }`; `grade: { tint: '#c79bff', kuat: .1, saturasi: 1.05, halftone: 0, grain: .05, vinyet: .55, debu: 0, garis: .06, kontras: .2 }`; efek `partikel` `hujan`, `berkas`, `kabut`, `glitch`; `musik: { sintesis: 'tegang' }`. *Celah mesin*: cahaya neon, bloom (akali: `berkas` warna magenta kuat .3 di satu sumber; teks bercahaya lewat `kustom`).

### 13. Corporate Premium
- **Rasa**: laporan tahunan yang enak ditonton; rapi, meyakinkan.
- **Tipografi**: Inter 600–800, hierarki tegas (judul/sub/label), angka tabular.
- **Warna**: latar `#F7F8FA` atau `#0F1B2D` · teks `#0F1B2D`/`#F7F8FA` · aksen `#1F6FEB` (utama) + `#12B886` (tumbuh) atau `#E5484D` (turun).
- **Transisi**: `geser`, `cocok`, `fokus`, `tutup` panel.
- **Tekstur**: hampir tidak ada.
- **Kamera**: dorong halus, parallax kartu.
- **Animasi**: outQuart, overshoot 2–4%, stagger 50 md; grafik tumbuh 0,8 dtk.
- **Bunyi**: klik bersih, whoosh lembut, musik korporat ringan rendah.
- **Tempo**: 2,5–3,5 dtk.
- **Komposisi**: grid 12 kolom, kartu, grafik dengan sumber.
- **Kegunaan**: laporan bisnis, fintech, startup, karier, B2B.
- **Hindari**: stok klise (jabat tangan), gradien ungu-biru generik, steril tanpa manusia.
- **Di mesin Kolase**: `tema: 'editorial'` + `palet: { kuning: '#1F6FEB', merah: '#E5484D' }`; `grade: { tint: '#ffffff', kuat: 0, saturasi: 1, halftone: 0, grain: .02, vinyet: .22, debu: 0, garis: 0, kontras: .08 }`; `benda: grafik`, `angka`, `kustom` kartu; `musik: { sintesis: 'ceria', vol: .5 }`.

### 14. Social Media Viral
- **Rasa**: cepat, lantang, langsung ke inti.
- **Tipografi**: Archivo Black/Anton besar, tepi hitam tebal, kata muncul saat diucapkan.
- **Warna**: latar terang atau `#111111` · teks `#FFFFFF` bertepi hitam · aksen `#FFE600` + `#FF3D00`.
- **Transisi**: potong keras di kata, punch-in (`dorong-kuat`), `sentak`, `kilat`.
- **Tekstur**: tidak ada.
- **Kamera**: punch-in 1,00→1,15 di penekanan, guncang di hantaman.
- **Animasi**: pop overshoot 15–20%, cepat (6–8 bingkai).
- **Bunyi**: pop, swoosh, ding; efek meme hanya bila memang lucu dan jarang.
- **Tempo**: 0,8–1,8 dtk.
- **Komposisi**: subjek tengah, teks besar di sepertiga atas.
- **Kegunaan**: fakta cepat, listicle, tips 15–30 dtk, olahraga.
- **Hindari**: SFX di setiap kata, caption di setiap kata seluruh video, zoom di setiap potongan.
- **Di mesin Kolase**: `tema: 'modern'`; teks `judul` `anim: 'pop'`, `ikut: true`, `garis: '#000'`; `kamera: 'dorong-kuat'`; efek `guncang`, `garis`; `musik: { sintesis: 'ceria' }`. Subtitle tetap mati kecuali diminta.

### 15. Psychological / Dark
- **Rasa**: pikiran yang terlalu sunyi; gelisah, menahan.
- **Tipografi**: serif kecil (Georgia), kata terisolasi, kadang satu kata besar sendirian.
- **Warna**: latar `#0C0C0E` · teks `#D9D6D0` · aksen `#8E1B1B` (merah tua, jarang).
- **Transisi**: `fokus`, potong ke hitam, `iris`, `bingkai` bentuk `kunci`, `lebur` lambat.
- **Tekstur**: grain sedang, vinyet sangat kuat, kabut.
- **Kamera**: dorong merayap 1,00→1,12 dalam 5 dtk, miring halus, kadang diam lama.
- **Animasi**: inOutSine lambat; tahan yang tidak nyaman; kedip singkat.
- **Bunyi**: drone, detak jantung, swell terbalik, hening, sub.
- **Tempo**: 3–6 dtk diselingi potongan sangat pendek (0,3–0,5 dtk).
- **Komposisi**: subjek kecil dan terisolasi, simetri, kegelapan luas.
- **Kegunaan**: psikologi, kecemasan, overthinking, manipulasi, kriminal psikologis.
- **Hindari**: jumpscare murahan, merah di mana-mana, nuansa menakutkan untuk topik kesehatan mental yang butuh empati.
- **Di mesin Kolase**: `tema: 'dosir'`; `grade: { tint: '#8fa0a6', kuat: .1, saturasi: .55, halftone: 0, grain: .07, vinyet: .6, debu: .2, garis: 0, kontras: .2 }`; efek `kabut`, `sorot`, `gelap`, `lensa`; SFX `jantung`, `sub`; `musik: { sintesis: 'misteri' }`.

### 16. Experimental Motion Graphics
- **Rasa**: bentuk dan huruf sebagai musik; berani, grafis.
- **Tipografi**: kinetik, sangat besar, kadang terpotong bingkai; satu keluarga tebal.
- **Warna**: 2–3 warna datar: `#111111` · `#F2F0EA` · aksen `#FF4F1F` + `#3A5BFF`.
- **Transisi**: transisi bentuk, `iris`, `strip`, `putar`, match cut bentuk.
- **Tekstur**: datar, grain sangat halus.
- **Kamera**: abstrak; rotasi, zoom besar.
- **Animasi**: easing kuat (pegas/outElastic), overshoot 10–15%, ritme ketat.
- **Bunyi**: synth hit, bunyi yang dirancang, berirama.
- **Tempo**: 0,8–2 dtk, dipimpin musik (tetap ≤ 60% di ketukan).
- **Komposisi**: geometris, simetris, grid tegas.
- **Kegunaan**: intro seri, konsep abstrak, musik, branding.
- **Hindari**: kekacauan tanpa narasi, huruf tak terbaca, bergerak terus tanpa jeda.
- **Di mesin Kolase**: `tema: 'modern'`; `latar: { pola: 'sinar' }` / `'spiral'`; `benda: kustom` bentuk; masuk `strip`/`iris`/`putar`; easing `pegas`/`outElastic`; `musik: { sintesis: 'pulsa' }`. *Celah mesin*: morph bentuk, deformasi huruf (akali: `kustom` menggambar bentuk antara dua keadaan dengan `K.lerp`).

### 17. Handcrafted / Organic
- **Rasa**: dibuat dengan tangan di meja kayu; hangat, dekat.
- **Tipografi**: Caveat untuk anotasi, serif untuk judul; tanpa huruf mesin yang dingin.
- **Warna**: latar `#EFE6D2` (kraft) · teks `#2B241C` · aksen `#C0583A` (terakota) + `#6B8F4E` (sage).
- **Transisi**: `tutup` kertas, `buka`, `cocok`, patah stop-motion.
- **Tekstur**: kertas, garis pensil, grain sedang.
- **Kamera**: dari atas meja (top-down), drift pelan.
- **Animasi**: on twos, goyang kecil, overshoot 6–8%.
- **Bunyi**: pensil, kertas, ketukan kayu, gitar akustik, ambience dapur/rumah.
- **Tempo**: 2,5–3,5 dtk.
- **Komposisi**: flat-lay, panah dan lingkaran tangan.
- **Kegunaan**: kuliner, parenting, edukasi anak, DIY, lingkungan, UMKM.
- **Hindari**: terlalu imut, huruf tangan untuk paragraf panjang.
- **Di mesin Kolase**: `tema: 'kartu'` + `palet` kraft, atau `'alam'`; `latar: { pola: 'kertas', warna: '#EFE6D2', tua: .4 }`; teks `tangan`; `coret` (lingkar, panah); `rig: 'goyang'`; `musik: { sintesis: 'jenaka' }` atau `'pad'`.

### 18. Y2K
- **Rasa**: internet awal 2000an; mengilap, ceria, sedikit norak dengan sengaja.
- **Tipografi**: Archivo lebar, gelembung; teks krom (lihat celah).
- **Warna**: latar `#E9F1FF` · teks `#1A1A2E` · aksen `#FF4FD8` + `#4FD1FF` + perak.
- **Transisi**: `iris`, `strip`, `putar`, `kilat` dengan kilau.
- **Tekstur**: mengilap, bokeh, kilau.
- **Kamera**: putar 3D (rig miring), zoom.
- **Animasi**: outBack 15%, berputar, memantul.
- **Bunyi**: bunyi UI era 2000an buatan sendiri, letupan gelembung, synth pop.
- **Tempo**: 1,5–2,5 dtk.
- **Komposisi**: terpusat, jendela UI lama, stiker.
- **Kegunaan**: budaya pop 2000an, HP lama, internet awal, fashion.
- **Hindari**: stiker berlebihan, teks pastel kontras rendah.
- **Di mesin Kolase**: `tema: 'tv'` + `palet: { kuning: '#FF4FD8', merah: '#4FD1FF' }`; `latar: { pola: 'spiral' }` pastel; `benda: hp`, `notif`; efek `bokeh`, `kilau`; `rig: 'miring'`. *Celah mesin*: teks krom (akali: `kustom` gradien perak 4 titik + garis tepi putih).

### 19. Vintage Commercial
- **Rasa**: iklan majalah 1950–1970an; optimis, menjual dengan senyum.
- **Tipografi**: Archivo/Anton display + Caveat sebagai pengganti skrip; lencana starburst.
- **Warna**: latar `#F3E3C3` · teks `#2A1E14` · aksen `#D9412B` + `#2F7F8A` + `#F2B544`.
- **Transisi**: `kartu`, `putar`, `jatuh`, latar `sinar` meledak.
- **Tekstur**: halftone, grain, kertas; cetak meleset (lihat celah).
- **Kamera**: panggung statis dengan produk di tengah, dorong.
- **Animasi**: outBack 10–15%, lencana berputar pelan.
- **Bunyi**: jingle ceria, ding, kaching.
- **Tempo**: 2–3 dtk.
- **Komposisi**: produk tengah + lencana + pita judul.
- **Kegunaan**: sejarah merek, produk lama, iklan jadul, promosi UMKM bergaya retro.
- **Hindari**: meniru iklan/maskot nyata, lencana terlalu banyak.
- **Di mesin Kolase**: `tema: 'tv'` atau `'pasar'`; `latar: { pola: 'sinar', warna: '#F2B544', warna2: '#F3E3C3' }`; `benda: label` + `ayun`; teks `stiker`; SFX `kaching`, `ding`; `musik: { sintesis: 'ceria' }` / `'jenaka'`. *Celah mesin*: cetak meleset (akali: duplikat lapisan teks bergeser 3 px warna cyan `alfa: .6` di belakang teks utama).

### 20. Cinematic Documentary
- **Rasa**: film dokumenter bioskop; nyata, besar, berbobot.
- **Tipografi**: judul bab serif, lower-third Inter, angka Anton untuk data besar.
- **Warna**: bayangan `#13232A` · highlight `#F2D3A8` · teks `#FFFFFF` · aksen `#E9B44C`. Teal-oranye ditahan.
- **Transisi**: potong, J/L-cut, `fokus`, `cocok`, `bingkai` sekali.
- **Tekstur**: grain sedang, vinyet, kabut atmosfer.
- **Kamera**: kesan drone/dolly (`naik`, `turun`, `mundur`), parallax 2,5D pada foto.
- **Animasi**: lambat, inOutSine.
- **Bunyi**: ambience kaya, pad orkestra, foley nyata, hening sebelum fakta berat.
- **Tempo**: 3–5 dtk.
- **Komposisi**: wide → medium → detail; skala manusia vs ruang.
- **Kegunaan**: sejarah besar, alam, luar angkasa, tragedi (hormat), biografi.
- **Hindari**: teal-oranye berlebihan, musik epik untuk topik kecil.
- **Di mesin Kolase**: `tema: 'alam'` / `'perang'` / `'modern'`; `grade: { tint: '#e9d2b0', kuat: .08, saturasi: .9, halftone: 0, grain: .05, vinyet: .4, debu: .08, garis: 0, kontras: .15 }`; `kamera: 'naik'`/`'turun'`/`'mundur'`; efek `kabut`, `berkas`; `musik: { sintesis: 'dokumenter' }`.

---

## Resep dari reel
Resep = gaya lengkap hasil bedah satu reel acuan, diberi nama orisinal, siap dipakai untuk topik apa pun (`../../SKILL.md` §4). Tiap resep berisi DNA 10 atribut, tata bahasa adegan, preset mesin, dan yang tidak boleh disalin.

| Resep | Asal bedah | Paling dekat dengan | Pakai untuk |
|---|---|---|---|
| `resep/sinema-kasus.md` (Sinema Kasus) | reel kebocoran game lewat TV hotel, VHS | Retro VHS + Dark Tech, bertempo Cinematic Documentary | kasus, peretasan, skandal, true crime |
| `resep/legenda-gelap.md` (Legenda Gelap) | reel asal-usul Halloween/Samhain | Psychological/Dark + Grunge | legenda, horor, asal-usul tradisi, sejarah kelam |
| `resep/piksel-kertas.md` (Piksel Kertas) | reel "Editing Alone" piksel + kertas | Handcrafted/Organic + Collage, huruf piksel retro | produktivitas, karier, komunitas, psikologi kerja |
| `resep/panggung-emas.md` (Panggung Emas) | reel pengumuman kompetisi | Luxury Editorial + Social Media Viral | pengumuman, kompetisi, peringkat, pencapaian |
| `resep/arsip-pop.md` (Arsip Pop) | reel mobil berbahan bakar kopi | Collage + Newspaper/Magazine + Vintage Commercial | fakta aneh, penemuan, rekor, sejarah merek |
| `resep/kaca-gradien.md` (Kaca Gradien) | reel SaaS + plugin gradien (16:9) | Corporate Premium + Futuristic UI + Minimalist | teknologi, aplikasi, AI, peluncuran produk |
| `resep/panggung-korporat.md` (Panggung Korporat) | reel naik-turun produsen HP | Corporate Premium + Cinematic Editorial (keynote gelap) | kisah bisnis, naik-jatuh merek, keputusan CEO |
| `resep/diorama-kreator.md` (Diorama Kreator) | reel @t1mline tentang skill sutradara (16:9, 1,7 dtk/bidikan) | Experimental Motion Graphics + Futuristic UI, sentuhan Handcrafted/Organic | alat AI, proses kreatif di balik layar, mitos "tombol ajaib", produk digital sendiri |

Resep boleh dicampur dengan salah satu dari 20 gaya (`campur-gaya.md` §5): resep tetap dominan, gaya kedua hanya memegang 1–2 lapisan.

## Cek cepat
- [ ] Gaya dipilih dari emosi + topik (tabel Pilih cepat), bukan kebiasaan
- [ ] Kesepuluh atribut gaya terisi di brief (huruf, warna, transisi, tekstur, kamera, animasi, bunyi, tempo, komposisi, kegunaan)
- [ ] Baris **Hindari** gaya itu sudah dicek di lembar kontak
- [ ] Hanya 2 warna aksen; satu grade untuk seluruh video
- [ ] Gaya berbeda dari video terakhir (kecuali seri/acuan), dicatat di riwayat
- [ ] Celah mesin gaya ini sudah diakali tanpa efek berlebihan

## Celah mesin
- Huruf piksel, huruf rusak (distressed), teks emas/krom metalik, teks neon bercahaya: belum ada sebagai gaya teks (akali: `kustom` dengan gradien/`shadowBlur`, atau potongan Flow bertulisan sebagai gambar).
- Tracking (jarak antarhuruf) untuk label mewah/minimal: belum ada di lapisan teks (akali: `kustom` + `c.letterSpacing`).
- Pisah warna per bingkai, pita tracking VHS, goyang nada: belum ada (akali: `glitch` pendek + `kustom` pita derau).
- Kaca buram (backdrop blur) untuk Futuristic UI / Kaca Gradien: belum ada (akali: isi semi-transparan + tepi gradien + bokeh di belakang).
- Bloom/halation untuk Analog Film dan Cyberpunk: belum ada (akali: efek `cahaya`/`berkas` lemah di satu sumber).
- Cetak meleset (misregistration) untuk Vintage Commercial: belum ada (akali: salinan teks bergeser berwarna di belakang).
- Morph bentuk untuk Experimental: belum ada (akali: `kustom` interpolasi bentuk).
- Usul mesin: tema baru `vhs`, `piksel`, `kaca`, `emas` yang membawa `grade` + `latar` + `gayaTeks` sekaligus, didaftarkan di `TEMA` + `GRADE_DASAR` templat dan `skill-edit-rizky/references/tema.md`.

## Teknik modern
- **Judul editorial campur huruf** (serif miring + display tebal + satu kata warna dalam satu judul): manfaat = rasa majalah tanpa efek; kapan = hook dan kartu bab; cara = `serif` di atas `tebal`, satu kata `*aksen*` (lihat grid acuan, judul "Fear … Painting").
- **Teks di belakang subjek** (huruf serif raksasa tertutup sebagian oleh potongan tokoh): manfaat = kedalaman instan; kapan = gaya Luxury, Cinematic Editorial, Panggung Emas; cara = urutan `lapis` latar → teks → potongan.
- **Gambar di dalam kalimat** (foto kecil berbentuk pil di sela kata): manfaat = membaca dan melihat sekaligus; kapan = Kaca Gradien, Minimalist; cara = `kustom` atau dua lapisan teks dengan potongan bersudut bulat di tengahnya.
- **Siluet peta panas (thermal)**: manfaat = misteri identitas tanpa wajah; kapan = hook, tokoh anonim; cara = potongan Flow siluet bergradien merah-oranye-kuning (prompt), `blur` sedikit.
