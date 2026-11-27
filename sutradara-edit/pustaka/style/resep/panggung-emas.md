# Resep: Panggung Emas

> Asal belajar: @earn.edits reel `DfM7ZyruNRU` (1 Nov 2026, 23,6 dtk, 4:3 mendatar, pengumuman kompetisi "Frame War") · angka bedah: 15 potongan, rata bidikan **1,5 dtk**, 27% potongan di ketukan (BPM ±101), kesan "gelap berwarna kuat", palet #00120f #383c33 #857d67 #d0ccb0 · lembar: `D:\automation\Video AI\Video Refrensi\earn.edits\reel-2026-11-27\bedah\DfM7ZyruNRU\acuan\`
> Terdekat dengan gaya: Luxury Editorial + Social Media Viral (`../gaya-visual.md`) · mesin: `skill-edit-rizky` (Kolase)

Satu kalimat: pengumuman bertaruhan tinggi yang terasa seperti malam penghargaan: huruf serif raksasa di **belakang** subjek, emas dan hijau botol, konfeti, piala, dan satu pertanyaan sinis yang membuat penonton bertahan.

## 1. DNA (10 atribut)
| Atribut | Isi |
|---|---|
| Tipografi | serif tinggi-kontras raksasa (Georgia tebal, 300–420 px) diletakkan di belakang subjek; kalimat pengantar sans tipis kecil di atasnya; satu kata berwarna (hijau/merah) dalam kalimat; coretan garis tangan merah melintas judul |
| Warna | latar hijau botol #00120f → #0d2a22 · teks krem #ece6cf · aksen 1 emas #d9a63a (hadiah, juara) · aksen 2 merah anggur #b3122e (taruhan, "TIDAK") · satu sisipan panas: gradasi termal jingga-merah untuk siluet |
| Transisi | potong cepat di kata; siluet termal → kertas krem; kabur lensa antar kalimat; uang/konfeti melintas menutupi potongan; bingkai jendela bidik kamera (REC) |
| Tekstur | bersih + grain halus; kilau emas; kedalaman lewat konfeti kabur di depan lensa |
| Kamera | dorong cepat 0,3–0,5 dtk ke subjek, lalu diam; konfeti di `z` besar memberi parallax |
| Bahasa animasi | tegas: outExpo 0,35–0,5 dtk, overshoot 6–10% pada piala/kepalan; huruf raksasa naik dari bawah di belakang subjek |
| Bunyi | hantaman sinematik pendek di tiap kata besar, sorak/tepuk tangan tipis, gemerincing koin, riser 1 dtk sebelum hadiah disebut |
| Tempo | cepat: ±1,5 dtk per bidikan; potongan ikut kata pengumuman |
| Komposisi | subjek tengah menutupi sebagian huruf raksasa (teks di belakang subjek); banyak ruang gelap; satu sumber cahaya hangat |
| Cocok untuk | pengumuman, giveaway, peringkat/juara, pencapaian, peluncuran produk, kompetisi, olahraga, "siapa paling…" |

## 2. Prinsip yang dipelajari (bukti → prinsip)
- **Siluet termal sebagai misteri** — bukti 0–2 dtk: sosok berwarna peta panas jingga-merah, kata-kata kecil di sekitarnya. Subjek dikenalkan tanpa wajah = rasa penasaran + gaya.
- **Judul di atas kertas krem dengan coretan** — bukti 2,5–3,5 dtk: nama acara merah tebal, garis tangan merah melingkar. Satu bidikan "terang" di tengah dunia gelap = kartu nama acara.
- **Kepalan/piala muncul bersama angka besar** — bukti 4,5–7 dtk: kepalan hijau naik di depan angka hadiah raksasa yang kabur, konfeti. Angka dibuat setengah tertutup supaya mata mencari.
- **Satu kata raksasa sendirian** — bukti 9–10 dtk: "FREE" serif putih di hitam, lalu "sounds too good to be true?" dengan kata terakhir hijau. Pola klaim → keraguan penonton diucapkan duluan.
- **Huruf raksasa di belakang subjek** — bukti 12–13,5 dtk ("NOT" merah di belakang sosok bertopeng, uang beterbangan) dan 15,5–19,5 dtk ("LIVE" merah di belakang patung, bingkai REC). Kedalaman tiga lapis: huruf → subjek → partikel.
- **Emas untuk payoff** — bukti 14–15 dtk: "TALENT" emas logam + piala diangkat + tangan meraih + konfeti emas. Warna emas ditahan untuk satu kata terpenting.

## 3. Tata bahasa adegan
| Beat | Visual khas | Teks | Transisi masuk | Bunyi |
|---|---|---|---|---|
| Hook | siluet termal/subjek misterius | 2–3 kata kecil melayang | `fokus` | dengung + napas |
| Nama | kertas krem + judul merah + coretan | nama acara/produk | potong + `kilat` warna krem | gores spidol |
| Taruhan | subjek/benda naik + angka besar setengah tertutup | angka hadiah | `terbang` dari bawah | riser → impact |
| Klaim | satu kata raksasa di hitam | 1 kata | potong keras di ketukan | boom pendek |
| Keraguan | kalimat tipis, kata terakhir berwarna | pertanyaan | `fokus` | hening 0,3 dtk |
| Pembalik | huruf raksasa di belakang subjek + partikel | "BUKAN …" | `sentak` | whoosh + koin |
| Payoff | emas + piala + konfeti | 1 kata emas | `dorong` | sorak tipis + boom |
| Ajakan | hitam, kalimat kecil (di deskripsi, bukan narasi) | — | `lebur` | ekor gema |

