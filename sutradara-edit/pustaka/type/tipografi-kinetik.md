# Tipografi Kinetik — teks sebagai bagian dari cerita, bukan subtitle

> Kategori **TYPE** · dipakai di langkah 9 (juga 6 storyboard, 14 polish) · terkait: `../motion/prinsip-animasi.md`, `../audio/musik.md`, `../visual/komposisi.md`, `../style/gaya-visual.md`, `../short-form/short-form.md`

Prinsip inti:
1. **Teks adalah aktor di bingkai.** Tampilkan hanya kata yang membawa makna (pembalik, angka, nama, benda kunci, vonis), bukan seluruh kalimat narasi.
2. **Satu bingkai, satu gagasan teks; satu baris, maksimal satu kata aksen.** Mata harus tahu kata mana yang dibaca duluan.
3. **Gerak teks mengikuti arti kata.** "Runtuh" jatuh, "pesan" diketik, "luas" melebar, "hilang" memudar. Gerak tanpa arti = hiasan.
4. **Terbaca dulu, indah kemudian.** Ukuran, kontras, dan lama tampil diperiksa sebelum gaya.
5. **Sistem huruf dikunci per video** (maks 2 keluarga + 1 aksen). Konsistensi = identitas.

---

## 1. Sistem huruf (kunci sebelum storyboard)

### 1.1 Pasangan keluarga huruf (maks 2 keluarga + 1 aksen)
| Pasangan | Rasa | Di mesin Kolase |
|---|---|---|
| Display grotesk tebal + sans netral | modern, tegas, informatif | `judul` (Archivo Black) + `label`/`tebal` (Inter) |
| Kondensasi tinggi + sans | berita, angka, urgensi | `padat` (Anton) + `label` |
| Serif miring kecil + sans tebal besar | editorial, cerdas, tenang | `serif` di atas `tebal`, kata penting di `sorot` |
| Serif miring besar + sans kecil | sinematik, elegan, berat | `elegan` + `label` |
| Mesin ketik + display | arsip, dokumen, bukti | `mesin`/`kutip` + `judul`; tanggal `tahun` |
| Tulisan tangan **hanya aksen** | personal, coretan, catatan | `tangan` (≤ 1 frasa per adegan) |

Aksen = **satu** warna dari palet tema (`*kata*`), atau satu gaya kontras (kotak `sorot`, `stiker`). Bukan keduanya di semua tempat.

### 1.2 Hierarki ukuran (bingkai 1080×1920)
| Tingkat | Ukuran (px) | Isi | Di mesin |
|---|---|---|---|
| Hero / oversized | 160–320 (1 kata/angka) · 110–150 (2–3 kata) | angka kunci, kata pembalik, vonis | `padat` `ukuran: 200–260`, atau `^kata^` (1,5×, ubah lewat `besar`) |
| Judul | 88–120 | frasa kunci 2–5 kata | `judul` 92 · `tebal` 104 · `elegan` 96 · `padat` 120 |
| Pengantar | 46–64 | konteks kecil di atas judul ("Tahun 1995,") | `serif` 50 · `kutip` 52 |
| Label | 36–48, kapital | tempat, tahun, sumber, nama | `label` 44 · `stiker` 74 (hanya untuk yang mendesak) |
| Kredit / caption | 30–40 (**minimal 28**) | kredit foto, "Sumber: …" | `label` `ukuran: 32` |

Di bawah 28 px tidak terbaca di HP. Selisih antar-tingkat minimal 1,5× supaya hierarki terlihat, bukan sekadar "sedikit lebih besar".

