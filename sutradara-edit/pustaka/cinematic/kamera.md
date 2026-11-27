# Bahasa Kamera Sinematik

> Kategori **CINEMATIC** · dipakai di langkah 7 (juga 6 storyboard, 10 transisi) · terkait: `../motion/transisi.md`, `../motion/prinsip-animasi.md`, `../visual/komposisi.md`, `../motion/kolase-editorial.md`, `../style/gaya-visual.md`; implementasi: `skill-edit-rizky/references/mesin.md` (kamera, `z`, momentum)

Prinsip inti:
1. **Kamera adalah mata penonton yang punya niat.** Mendekat = ini penting; menjauh = lihat konteksnya; diam = dengarkan.
2. **Kecepatan = emosi.** Lambat = berat, serius, intim. Cepat = energi, urgensi, kejutan.
3. **Kedalaman membuat gerak kecil terasa besar.** Tiga lapis (depan/tengah/belakang) dengan zoom 6% lebih sinematik dari satu lapis dengan zoom 30%.
4. **Satu gerak kamera per adegan pendek.** Kombinasi (push + roll + pan) hanya bila setiap komponennya punya arti.
5. **Kamera tenang saat informasi padat.** Teks panjang, data, angka: kamera hampir diam. Gerak kamera tidak menggantikan cerita.

---

## 1. Arti setiap gerak
| Gerak | Arti emosional | Kecepatan & lama | Easing | Kapan **tidak** |
|---|---|---|---|---|
| Push in (maju) | fokus, kesadaran, keintiman, tekanan naik | subliminal +3–8% per 2–3 dtk; dramatis +15–30% dalam 1–2 dtk | `linear`/`inOutSine` (pelan), `inOutCubic` (dramatis) | saat penonton perlu melihat konteks luas |
| Pull out (mundur) | konteks, skala, kesepian, pengungkapan, penutup | 1,3 → 1,0 dalam 1–1,5 dtk | `outCubic`, `outQuart` | saat detail baru saja diperkenalkan |
| Pan / truck (kiri-kanan) | menjelajah, membandingkan A ke B, mengikuti | 60–180 px per 2–3 dtk | `inOutSine` | dua pan berlawanan berturut-turut |
| Tilt / pedestal (naik-turun) | mengungkap tinggi/skala; naik = harapan, turun = beban/akibat | y ±300 px dalam 1–2 dtk | `outCubic` | teks di jalur gerak |
| Roll (dutch) | goyah, ganjil, bingung, salah | ±1,5–3° per adegan | `inOutSine` | topik tenang, data |
| Orbit | subjek penting, dilihat dari semua sisi, heroik | 6–15° per 2–3 dtk | `inOutSine` | foto datar satu lapis (terlihat palsu) |
| Dolly (maju dengan parallax kuat) | masuk ke dalam ruang, imersif | zoom 6–15% + beda `z` besar | `inOutSine` | latar polos tanpa lapisan |
| Zoom optik (datar) | memperhatikan, menginterogasi | cepat 4–8 bingkai (crash zoom) atau sangat pelan | `outExpo` (crash) | terlalu sering (terasa murah) |
| Whip | lompat perhatian, energi | 0,15–0,25 dtk + blur gerak | `inExpo` → `outQuart` | lebih dari 3 per video |
| Handheld | kehadiran, dokumenter, kejadian nyata, panik | 3–8 px, 0,3–0,8 Hz, roll ±0,3° | noise | gaya mewah/minimal |
| Static / tenang | kejelasan, berat, diam sebelum hantaman | zoom 3–4% per adegan | `linear` | gaya kolase lebih dari 1 dtk benar-benar diam (cek mesin menolak) |
| Dolly zoom (vertigo) | kesadaran mengejutkan, dunia runtuh | 1–2 dtk | `inOutSine` | lebih dari 1× per video |

---

## 2. Kedalaman: depan / tengah / belakang dan parallax 2,5D
Parallax mesin: tiap lapisan bergerak sebesar `0,35 + 0,65 × z` dari gerak kamera (z 0–2,4). Jadi z 0 bergerak 35%, z 1 bergerak 100%, z 2 bergerak 165%.

