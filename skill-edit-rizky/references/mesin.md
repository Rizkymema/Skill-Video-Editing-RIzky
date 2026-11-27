# Mesin Kolase 1.5 — API konfig

File: `assets/templat.html`. Per video hanya blok `<script id="konfig">` (KONFIG + ADEGAN) yang ditulis, lewat `jalankan.py rakit konfig.js film.html …`. Koordinat = piksel bingkai 1080×1920 (9:16) atau 1920×1080 (16:9). Waktu = detik **sejak adegan mulai**, atau **rujukan narasi**: `'L03'` (awal baris), `'L03.w4'` (kata ke-4 baris itu), `'L03.akhir'`, ditambah `+0.2`/`-0.3`; juga id adegan (`'koran.akhir'`). Contoh lengkap: `contoh/n250.konfig.js`.

## KONFIG
| Kunci | Bawaan | Isi |
|---|---|---|
| `judul` | — | judul (jadi `<title>` dan nama file ekspor) |
| `rasio`, `fps` | `'9:16'`, 30 | |
| `durasiTarget` | `[30, 70]` | rentang durasi yang lolos cek |
| `narasiMulaiMaks` | `.15` | batas detik narasi mulai (cek). Naikkan untuk **hook tanpa suara** (skit POV, kartu judul): mis. `7.3` bersama `rakit --mulai 7` (narasi baru terdengar di detik 7) |
| `ekorMaks` | `.9` | batas detik sesudah kata terakhir (cek). Naikkan untuk **penutup visual tanpa narasi** (bingkai akhir/loop ke hook): mis. `2.6` bersama `durasi: 'L27.akhir+2.2'` |
| `tema` | `'arsip'` | paket tampilan per jenis topik: `arsip` · `dosir` · `pasar` · `teknologi` · `tv` · `modern` · `perang` · `alam` · `editorial` · `kartu`, plus **8 tema gaya dari reel acuan** (27 Nov 2026): `sinema-kasus` · `legenda-gelap` · `piksel-kertas` · `panggung-emas` · `arsip-pop` · `kaca-gradien` · `panggung-korporat` · `diorama-kreator` (grade + warna aksen + stabilo + latar bawaan + gaya huruf; tabel di `tema.md`). Nama tema yang salah ketik diam-diam jatuh ke `arsip`. `grade`/`palet`/`gayaTeks`/`latar` yang ditulis sendiri tetap menang; musik tidak otomatis dari tema |
| `benih` | dari `judul` | angka variasi (progresi akord, nada dasar, pola petikan musik sintesis); otomatis beda tiap judul |
| `grade` | dari `tema` | `'arsip'` · `'hangat'` · `'dingin'` · `'tv'` (garis layar) · `'dosir'` (teal gelap kontras) · `'modern'` (pekat, tanpa halftone) · `'perang'` (pudar berdebu) · `'alam'` · `'polos'`, atau objek `{ tint, kuat, saturasi, halftone, grain, vinyet, debu, garis, kontras }` (menimpa `arsip`). Per adegan: `grade: {...}` |
| `palet` | dari `tema` | `{ kertas, gelap, merah, kuning, stabilo, biru, tinta }` (`kuning` = aksen kata `*…*`, `merah` = stiker/label/cap, `stabilo` = warna sorot bawaan) |
| `subtitle` | tanpa | **bawaan tanpa subtitle** (sejak 1.2, permintaan pengguna). Nyalakan hanya bila diminta: `{ gaya: 'pil' }` (pil gelap, 1–3 kata, ±62% tinggi); `maksKata`, `posisi` (0–1), `ukuran`. Per adegan: `subtitle: false`, `posisiSub` |
| `musik` | | `{ sintesis: 'dokumenter' \| 'misteri' \| 'tegang' \| 'pad' \| 'pulsa' \| 'ceria' \| 'jenaka', bpm, kunci (Hz), akord, vol, mulai, akhir }` (`kunci`/`akord` kosong = dipilih dari `benih`; pakai `musik` yang disarankan tema) atau daftar segmen; berkas lewat `rakit --musik` |
| `sumber` | wajib | `[{ fakta, url }]` — kosong = cek SALAH (kecuali `data: false`) |
| `sfx` | | SFX global `[{ t, jenis \| berkas, vol, lama }]` |
| `sfxOtomatis` | `true` | bunyi otomatis perpindahan + benda masuk + stabilo + angka + cap |
| `sfxPeta` | | ganti bunyi sintesis otomatis dengan berkas yang ditanam `rakit --sfx DIR` (nama berkas tanpa ekstensi): `{ whoosh: 'whoosh-sedang', swish: 'swish-cepat', kertas: 'kertas-amplop', stempel: 'stempel', dum: { berkas: 'boom-rendah', vol: .8, lama: 2 }, kamera: 'rana' }`. Jenis otomatis: `whoosh` `swish` `kertas` `stempel` `dum` `kamera` `spidol` `gulir` `ketik` `pop`. Bunyi tunggal di adegan: `sfx: [{ t: 'L06.w4+0.22', berkas: 'palu', vol: .9 }]`; matikan bunyi otomatis satu lapisan dengan `sfx: false` |
| `gayaTeks` | | gaya huruf global (biasanya dari acuan visual, `acuan.md`): `{ <nama gaya>: { font, gaya, uk, warna, kapital, bayang, kotak } }`, mis. `{ tebal: { warna: '#0b2a4a' }, serif: { warna: '#5a3b1c' } }`; per lapisan tetap bisa `gayaTeks: {...}` |
| `bunyiMuncul` | | bunyi tiap lapisan muncul (pengguna 20 Nov 2026: "di setiap ada teks atau icon muncul pakai sfx premium"; 28 Nov 2026: "harus ada sfx-nya yang cocok"). **Bawaan (tak ditulis / `true`) = pencocok otomatis dari pustaka** (lihat SFX di bawah). `false` = mati; objek `{ teks, gambar, benda, coret, vol }` = satu bunyi per jenis (gaya lama). Per lapisan: `bunyi: 'nama'` / `{ berkas, vol, geser }`; `sfx: false` membisukan |
| `kameraHidup` | `true` | napas kamera halus |
| `thumbnail` | | `{ t }` bingkai untuk `thumbnail` |
| `teks` | | tanpa narasi: `[{ mulai, akhir, teks }]` jadi subtitle |
| `ekor`, `lufs`, `rapatkan`, `lajuNarasi`, `bitrate` | 0,35 · −14 · 0,4 · 1 · otomatis | sama dengan cerita-html |
| `volume`, `volumeSfx`, `volumeSuara` | 0,9 · 1 · 1,1 | pengali bus master / semua SFX / narasi (sebelum kompresor dan normalisasi LUFS). Musik berkas (`rakit --musik`, `--vol-musik`) otomatis diredam ke 30% selama tiap baris narasi lalu naik lagi; musik sintesis ke 32% |

