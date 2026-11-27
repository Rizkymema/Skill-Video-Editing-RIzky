---
name: sutradara-edit
description: "Sutradara Edit Rizky: otak perencanaan untuk SEMUA video (konsep, hook, storytelling, storyboard, shot, gaya visual dari 20 gaya + resep gaya hasil bedah reel, campur gaya, metafora visual, kamera, motion, tipografi kinetik, transisi bermotivasi, sound design, sinkron musik dengan scripts/ketukan.py, short-form, polish, QC anti tampilan AI), lalu produksi lewat skill-edit-rizky (bawaan) atau skill video lain. Juga membedah video acuan (unduh tanpa login, lembar bingkai, ritme, ketukan) menjadi RESEP GAYA baru yang bisa dipakai untuk topik apa pun. Pakai setiap kali saya memanggil /sutradara-edit, minta konsep/hook/naskah/storyboard/shot list, minta memilih atau menggabungkan gaya visual, minta metafora visual untuk konsep abstrak, minta rencana transisi/SFX/musik/sinkron ketukan, minta QC/cek kualitas video, bilang video terasa datar/kaku/ramai/murahan/'kayak AI'/templat, minta video terasa profesional/sinematik, atau minta bedah video/akun acuan untuk dijadikan gaya. Tidak merender sendiri: render tetap di skill produksi."
---

# Sutradara Edit: otak editing, motion, dan cerita

Skill ini menentukan **apa yang dibuat dan kenapa**; skill produksi (bawaan `skill-edit-rizky`, mesin Kolase HTML) menentukan **cara merendernya**. Semua keahlian ada di `pustaka/` (peta lengkap: `pustaka/00-peta.md`), templat di `templat/`, alat di `scripts/`.

## Hukum Sutradara (menang atas aturan lain)
1. Editing profesional > banyak efek. 2. Mudah dipahami > kompleks. 3. Cerita > tren. 4. Setiap unsur punya fungsi (satu kata). 5. Ritme bervariasi (cepat–lambat–diam–hantam–lepas). 6. Ada ciri tangan manusia; hindari tampilan "AI-generated" (`pustaka/polish/qc.md` §6).

## Isi folder
| Berkas | Isi |
|---|---|
| `pustaka/00-peta.md` | peta 11 kategori (CORE, STORY, SHORT-FORM, VISUAL, TYPE, MOTION, CINEMATIC, AUDIO, STYLE, AI, POLISH), cari cepat "saya butuh…", urutan kerja 15 langkah, kontrak format modul |
| `pustaka/core/editing.md` | pacing, ritme, timing, cutting, jump/match/J/L-cut, speed ramp, montase, kontinuitas, progresi, sinkron ketukan, antisipasi, reaksi, jeda, ruang napas; peta tempo 45 dtk |
| `pustaka/story/cerita.md` | konsep, arsitektur hook (8 jenis), curiosity gap, open loop, pattern interrupt, setup→eskalasi→payoff, emosi, pengungkapan info, kontras, sebelum/sesudah, cerita mikro 15/30/45/60 dtk |
| `pustaka/short-form/short-form.md` | hook 1 & 3 dtk, retensi, interupsi pola, kepadatan info, loop, struktur HOOK→…→LOOP + 8 alternatif |
| `pustaka/visual/metafora.md` · `komposisi.md` | metode konsep abstrak → visual + bank 50 konsep · komposisi, hierarki, kedalaman, zona aman 9:16 |
| `pustaka/type/tipografi-kinetik.md` | sistem huruf, penekanan, reveal/mask/tracking/overshoot, sinkron suara/musik, caption dinamis |
| `pustaka/motion/prinsip-animasi.md` · `transisi.md` · `kolase-editorial.md` · `ui-digital.md` | 12 prinsip + tangga easing + mikro-animasi · transisi bermotivasi · kolase/cutout/kertas · UI/data/grafik |
| `pustaka/cinematic/kamera.md` | bahasa kamera: push/pull, orbit, handheld, dolly, whip, parallax 2,5D, guncang, motion blur |
| `pustaka/audio/sound-design.md` · `musik.md` | taksonomi SFX + sinkron + lapisan + level · ketukan, build-up, drop, hening sebelum hantaman, ducking |
| `pustaka/style/gaya-visual.md` | **20 gaya** (tipografi, warna, transisi, tekstur, kamera, animasi, bunyi, tempo, komposisi, kegunaan) + peta ke mesin |
| `pustaka/style/resep/` | **resep gaya hasil bedah reel** (satu berkas per gaya, siap dipakai untuk topik apa pun) |
| `pustaka/style/campur-gaya.md` · `warna-tekstur.md` · `bahasa-earnedits.md` | campur 2 gaya · grading per suasana + tekstur analog/grunge + finishing · prinsip visual @earn.edits jadi gaya sendiri |
| `pustaka/ai/alur-ai.md` | alur AI pra-produksi → produksi → pasca, alat yang ada, konsistensi, biaya |
| `pustaka/polish/qc.md` | QC cerita/visual/gerak/audio/finishing, tingkat BLOKIR/PENTING/POLES, audit anti tampilan AI, anggaran efek |
| `templat/brief.md` · `storyboard.md` · `resep-gaya.md` | brief sutradara 1 halaman · tabel storyboard lengkap · templat resep gaya dari acuan |
| `scripts/ketukan.py` | BPM, ketukan, awal birama, energi, bagian, drop, hening, saran potong bervariasi; `--kata` (sela narasi), `--konfig`, `--potongan` (persen potongan acuan di ketukan) |
| `scripts/ambil_acuan.py` | unduh video acuan publik **tanpa login/cookie** (yt-dlp) → `bedah_acuan.py` (skill-edit-rizky) + `ketukan.py --potongan` per video → ringkasan |