### 1.3 Panjang baris, jarak baris, tracking
- **Panjang baris**: hero 1–3 kata (≤ 14 karakter) · judul ≤ 18–22 karakter, maks 3 baris · pengantar ≤ 30 karakter · total di layar sekaligus ≤ 8–10 kata. Di mesin: `lebar` (bawaan 84% lebar layar) mengatur bungkus; untuk hero pakai `lebar: 700–860`, dan pecah baris manual dengan `\n` di batas makna (jangan memisahkan "1.400 / jam" atau "US$43 / miliar").
- **Jarak baris (leading)**: kapital display 0,9–1,0 · kalimat tebal 1,0–1,1 · serif/teks 1,15–1,3. Di mesin: `spasi` = pengali tinggi baris (bawaan 1,04): `spasi: .94` untuk judul kapital rapat, `1.2` untuk pengantar serif.
- **Tracking (jarak huruf)**: kapital display +2…+6% (0,02–0,06 em) · label kapital +8…+14% · huruf kecil tebal −1…−3% · Anton 0…+3% · serif miring 0 · teks kecil tidak pernah negatif. *Celah mesin*: lapisan `teks` belum punya tracking (jarak antar-kata tetap 0,26 × ukuran). Akali: benda `kustom` dengan `c.letterSpacing = '6px'` (Chrome mendukung), lihat §5.3.

### 1.4 Warna dan kontras
- Teks utama satu warna (putih atau tinta), aksen satu warna dari tema. Kontras minimal setara 4,5:1.
- Di atas foto ramai, urutan penyelamat: (1) pindahkan teks ke ruang kosong (sepertiga atas pelat Flow memang disiapkan untuk judul), (2) gelapkan area (`efek: { jenis: 'gelap' }`, vinyet grade), (3) bayangan bawaan gaya (`judul`, `padat`, `elegan` sudah `bayang`), (4) kotak (`sorot`, `label`). Garis tepi (`garis: '#000'`) paling akhir; mudah terlihat murahan.

---

## 2. Waktu baca (lama tampil)
- **Dengan narasi** (penonton mendengar kata yang sama): tampil ≥ **0,5 dtk + 0,25 dtk × jumlah kata**, dihitung sejak kata terakhir muncul ditambah tahan ≥ 0,3 dtk.
- **Tanpa narasi** (hook bisu, kartu judul, teks yang berbeda dari narasi): tampil ≥ **0,6 dtk + 0,35 dtk × jumlah kata**.
- Angka besar: tahan ≥ 1,0 dtk setelah mendarat (odometer selesai).
- Satu kata hero: minimal 18–21 bingkai (0,6–0,7 dtk). Cek mesin memberi saran bila teks < 0,7 dtk.
- Teks yang tidak sama dengan narasi (penonton membaca sambil mendengar hal lain) maksimal 5 kata; selebihnya pindahkan ke benda (koran, dokumen) sebagai tekstur, bukan untuk dibaca.

---

## 3. Tata bahasa penekanan
**Kata yang layak ditekankan** (urut prioritas): (1) pembalik makna: *padahal, ternyata, tapi, cuma*; (2) angka + satuan; (3) nama/benda kunci; (4) kata emosi/vonis. Bukan kata sambung, bukan kata kerja umum.

**Alat penekanan** (dari paling murah): ukuran (`^kata^`) → warna aksen (`*kata*`) → berat (gaya `tebal` di tengah `serif`) → kotak (`sorot`) → gerak khusus (jatuh, cap) → bunyi. **Maksimal 2 alat untuk satu kata** (mis. besar + warna). Semua alat sekaligus = berteriak.

**Kontras untuk mengecilkan**: `~kata~` (0,65×) untuk kata fungsi dalam frasa hero ("~yang~ ^HILANG^"), supaya kata penting terlihat lebih besar tanpa ditambah.

Contoh konfig:
```js
{ teks: 'Tahun 1995,', gaya: 'serif', x: 540, y: 520, t: 'L02' },
{ teks: 'Indonesia *terbang sendiri.*', gaya: 'tebal', lebar: 860, x: 540, y: 640, anim: 'luncur', ikut: true, t: 'L02.w3' }
```

---