**Opsi SFX berkas** (`{ t, berkas, vol, … }` di `sfx` adegan/global): `lama` (detik atau rujukan narasi sebagai waktu selesai), `ulang: true` (diulang, bawaan 4 dtk; untuk ambience/room tone), `masuk` (lama fade-in, bawaan 0,02, maks 0,3), `dari` (mulai dari detik ke-n di dalam berkas). Fade-out 0,3 dtk otomatis di akhir `lama`.
**Kamera dan easing berupa fungsi**: `kamera: t => ({ x, y, zoom, putar })` (t = detik sejak adegan mulai; untuk handheld berlapis atau gerak berirama musik) dan easing keyframe `[[t, nilai, x => …]]` (mis. tangga `x => Math.floor(x * 8) / 8` untuk gerak patah-patah). Keduanya didukung mesin sejak 1.1 tetapi baru dicatat 27 Nov 2026.

## ADEGAN (urut)
`{ id, mulai|durasi|akhir, masuk, arahMasuk, titikMasuk, lamaMasuk, kuatMasuk, bingkai, latar, kamera, lapis: [...], efek: [...], sfx: [...], gambar(c,t,d,T) }`
- `mulai`/`akhir`: angka atau rujukan narasi. Biasanya `mulai: 'L05.w4'` dan `akhir` dibiarkan (= mulai adegan berikutnya).
- `masuk`: perpindahan dari adegan sebelumnya (tabel di bawah). Tanpa `masuk` = potong keras.
- `latar`: pola di belakang semua lapisan (`{ pola, warna, ... }`, lihat Pola).
- `kamera`: preset (`'dorong'` bawaan · `'dorong-kuat'` · `'mundur'` · `'naik'` · `'turun'` · `'kiri'` · `'kanan'` · `'guling'` · `'tenang'`; preset direntang sepanjang adegan) atau keyframe `[[t, { x, y, zoom, putar }, ease], ...]`. `y` positif = kamera melihat lebih ke bawah.

### Perpindahan (`masuk`)
Tata bahasa acuan (bedah ulang 18 Nov 2026, video wabah @earn.edits): **perpindahan terjadi di kamera dan kedalaman, bukan dua gambar datar yang ditukar**. Adegan lama dipercepat ke satu arah sampai titik potong, adegan baru melanjutkan kecepatan itu lalu melambat (outQuart), lapisan depan (`z` besar) tertinggal lebih jauh dan kabur gerak lebih panjang, adegan baru mulai sedikit tidak fokus. Adegan baru sudah tergambar dan bergerak sebelum titik potong (lapisan yang mulai di detik 0 ikut tampil).

**Potong bermomentum** (lama 0; tidak dihitung potong keras):
| Nama | Gerak | Opsi | Bunyi |
|---|---|---|---|
| `dorong` | kamera melesat maju (zoom ×1,85 dipercepat), adegan baru mendarat dari zoom kecil | `titikMasuk: [x, y]` = titik di adegan **lama** yang didorong (foto koran, layar TV, jendela); `kuatMasuk` (pengali) | whoosh |
| `tarik` | kamera mundur cepat, adegan baru mulai dekat (×1,55) lalu terus mundur | `titikMasuk`, `kuatMasuk` | whoosh |
| `sentak` | whip: kamera melesat ke `arahMasuk` (adegan baru datang dari arah itu); latar penuh otomatis diperbesar supaya tepinya tak terlihat | `arahMasuk` (bawah/atas/kiri/kanan), `kuatMasuk` | swish |
| `putar` | kamera berputar + maju, adegan baru masih miring lalu tegak | `arahMasuk: 'kiri'` (berlawanan jarum jam) | whoosh |

**Perpindahan berlapis** (dua adegan digambar bersama, berpusat di batas adegan):
| Nama | Lama | Opsi adegan | Bunyi |
|---|---|---|---|
| `tutup` | 0,5 | `arahMasuk` (bawah/atas/kiri/kanan), `putarMasuk` (°, bawaan 0). Panel bersudut bulat naik (outQuart) dan **isinya tertinggal lalu menyusul** | kertas |
| `buka` | 0,45 | `arahMasuk` (arah adegan lama keluar) | kertas |
| `bingkai` | 0,95 | `bingkai: { lapis: 'id', bentuk, sisip, hp, garis, tebal }`. Adegan lama **mundur menjadi foto/layar** di lapisan ber-`id` adegan baru (lab → foto di koran, ruang → layar TV), berwarna → hitam-putih (`hp: false` mematikan). `bentuk`: `'kotak'` · `'bulat'` · `'peti'` (heksagon) · `'kunci'` (lubang kunci). `sisip: [kiri, atas, kanan, bawah]` (pecahan) bila fotonya hanya sebagian lapisan. `arahMasuk: 'masuk'` = kebalikannya: kamera **menyelam ke** bingkai lapisan ber-`id` di adegan lama sampai adegan baru memenuhi layar. Isi lapisan bingkai sebaiknya gambar yang sama supaya tidak meletup di akhir | whoosh |
| `zoom` | 0,5 | `titikMasuk: [x, y]` titik yang ditembus (versi datar; utamakan `dorong`) | whoosh |
| `fokus` | 0,5 | kabur lensa memuncak di titik potong, adegan baru menajam sambil sedikit mundur | swish |
| `geser` | 0,36 | `arahMasuk` (arah gerak; bawaan atas); isi adegan baru tertinggal sedikit | swish |
| `jatuh` | 0,55 | | dum |
| `lempar` | 0,5 | `arahMasuk: 'kiri'` | swish |
| `kartu` | 0,75 | | kertas |
| `strip` | 0,55 | `jumlahMasuk` (6) | swish |
| `iris` | 0,6 | `titikMasuk` | whoosh |
| `kilat` | 0,24 | `warnaMasuk` | kamera |
| `cocok` | 0,8 | `cocok: 'id'` (lapisan ber-`id` sama di kedua adegan) atau `{ dari: 'idLama', ke: 'idBaru' }`. Benda itu melayang dari posisi/ukuran/putaran di adegan lama ke posisinya di adegan baru (inOutCubic + blur gerak); bila gambarnya beda (amplop → dokumen surat) keduanya saling melebur di jalan. Latar lama kabur keluar, latar baru menajam masuk. Lapisan tujuan sebaiknya sudah tampil di detik 0 adegan baru | whoosh |
| `lubang` | 0,7 | **1.5.** Lingkaran berisi adegan baru tumbuh dari `titikMasuk` (titik di adegan **lama**: roda, lensa, lampu, mata, koin) sambil bergeser ke tengah, adegan lama ikut terdorong + kabur. `warnaMasuk` = warna cincin cahaya (bawaan putih, `false` = tanpa cincin), `putarMasuk` (°) = isi lingkaran berputar tegak | whoosh |
| `portal` | 0,85 | **1.5.** Kamera masuk lewat jendela/pintu/layar/lensa di adegan lama yang **sudah memperlihatkan** adegan baru. Ditulis di adegan baru: `portal: { kotak: [x, y, w, h] (piksel bingkai, lubang di adegan lama), bentuk: 'kotak'\|'bulat'\|'peti'\|'kunci' }`. Bedanya dengan `bingkai` arah `masuk`: tidak perlu lapisan ber-`id`, lubangnya boleh bagian dari foto (jendela di pelat) | whoosh |
| `sapu` | 0,6 | **1.5.** Benda gelap lewat dekat lensa (bayangan, tiang, orang lewat) menutup layar, adegan berganti di baliknya. `arahMasuk` = arah gerak benda (bawaan `'kiri'`), `warnaMasuk` (bawaan hampir hitam). Layar gelap penuh 1–2 bingkai di titik potong memang disengaja (cek mengecualikan ±0,1 dtk di sekitarnya); adegan tujuan tetap butuh gambar/latar bertekstur, bukan polos gelap | swish |
| `lepas` | 0,6 | **1.5.** Adegan lama (kertas, papan klip, foto, kartu) terangkat ke arah kamera: membesar, miring, kabur, memudar; adegan baru sudah menunggu di bawahnya. `arahMasuk` (bawaan `'bawah'`), `putarMasuk` (10°) | whoosh |
| `glitch` | 0,36 | irisan layar bergeser + pisah warna, adegan berganti di tengah (gaya animasi-html) | glitch |
| `lebur` | 0,4 | | — |
| `potong` | 0 | | — |

