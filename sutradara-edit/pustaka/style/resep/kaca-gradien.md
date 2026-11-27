# Resep: Kaca Gradien

> Asal belajar: @earn.edits reel `DgC40B3oLXu` (22 Nov 2026, 22,6 dtk, 16:9, "SaaS-style motion piece") dan `DfjnS4Oux4X` (10 Nov 2026, 20,7 dtk, 16:9, promosi plugin gradien) · angka bedah: 13 dan 9 potongan, rata bidikan **1,6 dan 2,1 dtk**, 23% dan **56%** potongan di ketukan (BPM ±92 / ±99), kesan "terang berwarna lembut" (kecerahan 0,81 / 0,67, saturasi rendah), palet #fbf9fc #8e9cbc · #f3f0f4 #221e28 #aa9fb1 · lembar: `…\reel-2026-11-27\bedah\DgC40B3oLXu\acuan\`, `…\bedah\DfjnS4Oux4X\acuan\`
> Terdekat dengan gaya: Minimalist + Futuristic UI + Corporate Premium (`../gaya-visual.md`) · mesin: `skill-edit-rizky` (Kolase)

Satu kalimat: penjelasan produk/teknologi yang terasa seperti situs startup premium: kanvas putih dengan garis tata letak tipis, teks kecil yang tenang, benda 3D krom/pelangi, kartu gradien, tombol kaca, dan satu sapuan biru penuh di akhir.

## 1. DNA (10 atribut)
| Atribut | Isi |
|---|---|
| Tipografi | sans geometris tipis-regular kecil (Inter 400–500, 34–48 px di 1080 lebar) dengan spasi lega; kalimat **terbelah** untuk memberi ruang benda ("Every ▢ great video"); **gambar di dalam kalimat** (pil gambar kecil di antara kata); kata raksasa tebal hitam/gradien hanya 1× ("One click", "CLICKCLICK") |
| Warna | latar putih kebiruan #fbf9fc · teks arang #221e28 · aksen 1 biru listrik #1f5cff (aksi, tombol) · aksen 2 gradien pelangi lembut (pink #f3a6d8 → ungu → biru) hanya di benda 3D/kartu |
| Transisi | garis tata letak bergeser jadi bingkai berikut; benda morf (kotak krom → bola pelangi → logo); kartu bertumpuk bergeser (swap); tombol ditekan lalu **meluas jadi layar penuh** biru; partikel titik membentuk bola dunia |
| Tekstur | nyaris tanpa tekstur; grain sangat tipis; bayangan lembut besar di bawah kartu; kilau kaca |
| Kamera | hampir diam; gerak datang dari benda; dorong kecil saat tombol ditekan |
| Bahasa animasi | **pegas** UI (overshoot 4–8%, settle 0,2–0,3 dtk), stagger 40–60 md, kursor menekan (skala 0,92), benda 3D melayang perlahan |
| Bunyi | klik UI halus, swoosh lembut, "tink" kaca, nada naik singkat saat tombol aktif; musik elektronik ringan bersih |
| Tempo | cepat-rapi: 1,6–2,1 dtk per bidikan; promosi lebih banyak ikut ketukan (hingga 56%) dibanding cerita |
| Komposisi | banyak ruang putih; satu benda di tengah; garis kisi dengan titik silang sebagai struktur; teks kecil di garis tengah |
| Cocok untuk | penjelasan aplikasi/AI, fitur produk, startup, keuangan digital, tutorial alat, ringkasan laporan, presentasi bisnis |

## 2. Prinsip yang dipelajari (bukti → prinsip)
- **Garis tata letak sebagai panggung** — bukti `DgC40B3oLXu` 0–1,5 dtk: kanvas putih dengan garis kisi dan titik silang, kata kecil di persimpangan; kisi bergeser membentuk bingkai. Struktur yang terlihat = rasa presisi.
- **Kalimat memberi ruang untuk benda** — bukti 1,5–2,5 dtk (kata terbelah, kotak krom muncul di celahnya) dan `DfjnS4Oux4X` 0–1,5 dtk (kumpulan kartu gradien di antara "Creating … Beautiful"). Benda menjadi kata.
- **Gambar di dalam kalimat** — bukti `DfjnS4Oux4X` 9–10,5 dtk: "create stunning [pil gambar] gradient backgrounds", pil gambar berganti isi. Contoh konkret tepat di tempat kata.
- **Benda morf sebagai benang merah** — bukti 2–5 dtk: kotak krom → bola pelangi → bola mengecil jadi titik. Satu benda yang berubah menjaga perhatian di tengah.
- **Tombol yang meluas jadi dunia** — bukti 16,5–18 dtk: tombol "Subscribe Today" ditekan, membesar jadi layar biru penuh dengan nama. Ajakan = aksi UI, bukan teks.
- **Satu kata raksasa** — bukti `DfjnS4Oux4X` 6–8 dtk ("One click" hitam besar terpotong di belakang tangkapan layar) dan 14,5 dtk ("CLICKCLICK" gradien). Kontras skala ekstrem hanya sekali.

