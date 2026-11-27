# Sound design: gerak + bunyi + waktu

> AUDIO · dipakai di langkah 11 (dan dicek di 15) · terkait: `musik.md`, `../core/editing.md`, `../motion/transisi.md`, `../motion/prinsip-animasi.md`, `../polish/qc.md`

Prinsip inti:
1. **Bunyi memberi berat pada gerak.** Animasi sederhana + bunyi tepat waktu terasa lebih mahal daripada animasi rumit yang bisu. Gerak yang "mendarat" tanpa bunyi terasa melayang.
2. **Narasi adalah raja.** Semua bunyi lain hidup di sela atau di bawah suara. Bunyi yang menutupi satu kata = salah, seindah apa pun bunyinya.
3. **Tidak semua yang bergerak berbunyi.** Pilih 1 bunyi utama per momen; sisanya diam atau tekstur samar. Diam yang disengaja adalah bunyi juga.
4. **Waktu lebih penting daripada pilihan bunyi.** Whoosh biasa di bingkai yang tepat menang atas whoosh mahal yang telat 3 bingkai.
5. **Variasi.** Bunyi yang sama berulang persis (whoosh ke-6 yang identik) membuat telinga sadar ada templat.

## 1. Patokan level dan panjang
| Lapisan | Target | Catatan |
|---|---|---|
| Narasi | −14 LUFS terintegrasi (mesin menormalkan seluruh campuran ke −14 ±1, puncak < 0 dBFS) | selalu paling jelas; konsonan terdengar di HP speaker |
| Musik di bawah narasi | ±−24 s/d −20 dB relatif narasi (mesin meredam musik berkas ke 30%, sintesis ke 32–40% saat baris narasi berbunyi) | lihat `musik.md` §6 |
| SFX tunggal (whoosh, pop, klik) | puncak 4–8 dB **di bawah** puncak narasi bila jatuh di atas kata; boleh setara narasi bila di jeda | ukur dengan telinga di speaker HP, bukan headphone saja |
| Hantaman besar (impact, boom) | boleh puncak tertinggi video, **hanya di jeda narasi** | maks 2–3 per video 45 dtk |
| Ambience / room tone | −30 s/d −24 dB relatif narasi | terasa bila dimatikan, tidak terdengar bila dinyalakan |
| Tekstur halus (desis pita, debu, dengung) | −36 s/d −28 dB | lapisan "udara", bukan peristiwa |

Panjang khas: klik/tik 0,02–0,08 dtk · pop 0,08–0,15 · swish 0,2–0,4 · whoosh 0,4–1,0 · impact 0,6–1,5 (ekor) · riser 0,8–3 · boom 1,5–4 · ambience = sepanjang adegan.

## 2. Aturan sinkron (offset dari bingkai visual)
| Gerak visual | Bunyi | Offset patokan (30 fps) |
|---|---|---|
| Potong bermomentum / whip / zoom tembus | whoosh atau swish | **puncak whoosh di titik potong**: mulai 0,15–0,35 dtk (5–10 bingkai) sebelum potong |
| Benda/teks mendarat, jatuh, dicap | impact / dum / stempel | transient **tepat di bingkai mendarat** (0 bingkai); telat 2+ bingkai terasa lepas |
| Kartu/teks muncul pop | pop / klik | 0–1 bingkai **sebelum** bingkai skala penuh (telinga sedikit lebih cepat daripada mata) |
| Ketegangan menuju pengungkapan | riser | riser **berhenti 0–2 bingkai sebelum** hantaman; lebih baik lagi: riser berhenti → 0,1–0,3 dtk hening → hantaman |
| Masuk ke adegan baru dengan "sedotan" | reverse swell (bunyi dibalik) | puncak swell di titik potong, lalu potong bersih ke adegan baru |
| Teks diketik | ketik | ketukan mengikuti huruf yang muncul, bukan loop rata; jeda di spasi |
| Angka bergulir | gulir / tik beruntun | rapat di awal, merenggang saat angka melambat; satu "ding"/hit saat angka final |
| Kursor klik / tombol | klik | tepat di bingkai tombol mengecil (skala 0,9) |
| Notifikasi turun | notif | 0–2 bingkai sebelum kartu berhenti |
| Glitch | glitch | durasi sama dengan glitch visual, potong mati bersamaan |
| Kamera mendorong pelan | (biasanya tanpa bunyi) / tekstur halus | gerak lambat yang berbunyi terasa dibuat-buat |