`sfxMasuk: false` membisukan bunyinya. Cek memberi saran bila satu jenis dipakai > 3 kali atau dua kali berturut-turut.

## Lapisan (`lapis`, digambar urut; `z` hanya mengatur parallax)
Sifat bersama:
| Kunci | Isi |
|---|---|
| `x`, `y` | pusat lapisan (bawaan tengah bingkai) |
| `z` | kedalaman parallax 0 (jauh, bergerak sedikit) … 1 (bawaan) … 2+ (depan, bergerak banyak). Pelat penuh bawaan 0,3, pola 0 |
| `lebar` / `tinggi` / `skala` | ukuran (gambar: piksel tampil; `skala` = pengali ukuran bawaan). Benda: lebar diatur di dalam `benda` |
| `putar` (°), `alfa`, `blur` (px), `balik` | |
| `poros` | `'atas'` (lama: berporos di tepi atas) atau **1.5** `[u, v]` (0–1 di lapisan) = titik putar/skala/condong lapisan, mis. `[.5, 1]` = berayun di dasarnya, `[0, .5]` = engsel kiri. Tanpa `poros` = tengah |
| `condong` | **1.5.** skew horizontal dalam derajat (bisa di `gerak`): pintu/daun jendela membuka, benda "menahan" sebelum bergerak, follow-through |
| `induk` | **1.5.** `'id'` lapisan lain di adegan yang sama: lapisan ini ikut geser, putar, skala, dan alfa induknya (label menempel pada benda yang bergoyang, tangan pada badan). `x`/`y` anak tetap ditulis dalam piksel bingkai saat induk diam di tempatnya. Induk belum/sudah tidak tampil = anak tidak tampil |
| gerak sekunder | **1.5.** osilasi terus-menerus, ditambahkan di atas `gerak`/`masuk` (juga di tiap elemen): `putaran: 240` (°/dtk; roda, kipas, jarum) · `goyang: { sudut: 3, periode: 2.4, fase }` (berayun di `poros`) · `denyut: { skala: .04, periode: 1.6, fase }` · `ombak: { x: 0, y: 8, periode: 3, fase }` (mengapung) · `arus: { x, y (px/dtk), skala (/dtk), pudar (/dtk) }` (awan, asap, debu) · `kedip: { kuat: .35, laju: 3 }` (lapisan: alfa berkedip). `true` = nilai bawaan. Beri `fase` berbeda (0–1) supaya benda sejenis tidak serempak |
| `elemen` | **1.5.** daftar wilayah di dalam **gambar lapisan ini** yang dihidupkan sendiri-sendiri (lihat `elemen` di bawah dan `references/gerak-elemen.md`) |
| `t`, `akhir` | muncul / hilang (detik adegan atau rujukan) |
| `masuk` | `'terbang'` · `'geser'` · `'jatuh'` · `'lempar'` · `'pop'` · `'tumbuh'` · `'kabur'` · `'naik'` · `'muncul'` · `'sapu'` · `'cap'`, atau `{ gaya, dari: 'bawah'\|'atas'\|'kiri'\|'kanan', lama, putar, guncang }`. **`terbang`** (acuan: tokoh/mik datang dari dekat lensa): mulai besar + kabur di tepi `dari`, melayang mundur ke tempatnya sambil menajam (outExpo 0,6 dtk); opsi `skala` (1,5 = 2,5× ukuran awal), `blur` (34), `jarak` (0,42) |
| `keluar` | `{ gaya: 'geser'\|'jatuh'\|'lempar'\|'kabur'\|'terbang'\|'susut'\|'pudar', ke, lama }` (mulai di `akhir`; `terbang` = melesat ke arah lensa) |
| `id` | nama lapisan (dipakai `bingkai` dan `cocok`) |
| `rig` | gerak bengkok seperti Puppet Pin (jaring segitiga 6×8, tidak untuk `urutan`): `'napas'` · `'goyang'` · `'tekuk'` · `'angguk'` · `'kibar'` · `'miring'` (putar 3D semu berperspektif ala kamera After Effects: `y` = putar kiri-kanan, `x` = depan-belakang, derajat/keyframe, `jarak` 2,2; juga untuk benda tanpa isi dinamis seperti `kartu`), objek `{ jenis, poros: [u, v] (0–1 di gambar), arah: 'atas'\|'bawah'\|'kiri'\|'kanan' (bagian yang bergerak dilihat dari poros), sudut, lentur (goyang, 1,4), lembut (tekuk/angguk, 0,08), amp, periode, fase, dari, panjang (kibar) }`, atau daftar beberapa. `sudut`/`amp` = angka, osilasi `{ amp, periode, fase, dasar }`, atau keyframe `[[t, nilai, ease], ...]`. Bawaan: goyang poros [.5, 1] ±2,2° / 3,6 dtk; tekuk 0°; angguk poros [.5, .32] ±3°; napas ±1,2% / 3,6 dtk; kibar dari kiri 2,5% / 1,6 dtk. Blur gerak lapisan ber-rig dibatasi 4 sampel |
| `klip` | kontrol klip (`urutan`, atau foto hidup pada `gambar`): `{ kode (foto hidup: klip yang menggantikan gambar ini), t (mulai bergerak, detik/rujukan), lebur (.25), mulai (detik di dalam video), laju (1; .5 = lambat), ulang, pantul, tahan }`. Foto hidup: bingkai pertama klip = gambar itu (klip Flow dibuat dari gambar itu), jadi peralihannya tak terlihat (`klip.md`) |
| `kilap` | `true` / `{ t, lama: .8, sudut: 24, lebar: .22, kuat: .6, warna }`: pita cahaya menyapu permukaan lapisan sekali (gambar, kartu, HP, cap) |
| `panel` | `[x, y, lebar, tinggi]` (piksel bingkai): lapisan hanya tampil di kotak layar itu dan kotaknya tidak ikut kamera, untuk **layar terbelah** atas-bawah/kiri-kanan. Contoh hook: `{ gambar: 'akar', x: 540, y: 470, lebar: 1140, panel: [0, 0, 1080, 955] }`, `{ gambar: 'piring', …, panel: [0, 965, 1080, 955] }`, garis pemisah `{ pola: { pola: 'polos', warna: '#f4efe2' }, panel: [0, 955, 1080, 10] }` |
| `jangkar` | potongan yang terpotong di gambar aslinya ditempel ke tepi layar (garis potong selalu di luar layar, juga saat kamera bergerak). Bawaan otomatis dari piksel tepi gambar transparan (sisi yang ≥ 3% pikselnya opak dan ≥ 40% sisi terkuat; yang didorong keluar hanya rentang opaknya). Sekali per lapisan, dari posisi diamnya (sesudah masuk): sisi yang perlu digeser ≤ 45% lebar/tinggi layar ditempel; sisi yang lebih jauh (lapisan sengaja di tengah) tidak menyeret lapisan, tetapi **dipudarkan halus** 20% dari sisi itu, dan cek memberi saran. `'bawah'`/`['bawah','kiri']` = paksa tempel; `false` = mati. Tidak berlaku untuk pelat penuh |
| `gerak` | keyframe nilai `[[t, { x, y, skala, putar, condong, alfa, blur }, ease], ...]`; `ease` = nama di `E` (`outCubic`, `outBack`, `pegas`, …) atau fungsi |
| `ayun` | `true` atau `{ sudut: 14, periode: 1.1, redam: 1.4, t }` — berayun berporos di atas (label harga) |
| `hidup` | `true`/angka px: melayang pelan |
| `bayangan` | `true`/0–1: bayangan jatuh (potongan & benda) |
| `tepi` | `true`/tebal: garis putih stiker di sekeliling potongan |
| `hitamPutih`, `campur` | `campur`: mode blend canvas (`'multiply'`, `'luminosity'`, …) |
| `blurGerak: false`, `cek: false`, `sfx` | `sfx: 'pop'` / `{ jenis, vol, geser }` / `false` |