## 4. Sinkron dengan suara dan musik
- **Suara**: kata muncul **0–2 bingkai sebelum** diucapkan (0–0,07 dtk). Terlambat terasa lambat; lebih dari 0,25 dtk lebih awal membocorkan kalimat. Di mesin: `ikut: true` memunculkan tiap kata tepat di awal kata dari `kata.json` (sudah dalam rentang itu).
- **Penutur cepat** (≥ 3,5 kata/dtk): jangan per kata (berkedip); tampilkan frasa utuh di awal kata pertama (`anim: 'muncul'`/`'luncur'` tanpa `ikut`), atau hanya kata kunci.
- **Hilang**: ≥ 0,3 dtk sesudah kata terakhir selesai, atau ikut keluar bersama perpindahan adegan. Jangan hilang di tengah kata berikutnya.
- **Musik**: hantaman teks besar (jatuh, cap, pop hero) di **downbeat/ketukan kuat** (`../audio/musik.md`, `scripts/ketukan.py`); teks kecil boleh di ketukan lemah. Tidak semua teks di ketukan: ritme datar terasa templat.
- **Hening sebelum hantaman**: teks hero boleh muncul tanpa bunyi selama 4–8 bingkai jeda musik, lalu hantam di ketukan berikutnya.
- **Bunyi teks**: maksimal satu bunyi teks per 0,5 dtk. `KONFIG.bunyiMuncul` membunyikan setiap lapisan muncul: pakai bunyi halus (klik/pop kecil, vol .35–.55), dan bisukan teks pendukung dengan `sfx: false`.

---

## 5. Katalog teknik

### 5.1 Tipografi kinetik (payung)
- **Kapan**: kata kunci, angka, pembalik, kartu judul. **Kenapa**: gerak memberi arti tambahan dan menahan mata di bingkai yang tidak punya gambar kuat. **Cara**: tentukan *kata kerja* gerak dari arti kata (jatuh/terbang/diketik/dicap/membesar), lalu satu gerak masuk + satu gerak keluar, sisanya diam. **Hindari**: setiap kata bergerak dengan cara berbeda; teks bergerak terus sementara harus dibaca.
- **Di mesin Kolase**: `anim` (`luncur`, `jatuh`, `ketik`, `pop`, `muncul`) + `masuk`/`keluar` lapisan + `gerak` keyframe. **Di editor lain**: AE text animator (range selector), CapCut "Text animation" in/out saja, tanpa loop.

### 5.2 Penekanan kata (word emphasis)
- **Kapan**: satu kata per baris yang membawa makna. **Kenapa**: penonton yang menggulir hanya membaca 1–2 kata; pastikan itu kata yang benar. **Cara**: §3; beri jeda 0,1–0,2 dtk sebelum kata aksen muncul bila ritme narasi memungkinkan (antisipasi). **Hindari**: aksen di setiap baris, aksen pada kata sambung.
- **Di mesin**: `*kata*`, `^kata^`, `~kata~`, `aksen: '#…'` per lapisan, gaya `sorot` untuk kata penting di tengah teks `serif`/`tebal`.

### 5.3 Tracking (text tracking)
- **Kapan**: kartu judul sinematik, kemewahan, "luas/tenang" (tracking melebar pelan); tekanan/kepanikan (tracking menyempit). **Kenapa**: perubahan jarak huruf terasa megah tanpa gerak posisi. **Cara**: melebar +0 → +8…+15% selama 1,5–3 dtk `outCubic`/`inOutSine`, dikombinasikan alfa 0→1 dalam 0,4 dtk pertama. **Hindari**: tracking pada teks yang panjang; tracking cepat (< 0,5 dtk) terlihat seperti kesalahan.
- **Celah mesin**: belum ada. **Akali**: benda `kustom`, di `lukis` hitung `const u = K.E.outCubic(K.jepit(t / 2))`, set `c.letterSpacing = (u * 14) + 'px'`, lalu `c.fillText`. Teks kustom tidak diperiksa `cek`: jaga sendiri zona aman.
- **Di editor lain**: AE Tracking Amount; CapCut "Spacing" keyframe.

