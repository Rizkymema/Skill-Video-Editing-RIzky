# Resep: Arsip Pop

> Asal belajar: @earn.edits reel `Df7Zz75uOGL` (19 Nov 2026, 41,8 dtk, 9:16, mobil berbahan bakar ampas kopi) · angka bedah: 11 potongan, rata bidikan 3,5 dtk, 18% potongan di ketukan (BPM ±135), kesan "gelap berwarna kuat + vinyet", palet #292524 #791f16 #bcc3b7 #7b846d · lembar: `D:\automation\Video AI\Video Refrensi\earn.edits\reel-2026-11-27\bedah\Df7Zz75uOGL\acuan\`
> Terdekat dengan gaya: Newspaper/Magazine + Vintage Commercial + Collage (`../gaya-visual.md`) · mesin: `skill-edit-rizky` (Kolase)

Satu kalimat: fakta aneh yang diceritakan seperti iklan majalah lama yang ceria: dunia hitam-putih dengan satu benda berwarna, label kertas sobek, latar warna datar yang berani, koran fiktif, dan peta rute dari atas.

## 1. DNA (10 atribut)
| Atribut | Isi |
|---|---|
| Tipografi | judul sans tebal **miring** putih dengan satu kata merah ("The Strangest *Fuel*"); kata stensil abu di beton; label merek di **kertas sobek** biru/putih; kata ditumpuk bertingkat kuning-merah miring; caption pil kecil satu-dua kata |
| Warna | dunia hitam-putih/beton #292524 · teks putih #f4f1ea · aksen 1 merah tomat #d4291c (benda utama, kata kunci) · aksen 2 biru label #2a5bd7 (nama, keterangan) · bidang warna datar penuh (merah, coklat kopi) sebagai "jeda halaman iklan" |
| Transisi | kabur gerak dari benda yang melaju; **asap/kabut putih** menutup layar; lingkaran warna yang tumbuh lalu jadi **cairan berpilin** (bentuk benda → tekstur bahan); latar warna datar berganti dengan potong keras |
| Tekstur | grain kasar + vinyet di adegan foto; bersih di bidang warna datar; koran menguning |
| Kamera | ikut benda (mobil masuk dengan kabur gerak); pandangan atas (top-down) untuk rute; dorong ke papan/label |
| Bahasa animasi | label menempel dengan pantulan (outBack 10%); stiker tahun pop; benda 3D berputar pelan dengan teks melingkar; progres rute linear |
| Bunyi | mesin mobil, mesin kopi mendesis, kertas sobek, pop stiker, cairan mengalir; musik funk/retro iklan 120–140 BPM sebagai alas |
| Tempo | ±3,5 dtk, potongan ikut kalimat; tiap adegan satu "lelucon visual" |
| Komposisi | benda berwarna di tengah dunia abu (warna selektif = fokus); label diagonal di sudut benda; koran tengah memenuhi lebar |
| Cocok untuk | penemuan aneh, rekor dunia, sejarah merek/produk, sains populer, kuliner, eksperimen, "ternyata bisa" |

## 2. Prinsip yang dipelajari (bukti → prinsip)
- **Warna selektif = fokus cerita** — bukti 0,5–2 dtk: jalan dan gedung hitam-putih, mobil putih-merah berwarna. Mata langsung ke benda utama tanpa panah.
- **Benda dengan teks melingkar** — bukti 4–4,5 dtk: mesin kopi 3D dengan kata-kata melilit di sekelilingnya. Teks menjadi bagian benda, bukan ditempel.
- **Stiker tahun** — bukti 5,5–7 dtk: "2010" kuning di kotak merah menempel di cetak biru di dinding garasi. Tanggal = benda fisik.
- **Label kertas sobek** — bukti 8–9,5 dtk: nama mobil di potongan kertas biru bertepi sobek, menempel lalu terbawa keluar. Nama diperkenalkan seperti etiket.
- **Lingkaran → cairan** — bukti 13–14,5 dtk: lingkaran coklat seperti gerhana, lalu layar penuh kopi berpilin, teks miring bertumpuk "BUT IT DIDN'T USE LIQUID COFFEE". Transisi lahir dari bahan topiknya sendiri.
- **Bidang warna datar sebagai halaman** — bukti 15–19,5 dtk: latar merah penuh, koran fiktif jatuh, judul disorot biru, caption pil kata demi kata. Ganti "halaman" = ganti warna datar.
- **Rute dari atas + bilah jarak** — bukti 20–23,5 dtk: mobil dari atas di jalan hijau, bilah 0–370 km dengan mobil kecil bergerak. Angka jarak dibuktikan dengan gerak.