## 3. Tata bahasa adegan
| Beat | Visual khas | Teks | Transisi masuk | Bunyi |
|---|---|---|---|---|
| Hook | kanvas kisi putih, kata kecil di persimpangan | 2–3 kata kecil | garis kisi tergambar | klik halus |
| Benda | kalimat terbelah, benda krom/gradien di celah | kalimat terbelah | benda `tumbuh` di celah | tink |
| Masalah | kartu/gambar gelap bergradasi abu | kata tipis | kisi bergeser (`geser`) | swoosh |
| Fitur | kartu gradien + tangkapan layar UI bertumpuk | label pil kecil | kartu ditukar (`kartu`/`cocok`) | klik + swoosh |
| Skala | partikel titik membentuk bola dunia | 2 kata di kiri-kanan | `fokus` | dengung lembut |
| Kata raksasa | 1 kata besar di belakang UI | 1–2 kata | potong di ketukan | impact lembut |
| Ajakan | tombol kaca ditekan → layar biru penuh | nama + pil alamat | `iris` dari tombol | klik + nada naik |

## 4. Preset mesin Kolase
**Sejak 27 Nov 2026 gaya ini tertanam di mesin `skill-edit-rizky`: cukup `tema: 'kaca-gradien'`** (grade, warna aksen, latar bawaan, dan gaya huruf ikut otomatis; musik tetap ditulis sendiri). Blok di bawah = rincian nilainya, dipakai untuk menimpa sebagian atau sebagai contoh lapisan.
```js
const KONFIG = {
  judul: '…', tema: 'editorial', rasio: '16:9',            // 9:16 juga bisa: teks tetap kecil, benda di tengah
  grade: { tint: '#ffffff', kuat: 0, saturasi: 1.0, halftone: 0, grain: .025, vinyet: .12, debu: 0, garis: 0, kontras: .05 },
  palet: { kuning: '#1f5cff', merah: '#1f5cff', stabilo: 'rgba(31,92,255,.14)' },
  gayaTeks: {
    judul: { font: '"KR Inter","Inter",sans-serif', gaya: '500', uk: 46, warna: '#221e28', kapital: false, bayang: false },
    tebal: { warna: '#111018' },
    label: { kotak: 'rgba(255,255,255,.75)', warna: '#221e28' }
  },
  musik: { sintesis: 'pulsa', bpm: 96 },
  sumber: [/* wajib bila ada klaim */]
};
// latar kisi: latar: { pola: 'grid', warna: '#fbf9fc', warnaGaris: 'rgba(40,40,80,.10)', jarak: 180 }
//   (atau { pola: 'editorial', grid: true, sabit: false } untuk garis putus + silang)
// gerak pegas: masuk: { gaya: 'pop' } atau gerak: [[0, { skala: .9, alfa: 0 }], [.35, { skala: 1, alfa: 1 }, 'pegas']]
// tombol meluas: benda kustom tombol (K.bulat), lalu adegan berikut berlatar biru penuh dengan masuk: 'iris', titikMasuk = pusat tombol
// gambar di dalam kalimat: dua lapisan teks kiri/kanan + lapisan gambar kecil bersudut bulat di tengah (x dihitung dari lebar teks)
```
Celah mesin: benda krom/pelangi 3D (akali: potongan Flow "iridescent chrome sphere, studio white" latar hijau + `hidup` + `kilap`); morf antar-benda (akali: `cocok` dua gambar berbeda = saling lebur di jalan); partikel membentuk bola dunia (akali: benda `kustom` titik-titik yang bergerak ke posisi bola); kaca bening/blur latar di balik tombol (akali: kotak putih 75% + bayangan lembut; backdrop blur sejati belum ada).

## 5. Dipakai untuk topik lain
| Topik | Penerapan |
|---|---|
| Cara kerja QRIS | kanvas kisi, HP ber-UI kaca, kalimat terbelah dengan ikon kode QR, tombol "Bayar" meluas biru |
| Fitur AI untuk UMKM | kartu gradien per fitur, gambar di dalam kalimat (contoh hasil), satu kata raksasa "OTOMATIS" |
| Ringkasan laporan keuangan | partikel titik jadi grafik, label pil angka, kisi rapi |
| Tutorial aplikasi | tangkapan layar di kartu bertumpuk, kursor pegas, sorot tombol |
| Perbandingan dua produk (generik) | dua kartu kaca kiri-kanan, garis kisi tengah, tukar posisi saat menang |

## 6. Variasi supaya tidak seragam
- Mode: terang (putih) · gelap (#0e0d14 dengan gradien yang sama).
- Benda tanda tangan: bola pelangi · kubus krom · kartu kaca.
- Aksen: biru listrik · hijau mint · oranye matahari (satu per seri).

## 7. Jangan disalin
- Logo, nama, URL, tangkapan layar produk, dan kalimat promosi akun acuan ("Make it yours", "One click", "Comment …").
- Tangkapan layar aplikasi nyata hanya milik pengguna atau buatan sendiri; jangan meniru antarmuka merek tertentu persis.

## Cek cepat
- [ ] Ruang putih ≥ 50% bingkai di sebagian besar adegan
- [ ] Teks kecil dan tenang; kata raksasa hanya sekali
- [ ] Semua gerak UI memakai pegas/overshoot kecil, stagger rapi
- [ ] Satu benda tanda tangan yang berubah menjaga benang merah
- [ ] Ajakan berupa aksi UI (tombol ditekan), bukan teks panjang