## 3. Katalog bunyi
### Whoosh
- **Kapan**: perpindahan bermomentum (`dorong`, `tarik`, `putar`, `bingkai`), benda besar melintas dekat lensa, teks terbang masuk.
- **Kenapa**: memberi rasa kecepatan dan "udara yang terdorong"; menyambung dua adegan secara telinga sehingga potongan terasa satu gerak.
- **Cara**: puncak di titik potong (mulai 5–10 bingkai lebih awal). Pan ikut arah gerak (kiri→kanan bila benda bergerak ke kanan). Gerak pendek = whoosh pendek bernada tinggi; gerak berat/besar = whoosh panjang bernada rendah. Siapkan 3–4 varian dan gilir.
- **Hindari**: whoosh pada setiap potongan; whoosh identik berulang; whoosh di atas kata kunci narasi; whoosh keras pada gerak kamera pelan.

### Swish
- **Kapan**: geser cepat, kartu dilempar, whip pendek (`sentak`, `geser`, `lempar`).
- **Kenapa**: versi ringan whoosh; tidak memenuhi spektrum, cocok di bawah narasi.
- **Cara**: 0,2–0,4 dtk, puncak di bingkai tercepat. Volume 60–75% whoosh.
- **Hindari**: swish untuk gerak yang lambat atau berat.

### Impact / hit
- **Kapan**: kata/angka kunci mendarat, vonis, "TAPI", benda jatuh, potong keras di puncak.
- **Kenapa**: titik tanda baca bagi telinga; memberi bobot dan otoritas pada informasi.
- **Cara**: susun 3 lapis: **transient** (klik/kayu/logam 10–30 ms) + **body** (dum/punch 80–200 Hz, 0,2–0,4 dtk) + **ekor** (boom/reverb 0,6–1,5 dtk). Transient tepat di bingkai mendarat. Didahului 0,1–0,3 dtk lebih sepi (musik turun, narasi jeda) supaya kontras.
- **Hindari**: lebih dari 1 impact per 6–8 dtk; impact di tengah kalimat; impact keras untuk informasi kecil (inflasi bobot).

### Riser
- **Kapan**: membangun ketegangan sebelum pengungkapan, angka besar, payoff, drop musik.
- **Kenapa**: menciptakan antisipasi; telinga menunggu sesuatu.
- **Cara**: 0,8–3 dtk, naik nada + volume; berhenti tepat sebelum hantaman atau sebelum **hening** 0,1–0,3 dtk. Riser + kamera `dorong-kuat` + teks yang menahan diri = antisipasi lengkap.
- **Hindari**: riser yang tidak berakhir pada apa pun (janji palsu); riser di bawah narasi panjang (bertabrakan dengan frekuensi suara).

### Klik / tik
- **Kapan**: tombol, kursor, centang, saklar, tiap butir daftar muncul, potongan kecil.
- **Kenapa**: konfirmasi "sesuatu terjadi" dengan biaya telinga minimal.
- **Cara**: 20–80 ms, transient tajam; variasi nada ±2 semitone antar butir supaya tidak seperti metronom.
- **Hindari**: klik di setiap kata yang muncul (jadi bising).

### Ketik (typing)
- **Kapan**: teks diketik di layar, prompt AI, dokumen, chat.
- **Kenapa**: membuat penonton membaca bersama; ritme ketik = ritme baca.
- **Cara**: satu ketukan per 1–3 huruf, tidak rata (acak ±20 ms), jeda di spasi/tanda baca, tombol Enter/kirim lebih berat. Volume rendah bila narasi bicara bersamaan.
- **Hindari**: loop ketik yang terus berjalan setelah teks berhenti.

### Bunyi UI (notif, pop, swipe, sukses, gagal)
- **Kapan**: antarmuka digital, notifikasi, layar HP, jawaban benar/salah (`../motion/ui-digital.md`).
- **Kenapa**: penonton mengenal bahasa bunyi ponsel; langsung terbaca sebagai "digital".
- **Cara**: buat palet UI kecil (3–4 bunyi sekeluarga: klik, pop, notif, sukses) dan pakai konsisten sepanjang video. Bunyi sukses naik nada, gagal turun nada.
- **Hindari**: bunyi notifikasi merek asli yang dikenali (iPhone/WhatsApp persis) — gunakan yang mirip fungsinya, bukan salinan.