### 5.4 Reveal (text reveal)
- **Kapan**: kalimat kunci yang diucapkan; daftar 3 poin. **Kenapa**: kata yang muncul bersama suara terasa "diucapkan oleh layar". **Cara**: per kata (`ikut`) untuk kalimat ≤ 8 kata; per frasa untuk lebih panjang; per huruf hanya untuk kata hero/ketik. Stagger 0,06–0,12 dtk bila tidak mengikuti narasi. **Hindari**: reveal per huruf untuk kalimat panjang (lambat, melelahkan).
- **Di mesin**: `anim: 'luncur', ikut: true` (kata dari kanan + jejak, 0,32 dtk), `anim: 'pop'` (per kata, outBack 0,3 dtk), `anim: 'ketik'` (per huruf, `tiap` .05), `tiap` untuk jeda manual.

### 5.5 Masking (teks muncul dari balik garis/benda)
- **Kapan**: judul editorial/sinematik, teks yang "keluar" dari balik benda, teks di balik subjek. **Kenapa**: mask memberi kesan ruang dan presisi desain, lebih elegan dari pudar. **Cara**: teks naik 60–100% tinggi hurufnya dari bawah garis mask, 0,35–0,5 dtk `outQuart`/`outExpo`, stagger antar-baris 0,08 dtk. **Hindari**: mask yang garisnya terlihat bergerak bersama kamera tidak sinkron.
- **Di mesin**: sebagian: `panel: [x, y, w, h]` membatasi lapisan pada kotak layar + `gerak: [[0, { y: 90 }], [.45, { y: 0 }, 'outQuart']]` = teks naik dari balik tepi panel (catatan: kotak panel tidak ikut kamera, pakai di adegan kamera `tenang`). Teks di balik subjek: susun `lapis` latar → teks → potongan (gaya.md §4a). *Celah mesin*: mask yang ikut kamera/benda dan teks berisi gambar (fill footage).

### 5.6 Deformasi (squash, stretch, skew, gelombang)
- **Kapan**: kata yang artinya fisik ("ditekan", "molor", "goyah"), gaya main-main/Y2K/eksperimental. **Kenapa**: huruf yang bereaksi seperti benda terasa punya massa. **Cara**: squash 8–15% saat mendarat, kembali dalam 6–8 bingkai; skew ±8–12° saat bergerak cepat lalu tegak. **Hindari**: deformasi pada teks informasi; deformasi terus-menerus.
- **Celah mesin**: `gerak` hanya `skala` seragam. **Akali**: benda `kustom` dengan `c.scale(sx, sy)` atau `c.transform` per huruf; atau tulis kata di benda `kartu`/`label` lalu `rig: 'miring'`/`'kibar'` (rig berlaku pada benda tanpa isi dinamis).

### 5.7 Displacement (huruf bergeser/bergetar)
- **Kapan**: glitch berita, rasa cemas, sinyal rusak, dunia digital. **Kenapa**: ketidakstabilan huruf = ketidakstabilan makna. **Cara**: geser irisan horizontal 4–20 px selama 3–8 bingkai, pisah warna merah/cyan 2–6 px, lalu bersih. **Hindari**: displacement lebih dari 0,5 dtk atau pada teks yang harus dibaca saat itu.
- **Di mesin**: `efek: [{ jenis: 'glitch', t, lama: .3, kuat: .6 }]` (seluruh bingkai), perpindahan `glitch`. *Celah mesin*: displacement per lapisan teks. Akali per huruf: `kustom` dengan offset `K.acak(i + Math.floor(t * 24))`.

### 5.8 Overshoot
- **Kapan**: teks hero, angka mendarat, stiker. **Kenapa**: lewat sedikit lalu kembali = tegas dan hidup. **Cara**: skala 0 → 1,06–1,10 → 1 (subtle 4–6% untuk korporat/mewah, 8–12% untuk sosial/ceria), 0,3–0,45 dtk. **Hindari**: overshoot di semua teks; overshoot > 15% di luar gaya kartun.
- **Di mesin**: `anim: 'pop'`, `masuk: 'pop'`/`'tumbuh'` (outBack ≈ 10%), `gerak` dengan easing `'outBack'` atau `'pegas'` (≈ 8% + satu ayunan kecil).

