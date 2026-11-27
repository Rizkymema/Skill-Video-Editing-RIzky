# Animasi UI, aplikasi, dan visual digital

> MOTION · dipakai di langkah 5–8 · terkait: `../visual/metafora.md`, `../type/tipografi-kinetik.md`, `prinsip-animasi.md`, `../audio/sound-design.md` §Bunyi UI, `../style/gaya-visual.md` (Futuristic UI, Dark Tech, Corporate Premium, Social Media Viral) · contoh mesin: `skill-edit-rizky/contoh/ai-mikir.konfig.js`, `contoh/prompt-ai.konfig.js`

Prinsip inti:
1. **UI dipakai untuk menjelaskan, bukan menghias.** Layar HP, dashboard, atau grafik muncul karena konsepnya memang paling jelas ditunjukkan begitu (proses, data, kebiasaan digital). Kalau narasinya bukan tentang hal digital, UI biasanya pengalih.
2. **Penonton harus mengenali, bukan mempelajari.** Pakai pola yang sudah dikenal (chat, feed, notifikasi, kolom ketik, tombol) yang disederhanakan: 30–50% unsur UI asli cukup.
3. **Satu interaksi per momen.** Kursor bergerak → berhenti → klik → hasil. Jangan tiga hal terjadi di layar sekaligus.
4. **Gerak UI lebih lambat dari UI asli.** Aplikasi nyata 150–250 ms; di video, beri 1,2–1,5× supaya mata sempat membaca.
5. **Data jujur.** Grafik yang menipu (sumbu terpotong, skala beda) merusak kepercayaan channel.

## 1. Aturan gerak UI
| Gerak | Durasi patokan | Easing | Catatan |
|---|---|---|---|
| Mikro (tombol ditekan, centang, toggle, ikon berubah) | 150–300 ms (5–9 bingkai) | outCubic / outBack ringan (overshoot ≤ 6%) | tekan = skala 0,9–0,95 selama 80–120 ms lalu kembali |
| Elemen masuk (kartu, gelembung chat, notifikasi) | 250–400 ms | outQuart / outCubic (melambat saat tiba) | geser 20–60 px + pudar; gelembung chat dari arah pengirim |
| Elemen keluar | 150–250 ms | inCubic (mempercepat saat pergi) | keluar selalu lebih cepat dari masuk |
| Pindah layar / halaman | 300–500 ms | inOutCubic / inOutQuart | layar lama bergeser sebagian (parallax 30%), layar baru menutupinya |
| Gulir (scroll) | 0,6–1,5 dtk per gulir | outQuart (momentum, berhenti pelan) | boleh sedikit memantul di ujung daftar |
| Daftar bertahap (stagger) | jeda 30–60 ms per butir (di video 60–120 ms bila tiap butir harus terbaca) | outCubic | maks 6–8 butir; lebih dari itu, tampilkan sebagai blok |
| Angka/indikator naik | 0,8–1,6 dtk | outCubic / outQuart | berhenti di angka final dengan ding/hit |

## 2. Koreografi kursor
- **Lintasan melengkung** (busur), bukan garis lurus: tangan manusia menggerakkan mouse berbentuk busur.
- **Easing inOutCubic**: mulai pelan, cepat di tengah, melambat sebelum sasaran; boleh lewat 4–8 px lalu kembali (overshoot kecil).
- **Berhenti 150–300 ms** di atas tombol sebelum klik (penonton sempat melihat sasaran).
- **Klik**: kursor + tombol mengecil ke 0,9 selama 80–120 ms + bunyi klik + gelombang lingkaran tipis (riak) 0,3 dtk.
- **Sesudah klik**: hasil muncul 100–200 ms kemudian (sebab → akibat terbaca).
- Kursor 1,4–2× ukuran asli supaya terlihat di HP; warna putih bertepi hitam atau sebaliknya menurut latar.

