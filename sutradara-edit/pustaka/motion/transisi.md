# Transisi Bermotivasi

> Kategori **MOTION** · dipakai di langkah 10 (juga 6 storyboard) · terkait: `../core/editing.md` (potong, J/L-cut, match cut), `../cinematic/kamera.md`, `../audio/sound-design.md`, `prinsip-animasi.md`, implementasi mesin: `skill-edit-rizky/references/gaya.md` §4 + `mesin.md` §Perpindahan

Prinsip inti:
1. **Transisi adalah kalimat penghubung.** Ia butuh hubungan nyata antara dua adegan: bentuk, warna, arah gerak, benda, gagasan, atau bunyi. Tanpa hubungan, transisi = hiasan.
2. **Potongan bersih sering yang terbaik.** Jangan menutupi potongan yang tidak bermasalah dengan efek. Transisi yang terlihat adalah tanda baca, bukan huruf.
3. **Energi transisi = energi cerita di titik itu.** Hook/tegang boleh keras; konteks/tenang lembut; payoff memakai transisi tanda tangan.
4. **Arah konsisten.** Gerak ke kanan/maju = waktu atau cerita maju; ke kiri/mundur = kilas balik atau kembali.
5. **Di mesin Kolase, tata bahasa `gaya.md` §4 adalah hukumnya**: momentum di kamera dan kedalaman, bukan dua gambar datar yang ditukar. Modul ini memilih *yang mana* dan *kenapa*; `gaya.md`/`mesin.md` menjelaskan *cara mesin melakukannya*.

---

## 1. Motivasi: hubungan antar-adegan → transisi
Tanya dulu: **apa yang sama, atau apa yang berubah, antara A dan B?**

| Hubungan A → B | Transisi | Di mesin Kolase (`masuk` adegan B) |
|---|---|---|
| Bentuk sama (bulan → piring, roda → jam, mata → lensa) | match cut bentuk | `potong` dengan posisi/ukuran bentuk sama; bila benda yang sama: `cocok` |
| Benda sama, dunia berbeda (amplop di tangan → surat di meja) | object carry / seamless environment | `cocok: { dari: 'idLama', ke: 'idBaru' }` |
| B ada **di dalam** A (foto di koran, layar TV, jendela, lubang kunci) | push-through / dive | `dorong` + `titikMasuk: [x, y]`; atau `bingkai` + `arahMasuk: 'masuk'` |
| A menjadi **bagian dari** B (lab → foto di koran, ruang → layar TV) | pull-out reveal | `bingkai: { lapis: 'id', bentuk }`; `tarik` |
| Arah gerak sama (orang lari ke kanan → mobil ke kanan) | whip / direction match | `sentak` + `arahMasuk` searah gerak |
| Lompatan waktu/zaman | potong keras / kilat / film terbakar | `potong` (maks 3 per video), `kilat`, efek `bakar` di akhir adegan A |
| Kejutan, fakta mengejutkan, sinyal rusak | glitch / flash | `glitch`, `kilat` |
| Kekacauan, krisis, "dunia terbalik" | rotation | `putar` (+`arahMasuk: 'kiri'`) |
| Dokumen/lapisan bertumpuk, babak baru | panel cover | `tutup`, `buka`, `kartu` |
| Fokus berpindah dengan tenang | rack focus | `fokus` |
| Warna dominan sama (lampu merah → darah → mawar) | colour match | `fokus` atau `lebur` pendek (`lamaMasuk: .2`) dengan warna sama di posisi sama |
| Suara B terdengar lebih dulu | J-cut | audio memimpin 0,2–0,5 dtk (`../core/editing.md`), visual bebas |
| Membuka cetak biru, peluncuran, data teknis | strip | `strip` (`jumlahMasuk: 6`) |
| Penutup, fokus ke satu hal | iris | `iris` + `titikMasuk` |
| Benda/adegan menghantam dari atas | drop | `jatuh` |
| Tidak ada hubungan visual | potong bersih atau potong bermomentum | `sentak`/`dorong` (momentum tanpa efek) atau `potong` |

Tidak menemukan hubungan? **Ubah storyboardnya**, bukan menambah efek: pindahkan benda yang sama ke dua adegan, samakan arah kamera, atau letakkan B di dalam benda A.