### 5.9 Bounce
- **Kapan**: tahun, angka yang "jatuh dari langit", gaya ceria/kartu. **Kenapa**: pantulan memberi berat dan humor. **Cara**: jatuh 0,45–0,6 dtk `outBounce`, stagger per huruf 0,04–0,06 dtk, satu bunyi `dum` di pendaratan pertama. **Hindari**: bounce untuk topik tragedi/serius; semua kata memantul.
- **Di mesin**: `anim: 'jatuh'` (huruf jatuh memantul), `masuk: 'jatuh'` (lapisan memantul + guncang otomatis).

### 5.10 Morphing (kata berubah jadi kata lain)
- **Kapan**: pembalik ("MUSTAHIL → MUNGKIN"), angka berubah, "dulu → sekarang". **Kenapa**: perubahan di tempat yang sama membuat kontras terbaca tanpa kata tambahan. **Cara**: posisi dan ukuran sama, kata lama blur + susut 0,15–0,2 dtk, kata baru menajam 0,2 dtk dengan tumpang tindih 3–4 bingkai; angka memakai odometer. **Hindari**: morph bentuk huruf yang buram di tengah dan tidak terbaca selama > 0,3 dtk.
- **Di mesin**: angka: `angka: { dari, ke, lama }` (odometer, digit baru beraksen). Kata: dua lapisan `teks` di posisi sama, lama `keluar: { gaya: 'kabur', lama: .2 }`, baru `masuk: 'kabur'` di `t` yang sama. *Celah mesin*: morph bentuk huruf.

### 5.11 Sinkron suara (typography synced to voice)
- **Kapan**: kalimat kunci yang ingin "dipaku". **Kenapa**: mata dan telinga menerima kata yang sama = daya ingat naik. **Cara**: §4; pilih 1–2 kalimat per 10 dtk yang sinkron penuh, sisanya hanya kata kunci. **Hindari**: setiap kalimat sinkron per kata (jadi karaoke).
- **Di mesin**: `ikut: true` + `t` di awal baris (`'L05'`). Rujukan kata `'L05.w4'` untuk satu kata hero.

### 5.12 Sinkron musik (typography synced to music)
- **Kapan**: hook tanpa narasi, montase, video musik, ending. **Kenapa**: teks menjadi alat musik visual. **Cara**: kata/baris baru di downbeat; kata hero di drop; di build-up, kata muncul makin rapat (1/2 → 1/4 ketukan); diam satu ketukan sebelum drop. **Hindari**: setiap ketukan ada kata (melelahkan).
- **Di mesin**: waktu dari `scripts/ketukan.py` (`saranPotong`, `ketukanBirama`) dimasukkan sebagai `t` detik adegan; `efek: { jenis: 'garis' }` atau `kilat` kecil di drop.

### 5.13 Caption dinamis (dynamic captions)
- **Kapan**: talking head, wawancara, penonton tanpa suara, aksesibilitas. **Bukan** bawaan video kolase (permintaan pengguna: tanpa subtitle bawah). **Kenapa**: ±setengah penonton menonton tanpa suara di awal. **Cara**: 1–3 kata per kartu, posisi 58–65% tinggi, ukuran 52–64 px, kata aktif disorot satu warna, ganti kartu di jeda frasa. **Hindari**: caption menutupi wajah/teks lain; setiap kata memantul dan berganti warna-warni.
- **Di mesin**: hanya bila diminta: `subtitle: { gaya: 'pil', maksKata: 3, posisi: .62, ukuran: 56 }`. *Celah mesin*: sorot kata aktif di dalam pil. Untuk video bicara, skill `video-edit-motion` lebih tepat.