## 3. Komponen
### Layar HP (smartphone UI)
- **Kapan**: kebiasaan pakai HP, aplikasi, media sosial, chat, belanja online, bukti tangkapan layar.
- **Kenapa**: penonton menonton di HP; layar HP di dalam video langsung dikenali sebagai "dunia saya".
- **Cara**: bingkai HP generik (tanpa logo), layar diisi UI sederhana; HP sedikit miring 3–8° dan melayang, atau dipegang tangan potongan. Masuk dari bawah dengan outQuart. Kamera mendorong ke layar untuk pindah ke "dalam aplikasi" (transisi `dorong`/`bingkai`).
- **Hindari**: HP dengan logo merek nyata; isi layar kecil yang tidak terbaca (teks di layar HP ≥ 36 px pada bingkai 1080).
- **Di mesin Kolase**: `benda: { jenis: 'hp', gambar | urutan, notif: { judul, teks, t, warnaIkon }, lukis: (c, ly, t, K) => {…} }` (isi layar digambar konfig), `masuk: { gaya: 'geser', dari: 'bawah' }`, `rig: { jenis: 'miring', y: … }`, `kilap: { t }`.

### Situs web dan dashboard
- **Kapan**: bisnis online, statistik, perbandingan harga, performa, "di balik layar" sebuah layanan.
- **Kenapa**: dashboard menyatukan banyak angka dalam satu bingkai yang terasa resmi.
- **Cara**: 1 angka besar + 2–3 widget kecil, kisi rapi, sudut bulat 16–28 px, latar gelap grafit atau putih bersih menurut gaya; widget muncul bertahap, angka bergulir, satu widget disorot (lainnya diredupkan 40–60%).
- **Hindari**: dashboard penuh angka yang tidak dibahas narasi; grafik mini yang tak terbaca.
- **Di mesin Kolase**: kartu-kartu lewat benda `kustom` (`K.bulat`), angka besar lewat lapisan `angka`, sorot dengan `efek: [{ jenis: 'sorot', titik, r }]` atau `alfa` lapisan lain diturunkan. *Celah mesin*: belum ada benda dashboard/widget siap pakai (lihat §5).

### Feed media sosial
- **Kapan**: algoritma, viral, perbandingan diri, kecanduan gulir, opini publik.
- **Kenapa**: gerak gulir feed adalah metafora "tak ada habisnya" yang langsung dipahami.
- **Cara**: kartu posting generik (avatar bulat abu, nama fiktif, gambar, ikon suka/komentar tanpa logo), gulir dengan momentum, satu posting berhenti tepat di tengah dan disorot. Angka suka bergulir naik.
- **Hindari**: meniru tampilan Instagram/TikTok persis (warna, ikon, logo); nama/akun orang nyata.
- **Di mesin Kolase**: *Celah mesin* (daftar gulir) — benda `kustom` dengan offset gulir (sketsa §5); angka suka lewat `angka`.

### Notifikasi
- **Kapan**: gangguan, kabar mendadak, tagihan, pesan penting, tumpukan distraksi.
- **Kenapa**: notifikasi memotong perhatian, persis seperti di kehidupan nyata (pattern interrupt alami).
- **Cara**: turun dari atas 250–350 ms outQuart + bunyi notif; tumpukan: tiap notifikasi baru mendorong yang lama turun 0,15–0,3 dtk berselang; untuk "kewalahan", jeda makin rapat (0,4 → 0,25 → 0,12 dtk).
- **Hindari**: notifikasi berisi teks panjang; ikon aplikasi nyata.
- **Di mesin Kolase**: `benda: { jenis: 'notif', judul, teks, waktu, ikonTeks, warnaIkon }` + `masuk: { gaya: 'geser', dari: 'atas' }`; di layar HP: `hp.notif`. Bunyi `notif` sintesis atau berkas.

