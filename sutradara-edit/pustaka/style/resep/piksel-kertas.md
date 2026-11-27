# Resep: Piksel Kertas

> Asal belajar: @earn.edits reel `DfEv7DuOgYT` (29 Okt 2026, 39,5 dtk, 9:16, ajakan komunitas editor "Editing Alone") · angka bedah: 12 potongan, rata bidikan 3,0 dtk, 25% potongan di ketukan (BPM ±90, lonjakan di 10,9 dan 18,3 dtk), kesan "gelap berwarna kuat + vinyet", palet #080904 #1c290b #d6c094 #907855 · lembar: `D:\automation\Video AI\Video Refrensi\earn.edits\reel-2026-11-27\bedah\DfEv7DuOgYT\acuan\`
> Terdekat dengan gaya: Handcrafted/Organic + Experimental Motion Graphics, sentuhan Y2K/retro game (`../gaya-visual.md`) · mesin: `skill-edit-rizky` (Kolase)

Satu kalimat: ilustrasi potongan kertas di atas kertas zaitun gelap, huruf ala gim 8-bit merah-putih, komputer jadul sebagai panggung, dan metafora benda yang sangat jelas (manusia di dalam toples kaca = kesepian) untuk topik pekerjaan dan perasaan sehari-hari.

## 1. DNA (10 atribut)
| Atribut | Isi |
|---|---|
| Tipografi | display ber-piksel/kotak putih-krem dengan bayangan blok; kata kunci di **pita merah** berpiksel; teks pendukung sans tebal kecil; tulisan "salah eja" disengaja untuk rasa buatan tangan (opsional, hati-hati) |
| Warna | latar zaitun gelap #1c290b / krem kertas #d6c094 · teks krem #efe6cf · aksen 1 merah #d62a1e (lengan baju, pita, peringatan) · aksen 2 kuning #f2c230 (solusi, sorot, piala) |
| Transisi | **luruh piksel** (gambar pecah jadi kotak lalu tersusun jadi adegan baru); tirai kertas; sorot lampu yang membuka adegan; benda tergantung turun dari atas |
| Tekstur | kertas bertekstur + vinyet kuat, halftone halus, butir; tepi potongan sedikit tidak rapi |
| Kamera | hampir datar (2D), dorong kecil ke benda pusat; geser horizontal untuk "jalan sendirian" |
| Bahasa animasi | **patah-patah / on twos** (gerak 12–15 fps terasa buatan tangan), pop dengan overshoot 8–12%, benda tergantung berayun, garis kecepatan horizontal |
| Bunyi | bunyi gim 8-bit hemat (blip saat kata muncul, nada naik saat "solved"), ketik keyboard mekanis, kertas; musik lo-fi/chip pelan |
| Tempo | ±3 dtk, tiap adegan punya satu aksi jelas (mengetik, berjalan, layar error → centang) |
| Komposisi | satu benda pusat besar di tengah-bawah, judul atas, banyak ruang gelap; tangan/lengan masuk dari tepi |
| Cocok untuk | produktivitas, karier, kesehatan mental kerja, komunitas, tips belajar, teknologi untuk pemula, gaming, cerita relatable |

## 2. Prinsip yang dipelajari (bukti → prinsip)
- **Tangan kertas sebagai subjek** — bukti 0–1,5 dtk: dua tangan potongan kertas berlengan merah mengetik di keyboard jadul. Manusia tanpa wajah = penonton bisa memasukkan dirinya.
- **Metafora harfiah satu benda** — bukti 8–10 dtk: editor mungil di dalam toples kaca tergantung; toples kedua turun di sebelahnya. "Sendirian" dan "ada teman" dijelaskan tanpa kata.
- **Masalah → solusi di layar yang sama** — bukti 11–13,5 dtk: monitor penuh jendela error, lalu layar kuning dengan centang "SOLVED". Satu benda, dua keadaan = before/after paling murah dan paling jelas.
- **Kata kunci di pita merah** — bukti 1–12 dtk: "ALONE", "EDITORES", "ASK" di pita/kotak merah di bawah kata pengantar krem. Hierarki: pengantar kecil → kata merah.
- **Kertas catatan robek + kaca pembesar** — bukti 14,5–16 dtk: daftar pertanyaan di kertas sobek, kaca pembesar menyapu. Daftar langkah jadi benda, bukan bullet.
- **Sorot lampu untuk emosi** — bukti 18,5–21 dtk: figur piksel duduk memeluk lutut di bawah sorot; tangan bayangan datang. Bagian sedih diberi ruang gelap luas dan gerak paling lambat.
- **Ujung dengan piala berpiksel di sorot kuning** — bukti 22,5–23,5 dtk: payoff = warna aksen kedua yang ditahan sejak awal.