### `gambar: 'kode'` / `urutan: 'kode'`
Gambar dari `rakit --gambar DIR` (nama berkas tanpa ekstensi). Gambar opak tanpa `x/y/lebar/tinggi/skala` = **pelat penuh** (menutup layar, `lebih: 1.16` ruang untuk kamera). `urutan` = bingkai klip (`rakit --klip nama=video.mp4@15`), diputar sejak `t` (bawaan berulang; `klip: { pantul | tahan | laju | mulai }`). `rakit --klip nama=video.mp4@15:hijau` = klip berlatar hijau polos dibuang latarnya per bingkai → **potongan bergerak** transparan (jangkar tepi, bayangan, rig napas tetap jalan). Klip Flow: `references/klip.md`.

### `elemen: [...]` pada lapisan `gambar` (Kolase 1.5, 27 Nov 2026)
Satu gambar (Flow, foto berlisensi, kiriman pengguna) dipecah jadi bagian yang bergerak sendiri: layar berkedip, roda berputar, pohon bergoyang, lampu menyala. Elemen dipotong dari gambar yang sama (tepi lembut, dibuat sekali lalu disimpan), digambar di koordinat gambar induknya, jadi **ikut semua gerak lapisan** (kamera, parallax, `gerak`, `rig`, perpindahan, blur gerak).
```js
{ gambar: 'lab', elemen: [
  { nama: 'layar', bulat: [.277, .567, .062], kedip: { kuat: .45, laju: 7 } },          // terang-gelap acak
  { nama: 'roda', bulat: [.33, .45, .072], putaran: 240 },                                 // poros = pusat wilayah
  { nama: 'pohon', kotak: [.6, 0, 1, .4], poros: [.92, .42], goyang: { sudut: 1.6, periode: 3.4 }, tambal: true },
  { nama: 'lampu', kotak: [.35, 0, .65, .35], t: 'L04.w2', gerak: [[0, { terang: -.5 }], [.4, { terang: .25 }, 'outBack']] } ] }
```
| Kunci | Isi |
|---|---|
| wilayah | `kotak: [u0, v0, u1, v1]` (+`sudut` pecahan untuk sudut bulat) · `bulat: [u, v, ru(, rv)]` (`ru` pecahan lebar, `rv` pecahan tinggi; tanpa `rv` = lingkaran) · `titik: [[u, v], ...]` (poligon). Semua pecahan 0–1 lebar/tinggi gambar asli. Baca dari `scripts/elemen.py kisi`, periksa dengan `elemen.py uji` |
| `poros` | `[u, v]` di gambar (bawaan pusat wilayah): sendi, engsel, pusat roda, pangkal batang |
| `gerak` | keyframe `[[t, { x, y, putar, skala, condong, alfa, terang, blur }, ease], ...]`; `x`/`y` dalam piksel layar; `terang` −1…+1 (−.5 = redup, +.3 = menyala) |
| sekunder | `putaran`, `goyang`, `denyut`, `ombak`, `arus` sama dengan lapisan. **`kedip` elemen = terang-gelap** (`{ kuat: .35, laju: 3, dasar: 0 }`; `dasar` = terang rata-rata), karena elemen ditumpuk di atas piksel yang sama sehingga alfa tak terlihat; `mode: 'alfa'` untuk alfa |
| `rig` | rig mesh seperti lapisan (`'napas'`, `'kibar'`, objek `{ jenis, poros, … }`) khusus potongan elemen ini |
| `tambal` | `true`: wilayah asli di gambar dasar ditutup warna sekitar yang sangat kabur, supaya elemen yang bergeser/berayun jauh tidak meninggalkan salinannya. Tidak perlu untuk gerak di tempat (putaran, kedip, denyut kecil) |
| `lembut` | lebar tepi lembut (px gambar; bawaan ±0,6% sisi pendek) |
| `t`, `akhir`, `nama` | muncul/hilang (detik adegan/rujukan); `nama` hanya catatan |
Aturan: 2–5 elemen bergerak per adegan, satu jadi pusat perhatian; elemen sejenis beda `fase`/`laju`; gerak besar yang memperlihatkan belakang benda butuh potongan terpisah, bukan elemen. Tidak untuk `urutan` (klip). Resep per jenis benda: `references/gerak-elemen.md`.

### `coret: 'lingkar'|'panah'|'garis'|'silang'|'centang'|'kotak'`
Coretan spidol yang tergambar bertahap (anotasi ala acuan): `x, y, lebar, tinggi, warna` (`merah` bawaan · `kuning` · `putih` · `hitam` · `stabilo` · rgb), `tebal` (11), `t`, `lama` (.5), `putar`, `arah: 'kiri'` (panah).