| Lapisan | `z` | Contoh | Catatan |
|---|---|---|---|
| Latar jauh | 0–0,15 | langit, pola, gradasi | hampir diam |
| Pelat penuh | 0,3 (bawaan) | ruangan, lanskap, jalan | `lebih: 1.16` memberi ruang kamera |
| Tengah (subjek) | 0,9–1,1 | tokoh, benda utama, kartu | tajam, kontras tertinggi |
| Teks | 0,8–1,0 (ikut subjek) atau 0,4–0,6 (di belakang subjek) | judul | jangan di depan lapisan depan |
| Depan | 1,6–2,4 | tangan, mik, kepala penonton, daun, bingkai jendela, debu | kabur (`blur` 6–14), gelap, sebagian keluar tepi |

- **Kedalaman atmosfer**: latar lebih terang/kurang kontras (`efek: kabut` tipis), depan lebih gelap dan kabur. Ini yang membuat 2,5D terasa sinematik, bukan sekadar bergeser.
- **Rasio**: dengan preset `dorong` (zoom +9%), latar bergerak ±3%, depan ±15%: cukup. Lebih dari itu, tepi lapisan mulai terlihat.
- **Satu foto jadi 2,5D**: buat pelat + potongan terpisah di Flow (`skill-edit-rizky/references/flow.md`), atau pisahkan foto asli (`ambil_media.py --potong`). Lubang di belakang potongan ditutup pelat yang dibuat tanpa subjek.
- Detail kolase foto: `../motion/kolase-editorial.md`.

---

## 3. Gerak satu per satu
Format: **Kapan** · **Kenapa** · **Cara** · **Hindari** · **Di mesin Kolase** · **Di editor lain**.

### 3.1 Push in
- **Kapan**: kalimat penting, wajah/benda yang baru dipahami artinya, ketegangan naik. **Kenapa**: mendekat = otak menganggap penting. **Cara**: subliminal +3–8% sepanjang adegan; dramatis +15–30% dalam 1–2 dtk diakhiri tepat di kata kunci. **Hindari**: push in di setiap adegan (jadi datar lagi); push ke ruang kosong.
- **Di mesin**: `kamera: 'dorong'` (1 → 1,09 linear), `'dorong-kuat'` (1 → 1,22 inOutSine), atau keyframe `[[0, { zoom: 1 }], ['L04.w6', { zoom: 1.2, y: 40 }, 'inOutCubic']]`.

### 3.2 Pull out
- **Kapan**: mengungkap skala ("ternyata ada ribuan"), konteks, kesepian, penutup. **Kenapa**: konteks yang baru terlihat = pengungkapan. **Cara**: mulai dekat (1,25–1,35), mundur `outCubic` 1–1,5 dtk, lapisan baru terlihat di tepi saat mundur. **Hindari**: mundur ke latar yang kosong/membosankan.
- **Di mesin**: `kamera: 'mundur'` (1,3 → 1,02 outCubic); perpindahan `tarik` untuk mundur lintas adegan.

### 3.3 Pan / truck dan tilt
- **Kapan**: menjelajah ruang, membandingkan dua hal, mengungkap tinggi. **Kenapa**: mata mengikuti arah gerak, cerita "membaca" ruang. **Cara**: pan 60–180 px per 2–3 dtk `inOutSine`; tilt y ±300 px `outCubic`; arah sama dengan arah baca cerita (kiri → kanan = maju). **Hindari**: pan dan tilt bersamaan tanpa alasan; pan yang membawa teks keluar zona aman.
- **Di mesin**: `'kiri'`/`'kanan'` (x ±90, zoom 1,08 → 1,11), `'naik'`/`'turun'` (y ±300 → ∓40). `y` positif = kamera melihat lebih ke bawah.