### Kolom ketik dan animasi mengetik
- **Kapan**: prompt AI, pencarian, pesan yang ditulis lalu dihapus (ragu), password.
- **Kenapa**: penonton membaca bersamaan dengan teks muncul; ketik-hapus-ketik menunjukkan keraguan tanpa narasi.
- **Cara**: 12–20 huruf/dtk (lebih cepat dari manusia, tetap terbaca), jeda 150–300 ms di tanda baca, kursor teks berkedip 2–2,5 Hz saat diam dan menyala terus saat mengetik, tombol kirim ditekan (skala 0,9) sesudah selesai.
- **Hindari**: ketik huruf-demi-huruf untuk kalimat > 60 huruf (terlalu lama; tampilkan per kata).
- **Di mesin Kolase**: gaya teks `anim: 'ketik'` (lapisan teks) atau benda `kustom` (contoh kolom ketik + kursor berkedip di `contoh/prompt-ai.konfig.js` fungsi `pChat`); bunyi `ketik` atau berkas tuts per huruf.

### Antarmuka chat
- **Kapan**: percakapan, AI menjawab, negosiasi, gosip, layanan pelanggan, "dialog batin".
- **Kenapa**: format tanya-jawab sangat cepat dipahami; gelembung bisa membawa naskah tanpa narator.
- **Cara**: gelembung pengirim kanan/gelap, penerima kiri/terang; indikator "mengetik…" (tiga titik berdenyut 0,6–1 dtk) sebelum jawaban; gelembung baru mendorong yang lama naik. Maks 3–4 gelembung terlihat.
- **Hindari**: chat panjang yang harus dibaca semua; tampilan aplikasi chat nyata yang persis.
- **Di mesin Kolase**: `benda: { jenis: 'balon', teks, gaya: 'bicara'|'pikir'|'teriak', ekor }` untuk balon komik; chat aplikasi lewat benda `kustom` (`contoh/prompt-ai.konfig.js` `pChat`, `contoh/ai-mikir.konfig.js` menu chat AI + papan peluang kata).

### Visualisasi data, grafik, diagram
- **Kapan**: perbandingan, pertumbuhan, proporsi, tren, ranking.
- **Kenapa**: angka di dalam bentuk dipahami 2–3× lebih cepat daripada angka diucapkan.
- **Cara**: satu pesan per grafik ("naik 3×", "separuhnya hilang"), bentuk paling sederhana yang menyampaikannya (batang untuk banding, garis untuk tren, donat untuk proporsi bagian-dari-keseluruhan, progres untuk menuju target). Tumbuh dari nol 0,8–1,4 dtk outCubic, batang bertahap 80–150 ms; nilai kunci disorot warna aksen, lainnya abu.
- **Hindari**: lebih dari 5 batang/kategori; legenda (labeli langsung di bentuknya); 3D grafik; warna pelangi.
- **Di mesin Kolase**: `benda: { jenis: 'grafik', judul, data, maks, bentuk: 'batang'|'progres', label, nilaiLabel, sorotData, satuan, labelMaks, format, t, lama }`; angka besar `angka: { dari, ke, lama, awal, akhir }` (odometer, bunyi `gulir` otomatis); papan kapur `benda: papan` untuk angka pasar. *Celah mesin*: grafik garis, donat/pie, diagram alir (sketsa §5).

### Progress bar dan loading
- **Kapan**: proses berjalan, menunggu, kemajuan menuju target, "baterai" energi/mental, hitung mundur.
- **Kenapa**: bentuk paling universal untuk "seberapa jauh lagi".
- **Cara**: progres tidak pernah linear rata — maju cepat, macet, maju lagi (terasa nyata dan menimbulkan ketegangan); angka persen menyertai; macet di 99% adalah lelucon/ketegangan yang dipahami semua orang. Loading spinner 0,8–1,2 dtk per putaran.
- **Hindari**: progress bar sebagai hiasan tanpa makna di narasi.
- **Di mesin Kolase**: `grafik` `bentuk: 'progres'`; progres bertingkat (macet) lewat benda `kustom` dengan keyframe `K.kunci(t, [[0, 0], [1, .6, 'outCubic'], [2.2, .62], [2.6, .99, 'inOutCubic']])`.