### `teks: '…'`
| Kunci | Isi |
|---|---|
| `gaya` | **gaya editorial (1.4, dari acuan pengguna)**: `'serif'` (serif miring kecil gelap, baris pengantar), `'tebal'` (Inter 800 besar gelap, tidak kapital), `'sorot'` (Inter 800 putih di kotak hitam); pasangan khas: `serif` di atas `tebal`, kata penting di `sorot`. · `'judul'` (Archivo Black putih berbayang, kapital) · `'padat'` (Anton) · `'tahun'` (serif miring merah tua) · `'kutip'` · `'mesin'` (ketik gelap) · `'stiker'` (kotak merah tepi putih) · `'label'` (pil hitam) · `'tangan'` (Caveat) · `'gelap'` (hitam, untuk kertas) · `'elegan'` (serif miring putih berbayang, kata melayang ala acuan; cocok tema dosir/perang/alam) |
| penanda | `*kata*` = warna aksen (`aksen`, bawaan kuning) · `^kata^` = besar (`besar`, 1,5×) · `~kata~` = kecil |
| `ukuran`, `lebar` (bungkus), `rata` (`'tengah'`/`'kiri'`/`'kanan'`), `spasi`, `warna`, `garis` (warna tepi) | |
| `anim` | `'luncur'` (kata dari kanan + jejak) · `'jatuh'` (huruf jatuh memantul) · `'ketik'` · `'pop'` (per kata) · `'muncul'` (bawaan; pakai `masuk` lapisan untuk gerak) |
| `ikut: true` | tiap kata muncul **saat diucapkan** (dicocokkan ke waktu kata narasi sekitar `t`) |
| `tiap` | jeda antar-kata/huruf bila tidak `ikut` |

### `benda: { jenis: 'kustom', … }` dan layar HP kustom (Kolase 1.4, 20 Nov 2026)
Untuk tampilan yang tidak ada di daftar benda (layar keyboard, obrolan AI, panel peluang, data mengalir, ikon) konfig **menggambar sendiri** di kanvas benda; benda ikut parallax, perpindahan, `bayangan`, `hidup`, `alfa`, `blur` seperti benda lain.
```js
{ benda: { jenis: 'kustom', lebar: 1060, tinggi: 1380,
    dasar: (x, w, h, K) => { /* digambar SEKALI (bingkai/kartu statis) */ },
    lukis: (c, ly, t, K) => { /* tiap bingkai; c sudah di titik kiri-atas benda; ly = { a:0, b:0, w, h, r }; t = detik sejak adegan mulai */ } },
  x: 540, y: 1100, skala: .98 }
```
`hp` juga menerima `lukis: (c, ly, t, K)`: isi layar digambar konfig (dipotong ke layar bulat HP, di atas `gambar`/`urutan`, di bawah `notif`).
`K` = alat bantu: `K.a` (adegan; `K.a.mulai` = detik mulai adegan), `K.ref('L03.w5')` (rujukan narasi → detik **sejak adegan mulai**; waktu mutlak = `K.ref(r) + K.a.mulai`, pakai itu bila keadaan harus sama di dua adegan berurutan), `K.E` (easing), `K.jepit`, `K.lerp`, `K.acak`, `K.bulat(c, x, y, w, h, r)` (path sudut bulat), `K.HURUF`, `K.P`, `K.bungkus`, `K.lebarTeks`, `K.kunci`, `K.SK`.
Aturan: beri kanvas **padding** (±60 px) bila kartu punya bayangan sendiri (`shadowBlur` di `dasar`); **reset `shadowColor`/`shadowOffsetY`** setelah menggambar bayangan (bayangan berbunyi blur 0 + offset tetap tetap tergambar sebagai salinan teks bergeser); teks di dalam kanvas **tidak** diperiksa `cek` (tata letak teks lapisan `teks` tetap diperiksa), jadi jaga sendiri zona aman (di bawah 76% tinggi dan kanan di bawah 42% tinggi = area tombol aplikasi); kesalahan di fungsi digambar dicatat sekali dan tidak menghentikan render. Contoh: `contoh/ai-mikir.konfig.js` (keyboard HP, obrolan AI + papan peluang kata, panel banding, data mengalir ke model, gulungan kata, checklist, ikon).

### `angka: { dari, ke, lama, t, awal, akhir }`
Angka bergulir ala odometer dengan pemisah ribuan; `awal`/`akhir` = teks depan/belakang (`' MENIT'`), `aksenBaru: false` mematikan warna aksen digit yang berubah. Gaya teks sama (`gaya`, `ukuran`, `aksen`).
**Hanya bilangan bulat** (nilai dibulatkan ke bawah). Untuk desimal, gulirkan bagian bulatnya dan taruh sisanya di `akhir`: "3,6 KG" = `{ dari: 0, ke: 3, akhir: ',6 KG' }`; "0,01 MP" lebih baik sebagai teks biasa (`gaya: 'padat'`, `anim: 'jatuh'`).

### `benda: { jenis, … }` (teks ditulis kode; `*^~` dibuang)
| Jenis | Isi |
|---|---|
| `koran` | `nama` (fiktif), `tanggal`, `judul`, `sub`, `foto` (kode gambar; hitam-putih kecuali `warnaFoto: true`), `tinggiFoto` (0,5 × lebar), `isi` (teks kolom, diulang), `kolom` (3), `lebar` (900), `rata`, `ukuranJudul` |
| `dokumen` | `kop`, `nomor`, `judul`, `baris: [...]`, `lebar` (820), `ukuranBaris`, `klip` (penjepit) |
| `kartu` | `gambar`, `keterangan`, `warnaKet`, `lebar` (520), `tinggiFoto`, `hitamPutih` |
| `papan` | `teks` (ditulis kapur huruf demi huruf mulai `t`, `lama`), `lebar`, `tinggi`, `ukuran` |
| `label` | `teks`, `warna`, `ukuran` (label harga; pasangkan `ayun`) |
| `cap` | `teks`, `warna`, `ukuran` (pakai `masuk: 'cap'`) |
| `grafik` | `judul`, `data: [...]`, `maks`, `bentuk: 'batang'\|'progres'`, `label`, `nilaiLabel`, `sorotData`, `satuan`, `labelMaks`, `format: v => …`, `t`, `lama` |
| `tv` | `gambar` (gambar atau kode klip; diputar di layar bergaris), `klip` (kontrol putar), `warna: true` (bawaan hitam-putih), `lebar` |
| `hp` | HP modern: `gambar` atau `urutan` (klip) di layar, `klip`, `notif: { judul, teks, t, warnaIkon }` (turun dari atas layar), `lebar` (520), `warna` |
| `notif` | kartu notifikasi: `judul`, `teks`, `waktu`, `ikonTeks` (huruf di ikon), `warnaIkon`, `lebar` (760); masuk `{ gaya: 'geser', dari: 'atas' }` |
| `balon` | balon bicara: `teks`, `gaya` (`bicara`/`pikir`/`teriak`), `ekor` (`kiri`/`kanan`/`bawah`), `ukuran` (50), `lebarMaks`, `warna`, `warnaTeks` |
`sorot: [{ baris, t, lama, warna }]` (koran/dokumen): stabilo menyapu baris saat `t`. `baris`: `'judul'` · `'sub'` · `'isi'` (+`dari`, `jumlah`) · nomor baris dokumen (0, 1, …) atau nomor baris judul koran. `warna: 'merah'` atau rgba. `t` negatif = sudah tersorot sejak awal adegan.

