# Storytelling: video sebagai cerita, bukan kumpulan footage

> STORY · dipakai di langkah 1–3, 5, 6 · terkait: `../short-form/short-form.md`, `../visual/metafora.md`, `../core/editing.md`, `../motion/transisi.md`, pola cerita mesin di `skill-edit-rizky/references/gaya.md` §0.2

Prinsip inti:
1. **Cerita = perubahan.** Ada keadaan awal, sesuatu mengganggu, keadaan akhir berbeda. Tanpa perubahan, yang ada hanya daftar fakta.
2. **Gambar bercerita lebih dulu, narasi melengkapi.** Kalau suara dimatikan, penonton tetap harus menangkap alurnya dari gerak, benda, dan teks kunci.
3. **Pertanyaan menahan, jawaban melepas.** Buka pertanyaan lebih cepat daripada menjawabnya; jawab tepat sebelum penonton menyerah.
4. **Satu emosi utama per video**, dengan satu belokan (kaget → paham, geram → lega).
5. **Spesifik mengalahkan umum.** "55 menit di udara" lebih kuat dari "terbang cukup lama".

---

## 0. Konsep (sebelum apa pun)
Tulis satu kalimat premis:
> **[Subjek]** **[mengalami/melakukan X]**, padahal/sehingga **[Y]**. Penonton akan merasa **[emosi]** dan pulang membawa **[satu hal]**.

Contoh: "Indonesia sudah menerbangkan pesawat buatan sendiri tahun 1995, padahal hari ini kita mengira tidak pernah bisa. Penonton akan merasa kaget lalu getir, dan pulang membawa: masalahnya waktu, bukan kemampuan."
- Emosi target (pilih satu utama): penasaran · kaget · geram · lega · kagum · bangga · geli · takut kehilangan · sedih yang hangat.
- Uji premis: bisa diceritakan dalam 10 detik ke teman? Ada belokannya? Ada benda yang bisa difoto/digambar? Kalau tidak, ganti sudut pandang sebelum menulis naskah.

## 1. Arsitektur hook
- **Kapan**: detik 0–3 setiap video.
- **Kenapa**: penonton memutuskan menonton atau menggeser dalam ±1–2 dtk; hook menjanjikan sesuatu yang hanya bisa didapat dengan terus menonton.
- **Cara**: hook = **kata** (klaim/pertanyaan) + **gambar** (bukti/keganjilan yang terlihat di bingkai 0) + **bunyi** (hantaman/tekstur pertama) + **janji** (apa yang akan terjawab). Ketiganya harus menunjuk ke hal yang sama. Kalimat pertama ≤ 12 kata.
- **Hindari**: salam, "tahukah kamu", logo/judul kanal di depan, gambar pembuka yang tidak berhubungan dengan klaim, hook yang tidak dibayar di akhir.
- **Di mesin Kolase**: bingkai 0 sudah berisi pelat + subjek + teks (`t: 0`), narasi mulai ≤ 0,15 dtk (cek), hook tanpa suara: `narasiMulaiMaks` + `rakit --mulai`. Detail detik demi detik: `../short-form/short-form.md` §1–2.

| Jenis hook | Contoh kalimat | Bingkai pertama | Bunyi | Cocok untuk |
|---|---|---|---|---|
| Kontras | "Pesawat yang kamu naiki mudik, hampir pasti buatan luar negeri." (lalu: "Padahal 1995…") | kabin pesawat biasa, lalu hangar arsip menyusul | dengung kabin → potong hening | sejarah terlupakan (`balik`) |
| Angka mengejutkan | "55 menit. Segitu lama pesawat buatan Indonesia pertama kali terbang." | angka 55 jatuh memantul di atas foto langit | hantaman sub + detak | `angka`, sejarah |
| Pertanyaan | "Kenapa jawaban AI-mu selalu terdengar kaku?" | layar chat dengan jawaban klise sedang mengetik | ketikan + ding | tips, tutorial |
| Aksi di tengah | "…dan saat itulah dokumennya dirobek." | tangan di tengah merobek kertas, blur gerak | sobekan kertas keras | misteri, kronologi |
| Pernyataan berani | "Daftar tugasmu justru yang bikin kamu malas." | daftar panjang menggulung keluar layar | gulungan kertas + dum | psikologi, produktivitas |
| Visual ganjil | "Gajimu naik. Tapi belanjaanmu menyusut." | tas belanja mengecil saat struk memanjang | kertas struk tercetak | ekonomi, `pasar` |
| "Kamu salah" | "Kamu salah pakai AI kalau masih nanya cuma satu kalimat." | tokoh menutup muka di depan laptop | buzz "salah" | seri tips, `mitos` |
| Sebelum/sesudah | "Kiri: prompt satu kalimat. Kanan: prompt empat unsur." | layar terbelah dua hasil | swish + ding | tutorial, perbandingan |
(Kalimat contoh = bentuk; fakta di video baru tetap diriset, `skill-edit-rizky/references/riset.md`.)