---

## 2. Ritme transisi sepanjang video
- **Video umum (talking head, vlog, CapCut)**: 70–90% sambungan adalah potongan bersih; transisi terlihat hanya di pergantian bab/gagasan.
- **Gaya kolase (mesin Kolase)**: hampir setiap pergantian adegan adalah **potong bermomentum** (`dorong`/`tarik`/`sentak`/`putar`, lama 0): terasa seperti potongan berenergi, bukan efek. Transisi berlapis (`tutup`, `bingkai`, `cocok`, 0,5–0,95 dtk) adalah tanda baca: 2–4 per 45 dtk. Transisi tanda tangan 1–2×.
- **Aturan mesin (dari `gaya.md`, jangan dilanggar)**: ≥ 6 jenis per video, satu jenis maks 3×, tidak dua kali berturut-turut, potong keras ≤ 3 (cek mesin menolak lebih).
- **Kurva energi**: hook keras (`sentak`, `dorong` kuat) → konteks lembut (`fokus`, `geser`) → tegang makin cepat (`sentak`, `glitch`, `putar`) → payoff tanda tangan (`bingkai`/`cocok` + `kilau`) → penutup tenang (`tarik`, `iris`, `lebur`).
- **Tempat**: di batas kalimat atau di kata kunci (`mulai: 'L05'` / `'L05.w4'`), tidak di tengah kata. Transisi panjang (> 0,6 dtk) diletakkan di jeda antar-kalimat supaya tidak menelan narasi.
- **Pembuka dan penutup** berbeda dari video terakhir (`gaya.md` §0.4, `riwayat.py lihat`).

---

## 3. Katalog transisi
Format: **Kapan** · **Kenapa** · **Cara** · **Hindari** · **Di mesin Kolase** · **Di editor lain**.

### 3.1 Match cut
- **Kapan**: dua adegan berbagi bentuk, posisi, gerak, atau gagasan (koin berputar → planet berputar). **Kenapa**: penonton merasakan hubungan makna tanpa penjelasan; transisi paling "cerdas". **Cara**: samakan posisi dan ukuran bentuk di layar (±5% lebar), samakan arah/kecepatan gerak bila match aksi, potong saat gerak di puncak. **Hindari**: match cut yang bentuknya hanya mirip sedikit (terasa kebetulan); dua match cut berturut-turut.
- **Di mesin**: `potong` (dihitung potong keras) atau `lebur` dengan `lamaMasuk: .12` (tidak dihitung); benda yang sama → `cocok`. Siapkan aset Flow dengan komposisi bentuk di posisi yang sama. **Di editor lain**: overlay 50% saat menyusun, lalu potong.

### 3.2 Whip (sentak)
- **Kapan**: berpindah tempat/topik dengan energi, daftar cepat, hook. **Kenapa**: kecepatan menyembunyikan potongan dan memompa tempo. **Cara**: kamera melesat 0,15–0,25 dtk dengan blur gerak kuat, potong di puncak kecepatan, adegan baru melanjutkan arah yang sama lalu melambat 0,4–0,7 dtk. **Hindari**: whip bolak-balik arah tanpa alasan; lebih dari 3 per video.
- **Di mesin**: `masuk: 'sentak', arahMasuk: 'kanan'|'kiri'|'atas'|'bawah'`, `kuatMasuk` (pengali). Bunyi bawaan swish. **Di editor lain**: CapCut "Whip"/blur arah + keyframe posisi; AE transform + directional blur.

### 3.3 Object transition (benda lewat menutup layar)
- **Kapan**: ada benda depan alami (orang lewat, tiang, pintu, tangan, kertas). **Kenapa**: potongan tersembunyi di balik benda nyata, terasa satu bidikan panjang. **Cara**: benda depan (z besar, kabur) melintas 0,3–0,45 dtk `inOutCubic`, adegan B mulai saat benda menutupi ≥ 95% layar, benda melanjutkan keluar di adegan B. **Hindari**: benda yang tidak ada hubungannya dengan dunia adegan.
- **Di mesin**: potongan Flow (`z: 2–2.4`, `blur: 8`) dengan `gerak` x dari −500 ke 1580 di akhir adegan A dan lanjutan geraknya di awal B; `masuk: 'lebur', lamaMasuk: .06` di B supaya tidak dihitung potong keras. *Celah mesin*: belum ada perpindahan "lewat-benda" sekali tulis. **Di editor lain**: AE/CapCut mask mengikuti tepi benda.

