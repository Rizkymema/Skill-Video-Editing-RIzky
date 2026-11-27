# Resep: Legenda Gelap

> Asal belajar: @earn.edits reel `DfIJjwfuKGL` (30 Okt 2026, 41,9 dtk, 9:16, asal-usul Halloween/Samhain) · angka bedah: 9 potongan, rata bidikan 4,2 dtk, **0%** potongan di ketukan (BPM ±89, dua lonjakan musik di 22,2 dan 36,3 dtk), kesan "gelap berwarna kuat", palet #231e1d #76524b #521f14 #b1b4ab · lembar: `D:\automation\Video AI\Video Refrensi\earn.edits\reel-2026-11-27\bedah\DfIJjwfuKGL\acuan\`
> Terdekat dengan gaya: Psychological/Dark + Collage (`../gaya-visual.md`) · mesin: `skill-edit-rizky` (Kolase)

Satu kalimat: dongeng gelap yang dijelaskan seperti penyidik sejarah, api jingga dan cahaya bulan biru berganti-ganti, papan tulis kapur dengan foto-foto yang disematkan tali merah, dan huruf yang terasa "dicakar".

## 1. DNA (10 atribut)
| Atribut | Isi |
|---|---|
| Tipografi | judul display bergelombang/terdistorsi kuning-jingga (akali: Anton + `rig` kibar halus); serif kecil miring sebagai anak judul; kata tabu disensor dengan tanda bintang ("MATI" → "M*TI") merah besar; angka tulisan kapur dalam kotak gambar tangan |
| Warna | latar arang #1d1a19 · teks krem #ece4d4 · aksen 1 jingga api #e8641c (dunia manusia/perayaan) · aksen 2 biru bulan #9fb6d8 (dunia arwah/dingin) · merah #d11f1f hanya untuk kata tabu |
| Transisi | lensa bulat (foto dalam lingkaran yang membesar jadi adegan); **lingkungan sama, musim berganti** (padang hijau → salju); lingkaran terbelah dua dunia; sapuan pola heksagon; bayangan kelelawar/jaring menutup layar |
| Tekstur | papan tulis/beton gelap berbutir, kabut rendah, bara/abu melayang (partikel ringan), polaroid kertas |
| Kamera | dorong pelan ke pusat yang menyeramkan (lubang kubur, api); tarik untuk memperlihatkan kerumunan; kamera hampir tidak pernah cepat |
| Bahasa animasi | masuk berat dan lambat (outQuart 0,6–0,8 dtk), judul masuk dengan kabur gerak dari dekat lensa (`terbang`), polaroid berayun di tali |
| Bunyi | angin, api berderak, dengung rendah, bisikan samar; hantaman dalam (sub-boom) hanya di 2 lonjakan musik; kertas/foto disematkan |
| Tempo | bidikan panjang (±4 dtk) yang selalu bergerak pelan; potongan ikut kalimat, tidak ikut ketukan; dua puncak energi menandai babak |
| Komposisi | pusat simetris untuk benda keramat (kubur, api, bulan); teks di sepertiga atas; papan investigasi dengan diagonal tali merah |
| Cocok untuk | asal-usul tradisi, mitos & legenda Nusantara, sejarah kelam, takhayul, kisah misteri, "kenapa kita melakukan X" |

## 2. Prinsip yang dipelajari (bukti → prinsip)
- **Judul membuka dua dunia** — bukti 0–2,5 dtk: bulan merah dan gerbang kuburan, judul display, lalu "wasn't always about candy and costumes" di bawahnya. Hook = kontras antara yang dikenal (pesta) dan yang tersembunyi (ketakutan).
- **Sensor kata sebagai penekanan** — bukti 5,0–6,5 dtk: "FEARED THE DE*D" merah besar. Bintang membuat penonton membaca dua kali; tabu terasa lebih berat.
- **Waktu ditulis kapur** — bukti 7,0–8,5 dtk: "2.000 YEARS AGO" merah di dalam kotak gambar tangan di papan gelap. Lompatan zaman terasa seperti catatan peneliti.
- **Papan investigasi berjalan** — bukti 8,5–10,5 dtk: polaroid disematkan dengan tali merah, kamera menggeser sepanjang tali sementara judul berjalan. Satu gerakan kamera = satu rantai sebab.
- **Lingkungan sama, isi berubah** — bukti 10,5–13,5 dtk: lingkaran lensa membesar menjadi lembah hijau, lalu lembah yang sama jadi musim dingin. "Akhir musim panas → awal musim dingin" dibuktikan dengan gambar, bukan teks.
- **Satu bentuk untuk dua dunia** — bukti 14–17 dtk: lingkaran terbelah (kiri api/manusia, kanan biru/arwah) dengan garis cahaya di tengah = "batas antara yang hidup dan yang mati".
- **Hamparan menutup babak** — bukti 22,5–23,5 dtk: jaring laba-laba + kelelawar jingga naik menutup layar, lalu satu kata tipis "TRADITIONS / BLENDED". Penutup babak ditandai tekstur, bukan potong keras.