## 3. Tata bahasa adegan
| Beat | Visual khas | Teks | Transisi masuk | Bunyi |
|---|---|---|---|---|
| Hook | dunia hitam-putih + benda berwarna melaju | judul miring + 1 kata merah | benda masuk dengan kabur gerak (`geser` + `garis`) | mesin + whoosh |
| Pembalik | beton gelap | kata stensil abu tumbuh | potong | dengung rendah |
| Bahan | benda pemicu (mesin kopi) berputar, teks melingkar | kata melingkar | `dorong` | desis |
| Kapan/di mana | dinding + cetak biru + stiker tahun | stiker "2010" | `tutup` | pop stiker |
| Siapa | ruang kerja, label kertas sobek pada benda | nama di label biru | `cocok` (benda tetap) | kertas sobek |
| Nama ide | beton, nama besar merah | 1 kata | asap putih menutup | semburan |
| Cara kerja | lingkaran → cairan berpilin | teks bertumpuk miring kuning-merah | `iris` lalu lebur ke tekstur | cairan |
| Bukti | bidang merah + koran fiktif tersorot | caption pil | `jatuh` | kertas + dum |
| Hasil | tampak atas + bilah rute | km | `sentak` ke bawah | mesin melaju |

## 4. Preset mesin Kolase
```js
const KONFIG = {
  judul: '…', tema: 'tv',
  grade: { tint: '#efe2c6', kuat: .06, saturasi: 1.0, halftone: .05, grain: .1, vinyet: .48, debu: .15, garis: 0, kontras: .2 },
  palet: { kuning: '#f6c12a', merah: '#d4291c', biru: '#2a5bd7', stabilo: 'rgba(42,91,215,.55)' },
  gayaTeks: {
    judul: { font: '"KR Archivo","Archivo Black",sans-serif', warna: '#f4f1ea', kapital: false, bayang: true },
    label: { kotak: '#2a5bd7', warna: '#ffffff' }
  },
  // subtitle: { gaya: 'pil', maksKata: 2, posisi: .7 },       // caption pil kecil: nyalakan hanya bila 62–72% tinggi kosong
  //                                                            (cek menolak subtitle yang menutupi teks/kartu)
  musik: { sintesis: 'ceria', bpm: 124 },
  sumber: [/* wajib */]
};
// warna selektif: pelat latar { gambar: 'jalan', hitamPutih: true } + potongan { gambar: 'mobil', ... } berwarna
// judul miring: { teks: 'Bahan Bakar Paling *Aneh*', gaya: 'judul', putar: -4, y: 330, anim: 'luncur', ikut: true }
// stiker tahun: { teks: '2010', gaya: 'stiker', ukuran: 110, putar: -6, masuk: 'pop', ayun: { sudut: 5 } }
// halaman warna datar: latar: { pola: 'polos', warna: '#c8231a' } + { benda: { jenis: 'koran', nama: 'Harian Nusantara', judul: '…', sorot: [{ baris: 'judul', t: .4, warna: 'rgba(42,91,215,.5)' }] }, masuk: 'jatuh' }
// rute: pelat tampak atas + benda grafik bentuk 'progres' (0–370 km) atau kustom bilah dengan ikon mobil
```
Celah mesin: label kertas sobek (akali: `teks` gaya `label` + `rig: 'miring'` + potongan tepi sobek PNG dari Flow di belakangnya; usul perpindahan `sobek`); cairan berpilin (akali: klip Flow pendek atau pelat Flow "liquid coffee swirl macro" + kamera `putar` pelan; transisi liquid sejati belum ada); teks melingkar di benda (akali: benda `kustom` yang menulis huruf di sepanjang busur).

## 5. Dipakai untuk topik lain
| Topik | Penerapan |
|---|---|
| Sejarah es teh manis | dunia abu + gelas teh berwarna, label sobek "1950-an", halaman warna coklat teh, koran fiktif |
| Penemuan rice cooker | dapur hitam-putih, panci berwarna, stiker tahun, cairan → uap, peta penyebaran dari atas |
| Rekor kerupuk terpanjang | warna selektif pada kerupuk, bilah panjang (meter) bergerak dari atas |
| Asal-usul merek lokal (generik, tanpa logo asli) | etiket kertas sobek, halaman iklan warna datar, koran fiktif |
| Sains: kenapa roti mengembang | bahan → tekstur berpilin, label nama zat, halaman warna datar per tahap |

## 6. Variasi supaya tidak seragam
- Warna "halaman" datar: merah · biru · kuning mustard (satu per babak, maksimal 3).
- Benda selektif: produk · kendaraan · makanan.
- Penutup: peta rute · grafik batang · koran dilipat.

## 7. Jangan disalin
- Mobil, nama merek, nama koran ("The Daily Chronicle"), kalimat, dan foto berita reel itu; nama koran di layar selalu fiktif buatan sendiri.
- Logo merek nyata tidak digambar; produk generik.

## Cek cepat
- [ ] Hanya benda utama yang berwarna di adegan warna selektif
- [ ] Tanggal/nama selalu menjadi benda (stiker, label, koran)
- [ ] Bidang warna datar ≤ 3 warna sepanjang video
- [ ] Satu transisi lahir dari bahan topik (cairan, uap, serbuk…)
- [ ] Angka besar dibuktikan dengan gerak (rute, bilah, grafik)
