# Campur gaya: dua gaya, satu bahasa visual

> STYLE · dipakai di langkah 4 (pilih gaya) dan 9–11 (huruf, transisi, bunyi) · terkait: `gaya-visual.md`, `warna-tekstur.md`, `resep/`, `../type/tipografi-kinetik.md`, `../motion/transisi.md`, `../audio/sound-design.md`, `../polish/qc.md`

Prinsip inti:
- **Campuran butuh alasan cerita.** Contoh alasan sah: topik punya dua dunia (masa lalu vs masa kini, data vs emosi, mesin vs manusia). "Biar keren" bukan alasan.
- **Satu gaya dominan, satu tamu.** Dominan (≥ 70% durasi dan layar) memegang warna, tekstur, kamera, dan tempo. Tamu hanya memegang 1–2 lapisan yang jelas (mis. tipografi saja, atau UI + bunyi UI saja).
- **Konstanta bersama tidak boleh dua**: satu grade, satu lapisan tekstur global, ≤ 2 warna aksen, satu keluarga transisi (dari gaya dominan).
- **Tamu muncul dengan pola**, bukan acak: selalu di jenis adegan yang sama (mis. semua kartu data memakai gaya tamu) supaya penonton belajar "kalau gaya ini muncul, artinya X".
- Campuran yang berhasil terlihat seperti **satu gaya baru**, bukan dua video yang ditempel.

## 1. Aturan pembagian kendali
| Lapisan keputusan | Dipegang | Catatan |
|---|---|---|
| Grade warna + tekstur global | **Dominan**, selalu | satu `KONFIG.grade`; tamu tidak membawa grain/VHS/halftone sendiri |
| Kamera + tempo | **Dominan** | tamu boleh mempercepat 1–2 adegan khasnya, tidak mengubah tempo keseluruhan |
| Transisi | **Dominan** | tamu boleh punya **satu** transisi tanda tangan yang hanya muncul saat masuk/keluar dunianya |
| Tipografi | dominan **atau** tamu | bila tamu memegang huruf, dominan tetap memegang ukuran hierarki dan posisi |
| UI / benda khas | tamu (bila topiknya menuntut) | mis. Dark Tech memegang layar dan panel saja |
| Bunyi | dominan untuk musik + ambience; tamu boleh memegang **satu** keluarga SFX | mis. bunyi UI hanya dari dunia tamu |
| Warna aksen | 1 dari dominan + 1 dari tamu, maksimal | aksen tamu hanya di lapisan yang ia pegang |

Rumus cepat: **Dominan = dunia. Tamu = lensa.** Penonton tinggal di dunia dominan dan sesekali melihat lewat lensa tamu.

## 2. Kecocokan pasangan
| Pasangan | Status | Kenapa |
|---|---|---|
| Cinematic + Documentary | baik | sama-sama realistis; dominan sinematik memberi rasa, dokumenter memberi kepercayaan |
| Editorial + Grunge | baik (hati-hati tekstur) | hierarki editorial menahan kekacauan grunge |
| Dark Tech + UI Motion (Futuristic UI) | baik | satu dunia digital; tinggal pilih siapa memegang warna |
| Retro VHS + tipografi modern | baik | kontras zaman jadi pesan ("dulu vs sekarang") |
| Luxury + Minimal | sangat baik | keduanya hidup dari ruang kosong |
| Psychological + Experimental | hati-hati | keduanya ekstrem; Experimental hanya untuk 2–3 momen "pikiran meledak" |
| Newspaper + Collage | sangat baik | sama-sama kertas |
| Corporate Premium + Futuristic UI | baik | data rapi + antarmuka depan |
| Cinematic Documentary + Analog Film | baik | analog untuk kilas balik saja |
| Handcrafted + Corporate | hati-hati | hangat vs steril; pakai Handcrafted untuk anotasi saja |
| Social Media Viral + Luxury | hindari | tempo dan nada bertabrakan; satu teriak, satu berbisik |
| Cyberpunk + Vintage Commercial | hindari | dua palet kuat, dua zaman, tidak ada alasan cerita bersama |
| Y2K + Psychological | hindari | kecuali parodi yang disengaja |
| Grunge + Luxury | hindari | tekstur kotor merusak rasa mahal; pilih salah satu |
| Retro VHS + Analog Film | hati-hati | dua tekstur analog berbeda; pilih satu sebagai tekstur global |

