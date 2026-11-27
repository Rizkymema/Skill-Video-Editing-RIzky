# Short-form: Reels, Shorts, TikTok (15–60 dtk)

> SHORT-FORM · dipakai di langkah 2, 3, 13 · terkait: `../story/cerita.md`, `../core/editing.md`, `../visual/komposisi.md`, `../type/tipografi-kinetik.md`, `../audio/musik.md`, `../polish/qc.md`

Prinsip inti:
1. **Detik 0 adalah sampul.** Tidak ada intro, logo, atau salam; bingkai pertama sudah menjual.
2. **Setiap 1,5–3 dtk ada perubahan yang terlihat**, tapi perubahan harus bermakna (informasi, skala, emosi), bukan sekadar efek.
3. **Satu gagasan per video.** Short yang mencoba mengajarkan tiga hal biasanya kehilangan ketiganya.
4. **Akhir menyambung ke awal.** Short yang selesai dengan "fade out" mengundang geser; short yang menyambung mengundang putar ulang.
5. **Struktur melayani cerita.** Pola di §11 adalah bawaan, bukan kewajiban (§12).

Patokan di mesin Kolase: 9:16 1080×1920, 30 fps, durasi lolos cek 30–70 dtk (`durasiTarget`), narasi mulai ≤ 0,15 dtk, tanpa subtitle bawah, tanpa CTA di narasi.

---

## 1. Hook 1 detik
- **Kapan**: bingkai 0–30 (detik 0–1).
- **Kenapa**: keputusan geser terjadi sebelum kalimat pertama selesai; bingkai harus bekerja tanpa suara.
- **Cara**: bingkai 0 berisi (a) subjek yang jelas di sepertiga tengah, (b) gerak yang sudah berjalan (kamera melesat, benda jatuh, teks meluncur), (c) teks ≤ 5 kata yang menimbulkan pertanyaan, (d) bunyi pertama di bingkai 0–3 (hantaman, ketikan, tekstur). Kontras tinggi dan satu warna aksen.
- **Hindari**: bingkai 0 hitam/kosong, fade-in, tokoh yang belum "di tempat", teks kecil, latar ramai tanpa titik fokus.
- **Di mesin Kolase**: semua lapisan hook `t: 0` (atau masuk 0–0,3 dtk dengan gerak sudah setengah jalan), `masuk: 'terbang'`/`'jatuh'` di bingkai 0, `sfx: [{ t: 0, jenis: 'impact' }]`; uji `kontak --t 0,0.33,0.66,1`.
- **Di editor lain**: pratinjau bingkai 0 sebagai gambar diam; kalau tidak membuat penasaran, ganti.

## 2. Hook 3 detik
- **Kapan**: detik 0–3.
- **Kenapa**: setelah berhenti menggeser, penonton butuh alasan untuk tinggal: klaim lengkap + janji.
- **Cara**: kalimat hook selesai ≤ 2,5 dtk; satu perubahan visual di ±1,2–2 dtk (potongan, zoom, benda kedua) yang **membuktikan** atau **memperdalam** klaim; janji tersirat ("…dan alasannya bikin geram"). Jenis hook: `../story/cerita.md` §1.
- **Hindari**: menjelaskan konteks sebelum klaim; dua klaim sekaligus.
- **Di mesin Kolase**: adegan pertama ≤ 3 dtk, adegan ke-2 masuk dengan perpindahan bermomentum (`dorong`/`sentak`); perpindahan pembuka berbeda dari video terakhir (`riwayat.py lihat`).

## 3. Retensi
- **Kapan**: menilai storyboard dan pratinjau.
- **Kenapa**: grafik retensi short biasanya jatuh di 3 tempat: 0–3 dtk (hook gagal), ±40–60% (tengah kendur), sebelum payoff (penonton menebak akhir).
- **Cara**: tiap titik rawan punya penangkal: 0–3 dtk = hook 1+3 detik; tengah = re-hook (open loop baru, belokan, angka baru) tiap 8–12 dtk; sebelum payoff = antisipasi singkat + jangan bocorkan jawaban di teks layar.
- **Hindari**: re-hook berupa "tunggu sampai akhir" (murahan dan melanggar aturan tanpa CTA di narasi).
- **Di mesin Kolase**: tandai re-hook di kolom storyboard; adegan re-hook memakai transisi tanda tangan atau `efek: kilau`.