### Ambience
- **Kapan**: adegan bertempat (kota, kantor, hujan, kelas, pasar, ruang sidang) terutama di hook dan di adegan yang ditahan lama.
- **Kenapa**: menempatkan penonton di ruang; foto diam terasa "ada udaranya".
- **Cara**: satu ambience per tempat, −30 s/d −24 dB, fade masuk 0,2–0,5 dtk, berganti saat tempat berganti (bisa J-cut: ambience adegan berikut masuk 0,3–0,6 dtk sebelum potong, lihat `../core/editing.md` J-cut).
- **Hindari**: ambience ramai di bawah narasi padat; ambience yang tidak cocok dengan gambar (burung di ruang server).

### Room tone
- **Kapan**: setiap jeda/hening, terutama "hening sebelum hantaman".
- **Kenapa**: hening digital (nol mutlak) terdengar seperti audio rusak; room tone membuat hening terasa disengaja.
- **Cara**: dengung ruang/desis halus −40 s/d −32 dB di bawah seluruh video atau minimal di jeda. Saat "potong ke hening", musik dan SFX berhenti, room tone tetap.
- **Hindari**: room tone yang berdesis keras (terdengar seperti rekaman jelek).

### Bass impact / sub
- **Kapan**: pengungkapan besar, judul muncul, drop musik, layar gelap ke terang.
- **Kenapa**: dirasakan di dada (headphone/speaker besar); memberi skala "sinematik".
- **Cara**: sine 30–60 Hz turun nada, 0,8–1,6 dtk, gabung dengan transient di atas 2 kHz supaya tetap terdengar di speaker HP (sub saja hilang di HP).
- **Hindari**: sub tanpa transient (tidak terdengar di HP); sub berulang yang membuat pembatas memompa (volume narasi ikut turun naik).

### Glitch
- **Kapan**: berita mengejutkan, teknologi rusak, kebohongan terbongkar, transisi `glitch`.
- **Kenapa**: mengganggu pola secara sengaja (pattern interrupt telinga).
- **Cara**: 0,15–0,45 dtk, dipotong mati bersamaan dengan visual; maks 1–2 kali per video (kecuali gaya Cyberpunk/Futuristic, lihat `../style/gaya-visual.md`).
- **Hindari**: glitch sebagai pengganti transisi biasa.

### Bunyi transisi khusus (kertas, kamera, proyektor, stempel, spidol)
- **Kapan**: transisi yang punya benda: koran menutup (`tutup` = kertas), kilat (`kamera`), kartu (`kertas`), cap (`stempel`), coretan (`spidol`), film arsip (`proyektor`).
- **Kenapa**: bunyi benda nyata membuat dunia kolase terasa fisik (`../motion/kolase-editorial.md`).
- **Cara**: bunyi diambil dari benda yang terlihat, tidak dari kategori generik. Kertas: 0,2–0,5 dtk, sedikit stereo.
- **Hindari**: bunyi kertas pada transisi digital (dan sebaliknya).

### Reverse sound (swell terbalik)
- **Kapan**: masuk ke kenangan, kilas balik, pengungkapan "ternyata…", transisi ke dunia lain.
- **Kenapa**: bunyi yang "terhisap" menuju titik potong menciptakan rasa ditarik ke depan.
- **Cara**: ambil ekor reverb/piano/cymbal, balik, letakkan sehingga ujungnya tepat di titik potong; 0,6–1,5 dtk.
- **Hindari**: lebih dari satu kali per video.

### Cinematic boom
- **Kapan**: judul besar, angka puncak, vonis akhir, `kilau` (mesin otomatis memberi `boom`).
- **Kenapa**: penanda "ini titik tertinggi cerita".
- **Cara**: boom = sub + body + ekor panjang 2–4 dtk; didahului hening/room tone 0,2–0,5 dtk; musik boleh berhenti total sesudahnya 0,5–1 dtk (lihat `musik.md` §5).
- **Hindari**: boom di setiap kartu judul; boom di video santai/tips (gunakan pop + ding).

### Tekstur halus (subtle texture)
- **Kapan**: gaya Retro/VHS (desis pita), Analog Film (derak proyektor halus), Grunge (debu, gesek kertas), Dark Tech (dengung listrik).
- **Kenapa**: menyamakan telinga dengan tekstur visual (`../style/warna-tekstur.md`); bunyi + grain = satu dunia.
- **Cara**: satu tekstur per gaya, −36 s/d −28 dB, menyala sepanjang adegan bergaya itu.
- **Hindari**: menumpuk dua tekstur; tekstur yang berdenyut di ketukan berbeda dari musik.