## 3. Campuran yang sudah dirancang
### A. Cinematic + Documentary (dominan Cinematic)
- **Kendali**: Cinematic memegang grade, kamera (dorong pelan), tempo 3 dtk, transisi `fokus`/`cocok`. Documentary memegang kartu foto asli berlabel kredit, lower-third, dan peta/grafik bersumber.
- **Palet**: latar `#0E0F11`, teks `#F2EEE6`, aksen `#C8A24A` (rasa) + `#FFD23F` hanya di label data.
- **Huruf**: serif miring + Inter 800 (dominan); label Inter 600 di pil gelap (tamu).
- **Transisi**: `fokus`, `cocok`, `bingkai` sekali; foto asli masuk lewat `kartu`.
- **Bunyi**: drone + sub-hit (dominan); rana kamera saat foto asli muncul (tamu).
- **Contoh topik**: "Proyek pesawat N250: dari hanggar ke museum".
- **Tanda berantakan**: foto asli digrade berbeda dari ilustrasi; label kredit memakai gaya huruf ketiga.

### B. Editorial + Grunge (dominan Editorial)
- **Kendali**: Editorial memegang latar terang, hierarki, kamera tenang, transisi `geser`/`fokus`. Grunge memegang **hanya** kata-kata emosi (huruf kasar, cap) dan bunyi kertas/stempel.
- **Palet**: latar `#F5F5F2`, teks `#121212`, aksen `#D7261E` (grunge, hanya di cap/kata marah).
- **Huruf**: Inter 800 + serif (editorial); Anton + `stiker`/`cap` untuk 1 kata per adegan (grunge).
- **Transisi**: `geser`, `fokus`; `jatuh`/`cap` hanya saat kata grunge mendarat.
- **Bunyi**: klik bersih (editorial); stempel, sobek kertas (grunge).
- **Contoh topik**: "Kenapa kamu capek padahal tidak ngapa-ngapain" (rapi, lalu tekanan meledak di kata kunci).
- **Tanda berantakan**: tekstur kertas kotor menutupi seluruh latar editorial; tiga cap dalam satu adegan.

### C. Dark Tech + UI Motion (dominan Dark Tech)
- **Kendali**: Dark Tech memegang grade gelap, kamera dolly, tempo, bunyi dengung. UI Motion memegang panel, kursor, grafik, dan easing mikro (outExpo 200 md, stagger 40 md).
- **Palet**: latar `#07080A`, teks `#E8EEF4`, aksen `#38E1FF` (sinyal) + `#5B8CFF` (UI aktif).
- **Huruf**: Inter 700 + Courier untuk log (dominan); angka monospace di UI.
- **Transisi**: `dorong` ke layar, `bingkai` ke monitor; antar-panel `cocok` (shared element).
- **Bunyi**: dengung + sub (dominan); klik/bip UI (tamu).
- **Contoh topik**: "Begini cara algoritma memilih video yang kamu tonton".
- **Tanda berantakan**: semua panel bercahaya; UI bergerak terus tanpa ada yang dibaca.

### D. Retro VHS + tipografi modern (dominan Retro VHS)
- **Kendali**: VHS memegang grade, garis layar, derau pembuka, tempo, bunyi pita. Tipografi modern (Inter 800 bersih, tanpa tekstur) memegang semua judul dan angka, supaya terbaca tajam di atas gambar lembek.
- **Palet**: latar `#10131C`, teks `#FFFFFF`, aksen `#FF3B3B` (satu kata per judul).
- **Huruf**: Inter 800 besar + Courier untuk cap waktu.
- **Transisi**: `kilat`, `glitch` ≤ 2, potong keras; teks masuk `geser` halus (modern) di atas gambar yang patah (VHS).
- **Bunyi**: desis pita, klak play/stop; whoosh bersih saat teks modern masuk.
- **Contoh topik**: "Warnet 2005: tempat satu generasi belajar internet".
- **Tanda berantakan**: tekstur VHS juga diterapkan ke teks; dua jenis huruf modern berbeda.

### E. Luxury + Minimal (dominan Luxury)
- **Kendali**: Luxury memegang serif, champagne, dolly lambat, bunyi senar. Minimal memegang tata letak (60–70% ruang kosong, satu benda per bingkai) dan aturan "satu kata aksen".
- **Palet**: latar `#EFE8DC`, teks `#1A1612`, aksen `#C9A45C`.
- **Huruf**: Georgia besar + label Inter kecil berjarak lebar.
- **Transisi**: `fokus`, `geser` lambat, `cocok`.
- **Bunyi**: senar, denting, hening panjang.
- **Contoh topik**: "Kenapa kopi seharga Rp300 ribu tetap laku".
- **Tanda berantakan**: kilau partikel emas; teks lebih dari 6 kata per bingkai.

### F. Psychological + Experimental (dominan Psychological)
- **Kendali**: Psychological memegang grade gelap, kamera merayap, tempo lambat, drone. Experimental hanya memegang **2–3 momen ledakan pikiran** (bentuk dan huruf berserakan, ritme cepat 0,3–0,5 dtk) yang selalu kembali ke gelap sunyi.
- **Palet**: latar `#0C0C0E`, teks `#D9D6D0`, aksen `#8E1B1B` + momen ledakan `#F2F0EA` putih datar.
- **Huruf**: serif kecil (dominan); kata besar tebal pecah-pecah di momen ledakan.
- **Transisi**: potong ke hitam, `fokus` (dominan); `strip`/`putar` hanya di momen ledakan.
- **Bunyi**: drone, detak jantung; momen ledakan = tumpukan bisikan/derau pendek lalu hening total.
- **Contoh topik**: "Overthinking jam 2 pagi: apa yang terjadi di otakmu".
- **Tanda berantakan**: ledakan lebih dari 3 kali; Experimental mulai mengubah grade.