## 4. Kadens interupsi pola
- **Kapan**: sepanjang video; diperiksa per 3 dtk di lembar kontak.
- **Kenapa**: mata cepat terbiasa; perubahan kecil berkala menjaga perhatian tanpa melelahkan.
- **Cara**: tiap 1,5–3 dtk ubah **minimal 1** dari 5 saluran, **maksimal 2** sekaligus, kecuali di titik belok (3+):

| Saluran | Contoh perubahan | Fungsi |
|---|---|---|
| Bingkai/skala | dekat ↔ lebar, objek baru masuk, potongan dalam | memberi info baru |
| Warna/cahaya | grade berganti, sorot, monokrom sesaat | menandai suasana/belokan |
| Bunyi | SFX baru, musik turun/naik, hening | menekankan tanpa gambar |
| Teks | kata kunci baru, angka, kotak sorot | mengarahkan mata |
| Arah gerak | kamera berbalik arah, benda masuk dari sisi lain | energi |

- **Hindari**: semua saluran berubah tiap potongan (melelahkan, terasa AI); interupsi yang tidak membawa isi.
- **Di mesin Kolase**: mesin menolak gambar hampir diam > 1 dtk dan menyarankan adegan > 4,5 dtk dipecah; lapisan beruntun `t` tiap 1–1,5 dtk (`gaya.md` §3).

## 5. Kepadatan informasi
- **Kapan**: menulis naskah dan teks layar.
- **Kenapa**: short ditonton sekali sambil lalu; terlalu padat = tidak ada yang diingat, terlalu longgar = geser.
- **Cara**: narasi ±2,3–2,6 kata/dtk (±100–110 kata per 45 dtk); satu angka penting per 3–5 dtk; teks layar ≤ 7 kata sekaligus, ≤ 3 baris; waktu tampil minimal 0,4 dtk + 0,25 dtk per kata (cek mesin menyarankan ≥ 0,7 dtk). Gagasan sulit = satu adegan sendiri + metafora (`../visual/metafora.md`).
- **Hindari**: narasi dan teks layar mengatakan hal berbeda; angka berderet tanpa jeda.
- **Di mesin Kolase**: `teks` hanya kata kunci dengan `*aksen*`; angka lewat `angka: { dari, ke }` supaya ada waktu membaca.

## 6. Variasi tempo
- **Kapan**: setelah struktur jadi.
- **Kenapa**: tempo rata terasa monoton walau cepat.
- **Cara**: susun gelombang: cepat (hook) → sedang (konteks) → makin cepat (ketegangan) → lambat sesaat (napas/belokan) → cepat (klimaks) → tahan (payoff). Tabel tempo 45 dtk: `../core/editing.md` §18.
- **Hindari**: semua adegan 2,5 dtk; payoff yang langsung dipotong.
- **Di mesin Kolase**: panjang adegan dari rujukan narasi; tahan payoff 1,5–3 dtk; musik bersegmen.

## 7. Ujung loop
- **Kapan**: 2–3 dtk terakhir setiap short.
- **Kenapa**: putaran ulang otomatis menambah waktu tonton; loop yang mulus membuat penonton baru sadar di detik ke-3 putaran kedua.
- **Cara** (pilih 1–2):
  1. **Bingkai akhir = bingkai awal**: gambar, posisi, dan skala sama; kamera adegan terakhir berakhir di keadaan kamera adegan pertama.
  2. **Kalimat menyambung**: kalimat terakhir menjadi awal kalimat pertama ("…dan itu sebabnya" → "Pesawat yang kamu naiki mudik…"), atau pertanyaan di akhir dijawab hook.
  3. **Jembatan bunyi**: musik tidak di-fade; ketukan terakhir mengarah ke hantaman bingkai 0; SFX yang terpotong di akhir "selesai" di awal.
  4. **Gerak menyambung**: benda keluar bingkai ke kanan di akhir, masuk dari kiri di awal.
- **Hindari**: kartu "terima kasih sudah menonton", fade ke hitam, logo penutup panjang.
- **Di mesin Kolase**: adegan akhir memakai `gambar` yang sama dengan adegan 1 dan keyframe kamera berakhir sama dengan awal adegan 1; `ekor` 0,35 dtk; bandingkan `kontak --t 0` dengan bingkai terakhir. *Celah mesin*: belum ada cek loop otomatis.