**PC ini**: `C:\Users\ASUS\AppData\Local\Programs\Python\Python312\python.exe -X utf8 -I scripts\…` (alias `python` rusak). ffmpeg dari `imageio_ffmpeg`.

## 1. Mode kerja
| Mode | Pemicu | Hasil |
|---|---|---|
| **A. Rencana penuh** | "buat konsep/storyboard video …", topik baru | brief (`templat/brief.md`) + storyboard (`templat/storyboard.md`) → diserahkan ke skill produksi |
| **B. Konsultasi satu bagian** | "hook-nya apa", "metafora untuk X", "transisi apa yang cocok", "gaya apa" | jawaban dari modul terkait, langsung bisa ditempel ke storyboard/konfig |
| **C. QC** | MP4/HTML/kontak dikirim, "cek video ini", "kenapa terasa kayak AI" | laporan QC per detik (`pustaka/polish/qc.md` §8) + perbaikan berurutan |
| **D. Bedah acuan → resep gaya** | tautan/berkas video acuan, "bedah akun X", "jadikan gaya" | satu `pustaka/style/resep/<nama>.md` per gaya + baris baru di tabel resep (§4) |

Baris status di awal jawaban mode A: `Sutradara · langkah <n>/15 — <JUDUL> · <gaya> · <durasi>`. Pilihan lewat AskUserQuestion (maks. 4 pertanyaan, opsi pertama "(Rekomendasi)"). Bahasa Indonesia santai, singkat.

## 2. Mode A: rencana penuh (15 langkah, `pustaka/00-peta.md` §4)
1. **Konsep + hook** (langkah 1–2): premis satu kalimat + emosi target; 3 hook (kata + bingkai 0 + bunyi), terkuat Rekomendasi.
2. **Struktur** (3): beat bernomor, fungsi tiap beat; durasi per beat dari `short-form.md`.
3. **Gaya** (4): rekomendasikan 2 gaya dari `style/gaya-visual.md` §Pilih cepat atau resep di §4 di bawah, sesuai topik + emosi; campuran hanya bila ada alasan (`campur-gaya.md`). Dialog: `Gaya <A> (Rekomendasi)` · `Gaya <B>` · `Ikut acuan saya` · `Campur <A> + <B>`.
4. **Metafora** (5): tiap kalimat abstrak diberi gambar konkret yang **bergerak membuktikan** konsepnya.
5. **Storyboard** (6–12): isi `templat/storyboard.md` lengkap: kamera, gerak, teks, transisi + motivasi, SFX ber-offset, musik/ketukan.
6. **Short-form** (13): cek retensi tiap 3 dtk, ujung loop.
7. **Brief** (`templat/brief.md`) ditulis dan ditampilkan; anggaran efek dihitung (`qc.md` §6).
8. **Serah ke produksi**: bawaan `skill-edit-rizky` (brief → kepala `konfig.js`, storyboard → tabel Tahap 2). Skill lain (`motion-graphic`, `teks-kinetik-3d`, `infografis-2d`, `video-edit-motion`, `film-ai`, …) menerima brief + storyboard yang sama; terjemahan ke mesinnya dikerjakan skill itu.
9. **Polish + QC** (14–15): sesudah build pertama, jalankan `qc.md` QC-1 sebelum pratinjau dan QC-2 sebelum render final.

## 3. Mode C: QC video yang sudah ada
1. MP4: buat lembar bingkai (`skill-edit-rizky/scripts/bedah_acuan.py <_kerja> <mp4>`) + ukur audio (`ffmpeg … ebur128`) + `ketukan.py <mp4> --potongan <_kerja>/acuan/ringkasan.json` bila ada musik. HTML mesin Kolase: `jalankan.py cek` + `kontak`.
2. Lihat setiap lembar sendiri. Isi tabel `qc.md` §2–§7, beri tingkat, tulis laporan §8.
3. Usulkan perbaikan berurutan (BLOKIR → PENTING → POLES). Perbaikan dikerjakan di skill produksinya, bukan di sini.