### G. Newspaper + Dark Tech (dominan Newspaper)
- **Kendali**: kertas, koran, halftone memegang dunia; Dark Tech memegang layar-layar yang "dicetak" di koran (foto layar di kolom, layar TV).
- **Palet**: `#ECE2C8`, `#1B1712`, aksen `#D7261E` + `#38E1FF` hanya di dalam layar.
- **Contoh topik**: "Virus komputer pertama yang bikin heboh koran 1999".
- **Tanda berantakan**: layar tanpa halftone terlihat ditempel di kertas (samakan grade).

### H. Cinematic Documentary + Handcrafted (dominan Cinematic Documentary)
- **Kendali**: dokumenter memegang foto/video alam dan kamera; Handcrafted memegang anotasi tangan (panah, lingkaran, label Caveat) di atas foto.
- **Palet**: grade dokumenter; aksen `#C0583A` hanya untuk coretan.
- **Contoh topik**: "Hutan bakau: tembok laut gratis yang kita tebang".
- **Tanda berantakan**: coretan di setiap bingkai; huruf tangan untuk kalimat panjang.

## 4. Langkah mencampur
1. Tulis alasan cerita satu kalimat ("dua dunia: …").
2. Pilih dominan (dunia) dan tamu (lensa). Isi tabel §1 di brief baris 6–7 (`../../templat/brief.md`).
3. Tentukan **pemicu tamu**: jenis adegan apa yang selalu memakai gaya tamu.
4. Satukan konstanta: satu grade, satu tekstur, ≤ 2 aksen, keluarga transisi dominan.
5. Bangun 2 adegan uji (satu dominan, satu tamu) → `kontak` → apakah terlihat satu keluarga? Bila tidak, kurangi lapisan tamu, jangan menambah.

## 5. Resep reel + salah satu dari 20 gaya
Resep (`resep/`) sudah merupakan gaya lengkap, jadi **resep selalu dominan**. Gaya tambahan hanya menjadi tamu dengan satu tugas:
| Resep | Tamu yang cocok | Tugas tamu |
|---|---|---|
| Sinema Kasus | Documentary | kartu bukti asli berkredit + tanggal |
| Legenda Gelap | Handcrafted | peta/coretan tangan asal-usul |
| Piksel Kertas | Corporate Premium | grafik data rapi di layar komputer piksel |
| Panggung Emas | Minimalist | layar penutup bersih (syarat, tanggal) |
| Arsip Pop | Futuristic UI | peta rute/indikator progres yang bersih |
| Kaca Gradien | Cinematic Editorial | satu adegan emosional (manusia nyata) di tengah dunia UI |
| Panggung Korporat | Newspaper/Magazine | kliping berita di babak jatuh |

## Cek cepat
- [ ] Ada alasan cerita satu kalimat untuk mencampur
- [ ] Dominan ≥ 70% dan memegang grade, tekstur, kamera, tempo
- [ ] Tamu memegang ≤ 2 lapisan dan muncul dengan pola yang sama
- [ ] Satu grade, satu tekstur global, ≤ 2 aksen
- [ ] Lembar kontak terlihat satu keluarga (uji 2 adegan)

## Celah mesin
- Grade hanya bisa diganti per adegan (`grade` di adegan), tidak per lapisan; tamu yang butuh warna lain di dalam adegan dominan harus memakai `hitamPutih`/`campur` atau gambar yang sudah diwarnai (akali: siapkan aset tamu dengan warna yang sudah cocok sebelum masuk mesin).
- Belum ada "set gaya" yang bisa dipanggil per adegan (`gaya: 'tamu'` yang sekaligus mengganti gayaTeks + SFX + transisi); usul: `KONFIG.gayaTamu` + `adegan.gaya: 'tamu'`.

## Teknik modern
- **Lensa tamu sebagai penanda makna**: gaya tamu hanya muncul saat penonton masuk "kepala" tokoh atau "dunia data". Manfaat: penonton membaca struktur tanpa narasi. Cara: tulis pemicu tamu di storyboard (`../../templat/storyboard.md` kolom Fungsi).
- **Peralihan gaya bertahap**: dominan perlahan "kemasukan" tamu sepanjang video (mis. dokumenter tenang makin terdistorsi saat konflik naik). Cara: naikkan satu parameter per babak (grain, garis, kontras) di `grade` per adegan, maksimal 3 langkah.
