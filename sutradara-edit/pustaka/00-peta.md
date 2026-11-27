# Peta Pustaka Sutradara Edit

Pustaka keahlian video editing + motion design + visual storytelling milik Rizky. Mesin produksi tetap di skill lain (bawaan `skill-edit-rizky`, mesin Kolase); pustaka ini menentukan **apa** yang dibuat dan **kenapa**, mesin menentukan **bagaimana dirender**.

## 1. Hukum Sutradara (berlaku di semua modul, menang atas aturan lain)
1. **Profesional > banyak efek.** Bila ragu antara menambah efek atau merapikan timing, rapikan timing.
2. **Mudah dipahami > kompleks.** Satu bingkai = satu gagasan utama. Penonton harus tahu ke mana harus melihat dalam 0,3 dtk.
3. **Cerita > tren.** Tren hanya dipakai bila melayani cerita; kalau dihapus ceritanya tidak rusak, berarti itu hiasan.
4. **Setiap unsur punya fungsi.** Gerak, transisi, teks, bunyi, tekstur: tulis fungsinya dalam satu kata (menunjukkan, menekankan, menghubungkan, memberi jeda, memberi suasana). Tanpa fungsi = buang.
5. **Variasi ritme, bukan ritme rata.** Cepat–lambat–diam–hantam–lepas. Ritme datar (semua potongan sama panjang, semua di ketukan) terasa seperti templat.
6. **Ciri tangan manusia.** Sedikit ketidaksempurnaan yang disengaja (tekstur, miring 1–3°, timing tidak simetris) lebih hidup daripada simetri sempurna. Lihat `polish/qc.md` §6 (anti tampilan AI).