## 4. Resep lapisan (stack) siap pakai
| Momen | Lapisan | Total |
|---|---|---|
| Teks judul mendarat | klik transient + dum + ekor reverb pendek | 0,6 dtk |
| Angka final | tik beruntun (gulir) → ding/hit di angka final | 1,2–1,6 dtk |
| Pengungkapan besar | riser 1,5 dtk → hening 0,2 dtk → transient + sub + boom | 3–4 dtk |
| Kartu foto dilempar | swish + kertas tipis saat mendarat | 0,5 dtk |
| Whip ke adegan baru | swish (puncak di potong) + ambience adegan baru masuk 3 bingkai sesudahnya | 0,4 dtk |
| HP menyala | klik tombol + dengung layar halus + notif | 0,8 dtk |
| Cap DITOLAK | stempel (transient) + dum ringan + guncang kamera | 0,4 dtk |

## 5. Bunyi untuk diam
- Setiap video punya minimal satu momen hampir hening (0,2–1 dtk) sebelum hantaman terpenting. Isi dengan room tone, bukan nol.
- Sesudah hantaman besar, beri **ruang napas** 0,5–1,5 dtk dengan hanya ekor + ambience sebelum bunyi baru masuk.
- Telinga lelah lebih cepat daripada mata: kurangi kepadatan SFX di 30% akhir video kecuali menuju payoff.