### Transisi antarmuka
- **Kapan**: pindah dari satu layar/aplikasi ke yang lain, masuk ke detail.
- **Kenapa**: meniru transisi aplikasi membuat perpindahan adegan terasa alami di dunia digital (`transisi.md` §Motivasi).
- **Cara**: kartu kecil membesar jadi layar penuh (shared element), layar bergeser ke samping, modal naik dari bawah.
- **Hindari**: transisi sinematik berat (bakar film, kertas) di tengah adegan UI.
- **Di mesin Kolase**: `cocok` (kartu yang sama membesar ke adegan baru), `tutup` (panel naik dari bawah seperti modal), `geser`, `dorong` dengan `titikMasuk` di layar HP, `bingkai` dengan `bentuk: 'kotak'`.

## 4. Resep konsep → UI
| Konsep | Visual UI | Kenapa berhasil | Di mesin Kolase |
|---|---|---|---|
| Algoritma | feed yang mengocok ulang urutan kartu sendiri, satu kartu ditarik ke atas | menunjukkan "ada yang memilihkan" | benda `kustom` kartu + `K.kunci` posisi |
| Inflasi | label harga sama yang angkanya bergulir naik, isi keranjang menyusut | angka + benda yang dikenal | `angka` (awal `'Rp'`), `benda: label` + `ayun` |
| Bunga majemuk | grafik batang per tahun, makin tinggi makin cepat | bentuk kurva = rasa "meledak" | `grafik` batang bertahap |
| Distraksi | notifikasi menumpuk makin rapat sampai menutupi layar | rasa kewalahan | `notif` beruntun, jeda menyempit |
| Overthinking | tab browser bertambah terus, judul tab saling bertentangan | metafora digital yang akrab (`../visual/metafora.md`) | benda `kustom` deretan tab |
| AI "berpikir" | papan peluang kata, kata dengan persen tertinggi dipilih | membongkar proses | `contoh/ai-mikir.konfig.js` |
| Viral | penghitung bagikan bergulir + titik-titik jaringan bercabang | pertumbuhan eksponensial terlihat | `angka` + benda `kustom` jaringan |
| Langganan/biaya diam-diam | kalender dengan tagihan otomatis jatuh tiap bulan, total berjalan | biaya kecil berulang jadi besar | benda `kustom` kalender + `angka` |
| Keamanan password | meteran kekuatan merah → hijau saat karakter ditambah | sebab-akibat langsung | `grafik` progres + `anim: 'ketik'` |
| Waktu layar | dashboard "7 jam 42 menit" dengan batang per aplikasi | angka pribadi yang menampar | `angka` + `grafik` batang |
| Data pribadi | paket data mengalir dari HP ke server | yang tak terlihat jadi terlihat | benda `kustom` titik mengalir (`ai-mikir` "data mengalir") |
| Prompt yang baik | kolom ketik prompt memanjang, tiap unsur distabilo warna berbeda | struktur terlihat | `contoh/prompt-ai.konfig.js` |

