# Warna, tekstur, dan finishing

> STYLE · dipakai di langkah 4 (palet), 14 (polish), 15 (QC finishing) · terkait: `gaya-visual.md`, `campur-gaya.md`, `bahasa-earnedits.md`, `../polish/qc.md` §6–§7, `skill-edit-rizky/references/mesin.md` (`grade`, `efek`)

Prinsip inti:
- **Warna membawa suasana sebelum otak membaca apa pun.** Tentukan suasana dulu, baru angka.
- **Satu grade per video.** Ganti grade per adegan hanya bila cerita berpindah dunia (kilas balik, mimpi, "di dalam layar").
- **Tekstur = satu lapisan global, bukan hiasan per adegan.** Tekstur menyatukan foto AI, foto asli, dan grafik kode menjadi satu dunia (fungsi utama), bukan untuk "biar retro".
- **Teks tidak pernah tenggelam oleh tekstur.** Bila tekstur mengurangi keterbacaan, tekstur yang mengalah.
- **Jangan semua video sama**: grade dan tekstur dirotasi per topik dan dicatat di riwayat.

Kunci `grade` mesin Kolase: `tint` (warna rona), `kuat` (kekuatan rona 0–.2), `saturasi` (.45–1.12), `halftone` (titik cetak 0–.16, diam), `grain` (butir 0–.1, bergerak tiap bingkai), `vinyet` (0–.6), `debu` (bintik bergerak 0–.7), `garis` (garis layar 0–.12), `kontras` (0–.22). Per adegan: `grade: {...}` di adegan menimpa global.

## 1. Grading per suasana
| Suasana | Kapan | Kenapa | `grade` (titik awal) | Palet patokan | Hindari |
|---|---|---|---|---|---|
| **Cinematic** | cerita berbobot, tokoh, esai | kontras dalam + highlight terkendali = serius dan mahal | `{ tint: '#e8dcc8', kuat: .06, saturasi: .85, halftone: 0, grain: .05, vinyet: .48, debu: .05, garis: 0, kontras: .16 }` | hitam `#0E0F11`, krem `#F2EEE6`, emas redup `#C8A24A` | hitam pekat yang menelan detail; teal-oranye berlebihan |
| **Editorial** | penjelasan cerdas, opini, gaya majalah | putih bersih + tipografi kuat = jelas dan percaya diri | `{ tint: '#ffffff', kuat: 0, saturasi: .9, halftone: 0, grain: .06, vinyet: .55, debu: .05, garis: 0, kontras: .08 }` (grade `editorial`) | `#F6F6F6`, `#141414`, aksen `#C8202E` | putih ke biru/abu kusam; aksen lebih dari satu |
| **Retro** | arsip 1900–1990, nostalgia | warna pudar + butir = jarak waktu | `{ tint: '#e9c58c', kuat: .2, saturasi: .82, halftone: .16, grain: .07, vinyet: .42, debu: .5, garis: 0, kontras: .12 }` (grade `arsip`) | krem `#ECE2C8`, tinta `#1B1712`, merah `#D7261E` | sepia total; foto modern tanpa disesuaikan |
| **Dark Tech** | AI, siber, data | hitam grafit + satu sinyal neon = presisi dan bahaya | `{ tint: '#9fb6d8', kuat: .08, saturasi: .8, halftone: 0, grain: .04, vinyet: .52, debu: .05, garis: .04, kontras: .18 }` | `#07080A`, `#E8EEF4`, `#38E1FF` | neon di semua tepi; biru-ungu generik |
| **Documentary** | berita, sains, kesehatan | warna alami = tidak dimanipulasi | `{ tint: '#ffffff', kuat: 0, saturasi: .95, halftone: 0, grain: .03, vinyet: .25, debu: 0, garis: 0, kontras: .08 }` | warna asli foto, panel `#111`, label `#FFD23F` | grade dramatis yang mengubah makna data |
| **Misteri/kasus** | kriminal, konspirasi | teal gelap + kontras = dingin dan menyelidik | grade `dosir` `{ tint: '#7fa6a3', kuat: .16, saturasi: .55, halftone: .1, grain: .08, vinyet: .56, debu: .45, garis: 0, kontras: .2 }` | `#0F1A1C`, `#F2ECDC`, `#C1121F` | hijau-teal ke kulit (wajah jadi mayat) |
| **Hangat/alam** | alam, kuliner, keluarga | rona emas = dekat dan hidup | grade `alam` / `hangat` | `#F3D9A4`, `#2B241C`, `#6B8F4E` | jingga berlebihan (kulit oranye) |
| **Kelam/tragedi** | perang, bencana | saturasi rendah + debu = berat, hormat | grade `perang` `{ tint: '#b9a98a', kuat: .18, saturasi: .45, halftone: .12, grain: .1, vinyet: .52, debu: .7, garis: 0, kontras: .22 }` | `#2A2620`, `#EBE5D3`, `#B3261E` | merah darah untuk dramatisasi korban |
| **Ceria/pop** | budaya pop, tips ringan | saturasi tinggi + kontras bersih = energik | grade `modern` `{ tint: '#ffffff', kuat: 0, saturasi: 1.12, halftone: 0, grain: .04, vinyet: .34, debu: .06, garis: 0, kontras: .17 }` | `#111`, `#FFF`, `#FFE600` | semua warna jenuh sekaligus |