### 3.4 Mask transition
- **Kapan**: B terlihat melalui bentuk di A (jendela, layar, huruf, lubang kunci, siluet). **Kenapa**: membuat hubungan "di dalam" atau "di balik". **Cara**: bentuk diam di A, kamera menyelam ke bentuk 0,6–0,9 dtk `inOutCubic` sampai B memenuhi layar. **Hindari**: bentuk yang tidak bermakna (bintang, hati) hanya karena tersedia.
- **Di mesin**: `bingkai: { lapis: 'id', bentuk: 'kotak'|'bulat'|'peti'|'kunci' }` + `arahMasuk: 'masuk'` (menyelam) atau tanpa (adegan lama mundur jadi foto di B); `iris` + `titikMasuk` (lingkaran). *Celah mesin*: mask berbentuk huruf/siluet bebas.

### 3.5 Shape transition
- **Kapan**: gaya grafis (Minimalist, Corporate, Y2K, Experimental), pergantian bab. **Kenapa**: bentuk geometris memberi ritme desain. **Cara**: bentuk tumbuh dari titik yang punya arti (tombol, logo, titik data) menutup 0,3–0,4 dtk, membuka B 0,3–0,4 dtk, warna dari palet. **Hindari**: bentuk dekoratif di gaya dokumenter/sinematik.
- **Di mesin**: `strip` (strip vertikal, `jumlahMasuk`), `tutup` (panel bersudut bulat, `putarMasuk`), `iris`, `kartu`. *Celah mesin*: bentuk bebas yang berubah (lingkaran → kotak).

### 3.6 Camera transition (kamera menyambung)
- **Kapan**: dua adegan bisa dianggap satu ruang (langit → jalan, meja → lantai). **Kenapa**: gerak kamera yang menyambung terasa satu bidikan sinematik. **Cara**: akhir A kamera tilt/pan dipercepat ke satu arah, B mulai dari posisi yang sama di arah itu dan melambat; horizon/garis utama di ketinggian sama. **Hindari**: arah kamera berlawanan di sisi potong.
- **Di mesin**: `sentak` + `arahMasuk` (whip vertikal = tilt), atau keyframe kamera A diakhiri `inCubic` + keyframe B diawali `outCubic` dengan `potong`/`lebur` singkat; momentum otomatis membuat lapisan depan bergerak lebih jauh.

### 3.7 Zoom transition (push-through)
- **Kapan**: menyelam ke detail di A yang menjadi B. **Kenapa**: rasa "masuk lebih dalam" ke cerita. **Cara**: zoom ×1,6–2 dipercepat menuju titik (0,3–0,4 dtk), B mendarat dari zoom kecil ke normal 0,4–0,6 dtk. **Hindari**: zoom ke titik kosong; zoom transition berturut-turut.
- **Di mesin**: `dorong` + `titikMasuk` (utama), `tarik` (kebalikan); `zoom` hanya bila momentum tidak cocok (versi datar).

### 3.8 Rotation transition
- **Kapan**: kekacauan, krisis, pembalik ("ternyata terbalik"), gaya energik. **Kenapa**: rotasi = dunia goyah. **Cara**: putar 20–90° dipercepat ke titik potong, B masih miring lalu tegak dengan `outQuart`. **Hindari**: di topik tenang; lebih dari 2× per video.
- **Di mesin**: `putar` (+`arahMasuk: 'kiri'` berlawanan jarum jam). Kartu berputar 3D di dalam adegan: lapisan `rig: { jenis: 'miring', y: [[0, -25], [2.5, 15, 'inOutSine']] }`.