## 8. Nilai tonton ulang
- **Kapan**: payoff dan adegan padat.
- **Kenapa**: penonton yang memutar ulang memberi sinyal kuat; detail tersembunyi memberi alasan.
- **Cara**: tanam detail kecil yang baru bermakna setelah payoff (benda di latar adegan 2, angka di koran), pengungkapan cepat 0,5–0,8 dtk yang menggoda dihentikan, loop yang tidak terasa berakhir.
- **Hindari**: detail penting yang terlalu cepat sehingga cerita tidak terbaca (tonton ulang harus bonus, bukan syarat).
- **Di mesin Kolase**: detail di lapisan `z` kecil (latar) yang kemudian di-`dorong` di payoff; `bingkai` ke detail yang sudah terlihat sejak awal.

## 9. Rasa penasaran
- **Kapan**: hook, tiap awal babak, sebelum payoff.
- **Kenapa**: penasaran adalah mesin retensi utama short edukasi.
- **Cara**: tunjukkan akibat sebelum sebab; spesifik tapi belum lengkap (nama tanpa rupa, angka tanpa konteks); visual tersembunyi sebagian (siluet, blur, kartu terbalik). Rincian: `../story/cerita.md` §2–3.
- **Hindari**: janji yang terlalu besar untuk isi.

## 10. Payoff
- **Kapan**: 75–95% durasi.
- **Kenapa**: payoff membayar hook; tanpa itu penonton merasa ditipu dan tidak berbagi.
- **Cara**: jawab hook secara harfiah (penonton harus bisa menunjuk "itu jawabannya"); payoff visual = benda/gambar tertanam + hantaman (kilau, bingkai, angka akhir) + tahan 1,5–3 dtk; satu kalimat vonis ≤ 10 kata.
- **Hindari**: payoff berupa daftar; payoff yang muncul di teks layar lebih dulu sebelum narasi.
- **Di mesin Kolase**: `efek: [{ jenis: 'kilau', t, titik }]`, `masuk: 'bingkai'` atau `'tarik'`, `kamera: 'tenang'` saat ditahan.

## 11. Struktur bawaan: HOOK → CONTEXT → TENSION → DEVELOPMENT → PAYOFF → LOOP
| Bagian | Fungsi | 15 dtk | 30 dtk | 45 dtk | 60 dtk |
|---|---|---|---|---|---|
| HOOK | klaim + bukti visual | 0–2 | 0–3 | 0–3 | 0–3 |
| CONTEXT | dunia/aturan yang perlu diketahui | 2–4 | 3–7 | 3–9 | 3–10 |
| TENSION | masalah, belokan, taruhan | 4–7 | 7–12 | 9–16 | 10–20 |
| DEVELOPMENT | bukti/langkah/eskalasi (+ re-hook) | 7–11 | 12–22 | 16–34 (re-hook ±25) | 20–45 (re-hook ±30) |
| PAYOFF | jawaban + vonis, ditahan | 11–14 | 22–28 | 34–42 | 45–56 |
| LOOP | sambungan ke detik 0 | 14–15 | 28–30 | 42–45 | 56–60 |

**Soal CTA**: aturan repo ini **tanpa CTA di narasi** (ajakan follow/komentar hanya di deskripsi dan komentar sematan, `kemasan.md`). Jadi bagian terakhir bawaannya **LOOP**, bukan CTA. CTA visual hanya bila pengguna memintanya: maksimal 1 dtk, kecil, di zona aman, tidak memutus loop (mis. label seri "Bagian 2" di pojok atas). Pertanyaan untuk komentar ditaruh di komentar sematan.

