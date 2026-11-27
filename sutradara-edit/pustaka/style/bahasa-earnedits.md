# Bahasa visual hasil belajar dari @earn.edits, jadi gaya Rizky sendiri

> STYLE · dipakai di langkah 4 (gaya), 6–14 (storyboard sampai polish) · terkait: `gaya-visual.md`, `resep/`, `warna-tekstur.md`, `../motion/transisi.md`, `../motion/kolase-editorial.md`, `../type/tipografi-kinetik.md`, `skill-edit-rizky/references/gaya.md` (implementasi mesin)

Yang dipelajari hanya **prinsip** (komposisi, ritme, gerak, tekstur, tipografi, bunyi). Nama, logo, kalimat iklan, kartu penutup iklan, musik, footage, gambar, dan file proyek mereka **tidak pernah** dipakai. Akun itu menjual templat After Effects; reel mereka adalah demo templat "retro-style motion piece" 20–47 dtk + iklan di akhir.

Bahan bedah:
- 18 Nov 2026: laporan + 26 lembar bingkai (`D:\automation\Video AI\Video Refrensi\earn.edits\`), reel ponsel IBM 1994, sidang mayat paus 897, uang tunai investor, roket-mobil, tutorial, video wabah. Implementasi di `skill-edit-rizky/references/gaya.md` §4–§4a.
- 27 Nov 2026: grid profil publik + 7 reel (`…\earn.edits\reel-2026-11-27\bedah\<id>\`): `DgKaZmro7dQ` kebocoran game (VHS, 45,9 dtk), `DfIJjwfuKGL` asal-usul Halloween (41,9 dtk), `DfEv7DuOgYT` "Editing Alone" piksel-kertas (39,4 dtk), `DfM7ZyruNRU` pengumuman kompetisi (4:3 mendatar, 23,6 dtk), `Df7Zz75uOGL` mobil kopi (9:16, 41,8 dtk), `DgC40B3oLXu` SaaS (16:9, 22,6 dtk), `DfjnS4Oux4X` plugin gradien (16:9, 20,7 dtk), `DgH9MT_ICph` naik-turun produsen ponsel (9:16, 47,5 dtk). Resep per reel: `resep/README.md`.

## 1. Temuan terukur (bukan kesan)
| Ukuran | Hasil | Artinya buat Rizky |
|---|---|---|
| Potongan yang jatuh di ketukan musik (`ketukan.py --potongan`, toleransi ±2,5 bingkai) | 8 reel terukur. Reel bercerita **0–25%** (kebocoran game 14%, Halloween 0%, Editing Alone 25%, mobil kopi 18%, produsen ponsel 10%); pengumuman/promosi 23–56% (kompetisi 27%, SaaS 23%, plugin gradien 56%) | potongan cerita mengikuti **kata narasi**, bukan beat; hanya promosi singkat yang boleh lebih ikut ketukan. Musik adalah alas suasana. Jangan memaksa semua potongan di ketukan (`../audio/musik.md`) |
| BPM musik | 89–146 | reel cerita ±90 BPM (tenang, memberi ruang narasi); reel ber-tempo tinggi tetap dipotong ikut kata |
| Rata-rata bidikan | reel cerita ±3 dtk (39–46 dtk / 12–15 potongan); reel promo ±1,5 dtk | tiap bidikan ±3 dtk tapi **di dalamnya selalu ada yang berubah** tiap 0,5–1,5 dtk (kamera, teks baru, benda masuk) |
| Gambar | ±90% gambar diam realistis yang dipotong jadi 3–5 lapisan | kekuatan ada di lapisan + kamera, bukan di video AI mahal |
| Teks | 1–5 kata per bingkai; caption kata-per-kata kecil hanya di sebagian reel | teks = desain, bukan subtitle |

## 2. Cinematic Editorial
| Prinsip | Bukti (reel · detik) | Cara Rizky memakainya | Jangan disalin |
|---|---|---|---|
| **Komposisi dramatis berlapis**: subjek nyata di ruang yang dalam, teks diletakkan di ruang kosong dan sering di **belakang** subjek | kompetisi `DfM7ZyruNRU` 12,0–13,5 (huruf serif merah raksasa di belakang tokoh bertopeng), 15,5–19,5 (kata besar di belakang patung) | urutan `lapis` latar → teks → potongan; untuk topik Indonesia: kata besar di belakang tokoh/benda lokal (becak, gedung, pejabat dari belakang) | tokoh bertopeng mereka, kata-kata mereka |
| **Judul editorial campur huruf**: serif miring + display tebal + satu kata warna | grid profil (judul "Fear … Painting"), Carpuccino `Df7Zz75uOGL` 1,0–2,0 (judul miring, satu kata merah) | `serif` di atas `tebal`, satu `*kata*` aksen; maksimal 2 keluarga | susunan judul mereka |
| **Gambar di dalam kalimat**: foto kecil bersudut bulat di sela kata | plugin gradien `DfjnS4Oux4X` 9,0–10,5 | kalimat definisi di video teknologi/produk: "aplikasi [ikon] yang…"; `kustom` atau dua teks + potongan | tampilan plugin mereka |
| **Kata memisah memberi ruang benda** | SaaS `DgC40B3oLXu` 0–1,5 ("Every … great video" terbelah oleh kotak), gradien 0–1,5 | hook: kalimat terbelah, benda kunci masuk di tengah | — |
| **Hierarki kuat + ruang kosong** | SaaS 13,5–15,5 (satu tombol di kanvas putih), Nokia (grid: dua kata besar + produk kecil) | satu unsur utama per bingkai; latar polos/gradasi | logo dan tombol mereka |
| **Kamera terkendali**: satu gerak per bidikan, gerak cepat hanya di sambungan | semua reel cerita | `dorong` pelan dalam adegan, momentum hanya di perpindahan (`../cinematic/kamera.md`) | — |

## 3. Retro / Analog
| Prinsip | Bukti | Cara Rizky | Jangan disalin |
|---|---|---|---|
| **Pembuka derau pita** 0,3–0,5 dtk sebelum gambar pertama | kebocoran game `DgKaZmro7dQ` 0,0 (garis vertikal VHS biru) | pembuka seri "arsip kasus": derau 0,3 dtk + desis pita, lalu bingkai hook (ingat: hook tetap harus terbaca di detik 1) | — |
| **Huruf merah menyala** untuk kata bahaya di atas gambar dingin | `DgKaZmro7dQ` 0,5 ("One Teenager" kecil merah di fasad gedung), 1,5–2,0 (dua baris: merah + putih) | aksen merah hanya untuk kata bahaya/pelaku; kata lain putih tipis | kata dan nama kasus mereka |
| **Layar di dalam adegan sebagai alat cerita** (progres "accessing…", forum, grid 90 klip) | `DgKaZmro7dQ` 2,5–4,5, 25,0–31,0 | proses digital dijelaskan di layar benda (`benda: tv`/`hp`/`kustom`), angka progres naik sesuai narasi | antarmuka merek nyata |
| **Adegan menjadi isi TV tabung** di penutup | `DgKaZmro7dQ` 40,5–42,5 (adegan awal diputar di TV CRT di meja) | penutup loop: adegan pembuka muncul di layar TV/HP lalu kamera mundur (`bingkai`, `../motion/transisi.md`) | kartu iklan sesudahnya |
| **Pergantian musim di komposisi yang sama** | Halloween `DfIJjwfuKGL` 11,0 → 12,0 (lembah hijau → bersalju, sudut sama) | "waktu berlalu" tanpa teks: pelat Flow sama, dua versi (musim/zaman/siang-malam), `cocok`/`lebur` 0,6 dtk | — |
| **Kartu "beberapa waktu kemudian"** berhuruf padat abu di atas tekstur gelap | `DgKaZmro7dQ` 35–37 | kartu jeda kronologi bertekstur; teks Indonesia sendiri ("TIGA HARI KEMUDIAN") | kalimat mereka |

## 4. Grunge
| Prinsip | Bukti | Cara Rizky | Jangan disalin |
|---|---|---|---|
| **Huruf display rusak/bergelombang** untuk judul bertema | Halloween `DfIJjwfuKGL` 0,5–3,0 (judul kuning bergelombang, masuk dengan blur zoom) | judul hook bertema (horor, panas, banjir) dibuat sebagai **gambar** Flow huruf bertekstur atau `kustom`; teks lain tetap mesin | bentuk huruf mereka |
| **Kata disensor** satu huruf (`DE*D`) | `DfIJjwfuKGL` 5,0–6,5 | untuk kata sensitif (mati, bunuh, utang) di hook: rasa tabu + menghindari filter; satu kali per video | — |
| **Papan penyelidikan**: polaroid disematkan + benang merah + teks berjalan | `DfIJjwfuKGL` 8,5–10,0; `DgKaZmro7dQ` 6,5–8,5 (kartu identitas + garis penghubung merah) | kronologi dan hubungan sebab-akibat: kartu foto disematkan, garis `coret: 'garis'`, kamera bergeser menyusuri papan | foto/tokoh mereka |
| **Label kertas sobek** pada benda | Carpuccino `Df7Zz75uOGL` 7,5–10,0 (label biru sobek nama mobil) | nama benda/tokoh/tempat di label sobek bertepi putih (`tepi: true`), miring 2–4° | — |
| **Papan tulis/kapur + kotak tangan** untuk angka sejarah | `DfIJjwfuKGL` 7,0–8,0 ("2.000 TAHUN LALU" merah + kotak putih tangan) | angka zaman di papan gelap, kotak `coret: 'kotak'` warna putih | — |
| **Tangan kertas potong** (cutout 2D) di dunia piksel | Editing Alone `DfEv7DuOgYT` 0–1,0, 3,5–5,0 | tokoh/tangan potongan kertas dengan lengan merah sebagai "pelaku" seri; `rig: 'tekuk'` | tangan dan karakter mereka |

## 5. Motion graphics
| Prinsip | Bukti | Cara Rizky | Jangan disalin |
|---|---|---|---|
| **Transisi topeng bentuk** (siluet tumbuh menutup layar lalu menjadi adegan berbentuk sama) | `DgKaZmro7dQ` 4,5–5,5 (siluet tudung putih → kerumunan bertudung) | motivasi bentuk: siluet benda kunci (peci, helm, payung) membesar → adegan penuh benda itu. *Celah mesin*: topeng bentuk bebas (akali: `bingkai` bentuk `bulat`/`kunci`/`peti`, atau potongan putih `terbang` + potong keras) | — |
| **Transisi cair** (lingkaran warna benda → pusaran cairan) | Carpuccino 13,0–14,5 (bulatan kopi → pusaran kopi) | perpindahan ke "bahan" topik (kopi, minyak, air, darah dengan hati-hati); *Celah mesin* liquid (akali: klip Flow pusaran 2 dtk sebagai `urutan` + teks di atasnya) | — |
| **Lingkaran terbelah dua dunia** | `DfIJjwfuKGL` 14–17 (satu lingkaran: kiri dunia hidup, kanan dunia mati) | metafora "batas/dua sisi" (`../visual/metafora.md`): dua gambar dalam satu `bingkai` bulat, `panel` dibagi | — |
| **Metafora benda yang harfiah** | Editing Alone 8–10 (editor kecil di dalam sungkup kaca = terisolasi), 11–13,5 (jendela galat → centang SELESAI), 21,5 (bar loading 97%) | ungkapan Indonesia diambil harfiah ("kerja sampai tipes", "otak ngebul"); bank `../visual/metafora.md` | gambar sungkup mereka |
| **Peta rute + bar progres** di atas gambar dari atas | Carpuccino 20–23,5 (mobil dari atas + bar 0–370 km) | perjalanan/jarak/proses bertahap: `benda: grafik` bentuk `progres` di atas pelat top-down | — |
| **Caption kata-per-kata kecil** (mono atau pil) di tengah-bawah | `DgKaZmro7dQ` 12–31 (mono kecil), `DfIJjwfuKGL` 10–21 dan Carpuccino 15–23 (pil gelap kecil) | **tidak** dipakai bawaan (preferensi Rizky: tanpa subtitle bawah). Bila diminta: `subtitle: { gaya: 'pil', maksKata: 1 }` kecil | — |
| **Siluet peta panas (thermal)** | kompetisi 0–1,5 | hook tokoh anonim/"siapa dia?": siluet gradien panas dari Flow | — |
| **Teks mengikuti benda** (huruf melingkari benda 3D) | Carpuccino 4,0–4,5 (teks mengelilingi mesin kopi) | *Celah mesin* (akali: dua lapisan teks di depan + belakang potongan dengan `putar` berbeda) | — |

## 6. Cinematic finishing
| Prinsip | Bukti | Cara Rizky | Jangan disalin |
|---|---|---|---|
| **Satu rona per video** (biru malam, oranye api, hijau zaitun) | GTA biru gelap; Halloween oranye-merah; Editing Alone hijau zaitun + merah | satu `grade` + dua aksen (`warna-tekstur.md` §1) | palet persis mereka per reel |
| **Warna selektif**: dunia hitam-putih, benda utama berwarna | Carpuccino 0,5–2,0 (jalan hitam-putih, mobil berwarna) | benda kunci berwarna di atas pelat `hitamPutih: true` | — |
| **Cahaya radial di belakang kepala** untuk menunjuk tokoh | `DgKaZmro7dQ` 15,0 | `efek: sorot` atau `kilau` lemah di belakang subjek | — |
| **Tekstur menyatukan foto AI dan UI** | semua reel: grain halus + vinyet | `grade.grain` .04–.07 untuk semua lapisan | — |
| **Bayangan dan kedalaman** pada setiap potongan | kartu polaroid, mesin kopi, sungkup kaca | `bayangan: .3–.6`, `z` berbeda | — |

## 7. Yang sengaja tidak diikuti
- Kartu iklan penutup, nama situs, ajakan "comment … to get it", dan kalimat promosi mereka.
- Logo merek nyata yang mereka tampilkan (konsol, TV streaming, ponsel) dan wajah orang nyata yang dibuat AI. Rizky: wajah tokoh nyata hanya dari foto berlisensi; merek hanya disebut, tidak digambar.
- Tokoh, karakter piksel, tangan kertas, desain kartu, dan gambar mereka. Semua aset Rizky dibuat ulang dari prompt sendiri.
- Musik mereka; Rizky memakai Epidemic/perpustakaan sendiri.

## 8. Tanda tangan Rizky (orisinal, diturunkan dari prinsip di atas)
1. **Pasangan aksen "bata + kunyit"**: merah bata `#C8402F` untuk bahaya/pelaku dan kuning kunyit `#E8B53A` untuk angka/temuan, di atas latar gelap hangat `#16130F` atau kertas `#EFE6D2`. Berbeda dari merah-putih yang umum dipakai akun acuan, dan berakar dari warna benda Indonesia.
2. **Transisi "sobek kalender"**: lembar kalender dinding harian disobek, adegan berikut ada di balik lembaran. Dipakai untuk lompatan waktu (maks 2× per video). Mesin saat ini: `tutup` arah atas + potongan lembar kalender Flow yang `keluar: { gaya: 'jatuh' }`; usul `masuk: 'sobek'`.
3. **Benda bukti berulang: map arsip cokelat** berlabel tulisan tangan. Setiap fakta penting "keluar" dari map (kartu foto, dokumen, struk), dan video ditutup dengan map yang tertutup = ujung loop. Mesin: potongan Flow map + `cocok` antar-adegan.
4. **Pasangan huruf**: Anton (`padat`) untuk kata besar + Georgia miring (`serif`/`elegan`) untuk bisikan/pengantar + Courier (`mesin`) untuk tanggal dan sumber. Tidak lebih.
5. **Palet bunyi khas**: ketuk meja kayu (masuk benda), gesek kertas HVS (kartu), klik pulpen (sorot), sub-boom pendek (angka kunci), dan **tanda bunyi 3 nada** bernuansa saron (sintesis `ding` dengan `nada` berbeda, mis. 1,0 · 1,2 · 1,5 × nada dasar) di payoff. Konsisten semua video, jadi penonton mengenali payoff dari telinga.
6. **Kata di belakang benda Indonesia**: satu momen per video, kata kunci raksasa diletakkan di belakang benda/tokoh lokal (gerobak, motor, gedung) — kedalaman instan, sekaligus menandai "ini Indonesia".
7. **Hook tanpa suara 1 dtk**: bingkai 0 selalu sudah berisi benda + kata bermakna (tidak pernah latar kosong), karena banyak penonton memutar tanpa suara.

Semua tanda tangan dicatat di brief (`../../templat/brief.md` baris 12–16) dan dipakai konsisten lintas seri; boleh diganti per seri, tetapi tidak per video.

## Cek cepat
- [ ] Tidak ada nama, logo, kalimat, kartu iklan, musik, atau aset akun acuan di video
- [ ] Potongan mengikuti kata narasi; ≤ 60% di ketukan musik
- [ ] Tiap bidikan ±2–3 dtk dengan perubahan internal tiap 0,5–1,5 dtk
- [ ] Minimal satu teknik lapisan khas (teks di belakang subjek, adegan menjadi isi layar, benda bertahan saat dunia berganti)
- [ ] Minimal 3 dari 7 tanda tangan Rizky muncul
- [ ] Wajah tokoh nyata hanya dari foto berlisensi

## Celah mesin
- Topeng bentuk bebas (siluet benda tumbuh menjadi adegan): baru ada bentuk `kotak`/`bulat`/`peti`/`kunci` di `bingkai`; usul `bingkai.bentuk: 'gambar'` memakai alfa potongan sebagai topeng.
- Transisi cair (pusaran): belum ada; akali klip Flow sebagai `urutan`.
- Teks melingkari benda 3D: belum ada; akali dua lapisan teks depan/belakang.
- Perpindahan sobek kalender (`masuk: 'sobek'`): belum ada; akali `tutup` + potongan lembar yang jatuh.
- Caption kata-per-kata kecil gaya mono: subtitle pil ada, gaya mono belum (akali: `subtitle` + `gayaTeks` khusus bila mesin mengizinkan, atau teks `mesin` `ikut: true` satu kata).

## Teknik modern
- **Lapisan + kamera di atas gambar diam** sebagai pengganti video AI mahal: manfaat = murah, konsisten, cepat dirender; kapan = 90% adegan; cara = Flow pelat + potongan latar hijau + mesin Kolase.
- **Musik sebagai alas, potongan ikut kata**: manfaat = narasi terasa dipimpin cerita, bukan klip musik; kapan = semua video bernarasi; cara = `ketukan.py --kata` untuk menaruh hantaman hanya di sela narasi.
- **Penutup loop lewat layar** (adegan awal diputar di TV/HP di adegan terakhir): manfaat = tonton ulang; cara = `bingkai` + `../short-form/short-form.md` §Loop.
