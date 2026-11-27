# Sampul video: dibuat di Google Flow, rasio mengikuti video, desain mengikuti style

Sejak 28 Nov 2026 (permintaan pengguna): "setelah video jadi sertakan judul/deskripsi dan sampul video. Kalau video potret, sampulnya potret; kalau lanskap, sampulnya lanskap. Desainnya dibuat bagus dan di-generate di Google Flow seperti contoh yang saya kirim; kalau video dibuat di cloud, kirim prompt" + "desain sampul juga menyesuaikan style masing-masing". Menggantikan sampul tata letak `_thumbnail` (sekarang hanya cadangan bila Flow gagal).

## 1. Aturan
- **Rasio = rasio video**: `KONFIG.rasio` 9:16 → satu sampul 9:16 **1080×1920**; 16:9 → satu sampul 16:9 **1280×720**. Tidak membuat rasio lain.
- **Dibuat di Google Flow** (`flow_agent_images`, Nano Banana, 0 kredit, tanpa izin terpisah), 3 varian, unduh `upscaled`. **Di cloud** (tanpa Flow): kirim prompt dari `prompt-sampul.md` di chat. Pengguna membuatnya di Flow/Gemini lalu mengirim gambarnya. Claude merapikannya dengan `sampul.py ambil` + `pilih`.
- **Desain mengikuti style video** (`KONFIG.tema` / resep): latar, bahan huruf judul, palet, dan properti khas diambil dari tabel §3. Kualitas komposisinya selalu setara contoh pengguna (§2).
- **Teks di sampul hanya**: judul sampul 2 baris (2–4 kata per baris, ≤ 22 huruf per baris) + kicker kecil opsional (2–5 kata). Judul sampul ≠ judul video. Isinya kait yang membuat penasaran (mis. video "Kodak Menemukan Kamera Digital, Lalu Kalah Olehnya" → sampul "PENEMUNYA / MALAH BANGKRUT").
- Flow kadang salah eja. **Lihat setiap varian** (`_calon.jpg`), dan pilih hanya yang ejaannya 100% benar. Bila semua salah, buat ulang dengan judul lebih pendek. Bila tetap salah, jalankan cadangan: varian tanpa teks + judul dari mesin `_thumbnail` (`D:\automation\Video AI\_thumbnail\PANDUAN.md`).
- Tanpa logo/merek asli, tanpa wajah orang nyata (tokoh nyata hanya lewat foto berlisensi di video, bukan di sampul AI), tanpa teks kecil acak di kartu UI.

## 2. Resep dari contoh pengguna ("7 Gembok Anti-Maling", 9:16)
| Unsur | Di contoh | Aturan umum |
|---|---|---|
| Subjek utama | HP 3D mengilap di tengah, wajah kartun bercahaya (cemas, setetes keringat) | satu subjek besar di tengah (±40–50% tinggi), benda kunci video; bila cocok diberi ekspresi yang sesuai kait (cemas, kaget, sombong), tidak pernah wajah orang nyata |
| Pendukung | 6–8 kartu kaca UI melayang miring di beberapa kedalaman, gembok, rantai, perisai | 4–8 benda dari isi video + simbol topik, berlapis depan/tengah/belakang, sebagian kabur |
| Gerak/energi | aliran partikel cyan melingkari subjek | satu "arus" yang membawa mata ke subjek (partikel, cahaya, kertas, bara, sesuai style) |
| Judul | "7 GEMBOK" krom perak 3D + "ANTI-MALING" emas 3D, raksasa, sepertiga bawah, ±85% lebar | 2 baris; baris 1 bahan netral, baris 2 (aksen) bahan/warna aksen style; huruf tebal, bevel/glow, terbaca di ukuran feed |
| Kicker | "Android & iPhone • 5 menit" kecil menyala di atas | janji nilai/konteks singkat (platform, tahun, durasi, angka) |
| Kedalaman | rantai kabur di sudut depan, bokeh belakang | selalu ada lapisan depan kabur + latar berbokeh/kabut |
| Palet | navy gelap, cyan listrik, krom, emas | palet style (§3), kontras tinggi antara judul dan latar |
| Yang tidak ditiru | teks kecil di kartu UI terbaca acak ("Kuriel Detecsi…") | kartu UI hanya ikon/toggle/bar, tanpa kata |

Tata letak: **9:16** subjek tengah, judul sepertiga bawah, kicker atas, semua penting di dalam zona aman (6% tepi kosong). **16:9** subjek besar di kanan, judul mengisi 55–60% kiri, sudut kanan bawah bebas (stempel durasi YouTube).