### 3.9 Displacement transition
- **Kapan**: gaya Experimental, Psychological, Retro VHS; ingatan, mimpi, distorsi. **Kenapa**: gambar meleleh/terdistorsi = realitas berubah. **Cara**: distorsi naik 0,2 dtk, potong di puncak, turun 0,2 dtk. **Hindari**: distorsi yang membuat wajah rusak; lebih dari 1× per video.
- *Celah mesin*: tidak ada peta displacement. **Akali**: `fokus` (blur memuncak di titik potong) + `efek: { jenis: 'glitch', lama: .25, kuat: .4 }`; atau klip transisi AI (§Teknik modern).

### 3.10 Liquid transition
- **Kapan**: air, tinta, cat, kopi, mimpi, perubahan organik. **Kenapa**: transisi organik cocok dengan topik cair/emosional. **Cara**: bentuk cair menutup dari tepi/bawah 0,5–0,7 dtk. **Hindari**: liquid tanpa hubungan dengan benda cair di cerita.
- *Celah mesin*: tidak ada. **Akali**: `tutup` dari bawah (`arahMasuk: 'bawah'`) dengan latar warna cairan + `efek: kabut`; atau klip Flow dari gambar A (cairan menutupi kamera) sebagai `urutan` di akhir A.

### 3.11 Glitch transition
- **Kapan**: teknologi, berita, fakta mengejutkan, sinyal/AI. **Kenapa**: kerusakan digital = kejutan/ketidakpastian. **Cara**: 6–11 bingkai, irisan bergeser + pisah warna, bunyi glitch tepat di titik potong. **Hindari**: lebih dari 2 per video; di gaya mewah/dokumenter.
- **Di mesin**: `masuk: 'glitch'` (0,36 dtk) atau `efek: { jenis: 'glitch', t, lama: .45 }`.

### 3.12 Light transition (kilat, cahaya bocor, terbakar)
- **Kapan**: kenangan (cahaya bocor), akhir babak/lompatan zaman (film terbakar), potong di ketukan (kilat). **Kenapa**: cahaya menyembunyikan potongan dan memberi suasana. **Cara**: kilat 4–8 bingkai; cahaya bocor 1–1,5 dtk menyapu melewati titik potong; terbakar 0,6–0,9 dtk dari tepi. **Hindari**: kilat putih berulang (melelahkan mata, berisiko untuk penonton sensitif cahaya); lebih dari 3 kilat per video.
- **Di mesin**: `masuk: 'kilat', warnaMasuk` (0,24 dtk); `efek: { jenis: 'cahaya', dari, lama: 1.4 }` di akhir A; `efek: { jenis: 'bakar', lama: .8 }`.

### 3.13 Seamless environment transition
- **Kapan**: subjek/benda tetap, dunia di sekitarnya berganti (zaman, musim, tempat). **Kenapa**: kontinuitas subjek + perubahan latar = cerita perubahan dalam satu napas. **Cara**: subjek di posisi dan ukuran sama, latar lama kabur keluar, latar baru menajam; kamera terus bergerak searah. **Hindari**: subjek bergeser posisi di titik potong.
- **Di mesin**: `cocok` (benda melayang dari posisi lama ke baru, latar kabur ↔ menajam), lapisan tujuan sudah tampil di detik 0 adegan baru; untuk subjek yang benar-benar diam, `fokus` dengan potongan subjek yang sama di kedua adegan.

### 3.14 Rack focus (fokus)
- **Kapan**: pergantian tenang, "membuka mata", dari benda ke tempat. **Kenapa**: lembut dan sinematik. **Cara**: blur memuncak di titik potong (0,25 dtk ke tiap sisi), B menajam sambil sedikit mundur. **Hindari**: di bagian cepat.
- **Di mesin**: `masuk: 'fokus'`. Di dalam satu adegan: `gerak` blur pada latar dan subjek bergantian (`../cinematic/kamera.md`).

---

## 4. Pasangan bunyi
Bunyi membuat transisi terasa disengaja; tanpa bunyi transisi besar terasa "melayang". Detail di `../audio/sound-design.md`.