### `pola: { pola, … }` (juga untuk `latar`)
`'editorial'` (1.4, dari acuan pengguna: gradasi terang `#f6f6f6 → #bdbdbd` atau `gelap: true`, dua lengkungan sabit abu yang berputar pelan, garis putus-putus berjalan, silang grid bila `grid: true`; `varian` 0–4 = susunan lengkungan, `warna`/`warnaTengah`/`warna2` gradasi, `warnaSabit: [..]`, `warnaPutus`, `sabit: false`, `putus: false`, `laju`) · `'kertas'` (krem bertekstur; `warna`, `tua` 0–1) · `'garis'` (kertas bergaris) · `'grid'` (kertas grid; `warna`, `jarak`, `warnaGaris`, `putar` °/dtk) · `'sinar'` (sinar dua warna berputar; `warna`, `warna2`, `jumlah`, `putar`) · `'spiral'` (cincin bergelombang; `warna`, `warna2`, `laju`) · `'polos'`.

## Efek adegan (`efek`)
`{ jenis: 'kilat', t, warna, lama, kuat, sfx }` · `{ jenis: 'kilau', t, lama: .9, kuat: 1, titik: [x, y], warna, sinar: 16, sfx }` (cahaya + sinar dari satu titik, ala reel acuan: palu diketuk, keputusan, angka puncak; bunyi `boom` otomatis) · `{ jenis: 'warna', t, akhir, warna, kuat }` (monokrom berwarna, mis. merah) · `{ jenis: 'lensa', t, akhir, r, titik }` (lingkaran teropong) · `{ jenis: 'gelap', t, akhir, kuat }` · `{ jenis: 'hue', t, akhir, derajat }` · `{ jenis: 'guncang', t, lama, kuat }`. Lapisan `jatuh`/`cap` otomatis mengguncang kamera saat mendarat.

**Efek ala After Effects (Kolase 1.3, gaya animasi-html yang ditulis ulang; semua gradien/bentuk murah, tanpa filter berat per bingkai kecuali glitch yang singkat):**
- Sekali jalan (`t`, `lama`): `{ jenis: 'cahaya', dari: 'kiri'|'kanan', y: .32, r: .5, warna, warna2, kuat: .75, lama: 1.4 }` cahaya bocor menyapu · `{ jenis: 'bakar', dari: 'kanan', lama: .8 }` film terbakar dari tepi + kilat · `{ jenis: 'glitch', lama: .45, kuat }` irisan bergeser + pisah warna · `{ jenis: 'garis', titik, jumlah: 40, dalam: 330, warna, lama: .6 }` garis kecepatan dari pusat.
- Berlangsung (`t` sampai `akhir`, masuk/keluar halus): `{ jenis: 'partikel', gaya: 'debu'|'abu'|'salju'|'kunang'|'hujan'|'gelembung'|'konfeti'|'koin', jumlah, warna, dari: [x, y] (konfeti/koin) }` · `{ jenis: 'bokeh', jumlah: 16, warna: [...], kuat: .5 }` · `{ jenis: 'berkas', titik, sudut: 20, sebar, jumlah: 6, lebar, panjang, warna, kuat }` (sinar cahaya) · `{ jenis: 'kabut', y: .62, tinggi: .2, laju, warna, kuat }` · `{ jenis: 'sorot', titik, keTitik, r: 330, kuat: .72 }` (lampu sorot, bisa bergeser).
- Cahaya ruang (**1.5**, berlangsung): `{ jenis: 'kerucut', titik: [x, y] (piksel bingkai, bawaan tengah atas), sudut: 28, panjang: 1.1 (× tinggi), kuat: .55, warna: '#fff4e0', gelap: 0–1 (gelapkan sekeliling) }` kerucut lampu gantung/sorot panggung + genangan cahaya di dasar · `{ jenis: 'jendela', titik, lebar: 620, tinggi: 760, panel: [2, 3], kusen: 26, sudut: -22, geser: 18, lembut: 14, kuat: .45, warna: '#fff1d6' }` cahaya jendela miring di dinding/lantai, kusen jadi bayangan, bergeser pelan. Keduanya membuat foto diam terasa punya ruang dan waktu (pagi, malam, panggung) tanpa gambar baru.
- Bunyi otomatis: glitch → glitch, bakar/garis → whoosh, cahaya → riser pelan (`sfx: false` mematikan).

## SFX (`sfx` adegan: `{ t, jenis, vol, lama }` atau `{ t, berkas, vol, lama, ulang, dari, puncak }`)
**Pustaka `sfx/` (sejak 28 Nov 2026, `sfx/README.md`, `scripts/pustaka_sfx.py`)**: `rakit` menemukan pustaka sendiri dan mengirim `sfxPetaBawaan` + `sfxInfo` (puncak tiap berkas) ke HTML, jadi setiap jenis di bawah otomatis dimainkan sebagai berkas Epidemic pustaka. Nama pustaka (`'hit-bersih'`) atau judul Epidemic aslinya boleh ditulis di `berkas`/`bunyi`/`sfxPeta`; hanya yang dipakai yang ditanam.
- `KONFIG.sfxPeta`: menimpa per kunci; kunci = jenis (`whoosh`) atau **peran** yang lebih khusus: `'masuk.<perpindahan>'` (`'masuk.sapu'`, `'masuk.portal'`, `'masuk.lepas'` sudah ada di bawaan) dan `'efek.<efek>'` (`'efek.kilau'`, `'efek.cahaya'`). Nilai = nama atau `{ berkas, vol, lama, dari, ulang }`. `sfxPeta: false` = bunyi sintesis lama; `rakit --tanpa-pustaka-sfx` = tanpa pustaka.
- **Puncak diselaraskan**: bunyi peta memuncak di titik kejadiannya (titik potong perpindahan, saat lapisan muncul/mendarat, akhir sapuan cahaya) memakai `puncak` di katalog; jenis berdurasi (`gulir`, `spidol`, `ketik`, `proyektor`, loop) tetap mulai di awal kejadian dan dipotong sepanjang `lama`-nya. Bunyi `berkas` yang ditulis sendiri mulai di `t`, kecuali `puncak: true` (puncaknya jatuh tepat di `t`); `bunyi` lapisan dan `bunyiMuncul` otomatis `puncak: true`.
- **Bunyi muncul cocok (bawaan sejak 28 Nov 2026)**: setiap lapisan teks, gambar non-latar, benda, dan coret yang muncul berbunyi, dipilih `kunciMuncul()` dari peta `muncul` di `sfx/katalog.json` (dikirim `rakit` sebagai `SUARA.bunyiMunculCocok`). Urutan kunci, paling khusus dulu: teks `teks.anim.<anim>` › `teks.<gaya>` › `masuk.<gaya>` › `teks`; gambar `masuk.<gaya>` › `gambar.ikon` (sisi tampil ≤ 400 px) / `gambar.potongan` (PNG transparan) / `gambar.foto` / `gambar.pelat` › `gambar`; benda `benda.<jenis>` › `masuk.<gaya>` › `benda`; coret `coret.<bentuk>` › `coret`; notifikasi HP `benda.notif` saat turun. Puncak bunyi di saat lapisan tiba (`jatuh`/`cap` saat mendarat); entri `durasi: true` (ketik, tulisan tangan, coretan) berbunyi sepanjang animasinya. Lapisan di detik 0 adegan juga berbunyi (0,12 dtk sesudah titik potong, sedikit lebih pelan); gambar utama yang datang bersama adegan tidak (bunyinya = bunyi perpindahan). Vol .9 (awal adegan .78) × vol entri, `laju` ±4% acak tetap tiap kemunculan; bertumpuk < 0,06 dtk → digeser 0,07 dtk; dekat puncak perpindahan → ×0,85. `bunyiMuncul: false` = mati; objek `{ teks, gambar, benda, coret, vol }` = satu bunyi per jenis (gaya 1.4). Per lapisan: `bunyi: 'nama'` / `{ berkas, vol, geser }`; `sfx: false` membisukan (cek memberi saran).
- `rakit --sfx DIR` (boleh berulang, termasuk subfolder): berkas khusus proyek, ditanam semua dan menang atas pustaka bila namanya sama.
Sintesis (cadangan bila pustaka tidak ada): `whoosh`, `swish`, `pop`, `klik`, `tik`, `ketik`, `impact`, `boom`, `riser`, `ding`, `benar`, `salah`, `kaching`, `koin`, `notif`, `glitch`, `dum`, `jantung`, `kamera`, `sub`, `kertas`, `stempel`, `spidol`, `gulir`, `proyektor`, `ketukan`.

