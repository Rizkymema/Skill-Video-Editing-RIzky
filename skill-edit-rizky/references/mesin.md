# Mesin Kolase 1.4 — API konfig

File: `assets/templat.html`. Per video hanya blok `<script id="konfig">` (KONFIG + ADEGAN) yang ditulis, lewat `jalankan.py rakit konfig.js film.html …`. Koordinat = piksel bingkai 1080×1920 (9:16) atau 1920×1080 (16:9). Waktu = detik **sejak adegan mulai**, atau **rujukan narasi**: `'L03'` (awal baris), `'L03.w4'` (kata ke-4 baris itu), `'L03.akhir'`, ditambah `+0.2`/`-0.3`; juga id adegan (`'koran.akhir'`). Contoh lengkap: `contoh/n250.konfig.js`.

## KONFIG
| Kunci | Bawaan | Isi |
|---|---|---|
| `judul` | — | judul (jadi `<title>` dan nama file ekspor) |
| `rasio`, `fps` | `'9:16'`, 30 | |
| `durasiTarget` | `[30, 70]` | rentang durasi yang lolos cek |
| `tema` | `'arsip'` | paket tampilan per jenis topik: `arsip` · `dosir` · `pasar` · `teknologi` · `tv` · `modern` · `perang` · `alam` (grade + 2 warna aksen + warna stabilo + musik; tabel kapan dipakai di `gaya.md` §0). `grade`/`palet`/`musik` yang ditulis sendiri tetap menang |
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
| `bunyiMuncul` | | bunyi tiap lapisan muncul (permintaan pengguna 20 Nov 2026: "di setiap ada teks atau icon muncul pakai sfx premium"): `{ teks: 'teks', gambar: 'ikon', benda: 'popup', coret: 'spidol', vol: .55 }` (nama berkas dari `rakit --sfx DIR`, atau objek `{ berkas, vol, geser }`); hanya lapisan yang muncul sesudah adegan mulai, `cap` tetap stempel. Per lapisan: `bunyi: 'salah'` / `{ berkas, vol, geser }`; `sfx: false` membisukan |
| `kameraHidup` | `true` | napas kamera halus |
| `thumbnail` | | `{ t }` bingkai untuk `thumbnail` |
| `teks` | | tanpa narasi: `[{ mulai, akhir, teks }]` jadi subtitle |
| `ekor`, `lufs`, `rapatkan`, `lajuNarasi`, `bitrate` | 0,35 · −14 · 0,4 · 1 · otomatis | sama dengan cerita-html |

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
| `t`, `akhir` | muncul / hilang (detik adegan atau rujukan) |
| `masuk` | `'terbang'` · `'geser'` · `'jatuh'` · `'lempar'` · `'pop'` · `'tumbuh'` · `'kabur'` · `'naik'` · `'muncul'` · `'sapu'` · `'cap'`, atau `{ gaya, dari: 'bawah'\|'atas'\|'kiri'\|'kanan', lama, putar, guncang }`. **`terbang`** (acuan: tokoh/mik datang dari dekat lensa): mulai besar + kabur di tepi `dari`, melayang mundur ke tempatnya sambil menajam (outExpo 0,6 dtk); opsi `skala` (1,5 = 2,5× ukuran awal), `blur` (34), `jarak` (0,42) |
| `keluar` | `{ gaya: 'geser'\|'jatuh'\|'lempar'\|'kabur'\|'terbang'\|'susut'\|'pudar', ke, lama }` (mulai di `akhir`; `terbang` = melesat ke arah lensa) |
| `id` | nama lapisan (dipakai `bingkai` dan `cocok`) |
| `rig` | gerak bengkok seperti Puppet Pin (jaring segitiga 6×8, tidak untuk `urutan`): `'napas'` · `'goyang'` · `'tekuk'` · `'angguk'` · `'kibar'` · `'miring'` (putar 3D semu berperspektif ala kamera After Effects: `y` = putar kiri-kanan, `x` = depan-belakang, derajat/keyframe, `jarak` 2,2; juga untuk benda tanpa isi dinamis seperti `kartu`), objek `{ jenis, poros: [u, v] (0–1 di gambar), arah: 'atas'\|'bawah'\|'kiri'\|'kanan' (bagian yang bergerak dilihat dari poros), sudut, lentur (goyang, 1,4), lembut (tekuk/angguk, 0,08), amp, periode, fase, dari, panjang (kibar) }`, atau daftar beberapa. `sudut`/`amp` = angka, osilasi `{ amp, periode, fase, dasar }`, atau keyframe `[[t, nilai, ease], ...]`. Bawaan: goyang poros [.5, 1] ±2,2° / 3,6 dtk; tekuk 0°; angguk poros [.5, .32] ±3°; napas ±1,2% / 3,6 dtk; kibar dari kiri 2,5% / 1,6 dtk. Blur gerak lapisan ber-rig dibatasi 4 sampel |
| `klip` | kontrol klip (`urutan`, atau foto hidup pada `gambar`): `{ kode (foto hidup: klip yang menggantikan gambar ini), t (mulai bergerak, detik/rujukan), lebur (.25), mulai (detik di dalam video), laju (1; .5 = lambat), ulang, pantul, tahan }`. Foto hidup: bingkai pertama klip = gambar itu (klip Flow dibuat dari gambar itu), jadi peralihannya tak terlihat (`klip.md`) |
| `kilap` | `true` / `{ t, lama: .8, sudut: 24, lebar: .22, kuat: .6, warna }`: pita cahaya menyapu permukaan lapisan sekali (gambar, kartu, HP, cap) |
| `panel` | `[x, y, lebar, tinggi]` (piksel bingkai): lapisan hanya tampil di kotak layar itu dan kotaknya tidak ikut kamera, untuk **layar terbelah** atas-bawah/kiri-kanan. Contoh hook: `{ gambar: 'akar', x: 540, y: 470, lebar: 1140, panel: [0, 0, 1080, 955] }`, `{ gambar: 'piring', …, panel: [0, 965, 1080, 955] }`, garis pemisah `{ pola: { pola: 'polos', warna: '#f4efe2' }, panel: [0, 955, 1080, 10] }` |
| `jangkar` | potongan yang terpotong di gambar aslinya ditempel ke tepi layar (garis potong selalu di luar layar, juga saat kamera bergerak). Bawaan otomatis dari piksel tepi gambar transparan (sisi yang ≥ 3% pikselnya opak dan ≥ 40% sisi terkuat; yang didorong keluar hanya rentang opaknya). Sekali per lapisan, dari posisi diamnya (sesudah masuk): sisi yang perlu digeser ≤ 45% lebar/tinggi layar ditempel; sisi yang lebih jauh (lapisan sengaja di tengah) tidak menyeret lapisan, tetapi **dipudarkan halus** 20% dari sisi itu, dan cek memberi saran. `'bawah'`/`['bawah','kiri']` = paksa tempel; `false` = mati. Tidak berlaku untuk pelat penuh |
| `gerak` | keyframe nilai `[[t, { x, y, skala, putar, alfa, blur }, ease], ...]` |
| `ayun` | `true` atau `{ sudut: 14, periode: 1.1, redam: 1.4, t }` — berayun berporos di atas (label harga) |
| `hidup` | `true`/angka px: melayang pelan |
| `bayangan` | `true`/0–1: bayangan jatuh (potongan & benda) |
| `tepi` | `true`/tebal: garis putih stiker di sekeliling potongan |
| `hitamPutih`, `campur` | `campur`: mode blend canvas (`'multiply'`, `'luminosity'`, …) |
| `blurGerak: false`, `cek: false`, `sfx` | `sfx: 'pop'` / `{ jenis, vol, geser }` / `false` |