**Cara**: mulai dari baris tabel → tempel di `KONFIG.grade` → `kontak` → cek tiga hal: kulit wajar, hitam tidak mengambang (kecuali retro/analog), aksen masih menonjol. Ubah satu kunci per putaran, ±.02–.04.

## 2. Retro / analog
Fungsi bersama: memberi **jarak waktu** dan menyatukan aset dari sumber berbeda. Pakai bila cerita memang tentang masa lalu atau rekaman lama.
| Tekstur | Kapan | Kenapa | Cara (angka) | Hindari | Mesin Kolase |
|---|---|---|---|---|---|
| Tekstur VHS | kasus 80–2000an, rekaman rumahan | penonton langsung membaca "rekaman lama" | garis layar 10–14%, saturasi .8–.9, rona magenta tipis, ketajaman turun | menutupi teks; di video data modern | `grade.garis: .12`, `tint: '#d6c3d9'` |
| Film grain | hampir semua gaya selain minimal/korporat | butir menyatukan foto AI + asli, menyembunyikan "terlalu mulus" | .03 (bersih) – .06 (sinema) – .09 (analog/VHS) | .1+ di layar HP (terlihat kotor) | `grade.grain` (bergerak tiap bingkai) |
| Debu | arsip, film, perang | permukaan fisik | .1–.5; .7 hanya untuk tragedi berdebu | debu besar di atas wajah | `grade.debu`; `efek: partikel gaya 'debu'` untuk debu melayang |
| Goresan | film tua, kilas balik | cacat seluloid | 1–2 garis vertikal tipis, muncul ≤ 0,2 dtk | goresan terus-menerus | *Celah mesin* (akali: `kustom` garis tipis acak tiap 1–2 dtk, `alfa` .3, `cek: false`) |
| Chromatic aberration | VHS, glitch, lensa murah | tepi warna meleset = "analog/rusak" | 2–4 px merah/cyan, hanya di tepi | CA di semua bingkai sampai teks berbayang | *Celah mesin* (akali: `glitch` 0,3 dtk; untuk statis: duplikat teks/gambar bergeser 3 px `alfa` .5) |
| Distorsi analog | transisi VHS, kenangan rusak | gambar "ditarik" pita | 0,2–0,4 dtk di sambungan | sepanjang adegan | `masuk: 'glitch'`, `efek: glitch` |
| Light leak | pembuka, kenangan, "dulu…" | cahaya bocor = hangat, film | 1–1,4 dtk, kuat .5–.75, dari tepi | di setiap adegan | `efek: { jenis: 'cahaya', dari: 'kiri', kuat: .6, lama: 1.4 }` |
| Kedip halus | film, proyektor | kecerahan tidak stabil = mekanis | ±3–5% kecerahan, tidak teratur | kedip kuat (lelah mata, risiko fotosensitif) | *Celah mesin* (akali: `efek: gelap` kuat .04 sangat singkat di 2–3 titik) |
| Derau pita | pembuka VHS, jeda babak | suara + gambar "pita diputar" | 0,3–0,6 dtk di detik 0 | di bawah narasi | SFX berkas desis; gambar: `kustom` pita derau atau klip derau `urutan` |
| Tepi tidak sempurna | foto cetak, polaroid, film | bukan potongan digital | tepi sedikit membulat/aus, bayangan lembut | potongan bertepi tajam sempurna | `benda: kartu`, `bayangan`, potongan Flow dengan margin |

