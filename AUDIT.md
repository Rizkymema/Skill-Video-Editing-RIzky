# Audit + upgrade skill video editing (27 Nov 2026)

Permintaan: audit semua skill di repo ini, pertahankan yang bagus, upgrade yang sederhana/umum/tumpang tindih, tambahkan yang kurang, sampai menjadi *personal video-editing intelligence system*. Lanjutan: unduh beberapa video @earn.edits, bedah, dan jadikan gaya-gaya yang bisa dipakai untuk berbagai topik.

## 1. Hasil audit per bagian
| Bagian lama | Kelompok | Alasan | Tindakan |
|---|---|---|---|
| `assets/templat.html` (mesin Kolase 1.4) | **Bagus → pertahankan** | deterministik, offline, cek kualitas bawaan, ekspor MP4 di browser, perpindahan bermomentum, rig, jangkar, kustom | tidak diubah; celah yang ditemukan pustaka dicatat di §5 |
| `scripts/` (jalankan, flow_kolase, ambil_media, bedah_acuan, potong_latar, riwayat) | **Bagus → pertahankan** | alur produksi lengkap dan teruji | tidak diubah; `bedah_acuan.py` dipakai ulang oleh `sutradara-edit/scripts/ambil_acuan.py` |
| `references/mesin.md` | Bagus, **kurang lengkap** | fitur yang sudah ada belum tercatat: `volume`/`volumeSfx`/`volumeSuara`, opsi SFX berkas `ulang`/`masuk`/`dari`, kamera & easing berupa fungsi, peredaman musik 30% saat narasi | dilengkapi (diverifikasi di `templat.html`) |
| `references/gaya.md` §4 (tata bahasa perpindahan), §4a (lapisan hidup) | **Bagus → pertahankan** | hasil bedah nyata dengan bukti per detik | dirujuk dari `sutradara-edit/pustaka/motion/transisi.md` sebagai implementasi mesin |
| `references/gaya.md` §0.1 tabel tema ↔ `references/tema.md` | **Tumpang tindih → gabung** | dua tabel tema dengan kolom berbeda | digabung ke `tema.md` (+ kolom transisi tanda tangan & musik + peta resep → tema); `gaya.md` §0.1 jadi penunjuk + urutan menang acuan > resep/gaya > tema |
| `references/gaya.md` §0.3 kartu identitas visual (6 baris) | **Terlalu sederhana → upgrade** | tidak memuat emosi, sistem huruf, bahasa gerak, metafora, bunyi, musik, yang sengaja tidak dipakai | menjadi bagian **Brief Sutradara** (`sutradara-edit/templat/brief.md`) |
| `references/gaya.md` §6 checklist kontak | Bagus, **kurang** | hanya teknis-visual; tidak menilai cerita, audio, anti tampilan AI | ditambah butir 14 → QC-1 `sutradara-edit/pustaka/polish/qc.md` |
| `references/flow.md` §6 "catatan lama" | **Outdated / tumpang tindih** | menggandakan `klip.md` | dipadatkan jadi penunjuk |
| `references/riset.md` §3 | **Outdated** | merujuk `visual-animasi-2d/scripts/ambil_footage.py` (skill lain, nama lama) | diganti `scripts/ambil_media.py` skill ini |
| `SKILL.md` paragraf Kolase 1.2/1.3/1.4 | **Tumpang tindih** | riwayat panjang di kepala skill, isinya sudah ada di references | dipadatkan jadi satu ringkasan fitur per versi + penunjuk |
| `SKILL.md` alur Tahap 1–4 | Bagus, **terlalu teknis** | alur produksi kuat, tetapi keputusan kreatif (hook, struktur, metafora, transisi bermotivasi, bunyi, musik, QC) belum punya pedoman | disambungkan ke pustaka: dialog **Gaya**, Brief Sutradara, storyboard + fungsi + metafora + motivasi transisi, QC-1/QC-2, `ketukan.py` |
| `references/klip.md`, `data-media.md`, `acuan.md`, `kemasan.md` | **Bagus → pertahankan** | spesifik dan teruji | tidak diubah |
| `contoh/*`, `aset/*` | **Bagus → pertahankan** | contoh teruji + aset konsisten | tidak diubah; `contoh/prompt-ai` dipakai untuk menguji preset resep |
| Pengetahuan editing umum (pacing, J/L-cut, prinsip animasi, tipografi, sound design, musik, gaya, QC) | **Kurang → tambah** | belum ada sama sekali di repo | skill baru `sutradara-edit` (§2) |
| Skill video lain di PC (motion-graphic, teks-kinetik-3d, video-edit-motion, infografis-2d, kartun-3d, film-ai, …) | Di luar repo → **tidak disunting** | aturan repo: jangan menyunting skill lain | boleh memakai pustaka `~/.claude/skills/sutradara-edit/pustaka/` (brief + storyboard sama) |
| Tren/efek tanpa fungsi (glow, partikel, transisi heboh) | **Tidak diprioritaskan** | bertentangan dengan Hukum Sutradara | dibatasi di `polish/qc.md` §6 (anggaran efek) |