## 2. Curiosity gap
- **Kapan**: hook dan setiap awal babak.
- **Kenapa**: otak tidak nyaman dengan informasi setengah; celah antara "tahu ada sesuatu" dan "tahu jawabannya" menahan tontonan.
- **Cara**: sebut **cukup spesifik untuk dipercaya, cukup kurang untuk penasaran**: tunjukkan akibat sebelum sebab, nama tanpa rupa, angka tanpa konteks. Gambar boleh menyembunyikan sebagian (siluet, kartu terbalik, bingkai blur, kotak sensor).
- **Hindari**: celah palsu yang tidak dijawab; celah terlalu lebar ("Rahasia sukses!") yang terasa clickbait.
- **Di mesin Kolase**: lapisan `blur` tinggi lalu menajam di kata jawaban (`gerak` blur → 0), `efek: lensa` (lingkaran teropong) yang membuka, kartu `rig: 'miring'` membalik.

## 3. Open loop
- **Kapan**: video > 25 dtk; tiap 8–12 dtk perlu satu pertanyaan baru yang belum dijawab.
- **Kenapa**: satu loop terbuka di depan hanya menahan sampai jawabannya; loop berlapis menahan sampai akhir.
- **Cara**: buka loop A di hook, buka loop B di tengah ("tapi ada satu hal yang aneh…") sebelum menutup A, tutup A, lalu tutup B di payoff. Loop B lebih besar dari A.
- **Hindari**: membuka lebih dari 2 loop di short (penonton lupa); loop yang ditutup tanpa diberi tanda visual.
- **Di mesin Kolase**: beri tanda visual konsisten untuk loop (benda yang sama muncul kembali saat ditutup: `cocok`), mis. kartu bertanda tanya yang kembali terbalik di payoff.

## 4. Pattern interrupt (tingkat cerita)
- **Kapan**: saat cerita mulai bisa ditebak (biasanya 35–60% durasi) atau setelah 3 fakta berpola sama.
- **Kenapa**: otak berhenti memperhatikan pola yang sudah dikenal; belokan memaksa perhatian kembali.
- **Cara**: ubah sesuatu yang besar sekaligus: arah cerita ("Tapi lalu…"), suasana (warna dingin, musik hilang), skala (dari detail ke peta besar), atau sudut pandang (dari tokoh ke angka). Kalimat pembelok ≤ 5 kata sebagai adegan sendiri.
- **Hindari**: interupsi tanpa isi (efek glitch tanpa belokan cerita); interupsi terlalu sering sampai jadi pola baru.
- **Di mesin Kolase**: adegan kartu teks pendek (`gaya: 'padat'`, `latar` kontras), perpindahan tanda tangan (`bingkai`, `putar`), `efek: warna` monokrom. Ritme visual per detik: `../short-form/short-form.md` §4.

## 5. Setup → eskalasi → payoff
- **Kapan**: hampir semua cerita pendek; paling cocok untuk humor, prestasi, kegagalan.
- **Kenapa**: penonton butuh aturan dunia (setup) supaya kenaikan (eskalasi) terasa, lalu pelepasan (payoff) memuaskan.
- **Cara**: setup 15–20% durasi (satu aturan jelas), eskalasi 50–60% (2–3 tingkat, tiap tingkat lebih besar, lebih cepat), payoff 15–20% (membayar janji hook, ditahan 1,5–3 dtk). Payoff sebaiknya memakai benda/gambar yang ditanam di setup.
- **Hindari**: eskalasi yang tidak naik (3 contoh setara); payoff yang memperkenalkan hal baru.
- **Di mesin Kolase**: eskalasi kamera `tenang` → `dorong` → `dorong-kuat`; skala benda makin besar; payoff dengan `efek: kilau` + tahan.