### 5.14 Tipografi editorial
- **Kapan**: penjelasan cerdas, opini, bisnis, teknologi elegan. **Kenapa**: kontras serif kecil + sans besar terasa seperti majalah: dipercaya dan tenang. **Cara**: rata kiri pada kolom 80–86% lebar, pengantar serif miring di atas judul tebal, kata kunci dalam kotak hitam, label kecil kapital bertracking lebar untuk kategori/tahun, banyak ruang kosong. **Hindari**: rata tengah semua baris, lebih dari 3 ukuran dalam satu bingkai.
- **Di mesin**: `serif` + `tebal` + `sorot`, `rata: 'kiri'`, latar `pola: 'editorial'`, `KONFIG.gayaTeks` untuk warna tinta. Contoh: `skill-edit-rizky/contoh/ai-mikir.konfig.js`.

### 5.15 Tipografi raksasa (oversized)
- **Kapan**: satu kata/angka yang menjadi "dunia" adegan, latar di belakang subjek, kartu bab. **Kenapa**: skala ekstrem langsung terbaca sebagai penting dan menjadi komposisi. **Cara**: 70–95% lebar layar, boleh terpotong tepi dengan sengaja (≥ 60% huruf tetap terlihat), sering di belakang subjek dengan kontras rendah (alfa .2–.4) atau hanya garis tepi. **Hindari**: lebih dari satu kata raksasa per bingkai; teks raksasa + teks judul bersaing.
- **Di mesin**: `{ teks: '1998', gaya: 'padat', ukuran: 380, alfa: .3, z: .5 }` di `lapis` sebelum potongan; `cek: false` hanya bila sengaja keluar tepi.

### 5.16 Tipografi minimal
- **Kapan**: jeda emosional, mewah, momen vonis, penutup. **Kenapa**: sedikit teks + ruang kosong = berat dan percaya diri. **Cara**: 1–5 kata, 48–80 px, pudar/naik halus 0,5–0,8 dtk `inOutSine`, tahan lama, tanpa bunyi atau dengan satu nada halus. **Hindari**: overshoot, warna aksen ramai, stiker.
- **Di mesin**: `gaya: 'elegan'` atau `'serif'`, `masuk: 'kabur'`, kamera `tenang`.

### 5.17 Tipografi sinematik
- **Kapan**: kartu judul, lokasi/tahun, kutipan penutup, trailer-style. **Kenapa**: meniru bahasa film: tenang, lebar, dipercaya. **Cara**: serif atau sans kondensasi, kapital bertracking lebar (+10–20%), tengah atau sepertiga bawah, muncul dari blur 12 → 0 px dan alfa 0 → 1 selama 0,6–1,0 dtk, tahan 1,5–2,5 dtk, keluar pudar. **Hindari**: memakai bahasa trailer di video informasi cepat; huruf bergaris tepi tebal.
- **Di mesin**: `gaya: 'elegan'` atau `label`, `gerak: [[0, { blur: 12, alfa: 0 }], [.8, { blur: 0, alfa: 1 }, 'outCubic']]`, latar gelap (`efek: { jenis: 'gelap' }`); tracking lebar = celah §5.3.

---

## 6. Teks sebagai benda (text as object)
- **Ditulis di benda dunia** (paling dipercaya, terasa bukti): koran, dokumen, papan kapur, label harga, cap, kartu foto, layar HP, notifikasi, balon. Di mesin: `benda: { jenis: 'koran'|'dokumen'|'papan'|'label'|'cap'|'kartu'|'hp'|'notif'|'balon' }` + `sorot` stabilo per baris.
- **Di ruang 3D**: teks di belakang subjek (urutan `lapis`), `z` teks berbeda dari latar supaya ikut parallax; benda bertulisan sedikit miring (`putar` ±2–6°).
- **Dipengaruhi dunia**: teks ikut guncang saat benda jatuh, ditandai `coret` (lingkar/garis bawah spidol), disapu `kilap`, ditembus kamera (`dorong` dengan `titikMasuk` di huruf atau angka).
- **Dibawa ke adegan berikut**: label/kartu yang sama pindah dengan `cocok` (benda tetap, dunia berganti).