## 3. Grunge
Fungsi: rasa **dibuat tangan, kasar, jujur**. Cocok untuk kisah perlawanan, tekanan, budaya jalanan. Tidak cocok untuk merek mewah atau kesehatan.
| Tekstur | Kapan | Kenapa | Cara | Hindari | Mesin Kolase |
|---|---|---|---|---|---|
| Tekstur kertas | kolase, arsip, grunge | permukaan fisik yang bisa disentuh | latar kertas, `tua` .5–.8 | kertas sebagai latar setiap adegan | `latar: { pola: 'kertas', tua: .7 }` |
| Tepi kasar/sobek | label, potongan, panel | tidak digital, buatan tangan | 1 label sobek per adegan maks | semua kotak bertepi sobek | potongan Flow "torn paper label" berlatar hijau; *Celah mesin* untuk transisi sobek |
| Tipografi distressed | judul tekanan, kata marah | huruf "tercetak rusak" = kasar | 1 kata per adegan | paragraf distressed tak terbaca | *Celah mesin* (akali: teks `padat` + lapisan `kustom` titik putih acak di atasnya, `campur: 'multiply'`) |
| Tekstur tinta | cap, stempel | bukti resmi/kasar | cap 1–2 per video | cap di semua kata | `benda: cap`, `masuk: 'cap'` |
| Overlay kotor | puncak tekanan | dunia "kotor" | `grade.debu` .5 + vinyet .5 | overlay noda besar acak | `grade` |
| Efek fotokopi | poster, zine, propaganda | kontras keras + halftone = salinan murah | `kontras` .22–.24 + `halftone` .14–.16 + saturasi .6–.7 | wajah menjadi hitam pekat | `grade`; *Celah mesin* ambang hitam-putih penuh (akali: `hitamPutih: true` + kontras tinggi) |
| Displacement | transisi kasar, "dunia retak" | gambar bergeser seperti dicetak ulang | 0,2–0,3 dtk | displacement terus-menerus | *Celah mesin* (akali: `glitch` lemah `kuat: .5`) |
| Ketidaksempurnaan organik | semua gaya tangan | miring 1–3°, posisi tidak simetris | `putar` −3…3 pada kartu/label | semua miring ke arah sama | `putar`, `rig: 'goyang'` lemah |

## 4. Finishing sinematik
Fungsi: menyatukan semua lapisan dan memberi **kedalaman**. Paling tidak kelihatan bila dikerjakan benar.
| Unsur | Kapan | Kenapa | Cara (angka) | Hindari | Mesin Kolase |
|---|---|---|---|---|---|
| Film grain | selalu (kecuali minimal/korporat) | menyatukan sumber | .03–.06 | membeku (grain diam = terlihat ditempel) | `grade.grain` sudah bergerak |
| Vinyet | hampir selalu | mengarahkan mata ke tengah | .25 (dokumenter) – .45 (sinema) – .6 (psikologis) | lingkaran hitam terlihat jelas | `grade.vinyet` |
| Bloom halus | sumber cahaya nyata (lampu, jendela, layar) | cahaya terasa "bernapas" | hanya highlight > ±85% kecerahan, 1 sumber per adegan | glow di teks dan semua tepi | *Celah mesin* (akali: `efek: berkas` kuat .2–.3 atau `cahaya` lemah di satu titik) |
| Distorsi lensa | dorong cepat, whip, POV | lensa nyata melengkung di tepi | ±2–4% di tepi saat gerak cepat saja | distorsi permanen | *Celah mesin* (akali: momentum `dorong`/`sentak` sudah memberi blur + skala z) |
| Bayangan realistis | setiap potongan di atas latar | potongan tanpa bayangan = stiker melayang | arah bayangan sama dengan cahaya latar; lembut, offset 12–24 px | bayangan beda arah antar-potongan | `bayangan: .3–.6`; `bayangKartu` otomatis pada benda |
| Kedalaman atmosfer | lanskap, ruang besar | jauh = lebih pudar + lebih biru | kabut tipis di 55–70% tinggi | kabut menutupi subjek | `efek: { jenis: 'kabut', y: .62, kuat: .4 }`, lapisan `z` kecil + `blur` |
| Color grading | selalu | satu dunia warna | satu `KONFIG.grade` | grade per adegan tanpa alasan | §1 |
| Integrasi tekstur | gambar AI + foto asli + grafik kode | semua terlihat difoto dengan kamera yang sama | grain + vinyet + rona sama untuk semua; foto asli `hitamPutih` bila tema arsip | grafik kode bersih sempurna di atas foto bertekstur | grade global berlaku ke semua lapisan |
| Motion blur terkendali | gerak cepat | mata membaca kecepatan | otomatis di perpindahan bermomentum; `blurGerak: false` untuk teks yang harus tajam | blur di gerak lambat | bawaan mesin (sampai 28 sampel) |

