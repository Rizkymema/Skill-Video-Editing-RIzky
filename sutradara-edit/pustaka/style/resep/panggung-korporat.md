# Resep: Panggung Korporat

> Asal belajar: @earn.edits reel `DgH9MT_ICph` (24 Nov 2026, 47,5 dtk, 9:16, naik-turunnya produsen ponsel terbesar) · angka bedah: 10 potongan, rata bidikan **4,3 dtk**, 10% potongan di ketukan (ketukan musik tidak jelas), kesan "sedang berwarna lembut", palet #111519 #9d9590 #c8d2d6 #e8e4da · lembar: `D:\automation\Video AI\Video Refrensi\earn.edits\reel-2026-11-27\bedah\DgH9MT_ICph\acuan\`
> Terdekat dengan gaya: Cinematic Editorial + Corporate Premium + Documentary (`../gaya-visual.md`) · mesin: `skill-edit-rizky` (Kolase)

Satu kalimat: kisah bangkit dan jatuhnya perusahaan/negara/tokoh yang diceritakan dengan **warna sebagai kekuasaan**: dunia abu-abu, sang raksasa berwarna merek, grafik batang 3D di kertas grafik, dokumen yang dicoret spidol, lalu panggung gelap tempat pesaing muncul.

## 1. DNA (10 atribut)
| Atribut | Isi |
|---|---|
| Tipografi | **pita/spanduk miring** bertumpuk dengan huruf padat kapital (oranye-kuning bergradasi) untuk gelar; angka uang besar kuning miring dengan bayangan merah; tahun hitam besar di kertas grafik; kalimat kesimpulan sans tipis 2 bobot ("The World's No.1 / Mobile Brand.") |
| Warna | dunia abu/hitam-putih #9d9590 · teks putih/hitam sesuai latar · aksen 1 **warna merek subjek** (mis. merah #d8261c — kekuasaan) · aksen 2 biru #2a59c9 untuk pembanding di grafik · panggung gelap #111519 untuk babak pesaing |
| Transisi | langit → gedung naik dari bawah (`tarik` ke atas); **warna berubah di benda yang sama** (gedung abu → merah saat diakuisisi/berkuasa); kertas grafik geser ke meja dokumen; layar gelap panggung dengan logo samar; produk di sorot abu |
| Tekstur | langit dramatis berawan dengan burung; kertas grafik krem; kertas dokumen kusut; sorot lampu di panggung |
| Kamera | naik (tilt up) memperlihatkan gedung; dorong ke jabat tangan; tetap di grafik saat batang tumbuh; dorong pelan ke pembicara di panggung |
| Bahasa animasi | batang grafik tumbuh dengan **overshoot** lalu menetap; pita judul masuk satu per satu dengan sedikit miring; tangan spidol menggaris baris tabel |
| Bunyi | angin/kota di pembuka, impact berat di angka uang, gesekan spidol, gemuruh penonton samar di panggung, nada menurun di kejatuhan |
| Tempo | lambat-berwibawa: ±4,3 dtk per bidikan, banyak gerak di dalam bidikan (batang tumbuh, spidol menggores) |
| Komposisi | gedung/produk di tengah dengan banyak langit; grafik dua batang kiri-kanan dengan label tag; dokumen memenuhi bingkai dengan tangan masuk dari kanan bawah |
| Cocok untuk | sejarah perusahaan, naik-turun merek, keputusan CEO, persaingan dua raksasa, ekonomi negara, karier tokoh, "kenapa X bangkrut" |

## 2. Prinsip yang dipelajari (bukti → prinsip)
- **Bangun dari langit** — bukti 0–2 dtk: langit biru kosong, gedung naik dari bawah, pita gelar bertumpuk muncul satu per satu. Hook = memperlihatkan kebesaran sebelum menyebut nama.
- **Warna sebagai kekuasaan** — bukti 2,5–6 dtk: dunia jadi hitam-putih, gedung berubah merah merek, dua tokoh berjabat tangan, angka miliar kuning besar. Perubahan pemilik/kekuasaan ditunjukkan dengan warna, bukan teks.
- **Grafik sebagai adegan** — bukti 6,5–12,5 dtk: tahun di kertas grafik, dua batang 3D dengan label tag tumbuh (satu jauh lebih tinggi), kesimpulan tipis di samping. Angka diperlihatkan sebagai perlombaan.
- **Dokumen + tangan spidol** — bukti 13–17 dtk: kertas siaran pers kusut di meja grid, tangan dengan spidol merah menggaris baris tabel. Bukti terasa diperiksa manusia.
- **Panggung gelap untuk pesaing** — bukti 17,5–22 dtk: pembicara di panggung gelap dengan nama produk besar di latar, lalu logo pesaing lain dengan kartu berita miring. Babak "ancaman datang" punya ruang sendiri: gelap, sorot, lambat.
- **Produk di sorot abu** — bukti 22,5–23,5 dtk: ponsel-ponsel di permukaan abu dengan sorot. Benda yang kalah diperlihatkan sunyi.