## 5. Sketsa benda kustom (untuk celah mesin)
Semua di `benda: { jenis: 'kustom', lebar, tinggi, lukis: (c, ly, t, K) => {…} }`; `t` = detik sejak adegan mulai, `K.ref('L03.w5')` = rujukan narasi dalam detik adegan, `K.E` = easing, `K.bulat` = path sudut bulat.
```js
// kursor: busur → berhenti → klik (skala .9 + riak). Bunyi: sfx: [{ t: tKlik, jenis: 'klik' }]
function kursor(c, K, t, p0, p1, t0, tKlik) {
  const u = K.E.inOutCubic(K.jepit((t - t0) / (tKlik - .25 - t0)));             // tiba 0,25 dtk sebelum klik
  const kx = (p0[0] + p1[0]) / 2, ky = Math.min(p0[1], p1[1]) - 140;              // titik kendali busur
  const x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * kx + u * u * p1[0], y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * ky + u * u * p1[1];
  const s = (t > tKlik && t < tKlik + .1 ? .9 : 1) * 1.7;
  c.save(); c.translate(x, y); c.scale(s, s); c.fillStyle = '#fff'; c.strokeStyle = '#111'; c.lineWidth = 2;
  c.beginPath(); [[0, 0], [0, 26], [7, 20], [12, 31], [17, 29], [12, 18], [21, 18]].forEach(([a, b], i) => i ? c.lineTo(a, b) : c.moveTo(a, b));
  c.closePath(); c.fill(); c.stroke(); c.restore();
  const q = (t - tKlik) / .35; if (q > 0 && q < 1) { c.strokeStyle = `rgba(255,255,255,${1 - q})`; c.lineWidth = 4; c.beginPath(); c.arc(x, y, 10 + q * 44, 0, 7); c.stroke(); }
}
// daftar gulir dengan momentum: kartu digambar dengan offset, dipotong ke layar
function gulir(c, K, t, w, h, kartu, t0, jarak) {
  const off = K.E.outQuart(K.jepit((t - t0) / 1.2)) * jarak;
  c.save(); K.bulat(c, 0, 0, w, h, 36); c.clip();
  kartu.forEach((gb, i) => { const y = 40 + i * 300 - off; if (y > -300 && y < h) gb(c, 30, y, w - 60, 270); });
  c.restore();
}
// grafik garis tumbuh dari kiri + titik nilai terakhir; sumbu nol selalu terlihat
function garis(c, K, t, w, h, data, maks, t0, lama, warna) {
  const u = K.E.outCubic(K.jepit((t - t0) / lama)), n = data.length - 1, X = i => 60 + i * (w - 120) / n, Y = v => h - 60 - v / maks * (h - 120);
  c.strokeStyle = 'rgba(0,0,0,.25)'; c.lineWidth = 3; c.beginPath(); c.moveTo(60, Y(0)); c.lineTo(w - 60, Y(0)); c.stroke();
  const ujung = u * n, i0 = Math.floor(ujung); c.strokeStyle = warna; c.lineWidth = 10; c.lineJoin = 'round'; c.beginPath();
  for (let i = 0; i <= i0; i++) i ? c.lineTo(X(i), Y(data[i])) : c.moveTo(X(i), Y(data[i]));
  const f = ujung - i0, xe = i0 < n ? K.lerp(X(i0), X(i0 + 1), f) : X(n), ye = i0 < n ? K.lerp(Y(data[i0]), Y(data[i0 + 1]), f) : Y(data[n]);
  c.lineTo(xe, ye); c.stroke(); c.fillStyle = warna; c.beginPath(); c.arc(xe, ye, 16, 0, 7); c.fill();
}
// donat: bagian dari keseluruhan
function donat(c, K, t, cx, cy, r, frac, t0, warna) {
  const u = K.E.outCubic(K.jepit((t - t0) / 1.1)); c.lineWidth = r * .32; c.lineCap = 'round';
  c.strokeStyle = 'rgba(0,0,0,.12)'; c.beginPath(); c.arc(cx, cy, r, 0, 7); c.stroke();
  c.strokeStyle = warna; c.beginPath(); c.arc(cx, cy, r, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * frac * u); c.stroke();
}
```
Aturan kanvas kustom (`mesin.md` benda kustom): padding ±60 px bila ada bayangan, reset `shadowColor` sesudah dipakai, jaga sendiri zona aman (teks di dalam kanvas tidak diperiksa `cek`).

