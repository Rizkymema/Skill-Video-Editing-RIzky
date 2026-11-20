# Skill Edit Rizky

Skill Claude Code untuk membuat video edukasi/explainer 9:16 (30–60 dtk) dari **satu file HTML**, untuk topik apa pun, dengan **tema yang bisa dipilih** atau **mengikuti video/gambar acuan**. Dulu bernama `kolase-retro`.

- Mesin: `skill-edit-rizky/assets/templat.html` (Kolase 1.4): kolase berlapis, kamera 2,5D, perpindahan bermomentum, efek ala After Effects, teks kinetik, UI digambar kode, bunyi per teks/ikon, ekspor MP4 langsung di browser (WebCodecs).
- Tema: `skill-edit-rizky/references/tema.md` (arsip, dosir, pasar, teknologi, tv, modern, perang, alam, editorial, kartu, atau ikut acuan).
- Contoh siap rakit: `skill-edit-rizky/contoh/` (konfig + naskah + waktu kata; tanpa audio).
- Aset gambar siap pakai: `aset/` (tokoh 3D Raka + ikon 3D).

Video, audio, musik, dan logo pihak lain **tidak disimpan di repo ini**.

## Pasang di PC
```powershell
git clone https://github.com/Rizkymema/Skill-Video-Editing-RIzky.git
cd Skill-Video-Editing-RIzky
powershell -ExecutionPolicy Bypass -File .\pasang.ps1
```
`pasang.ps1` menyalin skill ke `%USERPROFILE%\.claude\skills\skill-edit-rizky\` (+ `aset\`), dengan cadangan versi lama. Panggil di Claude Code: `/skill-edit-rizky`.

Kebutuhan: Python 3.12 + Playwright (Chrome terpasang), Pillow, numpy; ffmpeg untuk klip/pemeriksaan audio; Google Flow (flow-mcp) untuk gambar baru (opsional).

## Ubah skill
Sunting di repo ini, commit + push, lalu jalankan `pasang.ps1` lagi. Jangan menyunting salinan di `~/.claude/skills` langsung.