## 5. Anggaran tekstur
- **Satu lapisan tekstur global** per video (mis. "grain .05 + vinyet .45"), dihitung **satu efek** dalam anggaran `../polish/qc.md` §6.
- **Maksimal 2 tekstur ditumpuk** di satu bingkai (mis. kertas + grain). Tiga atau lebih (kertas + VHS + debu + halftone) = kotor, terlihat seperti filter aplikasi.
- **Tekstur tidak boleh menenggelamkan teks penting**: di mesin Kolase grade berlaku ke seluruh bingkai (termasuk teks), jadi jaga `halftone` ≤ .1 dan `garis` ≤ .1 saat ada teks kecil (< 50 px).
- **Tekstur sesaat** (light leak, glitch, film terbakar) bukan tekstur global; masuk anggaran efek dan maksimal 2–3× per video.
- **Uji keterbacaan**: lihat `kontak` di ukuran 25% (setara layar HP dilihat sekilas). Bila teks kecil hilang, turunkan tekstur dulu, baru naikkan ukuran teks.

## 6. Jangan membuat semua video terlihat sama
1. Awal Tahap 2: `riwayat.py lihat`. Jangan memakai suasana grade yang sama dengan video terakhir kecuali seri/acuan.
2. Bila topik menuntut suasana yang sama (dua video teknologi berturut-turut), ubah **dua** hal: rona (`tint`) + satu tekstur (mis. Dark Tech dingin → Dark Tech dengan garis layar dan aksen hijau terminal).
3. Satu seri boleh satu grade tetap; justru itu identitasnya. Tulis di `aset/<seri>/README.md`.
4. Catat grade akhir (`tint`, `saturasi`, `kontras`, tekstur utama) di riwayat bersama tema.
5. Rotasi kasar per minggu: terang–gelap–hangat–dingin–kertas. Feed yang selang-seling terlihat dikurasi, bukan dicetak.

## Cek cepat
- [ ] Satu grade untuk seluruh video (kecuali perpindahan dunia yang disengaja)
- [ ] Kulit wajar, hitam tidak mengambang (kecuali retro/analog), aksen menonjol
- [ ] Satu tekstur global; ≤ 2 tekstur ditumpuk; teks kecil tetap terbaca di 25%
- [ ] Bayangan potongan searah cahaya latar
- [ ] Bloom/light leak hanya di sumber cahaya nyata, ≤ 3 kali
- [ ] Grade berbeda dari video terakhir dan tercatat di riwayat

## Celah mesin
- Chromatic aberration per bingkai (tetap, bukan glitch sesaat): belum ada (akali: duplikat lapisan bergeser 2–3 px berwarna `alfa` .5; usul `grade.ca` px).
- Pita tracking VHS bergulir: belum ada (akali: `kustom` pita derau tipis bergeser vertikal, `cek: false`).
- Goresan film: belum ada (akali: `kustom` garis vertikal acak berumur 2–4 bingkai).
- Bloom/halation (sorot terang melebar kemerahan): belum ada (akali: `berkas`/`cahaya` lemah; usul `grade.bloom` dengan ambang .85).
- Distorsi lensa (barrel) saat gerak cepat: belum ada (akali: momentum + blur gerak bawaan).
- Ambang fotokopi hitam-putih penuh dan displacement map: belum ada (akali: `hitamPutih` + kontras .24; `glitch` lemah).
- Kedip film: belum ada (akali: `efek: gelap` sangat singkat; usul `grade.kedip`).

## Teknik modern
- **Halation**: highlight melebar merah-oranye seperti film fotokimia. Manfaat: rasa sinema tanpa filter murahan. Kapan: Analog Film, Cinematic Documentary, malam berlampu. Cara saat ini: `cahaya` lemah warna `#ff6a3d` di sumber cahaya; nanti `grade.bloom`.
- **Grain per seri** sebagai identitas: satu nilai grain + rona tetap untuk satu seri, berbeda antar-seri. Cara: simpan di `aset/<seri>/README.md` dan tempel ke `KONFIG.grade`.
- **Tekstur bertingkat sesuai babak**: tekstur naik pelan saat konflik naik (grain .03 → .06 → .09), kembali bersih di payoff. Manfaat: emosi lewat permukaan gambar. Cara: `grade` per adegan, maksimal 3 langkah.