### 3.4 Orbit
- **Kapan**: subjek heroik (produk, tokoh, benda bersejarah), "melihat dari sisi lain". **Kenapa**: memutari subjek = subjek dihormati, berdimensi. **Cara**: 6–15° per 2–3 dtk; depan bergerak berlawanan dengan latar. **Hindari**: orbit pada foto satu lapis (tidak ada sisi lain, terlihat palsu).
- **Di mesin**: *Celah mesin* (tidak ada kamera 3D sungguhan). **Akali**: subjek di kartu/benda dengan `rig: { jenis: 'miring', y: [[0, -12], [2.5, 10, 'inOutSine']] }`, kamera `'kanan'`, lapisan depan `z: 2` dengan `gerak` x berlawanan, latar `z: .2`. Untuk orbit sungguhan: klip Flow/Veo "slow orbit" dari gambar itu (`skill-edit-rizky/references/klip.md`).

### 3.5 Dolly vs zoom
- **Kapan**: dolly saat ingin masuk ke ruang; zoom saat ingin memperhatikan/menginterogasi. **Kenapa**: dolly mengubah parallax (imersif), zoom hanya membesarkan (datar, "mata kamera"). **Cara**: dolly = zoom kecil + beda `z` besar; crash zoom = 4–8 bingkai `outExpo` + bunyi hit. **Hindari**: crash zoom lebih dari 2× per video.
- **Di mesin**: dolly = `'dorong-kuat'` dengan lapisan depan `z: 2–2.4` dan latar `z: .2`; zoom datar = semua lapisan `z` dekat 1, keyframe zoom cepat.

### 3.6 Dolly zoom (vertigo)
- **Kapan**: kesadaran yang mengejutkan ("selama ini ternyata…"). **Kenapa**: subjek tetap, dunia menarik diri = pusing. **Cara**: subjek tetap ukuran, latar membesar/mengecil berlawanan 1–2 dtk. **Hindari**: lebih dari 1× per video.
- **Di mesin**: *Celah mesin* (belum ada sekali tulis). **Akali**: kamera `dorong-kuat`, latar `z: 0` + subjek `z: 1` dengan `gerak` skala subjek turun sebanding zoom kamera (1 → 0,82) supaya ukuran subjek tetap.

### 3.7 Handheld simulation
- **Kapan**: dokumenter, kejadian nyata, POV, panik, rekaman "bukti". **Kenapa**: getaran tangan = ada orang di sana. **Cara**: drift 3–8 px pada 0,3–0,8 Hz + roll ±0,3°, sesekali koreksi kecil; panik: 10–20 px + frekuensi 1–2 Hz. **Hindari**: handheld di gaya mewah/minimal/editorial; getaran seragam seperti gempa.
- **Di mesin**: `kameraHidup` (bawaan aktif: ±5 px, ±0,12°) = handheld halus. Lebih kuat: kamera sebagai fungsi (mesin sudah menerimanya, belum tercatat di `mesin.md`): `kamera: t => ({ x: 6 * Math.sin(t * 1.3) + 3 * Math.sin(t * 2.9), y: 5 * Math.sin(t * 1.1 + 1) + 2 * Math.sin(t * 3.7), zoom: 1.06, putar: .3 * Math.sin(t * .9) })`. Uji dengan `kontak` sebelum dipakai.

### 3.8 Whip
- **Kapan**: pindah perhatian cepat, daftar, hook. **Kenapa**: energi + menyembunyikan potongan. **Cara**: 0,15–0,25 dtk, jarak ≥ 1 layar, blur gerak kuat, mendarat 0,4–0,7 dtk. **Hindari**: whip lambat (terlihat seperti pan gagal).
- **Di mesin**: perpindahan `sentak` + `arahMasuk`; whip di dalam adegan: keyframe x ±600 dalam 6 bingkai `inExpo` (blur gerak otomatis).

### 3.9 Perspective transition
- **Kapan**: kartu/foto/layar yang berputar menampilkan sisi lain, peralihan ke dunia UI. **Kenapa**: perubahan bidang pandang = perubahan sudut pandang cerita. **Cara**: putar 3D 15–35° dengan perspektif, kembali datar `outQuart`. **Hindari**: perspektif ekstrem yang membuat teks tak terbaca.
- **Di mesin**: `rig: { jenis: 'miring', y: [[0, -30], [.6, 0, 'outQuart']], x: 6, jarak: 2.2 }` pada gambar/kartu; antar-adegan `putar`/`kartu`. *Celah mesin*: bidang 3D untuk seluruh adegan.