## 3. Tata bahasa adegan
| Beat | Visual khas | Teks | Transisi masuk | Bunyi |
|---|---|---|---|---|
| Hook | bulan + gerbang/benda keramat, kabut | judul display + anak judul serif | judul `terbang` dari lensa | angin + dengung |
| Pembalik | adegan kelam (kubur, sesaji, orang ketakutan) | kata tabu disensor merah | `fokus` | sub-boom pelan |
| Zaman | papan tulis gelap | angka kapur dalam kotak | potong + hening 0,3 dtk | kapur menggores |
| Rantai sebab | polaroid di tali merah, kamera menyusur | judul berjalan | `geser` sepanjang tali | kertas + jepit |
| Bukti alam | lensa bulat → lanskap → lanskap berubah musim | pil caption kecil | `bingkai` bentuk `bulat` / `cocok` | angin berganti |
| Konsep inti | lingkaran terbelah dua dunia | serif kecil + kata kunci merah | `iris` | dengung naik |
| Babak 2 | api unggun, kerumunan bertopeng | judul tebal krem | `tutup` | api berderak |
| Penutup | hamparan jaring/kelelawar, satu kata | kata tipis | `bakar` / partikel menutup | hening lalu satu nada |

## 4. Preset mesin Kolase
```js
const KONFIG = {
  judul: '…', tema: 'dosir',
  grade: { tint: '#e8a46a', kuat: .14, saturasi: .9, halftone: .06, grain: .09, vinyet: .58, debu: .35, garis: 0, kontras: .22 },
  palet: { kuning: '#f0a23a', merah: '#d11f1f', stabilo: 'rgba(209,31,31,.6)', kertas: '#ece4d4' },
  gayaTeks: {
    judul: { warna: '#f3c44a', bayang: true },               // judul display (Archivo) kuning api
    elegan: { warna: '#ece4d4' },                              // anak judul serif miring
    tangan: { warna: '#ece4d4' }                               // tulisan kapur
  },
  musik: { sintesis: 'misteri', bpm: 76 },
  sumber: [/* wajib */]
};
// papan kapur: latar: { pola: 'kertas', warna: '#26231f', tua: .8 }
// kata tabu: { teks: '^M*TI^', gaya: 'padat', warna: '#d11f1f', masuk: 'cap' }   (bintang ditulis biasa; penanda *…* jangan dipakai di kata ini)
// kotak kapur: { coret: 'kotak', x: 540, y: 980, lebar: 520, tinggi: 200, warna: 'putih', tebal: 7, t: .3 }
// polaroid di tali: { benda: { jenis: 'kartu', gambar: 'ritual', keterangan: 'ABAD KE-5' }, ayun: { sudut: 8, periode: 1.6 }, bayangan: true } + { coret: 'garis', warna: 'merah' }
// lingkungan berganti musim: dua pelat Flow dari prompt + acuan gambar yang sama, masuk: 'fokus' atau 'lebur' (bukan geser)
// suasana: efek: [{ jenis: 'partikel', gaya: 'abu', t: 0, akhir: 4 }, { jenis: 'kabut', y: .78, kuat: .5 }]
```
Celah mesin: huruf display bergelombang (akali: `rig: { jenis: 'kibar', amp: .012 }` pada teks yang dirender sebagai gambar, atau judul dibuat sebagai potongan PNG dari Flow tanpa teks + teks mesin di atasnya); lingkaran terbelah dua (akali: dua lapisan `panel` setengah lingkaran tidak bisa → benda `kustom` yang menggambar dua gambar ber-clip busur); sapuan pola heksagon (akali: `strip` atau `bingkai` bentuk `peti`).

## 5. Dipakai untuk topik lain
| Topik | Penerapan |
|---|---|
| Asal-usul malam 1 Suro | bulan + keris/sesaji, kata tabu disensor, papan kapur "ABAD KE-16", lanskap desa siang → malam |
| Mitos kuntilanak & pohon | pohon sama di siang dan malam (lingkungan berubah), papan rantai sebab cerita dari mulut ke mulut |
| Sejarah wabah | lensa bulat ke kota, polaroid korban (arsip berlisensi), lingkaran terbelah "sehat/sakit" |
| Psikologi rasa takut | lingkaran terbelah "otak tenang/otak panik", api ↔ biru sebagai dua sistem saraf |
| Kebiasaan aneh tahun baru | perayaan meriah → asal-usul kelam, dua lonjakan musik di dua pembalik |

## 6. Variasi supaya tidak seragam
- Pasangan dunia: api/bulan · darah/tulang · tanah/kabut — selalu dua warna yang punya arti.
- Media bukti: polaroid · daun lontar · peta tua.
- Penutup: kelelawar · kunang-kunang yang padam · pintu yang menutup.

## 7. Jangan disalin
- Gambar labu, tokoh berkostum, dan susunan adegan Halloween reel itu; huruf judulnya; kalimat narasinya.
- Untuk legenda Nusantara: jangan mengolok kepercayaan; bedakan "dipercaya" dan "tercatat" (sumber).

## Cek cepat
- [ ] Dua warna dunia (hangat vs dingin) dipakai konsisten sebagai makna
- [ ] Satu kata tabu disensor, tidak lebih dari 2× per video
- [ ] Setiap lompatan zaman ditulis di papan/kapur, bukan teks melayang biasa
- [ ] Minimal satu bukti "lingkungan sama, isi berubah"
- [ ] Potongan ikut kalimat; dentuman hanya di 2 puncak cerita
- [ ] Partikel/kabut ≤ 30% durasi, tidak menutupi teks