## 6. Masalah → ketegangan → solusi
- **Kapan**: edukasi, tips, explainer bisnis/teknologi.
- **Kenapa**: solusi tanpa rasa sakit tidak berharga; penonton harus merasakan masalahnya dulu.
- **Cara**: masalah ditunjukkan (bukan disebut) dalam situasi yang dikenal penonton; ketegangan = akibat kalau dibiarkan (angka, kerugian, rasa malu); solusi = satu langkah konkret yang terlihat bekerja (sebelum/sesudah).
- **Hindari**: solusi berupa daftar panjang; masalah abstrak ("kurang produktif") tanpa gambar.
- **Di mesin Kolase**: pola `mitos` atau `balik` (`gaya.md` §0.2); masalah di layar terbelah (`panel`), solusi menutupnya (`tutup`).

## 7. Visual storytelling (tunjukkan perubahan, bukan label)
- **Kapan**: setiap kalimat narasi. Pertanyaan wajib per baris: "kalau suara mati, apa yang dilakukan gambar?"
- **Kenapa**: teks yang mengulang narasi hanya membaca ulang; gambar yang berubah membuktikan.
- **Cara**: cari **perubahan fisik** yang mewakili kalimat: bertambah, berkurang, retak, tumbuh, berpindah, menumpuk, memudar. Teks di layar hanya kata kunci (1–3 kata) atau angka.
- **Hindari**: teks penuh kalimat di latar polos; gambar "suasana" yang tidak berubah sepanjang kalimat.
- **Contoh** narasi "Waktu terus berjalan.":
  - Lemah: teks WAKTU TERUS BERJALAN di latar gelap.
  - Kuat: tokoh duduk diam di meja yang sama; di belakangnya kalender sobek per hari makin cepat, cahaya jendela berganti pagi–malam–pagi, cangkir kopi menumpuk. Bunyi kertas makin rapat lalu hening. Maknanya bertambah: waktu jalan, tokoh tidak.
- **Di mesin Kolase**: lapisan beruntun (`t` makin rapat), `efek: hue`/`cahaya` untuk pergantian hari, `rig: 'napas'` pada tokoh yang diam. Bank metafora: `../visual/metafora.md`.

## 8. Pacing emosi
- **Kapan**: menyusun urutan beat dan musik.
- **Kenapa**: emosi butuh waktu tumbuh; emosi yang sama terus-menerus membuat mati rasa.
- **Cara**: gambar kurva emosi per 5 dtk (skala 1–5). Naik bertahap, satu penurunan kecil sebelum puncak (napas), puncak di 70–85% durasi, lalu lepas. Emosi berat (sedih/takut) butuh bidikan lebih panjang (+30–50%) dan bunyi lebih sedikit.
- **Hindari**: puncak emosi di awal; menempelkan musik dramatis pada isi biasa.
- **Di mesin Kolase**: kurva ini menentukan `kamera`, kepadatan lapisan, dan musik per segmen (`musik` daftar segmen). Musik: `../audio/musik.md`.

## 9. Pengungkapan informasi (information reveal)
- **Kapan**: angka, nama, wajah, jawaban, atau hasil.
- **Kenapa**: cara mengungkap menentukan bobotnya; info yang sama terasa biasa bila langsung, terasa besar bila diungkap bertahap.
- **Cara**: pilih teknik: bertahap (blur → tajam), dari detail ke utuh (`tarik`), hitung naik (odometer), kartu dibalik, sensor dicabut, sorot stabilo. Ungkap tepat di kata kuncinya, lalu tahan ≥ 0,8 dtk.
- **Hindari**: mengungkap sebelum narasi siap (merusak kejutan); semua info diungkap dengan teknik sama.
- **Di mesin Kolase**: `angka: { dari, ke }`, `masuk: 'tarik'`, `sorot` stabilo pada koran/dokumen, `rig: 'miring'` (kartu berputar), `coret: 'lingkar'`.

## 10. Antisipasi (tingkat cerita)
- **Kapan**: sebelum belokan, angka besar, atau payoff.
- **Kenapa**: memberi tahu penonton "sesuatu akan datang" membuat mereka menahan napas bersama video.
- **Cara**: tanda verbal ("Tapi…", "Sampai suatu hari…"), tanda visual (kamera melambat-mendekat, cahaya meredup, benda bergetar), tanda bunyi (riser, musik menipis). 0,5–1,5 dtk.
- **Hindari**: menjanjikan hal besar lalu membayar kecil.
- **Di mesin Kolase**: `../core/editing.md` §14.