## 4. Preset mesin Kolase
**Sejak 27 Nov 2026 gaya ini tertanam di mesin `skill-edit-rizky`: cukup `tema: 'panggung-emas'`** (grade, warna aksen, latar bawaan, dan gaya huruf ikut otomatis; musik tetap ditulis sendiri). Blok di bawah = rincian nilainya, dipakai untuk menimpa sebagian atau sebagai contoh lapisan.
```js
const KONFIG = {
  judul: '…', tema: 'modern',
  grade: { tint: '#ffe6b0', kuat: .06, saturasi: 1.05, halftone: 0, grain: .05, vinyet: .55, debu: 0, garis: 0, kontras: .22 },
  palet: { kuning: '#d9a63a', merah: '#b3122e', stabilo: 'rgba(217,166,58,.6)' },
  gayaTeks: {
    elegan: { font: 'Georgia,"Times New Roman",serif', gaya: '700', warna: '#ece6cf', kapital: true, bayang: false },   // huruf raksasa
    judul:  { font: '"KR Inter","Inter",sans-serif', gaya: '500', warna: '#ece6cf', kapital: false, bayang: true }      // pengantar tipis
  },
  musik: { sintesis: 'tegang', bpm: 104 },
  sumber: [/* wajib bila ada klaim */]
};
// huruf di belakang subjek (urutan lapis: latar -> teks -> subjek -> partikel):
// lapis: [ { gambar: 'latar-gelap' }, { teks: 'BUKAN', gaya: 'elegan', ukuran: 360, warna: '#b3122e', y: 620, masuk: { gaya: 'naik' } },
//          { gambar: 'sosok', y: 1150, tinggi: 1500, jangkar: 'bawah', rig: 'napas' } ]
// efek: [{ jenis: 'partikel', gaya: 'konfeti', t: 'L03.w2', akhir: 'L03.akhir', dari: [540, 1700] }, { jenis: 'kilau', t: 'L06.w1', titik: [540, 820] }]
// bingkai jendela bidik: benda kustom (sudut-sudut putih + titik REC merah + timecode)
// emas logam: kilap pada lapisan teks/benda: kilap: { t: 'L06.w1', warna: '#fff3c4', kuat: .7 }
```
Celah mesin: siluet peta panas (akali: potongan Flow latar hijau diwarnai gradasi jingga-merah lewat prompt "thermal camera heat map silhouette", atau grade per adegan `{ jenis: 'warna' }` merah + `hue`); teks emas bergradasi logam (akali: warna emas + `kilap` + bayangan gelap; gradasi isi butuh `kustom`); konfeti di depan lensa yang kabur (partikel ada, blur per kedalaman belum → akali: potongan konfeti PNG `z: 2.2` + `blur`).

## 5. Dipakai untuk topik lain
| Topik | Penerapan |
|---|---|
| Peringkat 5 orang terkaya Indonesia | siluet termal tiap tokoh (tanpa wajah AI), angka harta raksasa setengah tertutup, emas untuk peringkat 1 |
| Pengumuman giveaway channel | piala/hadiah naik, "GRATIS?" lalu keraguan, "BUKAN UNTUK SEMUA" merah di belakang subjek |
| Kemenangan timnas / atlet | kepalan dan piala, konfeti, satu kata emas "JUARA", jendela bidik siaran |
| Peluncuran produk UMKM | produk di sorot, harga raksasa di belakang, emas untuk fitur utama |
| "Gaji tertinggi di Indonesia" | angka raksasa, keraguan "masuk akal?", pembalik syaratnya |

## 6. Variasi supaya tidak seragam
- Latar: hijau botol · biru tinta · hitam beludru (emas tetap aksen).
- Partikel: konfeti · uang · kelopak — sesuai topik.
- Subjek misterius: siluet termal · siluet hitam berbingkai cahaya · tangan saja.

## 7. Jangan disalin
- Nama acara, nominal hadiah, kalimat ("sounds too good to be true?"), sosok bertopeng berlogo, dan kartu penutup akun acuan.
- Wajah orang kaya/atlet nyata tidak dibuat AI; pakai foto berlisensi atau siluet.

## Cek cepat
- [ ] Emas dipakai hanya untuk satu kata/benda payoff
- [ ] Minimal satu huruf raksasa di belakang subjek (tiga lapis kedalaman)
- [ ] Penonton diberi keraguan sebelum jawaban
- [ ] Tempo cepat tapi ada satu jeda 0,3 dtk sebelum payoff
- [ ] Partikel tidak menutupi angka/teks utama