---

## 7. Hindari
- Caption karaoke di seluruh video (setiap kata muncul + berganti warna + memantul).
- Lebih dari 2 keluarga huruf, atau tulisan tangan sebagai teks utama.
- Setiap kata memantul/berputar; animasi berulang (loop) pada teks yang sedang dibaca.
- Teks di bawah 70% tinggi atau kanan bawah (area tombol aplikasi; cek mesin menolak), teks menempel tepi < 5% lebar.
- Bayangan tebal + garis tepi + kotak sekaligus.
- Kalimat narasi utuh ditulis ulang di layar (layar bukan transkrip).
- Font "AI default" yang dipakai semua orang tanpa alasan, gradien pelangi pada huruf, glow neon pada teks informasi.

## Teknik modern
- **Teks di balik subjek (segmentasi)** · manfaat: kedalaman instan, judul terasa "di dalam" foto · kapan: hook, kartu bab, foto tokoh/benda kuat · cara: potongan subjek dari Flow latar hijau (`flow_kolase.py`) atau `ambil_media.py --potong` (rembg), lalu `lapis` pelat → teks raksasa → potongan.
- **Judul editorial campur huruf** (serif miring + display tebal + tulisan tangan dalam satu judul) · manfaat: rasa majalah, identitas kuat · kapan: hook pertanyaan, kartu konsep · cara: 2–3 lapisan `teks` terpisah dengan gaya berbeda disusun manual (x/y), satu kata aksen warna; maksimal sekali per video.
- **Tipografi distressed / fotokopi** · manfaat: rasa grunge/zine yang terlihat dibuat tangan · kapan: gaya Grunge, Collage, Psychological · cara: teks di benda `kartu`/`dokumen` + grade `halftone`/`grain` tinggi; tepi kasar per huruf = celah (akali `kustom` dengan `globalCompositeOperation: 'destination-out'` bintik acak `K.acak`).
- **Variable font (berat/lebar beranimasi)** · manfaat: penekanan halus tanpa ganti font · kapan: kata yang "menguat" · cara: celah mesin; akali dua lapisan (`label` → `tebal`) dengan lebur 0,15 dtk.

## Cek cepat
1. Sistem huruf ≤ 2 keluarga + 1 aksen, sama di seluruh video?
2. Setiap bingkai punya satu teks yang jelas dibaca duluan (selisih ukuran ≥ 1,5×)?
3. Tidak ada teks < 28 px, dan tidak ada teks di area tombol/di luar zona aman?
4. Lama tampil memenuhi rumus §2 (cek mesin tidak memberi saran "teks < 0,7 dtk")?
5. Maksimal satu kata aksen per baris dan maksimal 2 alat penekanan per kata?
6. Kata muncul 0–2 bingkai sebelum diucapkan, tidak terlambat?
7. Gerak tiap teks punya alasan dari arti katanya, dan teks diam saat sedang dibaca?
8. Tidak ada caption karaoke di seluruh video (kecuali diminta untuk talking head)?

## Celah mesin
- Tracking (jarak huruf) dan animasinya pada lapisan `teks` (akali: `kustom` + `c.letterSpacing`).
- Mask reveal yang ikut kamera/benda; teks berisi gambar/footage (akali: `panel` di adegan kamera tenang).
- Deformasi tidak seragam (squash/stretch/skew) dan per huruf (akali: `kustom`, atau teks di benda + `rig`).
- Displacement/glitch per lapisan teks (akali: efek `glitch` seluruh bingkai, atau `kustom`).
- Morph bentuk huruf antarkata (akali: dua lapisan kabur bersilang; angka pakai odometer).
- Sorot kata aktif di subtitle pil.
- Geser global sinkron kata (`ikut` selalu tepat di awal kata; belum ada opsi maju 1–2 bingkai).
- Variable font axis.