| Transisi | Bunyi | Waktu |
|---|---|---|
| `dorong`, `tarik`, `zoom`, `bingkai`, `cocok`, `iris` | whoosh (bawaan) | mulai 0,15–0,3 dtk sebelum titik potong, puncak tepat di titik potong |
| `sentak`, `geser`, `lempar`, `fokus`, `strip` | swish pendek | puncak di titik potong |
| `tutup`, `buka`, `kartu` | kertas | saat panel mulai bergerak |
| `jatuh` | dum / impact rendah | saat mendarat (±0,36 dtk sesudah mulai) |
| `kilat` | rana kamera / hit | tepat di bingkai kilat |
| `glitch` | glitch | tepat di titik potong |
| `putar` | whoosh + sub kecil | whoosh sebelum, sub di titik potong |
| potong bersih di momen dramatis | **hening** 4–8 bingkai lalu hit | hening sebelum, hit di bingkai pertama B |

- `sfxMasuk: false` membisukan bunyi bawaan bila adegan sudah punya bunyi utama.
- Ganti bunyi sintesis dengan berkas premium lewat `KONFIG.sfxPeta` (`whoosh`, `swish`, `kertas`, `dum`, `kamera`).
- Jangan semua transisi berbunyi keras: variasikan volume (0,4–0,9), dan biarkan beberapa potongan sunyi.

## 5. Hindari
- Transisi tanpa hubungan visual/gagasan (hanya karena tersedia di paket).
- Transisi yang sama berulang, atau satu "transisi favorit" di setiap sambungan.
- Transisi panjang di tengah kalimat penting (menelan informasi).
- Kilat putih beruntun, glitch di semua tempat, putar di topik tenang.
- Silang pudar (`lebur`) sebagai bawaan; di gaya kolase hanya bila tak ada yang cocok (`gaya.md` §4).
- Arah gerak bertabrakan di titik potong (A ke kiri, B datang dari kiri).

## Teknik modern
- **Transisi AI first/last-frame (morph)** · manfaat: transisi cair/morph yang tidak bisa digambar kode (benda A meleleh menjadi B, ruangan berubah jadi ruangan lain) · kapan: payoff atau transisi tanda tangan, maks 1× per video · cara: simpan bingkai akhir A dan bingkai awal B sebagai gambar, buat klip 2–4 dtk di Flow/Veo dengan bingkai pertama (dan bingkai terakhir bila didukung model; cek `../ai/alur-ai.md`), periksa lembar `_cek`, tanam `rakit --klip morph=klip/morph.mp4@15`, pakai sebagai lapisan `urutan` penuh di akhir A (`klip: { tahan: true }`), lalu B `masuk: 'lebur', lamaMasuk: .06`.
- **Match cut berbasis bentuk yang direncanakan dari prompt** · manfaat: match cut "cerdas" tanpa kebetulan · kapan: konsep perbandingan · cara: di `aset.json`, tulis komposisi yang sama untuk dua aset ("round object centered at 45% height, filling 40% width"), lalu `potong`/`lebur` singkat.
- **Adegan menjadi benda di adegan berikut (scene-to-object)** · manfaat: tanda tangan kolase yang sudah ada (`bingkai`) · kapan: momen terpenting · cara: rencanakan lapisan ber-`id` (foto di koran, layar TV) di adegan B sejak storyboard.

## Cek cepat
1. Setiap transisi terlihat punya hubungan yang bisa disebut dalam satu kalimat (§1)?
2. Sebagian besar sambungan adalah potongan bersih/bermomentum, transisi berlapis hanya 2–4 per 45 dtk?
3. ≥ 6 jenis, tidak ada jenis > 3×, tidak berturut-turut, potong keras ≤ 3 (aturan mesin)?
4. Transisi tanda tangan muncul di momen terpenting, maks 2×?
5. Arah gerak di titik potong searah?
6. Transisi panjang berada di jeda, bukan di tengah kalimat?
7. Setiap transisi besar punya bunyi yang puncaknya tepat di titik potong?

## Celah mesin
- Liquid transition (cairan menutup layar).
- Displacement map transition (distorsi berbasis tekstur).
- Shape morph (bentuk A berubah menjadi bentuk B) dan mask berbentuk huruf/siluet bebas.
- Object-wipe sekali tulis (benda depan melintas otomatis di kedua adegan).
- Transisi berbasis peta kedalaman (lapisan dekat pergi lebih dulu dari foto tunggal).