## 6. Di mesin Kolase
- **Otomatis** (`KONFIG.sfxOtomatis`, bawaan `true`): perpindahan berbunyi (dorong/tarik/putar/bingkai/zoom/iris/cocok → `whoosh`; sentak/geser/lempar/fokus/strip → `swish`; tutup/buka/kartu → `kertas`; jatuh → `dum`; kilat → `kamera`; glitch → `glitch`), dan **mesin sudah memajukan bunyi perpindahan** setengah lama transisi sebelum titik potong. Lapisan: `geser`/`lempar` → swish, `jatuh` → dum di bingkai mendarat, `pop`/`tumbuh` → pop, `cap` → stempel, `kabur` → whoosh; `angka` → gulir; `sorot` stabilo → spidol; `papan` → ketik; efek `kilau` → boom, `cahaya` → riser, `bakar`/`garis` → whoosh. Matikan per perpindahan `sfxMasuk: false`, per lapisan `sfx: false`, per efek `sfx: false`.
- **Bunyi sintesis manual** (`sfx` adegan, `t` = detik sejak adegan mulai atau rujukan narasi `'L05.w3+0.1'`): `whoosh` `swish` `pop` `klik` `tik` `ketik` `impact` `boom` `riser` `ding` `benar` `salah` `kaching` `koin` `notif` `glitch` `dum` `jantung` `kamera` `sub` `kertas` `stempel` `spidol` `gulir` `proyektor` `ketukan`. Contoh: `sfx: [{ t: 'L07.w2-0.9', jenis: 'riser', lama: .9 }, { t: 'L07.w2', jenis: 'impact' }]`.
- **Berkas** (`rakit --sfx <folder>`, nama berkas tanpa ekstensi): `{ t, berkas, vol, lama, ulang, masuk, dari }` — `dari` = mulai dari detik ke-n di berkas, `ulang: true` = loop (ambience/room tone), `masuk` = fade-in (maks 0,3 dtk), fade-out 0,3 dtk otomatis. Ambience sepanjang adegan: `sfx: [{ t: 0, berkas: 'kota-pagi', vol: .14, lama: 6, ulang: true, masuk: .3 }]`. Room tone seluruh video: `KONFIG.sfx: [{ t: 0, berkas: 'ruang', vol: .06, lama: 60, ulang: true }]` (`t` di `KONFIG.sfx` = detik mutlak).
- **Ganti bunyi otomatis dengan berkas**: `KONFIG.sfxPeta: { whoosh: 'whoosh-sedang', swish: 'swish-cepat', kertas: 'kertas-amplop', stempel: 'stempel', dum: { berkas: 'boom-rendah', vol: .8, lama: 2 }, kamera: 'rana' }`.
- **Bunyi muncul per jenis lapisan**: `KONFIG.bunyiMuncul: { teks: 'teks', gambar: 'ikon', benda: 'popup', coret: 'spidol', vol: .55 }`; per lapisan `bunyi: 'salah'` atau `{ berkas, vol, geser }` (`geser` = offset detik, pakai −0,03 untuk mendahului bingkai). Hati-hati: bunyiMuncul membuat SEMUA teks berbunyi — kurangi dengan `sfx: false` pada teks kecil/sekunder (Hukum §1.4).
- **Volume bus** (ada di mesin, belum tercatat di `mesin.md`): `KONFIG.volumeSfx` (bawaan 1), `KONFIG.volumeSuara` (1,1), `KONFIG.volume` (master 0,9). Seluruh campuran lewat kompresor master lalu dinormalkan ke `KONFIG.lufs` (−14).
- **Sumber berkas**: (1) pustaka lokal `D:\Sound\Sound Effect\` (55 folder: `Swooshes`, `User Interface`, `Paper`, `Designed`, `Ambience`, `Clocks`, `Computers`, `Crowds`, `Explosions`, `Footsteps`, `Doors`, `Machines`, `Scifi`, `Weather`, …); (2) Epidemic Sound (`SearchSoundEffects` → `DownloadSoundEffect`; tautan kedaluwarsa ±5 menit, unduh langsung); (3) agen `penata-sfx` untuk memotong, menyamakan puncak, dan menyerahkan folder + daftar waktu siap tanam. Potong berkas sampai transient di sampel pertama (tanpa hening di depan) supaya `t` = bingkai hantaman.

## Teknik modern
- **Edit dipimpin bunyi (sound-led edit)**: susun bunyi kunci (riser, hening, hantaman) di timeline lebih dulu, lalu potong gambar mengikutinya. Manfaat: ritme terasa disengaja, bukan bunyi ditempel belakangan. Kapan: hook dan payoff. Alur: tulis kolom SFX di storyboard sebelum kolom transisi (`../../templat/storyboard.md`), rakit SFX dengan `KONFIG.sfx` (detik mutlak), baru sesuaikan `mulai` adegan.
- **Foley mikro (detail ala ASMR)**: bunyi sangat dekat dan bersih untuk aksi kecil (kertas digeser, pena diklik, kartu diletakkan, tombol HP). Manfaat: kolase/UI terasa fisik dan mahal. Kapan: gaya Handcrafted, Collage, Luxury, Minimalist. Alur: berkas dari `D:\Sound\Sound Effect\Paper`, `Objects`, `User Interface` via `--sfx`, volume rendah, tepat di bingkai kontak.

## Cek cepat
- [ ] Tidak ada SFX yang menutupi kata narasi (dengar di speaker HP).
- [ ] Whoosh memuncak di titik potong; impact tepat di bingkai mendarat.
- [ ] Tidak ada bunyi identik berulang lebih dari 3 kali tanpa variasi.
- [ ] Maks 2–3 hantaman besar per 45 dtk, masing-masing didahului ruang/hening.
- [ ] Ada room tone/ambience; tidak ada hening nol mutlak di tengah video.
- [ ] Palet bunyi konsisten dengan gaya visual (kertas untuk kolase, UI untuk digital, pita untuk retro).
- [ ] Gerak kamera pelan dan teks sekunder tidak berbunyi.
- [ ] LUFS −14 ±1, puncak < 0 dBFS (`jalankan.py cek` + ukur ffmpeg ebur128 sesudah ekspor).

## Celah mesin
- **Balik (reverse) / ubah nada per berkas** tidak ada. Akali: siapkan berkas terbalik dengan `ffmpeg -i swell.wav -af areverse swell-balik.wav` (atau `asetrate`/`atempo` untuk nada), lalu tanam lewat `--sfx`.
- **Redam musik oleh SFX** (sidechain untuk hantaman) tidak ada; musik hanya diredam oleh narasi. Akali: edit berkas musik di titik hantaman (`ffmpeg … -af "volume=enable='between(t,12.2,12.8)':volume=0.3"`) atau pakai musik sintesis bersegmen dengan `vol` lebih rendah di segmen itu.
- **Pan dan EQ per berkas** tidak bisa diatur (sintesis whoosh/swish sudah ber-pan). Akali: siapkan versi kiri/kanan berkas di luar mesin.
- **Variasi otomatis** (gilir 3 varian whoosh) tidak ada; `sfxPeta` memetakan satu berkas per jenis. Akali: matikan bunyi otomatis transisi tertentu (`sfxMasuk: false`) dan tulis `sfx` manual dengan varian lain.
