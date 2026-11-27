# Quality control: sebelum video dianggap selesai

> POLISH · dipakai di langkah 15 (dan sekali lagi sebelum render final) · terkait: semua modul (`## Cek cepat` tiap modul), `../../templat/storyboard.md`, agen `pemeriksa-video`

Prinsip inti:
- QC menilai **pengalaman penonton**, bukan daftar fitur. Pertanyaannya selalu: "apa yang penonton rasakan/pahami di detik ini?"
- Dua putaran: **QC-1 sebelum pratinjau** (cerita, susunan, timing) dan **QC-2 sebelum render final** (audio akhir, finishing, ekspor). Masalah cerita yang lolos ke QC-2 mahal diperbaiki.
- Setiap temuan ditulis **per detik** + tingkat + perbaikan konkret. "Kurang greget" bukan temuan; "1,8–4,2 dtk: tiga bidikan sama besar, ganti bidikan ke-2 jadi close-up angka" adalah temuan.
- Lulus = tidak ada **BLOKIR**, maksimal 3 **PENTING** yang sudah disetujui pengguna untuk dibiarkan.

## 1. Cara menjalankan
1. **Cek mesin** (mesin Kolase): `jalankan.py cek _kerja/film.html` sampai BERES. Ini menangkap durasi, jeda narasi, teks keluar zona, gambar hilang, LUFS, potong keras, gambar diam.
2. **Lihat lembar kontak**: `jalankan.py kontak _kerja/film.html _kerja/kontak.jpg --n 36` + `--t` rapat (0,1 dtk) di hook (0–3 dtk), setiap perpindahan tanda tangan, dan payoff. Lihat **setiap** lembar, jangan menyimpulkan dari angka.
3. **Tonton penuh 3 kali dengan tujuan berbeda**: (a) bisu: apakah cerita terbaca dari gambar + teks saja? (b) mata tertutup: apakah audio sendiri sudah bercerita dan bersih? (c) normal di layar HP sebesar aslinya.
4. **Ukur audio** sesudah ekspor: `ffmpeg -i <mp4> -af ebur128=peak=true -f null -` → −14 ±1 LUFS, puncak < 0 dBFS (`audio/musik.md`, `audio/sound-design.md`).
5. **Isi tabel di §2–§6**, beri tingkat, lalu perbaiki dari BLOKIR ke bawah. Agen `pemeriksa-video` boleh menjalankan langkah 1–4 dan melaporkan per detik; perbaikan tetap diputuskan di sini.

Tingkat temuan:
| Tingkat | Arti | Contoh |
|---|---|---|
| **BLOKIR** | penonton salah paham, data salah, rusak teknis, atau hook gagal | angka beda dari sumber; hook baru jelas di detik 4; puncak audio > 0 dBFS; teks tertutup tombol aplikasi |
| **PENTING** | penonton masih paham, tetapi terasa amatir / murahan / "AI" | tiga transisi heboh berturut-turut; semua potongan di ketukan; glow di semua teks |
| **POLES** | detail yang membedakan bagus dan istimewa | overshoot terlalu besar 4%; whoosh 2 bingkai telat |

## 2. Cerita
| Cek | Lolos bila | Bila gagal → baca |
|---|---|---|
| Hook menarik? | bingkai 0 sudah ada **subjek + ketegangan** (pertanyaan, kontras, angka, aksi); tanpa suara pun terbaca dalam 1 dtk; kalimat pertama ≤ 12 kata | `../story/cerita.md` §Hook, `../short-form/short-form.md` §Hook 1 dtk |
| Penonton tahu apa yang terjadi? | dalam 3–5 dtk penonton bisa menjawab "ini tentang apa dan kenapa saya peduli" | `../story/cerita.md` §Pengungkapan info |
| Ada progresi? | tiap beat menambah sesuatu baru (info, taruhan, emosi); tidak ada dua beat yang fungsinya sama | `../story/cerita.md` §Setup → eskalasi → payoff |
| Payoff jelas? | ada satu momen yang menjawab janji hook; diberi ruang (jeda 0,3–0,8 dtk, gerak melambat, bunyi berubah) | `../story/cerita.md`, `../core/editing.md` §Jeda |
| Open loop ditutup? | setiap pertanyaan yang dibuka dijawab, kecuali sengaja untuk seri | `../story/cerita.md` §Open loop |
| Akhir | ujung loop / kalimat penutup terasa disengaja, bukan terpotong | `../short-form/short-form.md` §Loop |
| Data | semua angka/tanggal/nama di layar = `KONFIG.sumber`; perkiraan ditulis "±" | `skill-edit-rizky/references/riset.md` |