## 2. Struktur baru
```
skill-edit-rizky/      mesin produksi (tangan)  — Tahap 1–5, mesin Kolase, unggah YouTube
sutradara-edit/        otak                      — /sutradara-edit
  SKILL.md             mode A rencana penuh · B konsultasi · C QC · D bedah acuan → resep gaya
  pustaka/00-peta.md   Hukum Sutradara, peta 11 kategori, cari cepat, 15 langkah, kontrak format
  pustaka/core/        editing.md
  pustaka/story/       cerita.md
  pustaka/short-form/  short-form.md
  pustaka/visual/      metafora.md · komposisi.md
  pustaka/type/        tipografi-kinetik.md
  pustaka/motion/      prinsip-animasi.md · transisi.md · kolase-editorial.md · ui-digital.md
  pustaka/cinematic/   kamera.md
  pustaka/audio/       sound-design.md · musik.md
  pustaka/style/       gaya-visual.md (20 gaya) · campur-gaya.md · warna-tekstur.md · bahasa-earnedits.md · resep/ (8 resep)
  pustaka/ai/          alur-ai.md
  pustaka/polish/      qc.md
  templat/             brief.md · storyboard.md · resep-gaya.md
  scripts/             ketukan.py · ambil_acuan.py
```
Setiap teknik ditulis **kapan → kenapa → cara (angka patokan) → hindari → di mesin Kolase → di editor lain**; tiap modul ditutup *Cek cepat*, *Celah mesin*, dan *Teknik modern*.

## 3. Cakupan permintaan (nomor = poin permintaan)
| # | Permintaan | Di mana |
|---|---|---|
| 1 | audit | dokumen ini §1 |
| 2 | editing fundamentals (17 teknik) | `core/editing.md` §1–17 + peta tempo 45 dtk + J/L-cut untuk editing berbasis narasi |
| 3 | storytelling (15 teknik) | `story/cerita.md` (+ 8 jenis hook, cerita mikro 15/30/45/60 dtk, contoh "Waktu terus berjalan") |
| 4 | kinetic typography (16) | `type/tipografi-kinetik.md` |
| 5 | cinematic motion / kamera (15) | `cinematic/kamera.md` |
| 6 | bahasa visual earn.edits (5 kelompok) | `style/bahasa-earnedits.md` + `style/warna-tekstur.md` + `style/resep/` |
| 7 | kolase / editorial (13) | `motion/kolase-editorial.md` |
| 8 | UI / digital (15) | `motion/ui-digital.md` |
| 9 | metafora visual | `visual/metafora.md` (metode 5 langkah + bank 50 konsep + metafora berlapis + saringan klise) |
| 10 | sound design (15) | `audio/sound-design.md` |
| 11 | music sync | `audio/musik.md` + **`scripts/ketukan.py`** (baru, teruji) |
| 12 | transisi lanjutan (13) | `motion/transisi.md` (motivasi dulu) |
| 13 | mikro-animasi & polish | `motion/prinsip-animasi.md` §5 |
| 14 | prinsip animasi + tangga easing | `motion/prinsip-animasi.md` §3–4 |
| 15 | color grading per suasana | `style/warna-tekstur.md` §1 |
| 16 | 20 gaya visual (10 atribut) | `style/gaya-visual.md` (+ Pilih cepat + peta ke tema mesin) |
| 17 | campur gaya | `style/campur-gaya.md` (aturan dominan ≥ 70%, matriks, 8 campuran jadi) |
| 18 | alur AI | `ai/alur-ai.md` |
| 19 | short-form | `short-form/short-form.md` (+ 8 struktur alternatif) |
| 20 | QC | `polish/qc.md` (BLOKIR/PENTING/POLES, QC-1/QC-2) |
| 21 | jangan terlihat AI | `polish/qc.md` §6 (tanda, batas, anggaran efek, uji hapus) + Hukum Sutradara |
| 22 | struktur 11 kategori | §2 di atas, `pustaka/00-peta.md` |
| 23 | prioritas | Hukum Sutradara (`00-peta.md` §1), menang atas aturan lain |
| lanjutan | unduh + bedah reel → gaya | 9 reel dibedah (8 @earn.edits + 1 @t1mline), **8 resep** di `style/resep/`, alur berulang: mode D + `scripts/ambil_acuan.py` |