## 3. Tata bahasa adegan
| Beat | Visual khas | Teks | Transisi masuk | Bunyi |
|---|---|---|---|---|
| Hook | langit → gedung/benda naik | pita gelar bertumpuk | `tarik` ke atas / kamera `naik` | angin + impact |
| Puncak kuasa | dunia hitam-putih, subjek berwarna merek, jabat tangan | angka uang besar kuning | potong + perubahan warna (`warna` efek berakhir) | boom |
| Bukti angka | kertas grafik: tahun → dua batang tumbuh | tahun + label tag + kesimpulan tipis | `geser` ke bawah | gulir angka |
| Dokumen | kertas kusut + tangan spidol | — (coretan) | `tutup` | spidol |
| Ancaman | panggung gelap + pembicara (siluet bila tokoh nyata) | nama produk/gagasan pesaing | `fokus` | gemuruh penonton samar |
| Kejatuhan | subjek kembali abu, grafik menurun | angka turun | `cocok` (benda sama, warna hilang) | nada turun |
| Penutup | produk/gedung di sorot sunyi | 1 kalimat vonis | `lebur` lambat | hening + satu nada |

## 4. Preset mesin Kolase
**Sejak 27 Nov 2026 gaya ini tertanam di mesin `skill-edit-rizky`: cukup `tema: 'panggung-korporat'`** (grade, warna aksen, latar bawaan, dan gaya huruf ikut otomatis; musik tetap ditulis sendiri). Blok di bawah = rincian nilainya, dipakai untuk menimpa sebagian atau sebagai contoh lapisan.
```js
const KONFIG = {
  judul: '…', tema: 'modern',
  grade: { tint: '#e9ecef', kuat: .05, saturasi: .9, halftone: 0, grain: .06, vinyet: .42, debu: .05, garis: 0, kontras: .2 },
  palet: { kuning: '#f2b632', merah: '#d8261c', biru: '#2a59c9', stabilo: 'rgba(216,38,28,.45)' },
  gayaTeks: {
    stiker: { font: '"KR Anton","Anton",sans-serif', kotak: '#e8792b', tepiKotak: '#f2b632', warna: '#2a1a0a' },   // pita gelar
    padat:  { warna: '#f2b632', bayang: true },                                                              // angka uang
    serif:  { font: '"KR Inter","Inter",sans-serif', gaya: '300', warna: '#1d1d1f' },                         // kesimpulan tipis
    tebal:  { warna: '#1d1d1f' }
  },
  musik: { sintesis: 'dokumenter', bpm: 84 },
  sumber: [/* wajib: angka penjualan, nilai akuisisi, tanggal */]
};
// warna selektif = kekuasaan: { gambar: 'kota', hitamPutih: true } + { gambar: 'gedung-merah' } berwarna
//   atau efek: [{ jenis: 'warna', t: 0, akhir: 'L03.w2', warna: '#888' }] lalu warna kembali tepat di kata kunci
// pita bertumpuk: 3 lapisan teks gaya 'stiker', putar -5..-3, t berjenjang .15 dtk, masuk: { gaya: 'geser', dari: 'kiri' }
// angka uang: { angka: { dari: 0, ke: 7.2, lama: 1.2, awal: 'US$', akhir: ' MILIAR' }, gaya: 'padat', putar: -4 }
// grafik: latar: { pola: 'grid', warna: '#eeeae0', warnaGaris: 'rgba(0,0,0,.08)', jarak: 44 }
//   { benda: { jenis: 'grafik', bentuk: 'batang', data: [40, 15], label: ['MEREK A', 'MEREK B'], satuan: '%', t: .3, lama: 1.6 } }
// dokumen + spidol: { benda: { jenis: 'dokumen', … , sorot: [{ baris: 3, t: .8, warna: 'merah' }] } } + potongan tangan Flow masuk dari kanan bawah (jangkar)
```
Celah mesin: batang grafik 3D bervolume (akali: grafik batang biasa + `rig: 'miring'` sedikit + bayangan; atau `kustom` dengan sisi samping lebih gelap); pita miring bergradasi oranye (akali: `stiker` warna rata + `kilap`); perubahan warna satu benda di tempat (akali: dua lapisan gambar yang sama — hitam-putih dan berwarna — dengan `alfa` keyframe).

## 5. Dipakai untuk topik lain
| Topik | Penerapan |
|---|---|
| Naik-turun maskapai/perusahaan BUMN (data publik) | gedung kantor berwarna merek generik, grafik penumpang, dokumen laporan dicoret, panggung "pesaing" |
| Era warnet ke era HP | kota abu, warnet berwarna, batang "warnet vs ponsel" bertukar posisi |
| Kejatuhan pemutar musik portabel | produk di sorot abu sebagai penutup |
| Persaingan dua klub sepak bola | dua warna klub di grafik, stadion abu dengan satu sisi berwarna |
| Ekonomi negara (inflasi era tertentu) | gedung bank sentral, angka uang, grafik inflasi, dokumen kebijakan |

## 6. Variasi supaya tidak seragam
- Warna kuasa: merah · biru · hijau — **selalu warna merek/identitas subjek**, generik bila merek nyata.
- Bukti: grafik batang · garis waktu · tabel di dokumen.
- Babak pesaing: panggung gelap · ruang rapat kaca · layar berita.

## 7. Jangan disalin
- Logo dan nama merek nyata (ponsel, OS, mesin pencari), foto tokoh nyata buatan AI, dokumen siaran pers asli tanpa sumber.
- Untuk merek nyata: sebut di narasi, tampilkan benda generik atau foto berlisensi; angka wajib bersumber (`skill-edit-rizky/references/riset.md`).

## Cek cepat
- [ ] Warna merek hanya pada subjek dan hanya saat ia berkuasa
- [ ] Setiap angka besar punya grafik atau dokumen bukti
- [ ] Babak pesaing punya ruang visual berbeda (gelap, sorot)
- [ ] Kejatuhan diperlihatkan dengan warna/gerak yang hilang, bukan teks "bangkrut" saja
- [ ] Tidak ada logo nyata digambar ulang