## 2. Struktur pustaka (11 kategori)
| Kategori | Berkas | Isi | Pakai saat |
|---|---|---|---|
| **CORE** | `core/editing.md` | pacing, ritme, timing, cutting, jump/match/J/L cut, speed ramp, montase, kontinuitas, progresi adegan, sinkron ketukan, antisipasi, reaksi, jeda, ruang napas | menyusun storyboard + timing tiap potongan |
| **STORY** | `story/cerita.md` | arsitektur hook, curiosity gap, open loop, pattern interrupt, setup→eskalasi→payoff, masalah→tegang→solusi, emosi, pengungkapan info, transisi naratif, kontras, sebelum/sesudah, cerita mikro 15–60 dtk | konsep, naskah, urutan beat |
| **SHORT-FORM** | `short-form/short-form.md` | hook 1 dtk & 3 dtk, retensi, interupsi pola, kepadatan info, variasi tempo, ujung loop, nilai tonton ulang, struktur HOOK→…→LOOP/CTA dan alternatifnya | Reels/Shorts/TikTok 15–60 dtk |
| **VISUAL** | `visual/metafora.md` | metode konsep abstrak → visual konkret + bank metafora | tiap kalimat narasi yang abstrak |
| | `visual/komposisi.md` | komposisi, hierarki, ruang kosong, zona aman 9:16, depan/tengah/belakang, staging | menata tiap bingkai |
| **TYPE** | `type/tipografi-kinetik.md` | tipografi kinetik, penekanan kata, tracking, reveal, mask, deformasi, overshoot, morph, sinkron suara/musik, caption dinamis, editorial/besar/minimal/sinematik | semua teks di layar |
| **MOTION** | `motion/prinsip-animasi.md` | 12 prinsip animasi, tangga easing, mikro-animasi & polish | setiap gerak benda/teks |
| | `motion/transisi.md` | transisi bermotivasi: match, whip, objek, mask, bentuk, kamera, zoom, rotasi, displacement, liquid, glitch, cahaya, lingkungan mulus | pergantian adegan |
| | `motion/kolase-editorial.md` | kolase foto, cutout, kertas, majalah/koran, foto berlapis, foto hidup, sobek kertas, scrapbook | gambar diam jadi hidup |
| | `motion/ui-digital.md` | UI HP/web/dashboard/feed/notifikasi/kursor/gulir/ketik/chat, data viz, grafik, progres, loading, transisi antarmuka | menjelaskan konsep digital/data |
| **CINEMATIC** | `cinematic/kamera.md` | bahasa kamera: push/pull, orbit, handheld, dolly, whip, parallax 2,5D, kamera 3D, kedalaman, tracking, guncang, motion blur | memilih gerak kamera tiap adegan |
| **AUDIO** | `audio/sound-design.md` | whoosh, impact, riser, hit, klik, ketik, UI, ambience, room tone, bass, glitch, reverse, boom, tekstur; hubungan gerak + bunyi + waktu | lapisan bunyi |
| | `audio/musik.md` | deteksi ketukan (`scripts/ketukan.py`), potong di ketukan, build-up, drop, ketegangan, hening sebelum hantaman, ducking | musik dan sinkronnya |
| **STYLE** | `style/gaya-visual.md` | 20 gaya visual (tipografi, warna, transisi, tekstur, kamera, bahasa animasi, bunyi, tempo, komposisi, kegunaan) + peta ke mesin | memilih gaya sebelum storyboard |
| | `style/resep/` | **8 resep gaya hasil bedah reel** (Sinema Kasus, Legenda Gelap, Piksel Kertas, Panggung Emas, Arsip Pop, Kaca Gradien, Panggung Korporat, Diorama Kreator) + temuan ukuran ritme | gaya siap pakai untuk topik apa pun |
| | `style/campur-gaya.md` | menggabungkan 2 gaya tanpa berantakan | gaya campuran |
| | `style/warna-tekstur.md` | grading per suasana + tekstur retro/analog, grunge, finishing sinematik | grade + tekstur akhir |
| | `style/bahasa-earnedits.md` | prinsip visual hasil belajar dari @earn.edits, dan cara membuatnya jadi gaya Rizky sendiri | gaya kolase sinematik editorial |
| **AI** | `ai/alur-ai.md` | alur AI pra-produksi → produksi → pasca-produksi, alat yang tersedia, konsistensi | memakai Flow/Veo/ElevenLabs/Epidemic/Claude |
| **POLISH** | `polish/qc.md` | QC cerita/visual/gerak/audio/finishing + audit anti tampilan AI | sebelum pratinjau dan sebelum render final |

Templat kerja: `../templat/brief.md` (brief sutradara satu halaman), `../templat/storyboard.md` (tabel storyboard lengkap), `../templat/resep-gaya.md` (resep gaya dari acuan). Alat: `../scripts/ketukan.py` (ketukan, energi, drop, hening, persen potongan acuan di ketukan) dan `../scripts/ambil_acuan.py` (unduh acuan publik tanpa login + bedah + ketukan → ringkasan).

## 3. Cari cepat: "saya butuh…"
| Butuh | Baca |
|---|---|
| hook yang menahan jempol | `story/cerita.md` §Hook → `short-form/short-form.md` §Hook 1 dtk |
| narasi abstrak ("waktu berjalan", "overthinking") jadi gambar | `visual/metafora.md` |
| video terasa datar / membosankan | `core/editing.md` §Pacing + `short-form/short-form.md` §Retensi |
| video terasa ramai / murahan / "AI banget" | `polish/qc.md` §6 + `style/warna-tekstur.md` §Anggaran tekstur |
| gerak terasa kaku | `motion/prinsip-animasi.md` §Tangga easing |
| transisi terasa dipaksakan | `motion/transisi.md` §Motivasi |
| teks terlihat seperti subtitle biasa | `type/tipografi-kinetik.md` |
| bunyi tipis / tidak "nendang" | `audio/sound-design.md` §Lapisan |
| potongan tidak pas dengan musik | `audio/musik.md` + `scripts/ketukan.py` |
| memilih tampilan | `style/resep/README.md` (resep siap pakai) atau `style/gaya-visual.md` → bila 2 gaya: `style/campur-gaya.md` |
| gaya baru dari video/akun acuan | `../SKILL.md` §4 (mode D) + `../scripts/ambil_acuan.py` + `../templat/resep-gaya.md` |
| menjelaskan aplikasi/data/proses digital | `motion/ui-digital.md` |
| foto diam harus terasa hidup | `motion/kolase-editorial.md` + `cinematic/kamera.md` §Parallax |