## 3. Visual
| Cek | Lolos bila | Bila gagal → baca |
|---|---|---|
| Komposisi kuat? | tiap bingkai punya satu titik fokus yang jelas; garis/arah mengarah ke situ | `../visual/komposisi.md` |
| Hierarki jelas? | maksimal 1 unsur utama + 1 pendukung; mata tahu urutan baca dalam 0,3 dtk | `../visual/komposisi.md` §Hierarki |
| Terlalu ramai? | ≤ 4 unsur bergerak sekaligus; ≤ 2 gaya huruf per bingkai; ada ruang kosong | `../motion/prinsip-animasi.md` §Anggaran gerak |
| Setiap visual punya fungsi? | tiap lapisan bisa dijelaskan dengan satu kata fungsi (Hukum §1.4); hapus yang tidak | `00-peta.md` §1 |
| Metafora mendarat? | konsep abstrak punya gambar konkret yang **bergerak membuktikan** konsepnya, bukan ilustrasi tempelan | `../visual/metafora.md` |
| Konsisten gaya? | satu gaya utama (+ satu gaya kedua bila campur) dari awal sampai akhir; palet ≤ 2 aksen | `../style/gaya-visual.md`, `../style/campur-gaya.md` |
| Zona aman 9:16 | teks di 8–70% tinggi, kanan bawah kosong (tombol), tidak ada yang terpotong tepi | `../visual/komposisi.md` §Zona aman |

## 4. Gerak
| Cek | Lolos bila | Bila gagal → baca |
|---|---|---|
| Animasi kaku? | tidak ada gerak linear kecuali benda mekanis; masuk memakai ease-out/overshoot, keluar ease-in | `../motion/prinsip-animasi.md` §Tangga easing |
| Easing bagus? | overshoot 4–12% lalu settle 6–10 bingkai; benda besar lebih lambat dari benda kecil | `../motion/prinsip-animasi.md` |
| Gerak tak perlu? | setiap gerak kamera punya alasan (fokus, ungkap, hubungkan); tidak ada zoom acak | `../cinematic/kamera.md` |
| Transisi alami? | tiap transisi punya hubungan visual (bentuk, arah, benda, warna, gagasan); sisanya potong biasa | `../motion/transisi.md` §Motivasi |
| Ritme bervariasi? | panjang bidikan tidak seragam; ada minimal satu momen diam/lambat sebelum payoff | `../core/editing.md` §Pacing |
| Teks terbaca? | tiap teks tampil ≥ waktu baca (`../type/tipografi-kinetik.md` §Waktu baca); kata muncul 0–2 bingkai sebelum diucapkan | `../type/tipografi-kinetik.md` |

## 5. Audio
| Cek | Lolos bila | Bila gagal → baca |
|---|---|---|
| Suara jelas? | narasi selalu paling depan; kata pertama tidak terpotong; tidak ada SFX/musik menutupi konsonan | `../audio/sound-design.md` §Level |
| SFX sinkron? | transien impact tepat di bingkai mendarat; puncak whoosh di titik potong; tidak ada SFX di setiap unsur | `../audio/sound-design.md` §Sinkron |
| Musik terlalu keras? | musik ±18–24 dB di bawah narasi saat bicara; naik di jeda/payoff | `../audio/musik.md` §Ducking |
| Transisi audio? | ada sambungan bunyi antar-babak (riser, reverse, ekor gema, room tone); tidak ada hening digital mendadak | `../audio/sound-design.md` §Room tone |
| Hening dipakai? | minimal satu "tahan napas" sebelum hantaman terbesar (bila cocok dengan cerita) | `../audio/musik.md` §Hening sebelum hantaman |
| Teknis | −14 ±1 LUFS, puncak < 0 dBFS, tidak ada letupan di 0,1 dtk pertama | `skill-edit-rizky/SKILL.md` §Tahap 4 |

## 6. Anti tampilan "AI-generated" (wajib di QC-1 dan QC-2)
Hasil harus terasa dibuat **editor + motion designer + penutur cerita**, bukan mesin yang memakai semua efek yang ada. Tanda bahaya dan batasnya:

| Tanda "AI/templat" | Batas lolos | Ganti dengan |
|---|---|---|
| glow/bloom di mana-mana | bloom hanya di 1 sumber cahaya nyata per adegan; teks tanpa glow kecuali gaya neon/dark tech, dan itupun 1 kata | kontras nilai (terang-gelap), bukan cahaya |
| partikel terus-menerus | partikel hanya bila bermakna (debu arsip, hujan, koin di topik uang), ≤ 25% durasi | tekstur diam halus (grain) |
| transisi berlebihan | ≥ 50% sambungan adalah potong biasa / potong bermomentum; transisi "heboh" (glitch, putar, kilat) ≤ 3 per 45 dtk dan tidak berturut-turut | potong di gerak, match cut |
| kamera bergerak acak | tiap adegan satu gerak kamera dengan arah konsisten; tidak ada goyang/zoom tanpa alasan | kamera tenang + satu dorongan di kata kunci |
| tipografi ramai | ≤ 2 keluarga huruf + 1 aksen; ≤ 1 kata beraksen per baris; animasi teks ≤ 2 jenis per video | hierarki ukuran |
| efek tanpa fungsi | setiap efek tercatat fungsinya di storyboard; yang tak tercatat dihapus | — |
| warna terlalu neon | saturasi aksen ≤ 85%; neon hanya di gaya Cyberpunk/Dark Tech/Y2K, dan hanya 1 warna | aksen tunggal yang bermakna |
| animasi berbau templat | tidak semua unsur masuk dengan cara yang sama (pop-pop-pop); timing tidak simetris; ada jeda | variasi masuk berdasarkan peran (`../motion/prinsip-animasi.md`) |
| simetri & kebersihan sempurna | ada sentuhan tangan: miring 1–3°, tekstur kertas/grain, tepi tidak sempurna, bayangan lembut | `../style/warna-tekstur.md` |
| semua di ketukan | ≤ 60% potongan di ketukan; pola ketukan → tahan → antisipasi → hantam → lepas | `../audio/musik.md`, `scripts/ketukan.py` |
| wajah/tangan AI aneh, teks tak sengaja di gambar | nol; ganti gambarnya | `../ai/alur-ai.md` §QC artefak |

**Anggaran efek per video 45 dtk** (patokan; gaya tertentu boleh menggeser, tulis alasannya di brief):
- 1 efek tanda tangan (boleh muncul 2–3×) + maksimal 3 efek pendukung lain.
- Rata-rata ≤ 1,5 efek per adegan; adegan payoff boleh 2.
- 1 transisi tanda tangan; total jenis transisi 5–8.
- Tekstur global (grain/halftone/vinyet) dihitung sebagai **satu** efek, dan harus seragam satu video.

**Uji hapus**: pilih 3 efek/gerak secara acak, bayangkan dihapus. Bila video tidak kehilangan makna atau rasa, hapus sungguhan.

## 7. Finishing
| Cek | Lolos bila |
|---|---|
| Color grading | satu grade untuk semua adegan (per adegan hanya untuk alasan cerita: kilas balik, mimpi); kulit tidak oranye/abu; hitam tidak mengambang kecuali gaya retro/analog (`../style/warna-tekstur.md`) |
| Grain | seragam, bergerak (tidak membeku), tidak menutupi teks kecil |
| Tekstur | menyatu dengan gaya (kertas untuk kolase, VHS untuk retro); tidak ditumpuk 3 tekstur |
| Bayangan | potongan punya bayangan searah dengan cahaya latar; tidak ada potongan "melayang" tanpa bayangan kecuali disengaja |
| Motion blur | ada di gerak cepat (perpindahan bermomentum, whip), tidak di gerak lambat |
| Konsistensi | gaya huruf, warna aksen, bunyi UI sama dari awal ke akhir |
| Ekspor | 1080×1920 30 fps H.264, audio AAC; bingkai pertama dan terakhir dilihat; ukuran wajar; nama berkas = judul |

## 8. Laporan QC (format)
```
QC-1 · <judul> · <durasi> dtk · gaya: <gaya utama + kedua>
BLOKIR  0,0–1,2  hook: bingkai 0 latar kosong, subjek baru masuk di 0,9 → mulai adegan dari bingkai subjek sudah ada
PENTING 12,4–18,0 tiga adegan berturut-turut zoom maju → ganti adegan 2 jadi geser kiri, adegan 3 kamera tenang
POLES   22,3     impact 3 bingkai sebelum teks mendarat → geser +0,1 dtk
Anti-AI: efek 6/8 (lolos) · transisi heboh 2 (lolos) · potongan di ketukan 72% (GAGAL → lepas 3 potongan ke kata narasi)
Keputusan: perbaiki BLOKIR + PENTING, rakit, cek, kontak, lalu pratinjau.
```

## Cek cepat
- [ ] Hook terbaca tanpa suara dalam 1 dtk
- [ ] Penonton tahu topik + alasannya peduli dalam 5 dtk
- [ ] Payoff menjawab janji hook dan diberi ruang
- [ ] Tidak ada BLOKIR; PENTING ≤ 3 dan disetujui
- [ ] Anggaran efek dan transisi heboh lolos; ≤ 60% potongan di ketukan
- [ ] Narasi jelas, −14 ±1 LUFS, puncak < 0 dBFS
- [ ] Satu grade, tekstur seragam, bayangan searah