### 3.10 Seamless transition (kamera menyambung)
- **Kapan**: dua adegan dihubungkan gerak kamera. **Kenapa**: satu napas sinematik. **Cara**: lihat `../motion/transisi.md` §3.6. **Di mesin**: perpindahan bermomentum (`dorong`/`tarik`/`sentak`/`putar`) sudah memindahkan gerak kamera melewati titik potong; `cocok` bila benda yang sama bertahan.

### 3.11 Object tracking (kamera mengikuti benda)
- **Kapan**: benda bergerak yang ingin diikuti (mobil, kertas terbang, kursor). **Kenapa**: kamera yang mengikuti = benda itu tokoh utama. **Cara**: benda tetap dekat pusat/sepertiga, latar bergeser berlawanan; kamera sedikit tertinggal (lag 2–4 bingkai) supaya terasa operator manusia. **Hindari**: kamera menempel kaku 100% (terasa CG).
- **Di mesin**: keyframe kamera x/y dengan waktu yang sama dengan `gerak` benda, digeser 0,06–0,12 dtk lebih lambat. *Celah mesin*: pelacakan otomatis untuk klip (`urutan`); akali: baca posisi dari lembar `_cek-<kode>.jpg` lalu tulis keyframe manual. Footage asli: tracker CapCut/AE.

### 3.12 Camera shake (guncang)
- **Kapan**: hantaman, cap, benda jatuh, ledakan bunyi bass. **Kenapa**: dunia bereaksi terhadap massa. **Cara**: 4–10 px (ringan) hingga 20–30 px (ledakan), 0,25–0,4 dtk, meredam cepat, sinkron dengan bunyi. **Hindari**: guncang di setiap potongan; guncang tanpa bunyi.
- **Di mesin**: `efek: [{ jenis: 'guncang', t, lama: .3, kuat: .25–.4 }]` (±23 px × kuat); otomatis pada lapisan `masuk: 'jatuh'`/`'cap'` (matikan dengan `masuk: { gaya: 'jatuh', guncang: false }`, atur kekuatan dengan `guncang: .2–.8`).

### 3.13 Controlled motion blur
- **Kapan**: gerak cepat (whip, momentum, terbang, benda melesat). **Kenapa**: blur gerak adalah tanda gerak nyata; tanpa blur, gerak cepat terlihat seperti stop-motion murah. **Cara**: patokan rana 180°: panjang blur ≈ separuh perpindahan per bingkai; lapisan depan lebih kabur. **Hindari**: blur pada gerak pelan (gambar terlihat lembek) dan pada teks yang sedang dibaca.
- **Di mesin**: otomatis di perpindahan momentum (sampai 28 sampel, depan lebih panjang), lapisan ber-`rig` dibatasi 4 sampel; `blurGerak: false` pada teks/UI yang harus tetap tajam.

### 3.14 Rack focus di dalam adegan
- **Kapan**: memindahkan perhatian dari benda depan ke belakang (atau sebaliknya) tanpa potong. **Kenapa**: penonton diarahkan dengan lembut. **Cara**: blur lapisan A 0 → 8–14 px, lapisan B 10 → 0 px, 0,4–0,7 dtk `inOutSine`, bersamaan. **Hindari**: kedua lapisan kabur di tengah terlalu lama (> 0,3 dtk).
- **Di mesin**: `gerak: [[ 'L03.w2', { blur: 0 } ], [ 'L03.w2+0.5', { blur: 12 }, 'inOutSine' ]]` pada lapisan depan dan kebalikannya pada lapisan belakang.

### 3.15 Gerak kamera "3D" gabungan
- **Kapan**: adegan hero/payoff. **Cara**: maks dua komponen yang bermakna: push + naik (crane yang mengungkap), push + roll kecil (ketegangan), pan + orbit semu (eksplorasi). **Di mesin**: keyframe `{ x, y, zoom, putar }` bersama + parallax `z`.

---