## 12. Struktur alternatif (pakai bila cerita membutuhkan)
| Struktur | Urutan | Kapan | Hindari |
|---|---|---|---|
| Daftar / hitung mundur | hook janji jumlah → #3 → #2 → #1 (terkuat terakhir) → loop | tips, fakta berseri, peringkat | lebih dari 5 butir; butir setara tanpa eskalasi |
| Mitos → fakta | yang dipercaya → bukti 1–2 → fakta sebenarnya → cara mengingat | sains, kesehatan, kebiasaan | mengejek penonton; fakta tanpa sumber |
| Sebelum / sesudah | hasil akhir dulu → keadaan awal → proses singkat → hasil lagi | transformasi, tutorial | komposisi beda antara sebelum dan sesudah |
| Skit POV | situasi relatable (hook tanpa suara boleh, `narasiMulaiMaks`) → konflik → punchline → narasi penjelas singkat | humor edukatif, kebiasaan kerja | skit > 40% durasi sebelum ada isi |
| Pertanyaan → jawaban terbalik | pertanyaan → jawaban yang tampak jelas → "salah" → jawaban sebenarnya | psikologi, ekonomi, teknologi | pembalikan yang dibuat-buat |
| Satu angka | angka besar detik 0 → asalnya → 3 pecahan → artinya bagimu → vonis | uang, statistik (`angka`) | angka tanpa sumber |
| Detik demi detik | jam/tanggal di layar maju → titik balik → akibat → hari ini | bencana, peristiwa, penemuan (`kronologi`) | terlalu banyak tanggal |
| Duel | A vs B → 3 ronde dengan skor → pemenang tak terduga → pelajaran | merek, negara, teknologi (`duel`) | ronde tanpa skor visual |

## 13. Format seri (episode berulang)
- **Kapan**: topik yang bisa dipecah (seri tips AI bertokoh Raka, seri sejarah terlupakan, "apa jadinya kalau…").
- **Kenapa**: penonton yang mengenali format menonton lebih lama dan mencari episode lain; format juga mempercepat produksi.
- **Cara**: kunci 3 hal yang sama di tiap episode: bingkai pembuka khas (posisi tokoh/benda, warna), satu transisi tanda tangan, satu bunyi tanda tangan. Sisanya berganti sesuai topik. Judul episode di layar ≤ 1 dtk, kecil, zona atas.
- **Hindari**: intro seri berdurasi > 1 dtk; mengulang kalimat hook yang sama di tiap episode.
- **Di mesin Kolase**: aset seri di `aset/<seri>/`, tema dipakai ulang dengan sengaja (`tema.md` aturan seri), `riwayat.py` tetap dipakai untuk mengganti hook dan perpindahan pembuka.

## Cek cepat
- Bingkai 0 (tanpa suara) sudah membuat penasaran: subjek + gerak + teks ≤ 5 kata.
- Kalimat hook selesai ≤ 2,5 dtk dan ada perubahan visual sebelum detik 2.
- Tiap jendela 3 dtk ada minimal satu perubahan bermakna; tidak ada jendela dengan 3+ perubahan kecuali titik belok.
- Ada re-hook di 40–60% durasi (video ≥ 30 dtk).
- Payoff menjawab hook secara harfiah dan ditahan ≥ 1,5 dtk.
- Akhir menyambung ke awal (bingkai, kalimat, bunyi, atau gerak); tidak ada fade ke hitam.
- Tidak ada CTA di narasi.

## Celah mesin
- **Cek loop**: belum ada pembanding otomatis bingkai terakhir vs bingkai 0. Usulan: `cek` memberi saran bila selisih piksel rata-rata besar dan `KONFIG.loop: true`.
- **Peta retensi**: belum ada laporan perubahan per 3 dtk. Usulan: `cek` menghitung jumlah lapisan baru/perpindahan/SFX per jendela 3 dtk dan menandai jendela kosong atau terlalu padat.

## Teknik modern
- **Re-hook tiap 8–12 dtk** · manfaat: menahan penurunan retensi di tengah · kapan: video ≥ 30 dtk · cara: tulis kolom "re-hook" di storyboard; isi dengan open loop kecil atau angka baru, bukan "tunggu sampai akhir".
- **Loop kalimat (sentence loop)** · manfaat: putar ulang yang tidak disadari · kapan: short ≤ 45 dtk dengan hook berupa pernyataan · cara: tulis kalimat terakhir naskah dulu supaya tata bahasanya mengalir ke L01; uji dengan membaca L-akhir + L01 berurutan.
- **Teks pertama sebagai judul layar (on-screen title hook)** · manfaat: banyak penonton membaca sebelum mendengar · kapan: semua short · cara: teks hook di 15–45% tinggi, gaya utama video, ≤ 5 kata, muncul di bingkai 0–6.