### `gambar: 'kode'` / `urutan: 'kode'`
Gambar dari `rakit --gambar DIR` (nama berkas tanpa ekstensi). Gambar opak tanpa `x/y/lebar/tinggi/skala` = **pelat penuh** (menutup layar, `lebih: 1.16` ruang untuk kamera). `urutan` = bingkai klip (`rakit --klip nama=video.mp4@15`), diputar sejak `t` (bawaan berulang; `klip: { pantul | tahan | laju | mulai }`). `rakit --klip nama=video.mp4@15:hijau` = klip berlatar hijau polos dibuang latarnya per bingkai → **potongan bergerak** transparan (jangkar tepi, bayangan, rig napas tetap jalan). Klip Flow: `references/klip.md`.

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
- Bunyi otomatis: glitch → glitch, bakar/garis → whoosh, cahaya → riser pelan (`sfx: false` mematikan).

## SFX (`sfx` adegan: `{ t, jenis, vol, lama }`)
Sintesis: `whoosh`, `swish`, `pop`, `klik`, `tik`, `ketik`, `impact`, `boom`, `riser`, `ding`, `benar`, `salah`, `kaching`, `koin`, `notif`, `glitch`, `dum`, `jantung`, `kamera`, `sub`, `kertas`, `stempel`, `spidol`, `gulir`, `proyektor`, `ketukan`; berkas lewat `--sfx DIR` → `{ berkas: 'nama' }`.

## Cek (`hasilCek()`, `jalankan.py cek`)
Diperiksa tiap 0,1 dtk. **Salah**: durasi di luar `durasiTarget` · narasi mulai > 0,15 · jeda > 0,6 · ekor > 0,9 · potong keras > 3 · gambar hampir diam > 1 dtk · sumber kosong/tanpa url · teks keluar layar / di area tombol (kanan bawah, bawah 76%) / tertutup subtitle / saling menimpa · bingkai polos · LUFS ≠ −14 ±1 · galat konfig · gambar tidak ada. **Saran**: rata-rata > 3,2 dtk per adegan · adegan > 4,5 dtk · perpindahan < 4 jenis · teks < 0,7 dtk · teks dekat tepi/kecil · benda bertulisan di area keterangan · potongan yang digeser `jangkar` > 140 px ke tepi (atur posisinya). Teks yang sedang masuk (mengecil/kabur) tidak dinilai.