## Cek (`hasilCek()`, `jalankan.py cek`)
Diperiksa tiap 0,1 dtk. **Salah**: durasi di luar `durasiTarget` · narasi mulai > 0,15 · jeda > 0,6 · ekor > 0,9 · potong keras > 3 · gambar hampir diam > 1 dtk · sumber kosong/tanpa url · teks keluar layar / di area tombol (kanan bawah, bawah 76%) / tertutup subtitle / saling menimpa · bingkai polos · LUFS ≠ −14 ±1 · galat konfig · gambar tidak ada. **Saran**: rata-rata > 3,2 dtk per adegan · adegan > 4,5 dtk · perpindahan < 4 jenis · teks < 0,7 dtk · teks dekat tepi/kecil · benda bertulisan di area keterangan · potongan yang digeser `jangkar` > 140 px ke tepi (atur posisinya). Teks yang sedang masuk (mengecil/kabur) tidak dinilai.

## jalankan.py
Foto/video nyata untuk topik berdata: `scripts/ambil_media.py cari|ambil|daftar` (`data-media.md`). `suara` (Edge `--edge` / ElevenLabs; angka & singkatan dieja Indonesia, `--tanpa-eja`), `kata` (rekaman sendiri → waktu kata), `rakit` (+ `--gambar DIR`, `--maks 2400`, `--klip nama=video.mp4@12`, `--musik`, `--sfx`, `--laju-narasi`), `cek`, `kontak` (`--n` / `--t`), `bingkai`, `thumbnail`, `ekspor`. Riwayat pilihan visual antar-video: `scripts/riwayat.py lihat` / `catat <_kerja>` (`gaya.md` §0.4). Ekspor 46 dtk 1080×1920 di PC ini: lihat catatan uji di `SKILL.md`.