## 4. Memilih gerak per beat cerita
| Beat (`../story/cerita.md`) | Gerak utama | Alasan |
|---|---|---|
| Hook | `dorong-kuat` / crash zoom / whip masuk | energi + fokus dalam 1 dtk |
| Konteks | `kiri`/`kanan`/`naik` pelan | menjelajah dunia |
| Ketegangan | push pelan yang makin cepat, roll ±2° | tekanan naik |
| Pembalik / kejutan | diam 4–8 bingkai lalu whip/putar/guncang | kontras diam → hantam |
| Pengembangan data | `tenang` | informasi dibaca |
| Payoff | pull out reveal atau push ke detail + `kilau` | pengungkapan |
| Penutup / loop | `mundur` atau `tenang`, kembali ke komposisi hook | rasa selesai / bisa diulang |

Variasi: jangan memakai preset yang sama di dua adegan berurutan (`skill-edit-rizky/references/gaya.md` §0.4 butir 4). Gerak kamera di sisi potong searah dengan perpindahan (`../motion/transisi.md` §2).

## 5. Angka patokan ringkas
| Hal | Patokan |
|---|---|
| Push subliminal | +3–8% zoom per adegan 2–3 dtk |
| Push dramatis | +15–30% dalam 1–2 dtk |
| Pull reveal | 1,3 → 1,0 dalam 1–1,5 dtk |
| Pan | 60–180 px per 2–3 dtk |
| Tilt | y ±300 px dalam 1–2 dtk |
| Roll | ±1,5–3° |
| Whip | 0,15–0,25 dtk, ≥ 1 layar |
| Guncang | 4–10 px ringan, 20–30 px berat, 0,25–0,4 dtk |
| Handheld | 3–8 px, 0,3–0,8 Hz, roll ±0,3° |
| Beda `z` minimum agar parallax terasa | 0,6 antara latar dan subjek |

## Teknik modern
- **Peta kedalaman dari satu foto (depth map → 2,5D)** · manfaat: parallax sinematik dari satu foto asli tanpa membuat potongan manual · kapan: foto arsip/berlisensi yang tidak bisa dibuat ulang di Flow · cara: buat peta kedalaman (model depth estimation, mis. Depth Anything) → pisahkan foto jadi 3–4 irisan kedalaman berlatar transparan → tanam sebagai lapisan `z` 0,2 / 0,8 / 1,6; lubang diisi pelat inpaint. Belum ada alatnya di repo (celah).
- **Klip gerak kamera AI dari gambar diam** · manfaat: orbit/dolly sungguhan dengan parallax benar · kapan: 1–2 momen hero per video · cara: alur klip Flow (`skill-edit-rizky/references/klip.md`) dengan kamera "slow orbit"/"slow push-in", lalu foto hidup (`klip: { kode, t }`) supaya mulai dari foto yang sama.
- **Kamera sebagai fungsi** · manfaat: handheld, napas, atau gerak berirama musik yang presisi · kapan: gaya Documentary/Cinematic Documentary, adegan yang sinkron ketukan · cara: `kamera: t => ({ … })` (§3.7), nilai ketukan dari `scripts/ketukan.py`.

## Cek cepat
1. Setiap gerak kamera punya arti yang bisa disebut (fokus, konteks, jelajah, goyah, energi)?
2. Satu gerak kamera utama per adegan pendek; tidak ada kombinasi tanpa alasan?
3. Ada minimal 2–3 lapis kedalaman dengan beda `z` ≥ 0,6 di adegan foto?
4. Kamera tenang saat teks panjang/data dibaca?
5. Preset kamera tidak sama di dua adegan berurutan?
6. Guncang hanya di hantaman dan selalu bersama bunyi?
7. Blur gerak hanya pada gerak cepat; teks yang dibaca tetap tajam?
8. Arah kamera di sisi potong searah dengan perpindahan?

## Celah mesin
- Orbit/kamera 3D sungguhan dan bidang perspektif untuk seluruh adegan (akali: `rig: 'miring'` + parallax berlawanan, atau klip Flow).
- Dolly zoom sekali tulis (akali: zoom kamera + skala subjek terbalik).
- Kekuatan handheld bertingkat (`kameraHidup` hanya hidup/mati); kamera sebagai fungsi sudah didukung mesin tetapi belum tercatat di `mesin.md`.
- Pelacakan benda otomatis untuk klip `urutan`.
- Peta kedalaman dari satu foto (pemisah irisan kedalaman otomatis).