## 4. Bedah reel @earn.edits (27 Nov 2026)
- Diunduh tanpa login/cookie (yt-dlp) ke `D:\automation\Video AI\Video Refrensi\earn.edits\reel-2026-11-27\` (video + lembar bedah, **tidak masuk repo**). Ringkasan: `ringkasan-acuan.md` di folder itu.
- 7 resep: Sinema Kasus, Legenda Gelap, Piksel Kertas, Panggung Emas, Arsip Pop, Kaca Gradien (2 reel), Panggung Korporat. Nama orisinal; yang dipelajari hanya prinsip.
- Tambahan atas permintaan pengguna: reel @t1mline `DgGzUj-Sgik` (59,5 dtk, 16:9, 34 potongan, 1,7 dtk/bidikan, 21% di ketukan) → resep **Diorama Kreator**, dibedah lewat `ambil_acuan.py` ke `D:\automation\Video AI\Video Refrensi\t1mline\reel-2026-11-27\`.
- Temuan terukur: video **bercerita** dipotong ikut kalimat (hanya 0–25% potongan di ketukan, rata bidikan 3–4,3 dtk tetapi selalu ada perubahan di dalam bidikan tiap 0,5–1 dtk); **promosi/pengumuman** lebih cepat (1,5–2,1 dtk) dan boleh lebih ikut ketukan (hingga 56%). Masuk ke `audio/musik.md`, `polish/qc.md` §6, dan `resep/README.md`.

## 5. Celah mesin (usulan pengembangan `templat.html`, berurutan menurut manfaat)
Belum dikerjakan (mesin sengaja tidak diubah di upgrade ini). Tiap fitur baru: tambah ke `templat.html`, rakit `contoh/n250` + `contoh/ai-mikir`, `cek` BERES, catat di `mesin.md`.
| Prioritas | Fitur | Untuk | Akali sementara |
|---|---|---|---|
| 1 | Rujukan ketukan di waktu (`'B16'`, `KONFIG.ketukan` dari `ketukan.py`) | sinkron musik tanpa hitung manual | tempel `const KETUKAN` + `KETUKAN.drop[0] - mulai` |
| 1 | Cek anti tampilan AI di `cek` (efek per adegan, transisi heboh berturut-turut, % potongan di ketukan, unsur bergerak sekaligus) | QC otomatis | hitung manual dengan `polish/qc.md` §6 |
| 1 | `jedaSengaja`: izinkan jeda narasi > 0,6 dtk yang ditandai | "tahan napas" sebelum payoff | jeda ≤ 0,6 dtk + gerak melambat |
| 2 | Teks: tracking beranimasi, mask reveal, per huruf (`anim: 'topeng'`, `'lacak'`) | tipografi sinematik/editorial | benda `kustom` + `c.letterSpacing`, `panel` + `gerak` |
| 2 | Grade: aberasi warna (`ca`), bloom/halation, kedip film, goresan, pita VHS | resep Sinema Kasus, gaya Retro/Analog | `glitch` singkat, `garis`, `cahaya` |
| 2 | Perpindahan `sobek` (kertas robek) | kolase, Arsip Pop | `tutup` + PNG tepi sobek |
| 2 | `klip.laju` keyframe (speed ramp sejati) | velocity edit di klip | kamera keyframe inExpo → outQuart |
| 3 | Huruf piksel, teks gradien emas/krom, teks neon | Piksel Kertas, Panggung Emas, Cyberpunk | Anton + bayang keras, `kilap` |
| 3 | Benda UI: kursor, daftar gulir/feed, grafik garis/donat, widget dashboard | `motion/ui-digital.md` | sketsa `kustom` di modul itu |
| 3 | Backdrop blur (kaca buram) | Kaca Gradien, Futuristic UI | kotak putih 75% + bayangan |
| 3 | Transisi liquid/displacement, morph bentuk, topeng dari alfa potongan (`bingkai.bentuk: 'gambar'`) | transisi bermotivasi bentuk | `cocok` dua gambar, `iris`, klip Flow |
| 3 | Parallax dari peta kedalaman satu foto, fokus kedalaman otomatis (`KONFIG.fokus`) | 2,5D dari satu gambar | potong lapisan di Flow (pelat + potongan) |
| 4 | `KONFIG.patah` (on twos global), kamera `'lompat'` (jump cut), cek loop (bingkai akhir vs awal), peta retensi per 3 dtk | Piksel Kertas, short-form | easing tangga, keyframe bertangga |
| 4 | Tema baru dari resep: `vhs`, `piksel`, `kaca`, `emas` | resep jadi satu kata | tempel preset resep |
Rincian per modul ada di bagian *Celah mesin* masing-masing.

## 6. Teknik modern yang ditambahkan (ringkas)
| Teknik | Manfaat | Modul |
|---|---|---|
| Hook visual tanpa suara (silent-first) | banyak penonton menggulir tanpa suara; hook harus terbaca dari gambar | `story/cerita.md`, `short-form.md` |
| Loop kalimat (kalimat akhir mengalir ke L01) | nilai tonton ulang | `short-form.md` §7 |
| Re-hook tiap 8–12 dtk | menahan retensi di tengah | `short-form.md` |
| Teks di belakang subjek | kedalaman 3 lapis, terlihat "didesain" | `type/`, `visual/komposisi.md`, resep Panggung Emas |
| Gambar di dalam kalimat | contoh konkret tepat di kata | resep Kaca Gradien, `type/` |
| Metafora harfiah surealis | hook kuat dari ungkapan sehari-hari | `visual/metafora.md` |
| Warna selektif sebagai makna (kuasa, fokus) | mata langsung ke inti tanpa panah | resep Arsip Pop, Panggung Korporat |
| Layar di dalam adegan membawa data | data terasa nyata, kamera bisa menyelam | resep Sinema Kasus, `motion/ui-digital.md` |
| Lingkungan sama, isi berubah (musim/waktu) | membuktikan perubahan tanpa teks | resep Legenda Gelap, `motion/transisi.md` |
| Siluet peta panas (thermal) | misteri + gaya tanpa wajah | resep Panggung Emas |
| Morph bingkai awal/akhir AI, parallax peta kedalaman, relight AI | transisi & 2,5D dari gambar diam | `ai/alur-ai.md`, `cinematic/kamera.md` |
| Edit dipimpin bunyi, speed ramp di ketukan, stem musik per babak | energi tanpa menambah potongan | `audio/` |
| Kurva easing tanda tangan per seri, gerak hold-then-snap | identitas gerak | `motion/prinsip-animasi.md` |
| Halation + grain per seri | finishing film yang konsisten | `style/warna-tekstur.md` |

## 7. Verifikasi
- `ketukan.py`: trek sintetis 120 BPM (hening 15–16 dtk, drop 16 dtk) → BPM 119,8, ketukan & awal birama tepat ±1 bingkai, drop 15,97, "tahan" 15,00; musik nyata `D:\Sound\Backsound\Cinematic Epic\` → 129,5 BPM, drop 31,6 dtk; 8 reel → persen potongan di ketukan (§4).
- `ambil_acuan.py`: diuji pada 1 URL reel (unduh tanpa cookie berhasil) + 7 berkas lokal → bedah + ketukan + `ringkasan-acuan.md`.
- Preset resep **Sinema Kasus** ditempel ke `contoh/prompt-ai` → `rakit` OK, tidak ada galat konfig, `kontak` dilihat (judul Inter tipis, grade biru dingin). `cek` memberi 2 SALAH: caption pil menutupi kartu (→ caption di preset resep dijadikan opsional + peringatan) dan durasi di luar `durasiTarget` karena contoh dirakit tanpa audio narasi (bukan karena preset). Preset **Diorama Kreator** juga diuji (preset + latar tiga "ruang warna" + sorot): tidak ada galat, latar tampil benar; temuan: efek `sorot` ikut menggelapkan teks di luar lingkarannya (dicatat di resep). Preset 6 resep lain belum diuji di mesin.
- Tautan relatif antar-modul diperiksa otomatis: semua ada (satu pengecualian disengaja: templat resep relatif ke folder `resep/`).
- Belum: video baru end-to-end dengan resep (butuh topik + narasi), uji `pasang.ps1` di PC lain.