## Riwayat
- 28 Nov 2026 pagi — video "7 Gembok Anti-Maling" (tema `kaca-gradien`, ±116 dtk dari storyboard pengguna): `KONFIG.ekorMaks` (penutup visual 2 dtk tanpa narasi); naskah `# ucap: HP = ha-pe; Face = feis; ID = ai-di` (ejaan ucapan khusus dikirim ke Edge/ElevenLabs, subtitle + rujukan tetap token naskah); `flow_kolase.py` gaya `studio3d` (render 3D krom untuk kaca-gradien). Catatan: keyframe `gerak` yang tidak menyebut `x`/`y` kembali ke nilai dasar lapisan, jadi tulis ulang posisi di setiap kunci. N250 dirakit ulang → BERES.
- 28 Nov 2026 dini hari (2) — **setiap teks/ikon yang muncul berbunyi cocok** (pengguna, sesudah melihat demo: "di setiap animasi baik teks atau icon yang muncul harus ada sfx-nya yang cocok"): `kunciMuncul()` + peta `muncul` (45 aturan) di katalog, bawaan aktif, `laju` acak tipis, penggeseran bunyi bertumpuk, notifikasi HP berbunyi, cek memberi saran untuk teks/ikon yang dibisukan. Diuji di Kodak: 53 lapisan muncul → 51 bunyi otomatis (2 sisanya dibisukan `sfx: false` di konfig lama; contoh revisi tanpa pembisuan itu), bunyi muncul 5–10 dB di bawah puncak narasi, cek BERES −14 LUFS.
- 28 Nov 2026 dini hari — **pustaka SFX jadi sumber utama** (permintaan pengguna: "utamakan sfx/sound efek pakai yang ada di sini … rapihkan foldernya … yang tidak cocok cari baru di Epidemic"). Folder `sfx/` dirapikan: 61 berkas datar bernama judul Epidemic → 7 kategori bernama pendek, hening depan dipotong, keras disamakan per kategori, puncak ≤ −1 dBFS (7 berkas dulu lewat 0 dBFS), `katalog.json`. Yang tidak cocok: "Cinematic Hit… Absolute Clean 04" ternyata dengung tertahan (jadi `dengung-naik`, hantaman diganti `hit-bersih`), glitch 1,9 dtk terlalu panjang untuk perpindahan 0,36 dtk (bawaan jadi `glitch-pendek`); 10 SFX baru dari Epidemic untuk celah (koin, lampu neon, saklar, roda/kaset berputar, sapuan rendah untuk `sapu`, angin untuk `portal`, hit gelap). Mesin: peta bawaan dari pustaka, kunci peran `masuk.*`/`efek.*`, puncak berkas diselaraskan ke titik kejadian, `puncak: true`, `bunyiMuncul: true`; `rakit` menemukan pustaka sendiri dan hanya menanam yang dipakai; `scripts/pustaka_sfx.py lihat|cek|tambah`. Diuji: video Kodak dirakit ulang → BERES, −14 LUFS, puncak −1 dB, 0 bunyi sintesis tersisa; SFX pustaka 3–8 dB di bawah puncak narasi (dulu swish/kertas/spidol/stempel sintesis 20–30 dB di bawah, nyaris tak terdengar); konfig uji 1.5: `portal`/`lubang`/`sapu`/`lepas` memuncak tepat di titik potong. Cek "bingkai polos" kini mengecualikan ±0,1 dtk di titik potong `sapu` (gelap penuh sesaat = wujud sapuan benda dekat lensa).
- 27 Nov 2026 larut — **Kolase 1.5: elemen hidup + rigging lapisan + 4 sambungan baru** (permintaan pengguna sesudah membedah reel @earn.edits `Del7Vohuw9D`: transisi kurang beragam, terlalu bergantung pada Google Flow, "tambahkan rigging, motion design, dan image animation… tanpa mengubah flow"). Baru: `elemen` (wilayah di dalam satu gambar dihidupkan sendiri, tepi lembut dibuat sekali, `tambal`), gerak sekunder `putaran`/`goyang`/`denyut`/`ombak`/`arus`/`kedip` untuk lapisan + elemen, `poros` lapisan berupa `[u, v]`, `condong` (skew), `induk` (lapisan anak ikut induk), `terang` di keyframe elemen; perpindahan `lubang`, `portal`, `sapu`, `lepas` (dari reel itu: jendela jadi portal ±1,5 dtk, lingkaran dari benda ±3,2/7,3/24,8 dtk, papan klip terangkat ±26,8 dtk, sapuan dekat lensa ±30,8 dtk); efek `kerucut` + `jendela`; `scripts/elemen.py kisi|saran|uji`; panduan `references/gerak-elemen.md`. Three.js tidak ditambahkan (Canvas 2,5D sudah cukup, ekspor tetap cepat). Diuji: konfig 5 adegan tanpa gambar baru, 0 galat; gerak elemen diukur (selisih piksel wilayah layar 33,9 vs dinding 6,9; roda kaset 38,6 vs 13,3; pohon dengan kamera diam 12,0 vs 2,4); semua sambungan + efek dilihat bingkainya. Kompatibel mundur: video Kodak dirakit ulang dengan mesin 1.5 → BERES 50,52 dtk, bingkai 3/17/33/45 dtk identik piksel dengan mesin 1.4.
- 27 Nov 2026 malam — **8 tema gaya dari reel acuan** ditanam di `TEMA` + `GRADE_DASAR` (`sinema-kasus`, `legenda-gelap`, `piksel-kertas`, `panggung-emas`, `arsip-pop`, `kaca-gradien`, `panggung-korporat`, `diorama-kreator`; permintaan pengguna: "skill saya diupdate agar ada beberapa style"). Data saja (tidak ada logika baru); huruf ditulis sebagai teks biasa karena `HURUF` dideklarasikan sesudah `TEMA`. `riwayat.py` kini membaca nama tema bertanda hubung. Diuji: konfig uji yang sama dirakit dengan tiap tema, bingkai dilihat, `cek` tanpa galat konfig.
- 27 Nov 2026 — dokumentasi saja (mesin tidak diubah): `volume`/`volumeSfx`/`volumeSuara`, opsi SFX berkas (`ulang`/`masuk`/`dari`/`lama`), kamera + easing berupa fungsi, peredaman musik saat narasi. Keputusan kreatif dipindah ke skill saudara `sutradara-edit` (pustaka 11 kategori + 7 resep gaya + `ketukan.py`); daftar celah mesin yang ditemukan pustaka ada di `AUDIT.md` akar repo.
- 20 Nov 2026 malam — acuan visual (permintaan pengguna: "setiap kali saya kirim referensi untuk visualnya dapat mengikuti juga, topik apa pun"): pola `editorial`, gaya teks `serif`/`tebal`/`sorot`, `KONFIG.gayaTeks` global, `scripts/bedah_acuan.py`, `references/acuan.md`; `contoh/ai-mikir` diubah memakai fitur itu (tanpa latar kustom).
- 20 Nov 2026 — Kolase 1.4 (video "AI Sebenarnya Nggak Mikir Kayak Manusia", storyboard dan 3 logo dari pengguna): benda `kustom` + `hp.lukis` (gambar-sendiri di kanvas benda, `K` alat bantu), `KT()` di mesin; tema `teknologi` tanpa foto Flow, semua visual digambar kode; logo kiriman pengguna (resolusi kecil, latar putih) diubah jadi ubin app-icon tajam lewat skrip sekali pakai (alfa dari ambang + penyebaran warna terdekat; dua-warna dipoles ulang dengan smoothstep). `contoh/ai-mikir.*` ditambahkan.
- 18 Nov 2026 malam — Kolase 1.3 (permintaan pengguna: kombinasi klip video Flow "hanya di bagian yang bagus" atau foto saja, efek "seperti animasi-html", "seolah saya mengedit dari After Effects", render tetap cepat): foto hidup (`gambar` + `klip.kode`), kontrol putar klip (`mulai`/`laju`/`pantul`/`tahan`), klip berlatar hijau → potongan bergerak (`rakit --klip …:hijau`), `flow_kolase.py klip`/`ambil-klip`, efek `cahaya`/`bakar`/`glitch`/`garis`/`partikel`/`bokeh`/`berkas`/`kabut`/`sorot`, lapisan `kilap`, `coret`, rig `miring` (3D), benda `hp`/`notif`/`balon`, perpindahan `glitch`, `panel` layar terbelah. Diuji dengan klip buatan ffmpeg (tanpa kredit) + contoh N250 (cek BERES).
- 18 Nov 2026 malam — Kolase 1.2 (permintaan pengguna: "tidak perlu ada subtitle pada bagian bawah", "pakai teknik rigging", "tidak ada objek yang terpotong", "transisi foto bagus… terapkan layer" seperti reel DffBJweOo9e): subtitle bawaan mati; `jangkar` tepi otomatis untuk potongan yang terpotong di gambar aslinya; `rig` jaring segitiga (`napas`/`goyang`/`tekuk`/`angguk`/`kibar`); perpindahan `cocok` (benda tetap, dunia berganti); efek `kilau`; cek saran jangkar; `scripts/ambil_media.py` (foto/video nyata Wikipedia/Commons/NASA/YouTube/berkas pengguna + kredit). Diuji di proyek Gibran: cek BERES, 13 jenis perpindahan, tangan tidak terpotong lagi.
- 18 Nov 2026 — Kolase 1.1 (permintaan pengguna: "transisinya masih sangat jauh", acuan video wabah @earn.edits `igexport-De6bR-1OtGX.mp4`, 42,7 dtk): momentum kamera (`dorong`, `tarik`, `sentak`, `putar`), adegan baru tergambar sebelum titik potong + isi tertinggal (`tutup`, `geser`, `fokus`), `bingkai` (adegan jadi foto/layar), lapisan `terbang`, blur gerak sampai 28 sampel, latar penuh otomatis menutup saat kamera berputar/bergeser, kabur lensa adegan di titik potong; `tema` per topik + `benih` musik, gaya teks `elegan`, grade `dosir`/`modern`/`perang`/`alam`; cek saran perpindahan berulang + tema kosong; `contoh/n250` 11 jenis perpindahan, 0 potong keras, cek BERES.
- 18 Nov 2026 — Kolase 1.0: dibuat dari bedah @earn.edits; uji `contoh/n250` (46,5 dtk, 17 adegan, 9 jenis perpindahan, cek BERES, −14 LUFS). Penyelaras kata Edge diganti (difflib + pecah token gabungan).