## 4. Urutan kerja sutradara (15 langkah) → modul
| # | Langkah | Modul | Hasil |
|---|---|---|---|
| 1 | Konsep | `story/cerita.md` §Konsep | satu kalimat premis + emosi target |
| 2 | Hook | `story/cerita.md` §Hook, `short-form/short-form.md` | 3 opsi hook (kata + gambar + bunyi) |
| 3 | Struktur cerita | `story/cerita.md`, `short-form/short-form.md` §Struktur | beat bernomor + fungsi tiap beat |
| 4 | Gaya visual | `style/gaya-visual.md`, `style/campur-gaya.md` | gaya utama (+ gaya kedua) |
| 5 | Metafora visual | `visual/metafora.md` | 1 metafora per beat abstrak |
| 6 | Storyboard + shot | `core/editing.md`, `visual/komposisi.md`, `../templat/storyboard.md` | tabel storyboard |
| 7 | Kamera | `cinematic/kamera.md` | gerak kamera + alasannya per adegan |
| 8 | Motion | `motion/prinsip-animasi.md`, `motion/kolase-editorial.md`, `motion/ui-digital.md` | bahasa gerak |
| 9 | Tipografi | `type/tipografi-kinetik.md` | sistem huruf + kata yang ditekankan |
| 10 | Transisi | `motion/transisi.md` | transisi bermotivasi per sambungan |
| 11 | Sound design | `audio/sound-design.md` | daftar SFX bertanda waktu |
| 12 | Musik | `audio/musik.md` | musik + peta ketukan + titik hantam/hening |
| 13 | Short-form | `short-form/short-form.md` | cek retensi tiap 3 dtk + ujung loop |
| 14 | Polish | `style/warna-tekstur.md`, `motion/prinsip-animasi.md` §Mikro | grade, tekstur, detail kecil |
| 15 | QC | `polish/qc.md` | daftar lolos/gagal + perbaikan |

## 5. Kontrak format modul (untuk menambah/mengubah modul)
- Bahasa Indonesia yang lugas; istilah industri boleh dalam bahasa Inggris (J-cut, easing, tracking) dengan padanan sekali.
- Kepala berkas: judul + baris `> Kategori · dipakai di langkah # · terkait: …` + 3–6 prinsip inti.
- **Setiap teknik utama ditulis empat bagian**: **Kapan** → **Kenapa** → **Cara** (langkah konkret + angka patokan: detik, bingkai pada 30 fps, persen, easing) → **Hindari**. Lalu **Di mesin Kolase** (fitur/konfig nyata dari `skill-edit-rizky/references/mesin.md`; bila belum ada: tulis *Celah mesin* + cara mengakalinya) dan, bila berguna, **Di editor lain** (CapCut/After Effects/Premiere, satu baris).
- Katalog panjang (bunyi, metafora, gaya) boleh berbentuk tabel, tetapi tetap memuat kolom kapan/kenapa/hindari.
- Angka adalah **patokan**, bukan hukum; tulis rentang.
- Penutup berkas: `## Cek cepat` (3–8 butir ya/tidak, dipakai `polish/qc.md`) dan, bila ada, `## Celah mesin` (fitur yang belum ada di mesin Kolase + usulan).
- Teknik baru yang relevan masuk bagian `## Teknik modern` dengan **manfaat · kapan · cara memasukkan ke alur**.
- Tidak ada aturan yang bertentangan dengan §1. Tidak menyalin karya/nama/logo/kalimat/musik pihak lain.