## 11. Transisi naratif
- **Kapan**: pindah waktu, tempat, sudut pandang, atau babak.
- **Kenapa**: penonton harus tahu "kita sekarang di mana" tanpa kehilangan benang.
- **Cara**: jembatan verbal (kata yang menghubungkan: "Sementara itu", "15 tahun kemudian") **dan** jembatan visual (benda yang sama, bentuk mirip, gerak berlanjut). Lompatan zaman boleh potong keras + tanggal besar.
- **Hindari**: pindah tempat tanpa penanda; transisi mewah untuk perpindahan yang tidak penting.
- **Di mesin Kolase**: `cocok` (benda tetap, dunia berganti), `bingkai` (adegan jadi foto di adegan berikut), tanggal `gaya: 'padat'` `anim: 'jatuh'`. Katalog: `../motion/transisi.md`.

## 12. Metafora visual
- **Kapan**: kalimat abstrak (perasaan, sistem, waktu, risiko).
- **Kenapa**: konsep abstrak tidak bisa difoto; metafora memberi benda yang bisa bergerak.
- **Cara**: lima langkah di `../visual/metafora.md` §1; satu metafora utama boleh berevolusi sepanjang video (metafora berlapis).
- **Hindari**: metafora yang butuh penjelasan; mencampur 3 metafora dalam satu kalimat.

## 13. Kontras
- **Kapan**: setiap kali ingin menekankan perbedaan, skala, atau ironi.
- **Kenapa**: otak membaca perbedaan lebih cepat daripada nilai mutlak.
- **Cara**: pasangkan dua hal yang beda satu sumbu (besar/kecil, mahal/murah, dulu/sekarang, ramai/sepi, terang/gelap). Kontras visual harus sejajar dengan kontras isi: posisi sama, skala beda; warna beda, bentuk sama.
- **Hindari**: kontras di banyak sumbu sekaligus (jadi dua gambar acak).
- **Di mesin Kolase**: `panel` layar terbelah, grade per adegan (`grade: {...}`), `efek: warna` untuk "dulu".

## 14. Cerita sebelum/sesudah
- **Kapan**: tips, transformasi, perbandingan cara lama vs cara baru, dampak kebijakan.
- **Kenapa**: bukti paling cepat; penonton melihat hasil, bukan diberi tahu.
- **Cara**: komposisi identik (posisi kamera, ukuran, cahaya) supaya hanya satu hal berubah. Urutan: sesudah dulu (hook) → sebelum → proses → sesudah lagi (payoff), atau sebelum → sesudah dengan sapuan.
- **Hindari**: sebelum/sesudah dengan sudut kamera berbeda (perubahan tidak terbaca).
- **Di mesin Kolase**: dua lapisan di posisi sama + `masuk: 'sapu'`/`'geser'`, `panel` kiri-kanan, atau `cocok` dengan gambar beda (melebur).

## 15. Cerita mikro 15–60 dtk
- **Kapan**: semua Shorts/Reels.
- **Kenapa**: durasi pendek tetap butuh awal-tengah-akhir; yang dipangkas detail, bukan strukturnya.
- **Cara**: satu tokoh/benda, satu konflik, satu belokan, satu payoff. Setiap beat satu kalimat. Pilih pola mesin: `balik`, `misteri`, `angka`, `kronologi`, `duel`, `mitos` (`gaya.md` §0.2) atau struktur di `../short-form/short-form.md` §8–9.
- **Hindari**: memasukkan dua konflik; "intro" lebih dari 3 dtk.

### Contoh 15 dtk — "Prokrastinasi" (pola mitos singkat)
| Dtk | Narasi | Gambar melakukan | Bunyi |
|---|---|---|---|
| 0–2 | "Kamu bukan malas." | tokoh rebahan, daftar tugas melayang di atasnya terlipat jadi pesawat kertas | kertas dilipat |
| 2–6 | "Otakmu cuma menghindari rasa tidak enak." | pesawat kertas terbang menjauh dari tugas yang menyala merah | whoosh + dengung rendah |
| 6–11 | "Jadi kecilkan tugasnya sampai tidak menakutkan: dua menit saja." | tugas besar dipotong gunting jadi kepingan kecil, satu keping masuk tangan | gunting, klik |
| 11–15 | "Mulai yang dua menit. Sisanya ikut." | keping kecil selesai, keping lain ikut tercentang beruntun, kembali ke tokoh yang kini duduk (bingkai mirip awal = loop) | centang beruntun → ding |

