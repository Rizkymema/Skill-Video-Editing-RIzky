# Skill Video Editing Rizky

Dua skill Claude Code yang bekerja berpasangan:

| Skill | Peran | Panggil |
|---|---|---|
| `sutradara-edit/` | **otak**: konsep, hook, storytelling, storyboard, gaya visual (20 gaya + 8 resep hasil bedah reel), campur gaya, metafora visual, kamera, motion, tipografi kinetik, transisi bermotivasi, sound design, sinkron musik, short-form, polish, QC anti tampilan AI; juga membedah video acuan jadi resep gaya baru | `/sutradara-edit` |
| `skill-edit-rizky/` | **tangan**: video edukasi/explainer 9:16 (30–60 dtk) dari satu file HTML (mesin Kolase 1.5: elemen hidup di dalam satu gambar + rigging lapisan + sambungan dari benda), 10 tema dasar + **8 gaya bawaan dari reel acuan** (satu kata: `tema: 'diorama-kreator'` dst.) atau ikut acuan visual, gambar Flow + media berlisensi, ekspor MP4 di browser, unggah YouTube | `/skill-edit-rizky` (nama lama `/kolase-retro`) |

`skill-edit-rizky` memakai pustaka `sutradara-edit` di Tahap 1–4 (brief, storyboard, QC-1/QC-2). Skill video lain di PC ini juga boleh memakai pustakanya (`~/.claude/skills/sutradara-edit/pustaka/`).

## Isi
- `sutradara-edit/pustaka/` — 11 kategori: CORE, STORY, SHORT-FORM, VISUAL, TYPE, MOTION, CINEMATIC, AUDIO, STYLE, AI, POLISH. Mulai dari `pustaka/00-peta.md`.
- `sutradara-edit/pustaka/style/resep/` — 8 resep gaya (Sinema Kasus, Legenda Gelap, Piksel Kertas, Panggung Emas, Arsip Pop, Kaca Gradien, Panggung Korporat, Diorama Kreator).
- `sutradara-edit/templat/` — brief sutradara, storyboard, resep gaya.
- `sutradara-edit/scripts/ketukan.py` — BPM, ketukan, birama, energi, drop, hening, saran potong bervariasi, persen potongan acuan di ketukan.
- `sutradara-edit/scripts/ambil_acuan.py` — unduh video acuan publik tanpa login + bedah + ketukan → ringkasan.
- `skill-edit-rizky/assets/templat.html` — mesin Kolase 1.5; `references/` panduan mesin; `contoh/` konfig siap rakit (tanpa audio).
- `aset/` — gambar siap pakai (tokoh 3D Raka + ikon 3D).
- `Hasil Video/` — **semua hasil video skill-edit-rizky** (sejak 28 Nov 2026; MP4, HTML, sampul, info YouTube, `_kerja`); ada di `.gitignore`, tidak pernah di-commit.
- `sfx/` — **pustaka SFX utama** (71 SFX Epidemic per kategori, dipakai otomatis oleh `rakit`); yang di-commit hanya `README.md` + `katalog.json` (audio di `.gitignore`). Tambah SFX: `skill-edit-rizky/scripts/pustaka_sfx.py tambah`.
- `AUDIT.md` — hasil audit skill (dipertahankan / diupgrade / digabung / ditambah) + celah mesin.

Video, audio, musik, logo pihak lain, dan video acuan yang dibedah **tidak disimpan di repo ini** (acuan ada di `D:\automation\Video AI\Video Refrensi\`).

## Pasang di PC
```powershell
git clone https://github.com/Rizkymema/Skill-Video-Editing-RIzky.git
cd Skill-Video-Editing-RIzky
powershell -ExecutionPolicy Bypass -File .\pasang.ps1
```
`pasang.ps1` menyalin `skill-edit-rizky` (+ `aset\`) dan `sutradara-edit` ke `%USERPROFILE%\.claude\skills\`, dengan cadangan versi lama di `.claude\skills-cadangan\`.

Kebutuhan: Python 3.12 + Playwright (Chrome terpasang), Pillow, numpy; ffmpeg (atau `imageio_ffmpeg`) untuk klip, audio, dan `ketukan.py`; `yt-dlp` untuk `ambil_acuan.py`; Google Flow (flow-mcp) untuk gambar baru (opsional).

## Ubah skill
Sunting di repo ini, commit + push, lalu jalankan `pasang.ps1` lagi. Jangan menyunting salinan di `~/.claude/skills` langsung.