## 6. UI meyakinkan tanpa merek nyata
- Nama aplikasi/akun fiktif yang netral ("Pesan", "Belanja", "@pengguna_123"); ikon bentuk umum (gelembung, keranjang, hati).
- Logo merek hanya bila pengguna mengirimkannya untuk video itu (`skill-edit-rizky/references/acuan.md` §3).
- Warna dan susunan boleh mengingatkan pada kategori aplikasi (chat hijau, belanja oranye), tidak menyalin satu aplikasi persis.
- Data di layar = data dari riset dengan sumber (`KONFIG.sumber`), bukan angka karangan yang terlihat nyata.

## 7. Kejujuran data
- Batang selalu mulai dari **nol**; bila harus memperbesar perubahan kecil, pakai grafik garis dan tulis rentang sumbunya.
- Satuan selalu tertulis (Rp, %, juta, per tahun); angka perkiraan diberi "±".
- Dua grafik yang dibandingkan memakai skala yang sama.
- Sumber data tampil di layar (label kecil, gaya `label`, ±1330 px) selama grafik tampil.
- Persen vs poin persen dibedakan; jangan membulatkan tanpa tanda.

## Teknik modern
- **UI kaca bening (glassmorphism / liquid glass)**: panel semi-transparan dengan blur latar dan tepi terang. Manfaat: kesan perangkat terbaru, cocok gaya Futuristic UI. Kapan: teknologi 2025+, produk digital. Alur: benda `kustom` dengan isi latar disalin buram (gambar ulang latar dengan `c.filter = 'blur(20px)'` di dalam `clip` panel) — mahal, pakai di 1–2 adegan saja.
- **Screen recording nyata diperbesar (zoom-follow)**: rekaman layar asli, kamera mengikuti kursor dan membesar ke area aksi. Manfaat: tutorial yang terbaca di HP. Alur: rekaman pengguna → `rakit --klip` → `urutan` di dalam `benda: hp` atau penuh + `kamera` keyframe mengikuti titik klik.
- **Shared-element transition**: kartu kecil menjadi layar penuh adegan berikut. Manfaat: kesinambungan objek (`transisi.md`). Alur: `masuk: 'cocok'` dengan `cocok: { dari, ke }`.

## Cek cepat
- [ ] Tiap UI di layar menjelaskan sesuatu yang disebut narasi.
- [ ] Teks di UI terbaca di HP (≥ 36 px pada 1080 lebar), maks 3–4 gelembung/kartu terlihat.
- [ ] Gerak UI memakai easing (masuk melambat, keluar mempercepat), tidak linear.
- [ ] Kursor bergerak melengkung, berhenti sebelum klik, klik berbunyi dan mengecil.
- [ ] Tidak ada logo/tampilan aplikasi nyata yang tidak dikirim pengguna.
- [ ] Grafik dari nol, bersatuan, bersumber di layar; satu pesan per grafik.

## Celah mesin
- **Kursor** belum ada sebagai benda. Akali: sketsa `kursor` §5 di benda `kustom`. Usulan mesin: `benda: { jenis: 'kursor', jalur: [[t, x, y], …], klik: [t, …] }` dengan busur + riak + bunyi otomatis.
- **Daftar gulir / feed** belum ada. Akali: sketsa `gulir` §5. Usulan: `benda: { jenis: 'feed', kartu: [...], gulir: [[t, offset, ease]] }`.
- **Grafik garis, donat/pie, diagram alir** belum ada (`grafik` hanya batang/progres). Akali: sketsa `garis`/`donat` §5. Usulan: `grafik.bentuk: 'garis' | 'donat'`.
- **Widget dashboard** belum ada. Akali: benda `kustom` kartu-kartu + lapisan `angka` terpisah di atasnya.
- **Gelembung chat aplikasi** (bukan balon komik) belum ada sebagai benda. Akali: `pChat` di `contoh/prompt-ai.konfig.js`. Usulan: `benda: { jenis: 'chat', pesan: [{ dari: 'kiri'|'kanan', teks, t }], mengetik: true }`.