### Contoh 30 dtk — "Prompt satu kalimat" (seri Raka, pola balik)
| Dtk | Narasi | Gambar melakukan | Bunyi |
|---|---|---|---|
| 0–3 | "Kamu salah pakai AI kalau masih nanya cuma satu kalimat." | Raka menutup muka, layar chat di belakangnya | buzz |
| 3–8 | "Misalnya: buatkan caption jualan kopi. Hasilnya? Kaku, klise, kayak robot." | prompt diketik, jawaban klise muncul, kata klise dicoret spidol satu per satu | ketik, spidol |
| 8–12 | "Masalahnya bukan AI-nya. Kamu belum kasih bahan." | kamera mundur: kartu prompt ternyata kosong kecuali satu baris | dum |
| 12–24 | "Tambahkan empat hal: peran, konteks, tugas, format." | 4 kartu berwarna masuk beruntun, kartu prompt memanjang dan terstabilo per unsur | pop × 4 naik nadanya |
| 24–30 | "Hasilnya langsung beda." | layar terbelah: jawaban lama vs baru; Raka jempol; bingkai akhir kembali ke layar chat (loop) | swish + ding |

### Contoh 45 dtk — "N250" (pola balik 6 ketukan, `contoh/n250`)
| Dtk | Beat | Gambar melakukan |
|---|---|---|
| 0–3 | dunia dikenal | kabin pesawat biasa; teks "BUATAN LUAR NEGERI" |
| 3–7 | pembalik | `tutup` koran tua naik: 1995, foto hangar |
| 7–20 | pengenalan + 3 fakta | `dorong` ke foto koran → pesawat di landasan; angka 55 MENIT bergulir; 50 penumpang sebagai ikon kursi terisi |
| 20–24 | masalah | kartu "TAPI LALU, KRISIS DATANG" + `putar` |
| 24–38 | konsekuensi | dokumen + cap DIHENTIKAN, grafik dana jatuh, pesawat diselimuti terpal |
| 38–46 | hari ini + vonis | `bingkai`: pesawat jadi foto di museum; "Pesawatnya sudah jadi. Yang tidak siap, zamannya." ditahan |

### Contoh 60 dtk — "Bunga majemuk" (pola angka, dengan re-hook)
| Dtk | Beat | Narasi (ringkas) | Gambar melakukan |
|---|---|---|---|
| 0–3 | hook angka | "Satu juta bisa jadi 17 juta tanpa kamu tambah sepeser pun." | angka 1.000.000 bergulir naik |
| 3–10 | konteks | "Syaratnya cuma satu: waktu." | tumpukan koin di meja, kalender di belakang |
| 10–20 | mekanisme | "Bunga tahun ini ikut berbunga tahun depan." | koin melahirkan koin kecil yang ikut menumpuk (bukan hanya bertambah dari luar) |
| 20–30 | re-hook | "Tapi ada yang aneh di tahun-tahun awal." | grafik nyaris datar, kamera mendekat ke garis datar |
| 30–45 | ketegangan | "10 tahun pertama terasa sia-sia. Di sinilah kebanyakan orang berhenti." | tokoh berhenti, garis grafik tetap merayap; jam berputar |
| 45–55 | payoff | "Di tahun ke-30, kurvanya meledak: ±17 kali lipat." | `tarik` dari garis ke kurva melengkung tajam, kilau di puncak |
| 55–60 | vonis + loop | "Yang mahal bukan uangnya. Tapi waktunya." | kamera kembali ke koin pertama (bingkai awal) |
(Hitungan contoh: 10%/tahun, 30 tahun, 1,1^30 ≈ 17,4; tulis asumsinya di layar.)

## Cek cepat
- Premis satu kalimat + emosi target tertulis sebelum naskah.
- Hook menggabungkan kata + gambar + bunyi yang menunjuk hal sama, dan dibayar di akhir.
- Dengan suara mati, alur masih terbaca dari gambar (uji di lembar kontak).
- Ada minimal satu belokan/pattern interrupt sebelum 60% durasi.
- Setiap open loop ditutup, dan ditutup dengan tanda visual.
- Payoff memakai benda/gambar yang sudah ditanam sebelumnya.
- Teks layar hanya kata kunci/angka, bukan kalimat narasi penuh.

## Teknik modern
- **Hook visual tanpa suara (silent-first)** · manfaat: banyak penonton menonton tanpa suara di 1–2 dtk pertama · kapan: semua short · cara: bingkai 0 sudah menunjukkan keganjilan + teks ≤ 5 kata; uji `kontak --t 0,0.5,1` tanpa audio.
- **Payoff tertanam (planted payoff)** · manfaat: menambah nilai tonton ulang · kapan: video > 30 dtk · cara: benda payoff muncul kecil di latar adegan awal; tulis di kolom storyboard "tanam di adegan #".