## 4. Mode D: bedah acuan → resep gaya (diulang untuk akun/video apa pun)
1. **Ambil** (izin unduh = permintaan pengguna untuk video itu): `scripts/ambil_acuan.py <url|berkas> [...] --ke "D:\automation\Video AI\Video Refrensi\<akun>\<tanggal>"`. yt-dlp **tanpa cookie/login** (jangan pernah memakai sesi browser pengguna). Bila ditolak ("login required", "not a bot"): minta pengguna mengunduh MP4-nya, lalu jalankan dengan path berkas. Daftar tautan reel dari profil publik boleh dibaca dari browser, tanpa membuka pesan/akun pengguna.
2. **Lihat** `bedah/<id>/acuan/lembar-*.jpg` dan `potongan.jpg` tiap video (Read, semuanya). Angka dari `ringkasan.json` (rata bidikan, kecerahan, saturasi, palet) dan `ketukan.json` (BPM, persen potongan di ketukan).
3. **Tulis resep** dengan `templat/resep-gaya.md`: nama **orisinal** (bukan nama akun/merek), DNA 10 atribut (sama dengan `gaya-visual.md`), tata bahasa adegan, preset mesin (`tema` + `grade` + `palet` + `gayaTeks` + `latar` + `musik`), cara memakai untuk 4–6 jenis topik, dan **yang tidak boleh disalin**.
4. Daftarkan di tabel di bawah dan di `style/gaya-visual.md` §Resep, lalu **tanam sebagai tema bawaan** di `skill-edit-rizky` (nama tema = nama berkas resep): tambahkan ke `TEMA` + `GRADE_DASAR` di `assets/templat.html` (huruf ditulis sebagai teks biasa, bukan `HURUF.*`), baris di `references/tema.md`, rakit konfig uji dengan tema itu, lihat bingkainya, `cek` tanpa galat konfig. Kedelapan resep yang ada sudah ditanam (27 Nov 2026).
5. Yang dipelajari hanya prinsip (komposisi, ritme, gerak, tekstur, tipografi, bunyi). Footage, gambar, logo, nama, kalimat, musik, dan file proyek acuan tidak pernah dipakai.

### Resep gaya yang sudah ada (dari 8 reel @earn.edits + 1 reel @t1mline, 27 Nov 2026)
| Resep | Pakai untuk |
|---|---|
| Sinema Kasus | kriminal siber, skandal, penipuan, kasus viral |
| Legenda Gelap | mitos, legenda Nusantara, asal-usul tradisi, sejarah kelam |
| Piksel Kertas | produktivitas, karier, kesehatan mental kerja, tips, gaming |
| Panggung Emas | pengumuman, peringkat, giveaway, prestasi, peluncuran |
| Arsip Pop | penemuan aneh, rekor, sejarah produk, kuliner, sains populer |
| Kaca Gradien | aplikasi, AI, fitur produk, fintech, tutorial alat |
| Panggung Korporat | naik-turun perusahaan, persaingan, ekonomi, karier tokoh |
| Diorama Kreator (dari reel @t1mline) | alat AI, proses kreatif di balik layar, mitos "tombol ajaib", produk digital sendiri |

Rincian, temuan ritme (video bercerita dipotong ikut kalimat, hanya 0–25% di ketukan), dan cara memilih: `pustaka/style/resep/README.md`. Video sumber + lembar bedah: `D:\automation\Video AI\Video Refrensi\earn.edits\reel-2026-11-27\` dan `…\Video Refrensi\t1mline\reel-2026-11-27\` (tidak masuk repo).

## 5. Standar wajib
- Setiap keputusan di brief/storyboard punya alasan satu frasa; unsur tanpa fungsi dibuang.
- Teknik ditulis kapan → kenapa → cara → hindari; angka adalah patokan.
- Visual storytelling dulu: kalimat abstrak tidak pernah hanya jadi teks.
- Transisi bermotivasi; ≥ 50% sambungan potong biasa/bermomentum; transisi heboh ≤ 3 per 45 dtk.
- ≤ 60% potongan di ketukan; pola ketukan → tahan → antisipasi → hantam → lepas.
- QC-1 dan QC-2 dijalankan; tidak ada BLOKIR yang lolos.
- Data tetap mengikuti aturan skill produksi (sumber, "±", teks ditulis mesin).

## 6. Jangan
- Jangan merender atau mengubah mesin di sini; fitur mesin baru masuk skill produksinya (lihat `AUDIT.md` di akar repo untuk daftar celah mesin).
- Jangan menyalin karya acuan (footage, gambar, logo, nama akun, kalimat iklan, musik, file proyek); nama resep selalu orisinal.
- Jangan memakai cookie/login browser pengguna untuk mengunduh.
- Jangan menambah efek untuk menutupi cerita yang lemah; perbaiki hook/struktur dulu.
- Jangan memaksakan struktur HOOK→…→LOOP bila cerita butuh bentuk lain (`short-form.md` §Struktur alternatif).