## 3. Tata bahasa adegan
| Beat | Visual khas | Teks | Transisi masuk | Bunyi |
|---|---|---|---|---|
| Hook | tangan kertas + benda jadul di latar gelap | 2 kata: krem + pita merah | luruh piksel | ketik + blip |
| Masalah | figur berjalan sendiri / layar error | pengantar + kata merah | `geser` horizontal + garis gerak | langkah, buzz error |
| Metafora | benda kaca/kotak/kurungan berisi tokoh mungil | "made for …" | benda `jatuh`/turun berayun | denting kaca |
| Solusi | layar yang sama berubah jadi centang kuning | "SOLVED" / "kami bantu" | potong di layar (`cocok`) | nada naik 8-bit |
| Daftar | kertas catatan sobek bernomor + kaca pembesar | judul 2 baris | `tutup` | kertas |
| Bukti sosial | gelembung komentar kertas muncul berurutan | — | pop berjenjang 0,15 dtk | pop kecil |
| Emosi | figur di bawah sorot, ruang gelap | 1 kalimat lambat | `fokus` | hening + dengung |
| Payoff | benda emas/kuning di sorot | judul + pita | luruh piksel | nada kemenangan pendek |

## 4. Preset mesin Kolase
```js
const KONFIG = {
  judul: '…', tema: 'kartu',
  grade: { tint: '#d9c08a', kuat: .1, saturasi: .92, halftone: .1, grain: .09, vinyet: .6, debu: .2, garis: 0, kontras: .16 },
  palet: { kuning: '#f2c230', merah: '#d62a1e', stabilo: 'rgba(242,194,48,.7)', kertas: '#d6c094' },
  gayaTeks: {
    judul: { font: '"KR Archivo","Archivo Black",sans-serif', warna: '#efe6cf', kapital: true, bayang: true },
    stiker: { kotak: '#d62a1e', tepiKotak: '#d62a1e', warna: '#ffffff' }   // pita merah tanpa tepi putih
  },
  musik: { sintesis: 'jenaka', bpm: 92 },
  bunyiMuncul: { teks: 'blip', gambar: 'pop', vol: .45 },   // berkas dari rakit --sfx (blip 8-bit pendek)
  sumber: [/* wajib bila ada klaim; KONFIG.data: false untuk video tanpa fakta */]
};
// latar zaitun: latar: { pola: 'kertas', warna: '#26351a', tua: .7 }   ·  latar krem: { pola: 'kertas', warna: '#d6c094', tua: .5 }
// pengantar + pita: { teks: 'made for', gaya: 'judul', ukuran: 58, y: 1180 }, { teks: 'EDITOR', gaya: 'stiker', y: 1270, masuk: 'pop' }
// toples tergantung: potongan Flow latar hijau + ayun: { sudut: 6, periode: 2.2 } + masuk: { gaya: 'jatuh', dari: 'atas' }
// error -> centang: benda kustom di layar monitor, atau dua lapisan gambar di posisi sama + masuk: 'cocok'
// gerak patah-patah: gerak keyframe dengan easing fungsi tangga: ease: x => Math.floor(x * 8) / 8
```
Celah mesin: huruf piksel (akali: Anton/Archivo + `bayang` keras, atau judul digambar `kustom` per kotak 12 px); perpindahan luruh piksel (akali: `strip` + `glitch` pendek, atau `kustom` yang menggambar adegan baru per blok berurutan); on twos global (akali: easing fungsi tangga per lapisan; usul `KONFIG.patah: 12`).

## 5. Dipakai untuk topik lain
| Topik | Penerapan |
|---|---|
| Burnout kerja | tangan kertas mengetik makin cepat, toples kaca penuh sticky note, layar error → istirahat (centang kuning) |
| Tips belajar efektif | catatan sobek bernomor + kaca pembesar, figur piksel naik tangga level, piala di akhir |
| Cara kerja algoritma | komputer jadul yang memilih kartu-kartu kertas, pita merah "KAMU" |
| Sejarah gim Indonesia | konsol jadul, figur piksel, papan skor — cocok penuh |
| Literasi keuangan pemula | celengan kertas, dompet kosong di sorot, nota sobek bernomor |

## 6. Variasi supaya tidak seragam
- Warna kertas latar: zaitun · biru tinta · merah bata (satu per seri).
- Benda panggung: komputer jadul · konsol gim · mesin kasir.
- Tingkat piksel: hanya judul (ringan) · judul + transisi · seluruh tokoh (penuh).

## 7. Jangan disalin
- Figur, toples, piala, kalimat ("Editing Alone", "made for editores"), dan logo komunitas akun acuan.
- Jangan pakai salah eja disengaja di topik serius/data; hanya untuk nada santai.

## Cek cepat
- [ ] Satu metafora benda yang bisa dipahami tanpa narasi
- [ ] Masalah dan solusi ditunjukkan di benda yang sama
- [ ] Kuning ditahan untuk payoff
- [ ] Bunyi 8-bit hemat (≤ 1 per 2 dtk), tidak di setiap kata
- [ ] Gerak patah-patah konsisten (jangan campur dengan gerak super halus di adegan yang sama)