## jalankan.py
Foto/video nyata untuk topik berdata: `scripts/ambil_media.py cari|ambil|daftar` (`data-media.md`). `suara` (Edge `--edge` / ElevenLabs; angka & singkatan dieja Indonesia, `--tanpa-eja`), `kata` (rekaman sendiri → waktu kata), `rakit` (+ `--gambar DIR`, `--maks 2400`, `--klip nama=video.mp4@12`, `--musik`, `--sfx`, `--laju-narasi`), `cek`, `kontak` (`--n` / `--t`), `bingkai`, `thumbnail`, `ekspor`. Riwayat pilihan visual antar-video: `scripts/riwayat.py lihat` / `catat <_kerja>` (`gaya.md` §0.4). Ekspor 46 dtk 1080×1920 di PC ini: lihat catatan uji di `SKILL.md`.

## Riwayat
- 20 Nov 2026 malam — acuan visual (permintaan pengguna: "setiap kali saya kirim referensi untuk visualnya dapat mengikuti juga, topik apa pun"): pola `editorial`, gaya teks `serif`/`tebal`/`sorot`, `KONFIG.gayaTeks` global, `scripts/bedah_acuan.py`, `references/acuan.md`; `contoh/ai-mikir` diubah memakai fitur itu (tanpa latar kustom).
- 20 Nov 2026 — Kolase 1.4 (video "AI Sebenarnya Nggak Mikir Kayak Manusia", storyboard dan 3 logo dari pengguna): benda `kustom` + `hp.lukis` (gambar-sendiri di kanvas benda, `K` alat bantu), `KT()` di mesin; tema `teknologi` tanpa foto Flow, semua visual digambar kode; logo kiriman pengguna (resolusi kecil, latar putih) diubah jadi ubin app-icon tajam lewat skrip sekali pakai (alfa dari ambang + penyebaran warna terdekat; dua-warna dipoles ulang dengan smoothstep). `contoh/ai-mikir.*` ditambahkan.
- 18 Nov 2026 malam — Kolase 1.3 (permintaan pengguna: kombinasi klip video Flow "hanya di bagian yang bagus" atau foto saja, efek "seperti animasi-html", "seolah saya mengedit dari After Effects", render tetap cepat): foto hidup (`gambar` + `klip.kode`), kontrol putar klip (`mulai`/`laju`/`pantul`/`tahan`), klip berlatar hijau → potongan bergerak (`rakit --klip …:hijau`), `flow_kolase.py klip`/`ambil-klip`, efek `cahaya`/`bakar`/`glitch`/`garis`/`partikel`/`bokeh`/`berkas`/`kabut`/`sorot`, lapisan `kilap`, `coret`, rig `miring` (3D), benda `hp`/`notif`/`balon`, perpindahan `glitch`, `panel` layar terbelah. Diuji dengan klip buatan ffmpeg (tanpa kredit) + contoh N250 (cek BERES).
- 18 Nov 2026 malam — Kolase 1.2 (permintaan pengguna: "tidak perlu ada subtitle pada bagian bawah", "pakai teknik rigging", "tidak ada objek yang terpotong", "transisi foto bagus… terapkan layer" seperti reel DffBJweOo9e): subtitle bawaan mati; `jangkar` tepi otomatis untuk potongan yang terpotong di gambar aslinya; `rig` jaring segitiga (`napas`/`goyang`/`tekuk`/`angguk`/`kibar`); perpindahan `cocok` (benda tetap, dunia berganti); efek `kilau`; cek saran jangkar; `scripts/ambil_media.py` (foto/video nyata Wikipedia/Commons/NASA/YouTube/berkas pengguna + kredit). Diuji di proyek Gibran: cek BERES, 13 jenis perpindahan, tangan tidak terpotong lagi.
- 18 Nov 2026 — Kolase 1.1 (permintaan pengguna: "transisinya masih sangat jauh", acuan video wabah @earn.edits `igexport-De6bR-1OtGX.mp4`, 42,7 dtk): momentum kamera (`dorong`, `tarik`, `sentak`, `putar`), adegan baru tergambar sebelum titik potong + isi tertinggal (`tutup`, `geser`, `fokus`), `bingkai` (adegan jadi foto/layar), lapisan `terbang`, blur gerak sampai 28 sampel, latar penuh otomatis menutup saat kamera berputar/bergeser, kabur lensa adegan di titik potong; `tema` per topik + `benih` musik, gaya teks `elegan`, grade `dosir`/`modern`/`perang`/`alam`; cek saran perpindahan berulang + tema kosong; `contoh/n250` 11 jenis perpindahan, 0 potong keras, cek BERES.
- 18 Nov 2026 — Kolase 1.0: dibuat dari bedah @earn.edits; uji `contoh/n250` (46,5 dtk, 17 adegan, 9 jenis perpindahan, cek BERES, −14 LUFS). Penyelaras kata Edge diganti (difflib + pecah token gabungan).
