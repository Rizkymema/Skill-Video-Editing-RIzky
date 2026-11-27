# Brief Sutradara — <JUDUL KERJA>

> Satu halaman, ditulis SEBELUM storyboard. Bila dipakai di `skill-edit-rizky`, ringkasannya (8–10 baris) jadi komentar kepala `konfig.js`, menggantikan "kartu identitas visual" lama (isinya tetap tercakup).
> Isi tiap baris dengan keputusan + **alasan satu frasa**. Baris tanpa alasan = belum diputuskan.

| # | Keputusan | Isi | Alasan |
|---|---|---|---|
| 1 | **Premis** (1 kalimat) | <siapa/apa> + <keanehan/konflik> + <kenapa penonton peduli> | |
| 2 | **Emosi target** | mis. penasaran → kaget → paham → puas | |
| 3 | **Format** | rasio · durasi · platform · narator (Edge/ElevenLabs/rekaman) | |
| 4 | **Hook** (pilih 1 dari 3) | kata pertama · bingkai 0 · bunyi 0 | `story/cerita.md` §Hook |
| 5 | **Struktur** | HOOK→CONTEXT→TENSION→DEVELOPMENT→PAYOFF→LOOP, atau alternatif | `short-form/short-form.md` §Struktur |
| 6 | **Gaya utama** | salah satu dari 20 gaya / gaya acuan / resep reel | `style/gaya-visual.md` |
| 7 | **Gaya kedua** (opsional) | gaya + **apa yang ia kuasai** (mis. hanya tipografi + bunyi UI) | `style/campur-gaya.md` |
| 8 | **Palet** | latar · teks · aksen 1 (makna) · aksen 2 (makna) | `style/warna-tekstur.md` |
| 9 | **Sistem huruf** | hero · pendukung · label; kata yang ditekankan dengan apa | `type/tipografi-kinetik.md` |
| 10 | **Bahasa gerak** | easing tanda tangan · overshoot % · gerak kamera dasar | `motion/prinsip-animasi.md`, `cinematic/kamera.md` |
| 11 | **Metafora utama** | 1 benda/gambar yang berevolusi sepanjang video | `visual/metafora.md` §Metafora berlapis |
| 12 | **Benda khas** | 1–2 benda bertulisan yang jadi "wajah" video | |
| 13 | **Transisi tanda tangan** | 1 transisi + di momen apa (maks 2–3×) | `motion/transisi.md` |
| 14 | **Efek tanda tangan** | 1 efek + fungsinya; anggaran efek total | `polish/qc.md` §6 |
| 15 | **Palet bunyi** | 3–5 bunyi khas (mis. kertas, rana kamera, sub-boom) + ambience | `audio/sound-design.md` |
| 16 | **Musik** | suasana · BPM · titik hening · titik hantam (dari `ketukan.py`) | `audio/musik.md` |
| 17 | **Tekstur/finishing** | grain · vinyet · tekstur khusus (kertas, VHS) — satu lapisan global | `style/warna-tekstur.md` |
| 18 | **Beda dari video terakhir** | apa yang diganti (riwayat) — dilewati bila seri/acuan | `skill-edit-rizky` `riwayat.py lihat` |
| 19 | **Yang sengaja TIDAK dipakai** | mis. tanpa glitch, tanpa partikel, tanpa subtitle | Hukum Sutradara |

## Ringkasan untuk kepala konfig.js
```
/* ── Brief Sutradara (sutradara-edit/templat/brief.md)
   premis ....... …
   emosi ........ …
   gaya ......... <utama> (+ <kedua>: hanya <bagian>)
   palet ........ latar … · teks … · aksen … (= …) · aksen … (= …)
   huruf ........ hero … · pendukung … · label …
   gerak ........ easing …, overshoot …%, kamera dasar …
   metafora ..... …
   tanda tangan . transisi … · efek … · bunyi …
   musik ........ … BPM, hening …, hantam …
   tidak dipakai  …
*/
```