## 3. Style sampul per tema (`python scripts/sampul.py gaya`)
| Tema / resep | Latar | Judul baris 1 / baris aksen | Ciri |
|---|---|---|---|
| `teknologi` (= contoh pengguna) | navy-hitam, bokeh biru, percik emas | krom perak / emas | kartu kaca UI, ikon hologram cyan, arus partikel |
| `kaca-gradien` | studio putih-lavender, lantai kisi abu | arang mengilap / biru listrik kaca | benda krom/kaca, tombol kaca melayang, garis cahaya biru |
| `sinema-kasus` | malam biru-hitam, pantulan basah, cahaya monitor | putih tulang / merah neon | layar data kabur, map kasus, tali merah, grain film |
| `legenda-gelap` | arang, bulan biru vs api jingga, tekstur papan kapur | krem berukir kapur / kuning api | polaroid bertali merah, bara melayang, simbol kapur |
| `piksel-kertas` | diorama kertas zaitun | krem kertas potong 3D / merah di pita | ikon kertas potong, pita merah, detail piksel |
| `panggung-emas` | panggung hijau botol, lampu sorot emas | serif emas raksasa di belakang subjek / emas berkilau | konfeti emas, podium, kuningan |
| `arsip-pop` | halaman iklan majalah merah datar, halftone | putih retro berbayang tebal / kuning mustard bergaris biru | foto hitam-putih dengan satu warna, label sobek biru |
| `panggung-korporat` | panggung gelap, dunia abu, kertas grafik | putih padat (Anton) / jingga di pita | satu benda berwarna kuasa, panah grafik jatuh/naik |
| `diorama-kreator` | dunia mainan voxel di bawah satu sorot | putih tipis / tulisan tangan merah | layar chat biru, kartu krem berangka, miniatur |
| `arsip` | kolase kertas krem, kliping koran, halftone | hitam padat tercetak / merah + stabilo kuning | foto arsip halftone, perangko, cap tanggal |
| `dosir` | ruang investigasi teal gelap, papan gabus | putih tulang bergrit / merah cap | dokumen kasus, kaca pembesar, lubang kunci |
| `pasar` | meja trading hangat, dinding grafik | putih bertepi emas / hijau limau berbayang jingga | grafik hijau naik, label harga, koin |
| `tv` | ruang keluarga retro, pola sinar | putih retro tebal / kuning + merah muda | TV kayu, stiker, garis layar |
| `modern` | kota malam kaca + neon | putih mengilap / kuning berbayang merah | layar HP (ikon saja), pin peta, kartu foto |
| `perang` | medan berdebu, peta tua, asap | stensil putih tulang / stensil merah tua | peta rute, siluet puing, lingkar spidol merah |
| `alam` | lanskap dramatis jam emas | putih / emas hangat | kartu spesimen, sinar matahari, serbuk sari |
| `editorial` | abu terang, lengkungan + garis putus | hitam matte / putih di kotak merah | kartu putih membulat, kotak sorot hitam |
| `kartu` | navy #051D40 berkisi, kartu kertas retro | putih bergaris navy / stiker merah | tokoh 3D seri (Raka) atau benda kunci 3D |
| ikut acuan | ikuti `acuan/gaya-acuan.md` (palet, huruf, benda) lewat `isi.json` → `gaya` | | |

Isi `isi.json` → `gaya` boleh menimpa unsur mana pun (`latar`, `judul1`, `judul2`, `props`, `palet`, …), mis. untuk seri atau acuan pengguna.

## 4. Alur (Tahap 4, sesudah ekspor MP4)
1. Tulis `_kerja/sampul/isi.json` (templatnya dibuat `sampul.py rencana` bila belum ada):
   `{ "judul": ["PENEMUNYA", "MALAH BANGKRUT"], "aksen": 1, "kicker": "Kodak · 1975", "subjek": "<benda kunci video, bahasa Inggris, + ekspresi bila cocok>", "pendukung": ["<4–6 benda dari isi video>"], "tambahan": "<suasana>", "tema": "<tema video>" }`
2. `python -X utf8 scripts/sampul.py rencana <_kerja>` → `_kerja/sampul/flow_sampul.json` (3 varian) + `<folder video>/prompt-sampul.md`.
3. **PC**: `flow_agent_images` dengan `project`, `aspect_ratio`, `scenes` dari `flow_sampul.json` + `download_quality: 'upscaled'`, lalu `flow_wait` sampai selesai. Gambarnya ada di `C:\Users\ASUS\flow-mcp-out\<project>\`. **Cloud**: tempel isi `prompt-sampul.md` di chat (varian 1 cukup), minta pengguna membuatnya di Flow dengan rasio yang sama lalu mengirim hasilnya.
4. `python -X utf8 scripts/sampul.py ambil <_kerja> --dari <folder hasil Flow>` → `calon-N.jpg` + `_calon.jpg`. **Lihat** `_calon.jpg`: ejaan judul, keterbacaan di ukuran feed (kolom kanan), satu titik fokus, tidak ada teks acak/logo/wajah orang nyata, style terasa sama dengan videonya.
5. `python -X utf8 scripts/sampul.py pilih <_kerja> <N>` → `<folder video>/sampul.jpg` (≤ 2 MB, batas thumbnail YouTube).
6. Kirim `sampul.jpg` bersama MP4 + HTML, dan tulis judul + deskripsi di chat (`kemasan.md` §1). `youtube.json` → `"thumbnail": "sampul.jpg"`.

## 5. Cek cepat
- [ ] Rasio sampul = rasio video, ukuran pas (1080×1920 / 1280×720), ≤ 2 MB
- [ ] Ejaan judul + kicker benar huruf demi huruf
- [ ] Judul terbaca di ukuran feed; subjek jelas dalam 1 detik
- [ ] Style sama dengan video (palet, bahan huruf, benda khas)
- [ ] Tidak ada teks kecil acak, logo/merek, wajah orang nyata, tanda air
