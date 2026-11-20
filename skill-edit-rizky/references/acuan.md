# Acuan visual dari pengguna: gaya ikut acuan, topik tetap bebas

Sejak 20 Nov 2026 (permintaan pengguna: "setiap kali saya kirim referensi untuk visualnya dapat mengikuti juga, topik apa pun itu"). Pengguna boleh mengirim **video, gambar, tangkapan layar, atau tautan** sebagai acuan tampilan. Yang diikuti hanya **gaya** (latar, huruf, warna, bentuk kartu, gerak, ritme, bunyi). **Topik, naskah, data, dan aset tetap dari pengguna/riset**, dan tidak ada isi akun acuan yang disalin.

Contoh nyata: video "AI Sebenarnya Nggak Mikir Kayak Manusia" (20 Nov 2026): versi pertama memakai tema `teknologi` (gelap biru), lalu pengguna mengirim reel editorial monokrom; hasil akhirnya `contoh/ai-mikir.*` (latar `editorial`, gaya teks `serif` + `tebal` + `sorot`, kartu putih berbayang, menu chat dan keyboard mode terang).

## 1. Kapan berlaku
- Pengguna melampirkan video/gambar (atau menyebut berkas di `Downloads`, folder `Video Refrensi\<akun>\`, atau tautan) dengan kata seperti "visualnya seperti ini", "gaya ini", "seperti video yang saya kirim", "acuan".
- Bisa di Tahap 1 (sebelum naskah) atau di tengah (sesudah pratinjau): bila di tengah, naskah + waktu kata tetap; hanya tampilan dibangun ulang (simpan konfig lama sebagai `konfig-v1-<nama>.js`).
- Acuan **menang atas** tema bawaan (`gaya.md` §0.1) dan aturan beda-dari-video-terakhir (§0.4): pengguna memilih tampilan itu dengan sengaja. Pola cerita tetap dipilih dari topik.
- Tautan YouTube/IG/TikTok yang menolak diunduh tanpa login: minta pengguna mengunduh MP4-nya (jangan memakai cookie pengguna).

## 2. Bedah (wajib, sebelum menulis konfig)
1. `python -X utf8 -I scripts/bedah_acuan.py <_kerja> <video/gambar ...>` → `_kerja/acuan/`: `lembar-*.jpg` (2 bingkai/dtk berlabel detik), `potongan-*.jpg` (bingkai di tiap potongan), `ringkasan.json` (kecerahan, saturasi, kontras, palet 6 warna, jumlah potongan, rata-rata bidikan), `gaya-acuan.md` (kartu gaya; angka terisi).
2. **Lihat semua lembar sendiri** (Read gambar). Isi bagian » di `gaya-acuan.md`: latar, huruf, penekanan, gambar/benda, gerak + perpindahan, efek, ritme, bunyi, dan **yang tidak boleh ditiru**.
3. Video acuan bersuara: catat suasana musik (tempo, alat, gelap/terang) dan jenis efek bunyi dari yang terlihat (ketik, whoosh, pop, stempel); cari yang senada di Epidemic. Jangan memakai audio acuan.
4. Tulis ringkasan 6–8 baris di chat (seperti kartu identitas visual, `gaya.md` §0.3) dengan judul "Gaya acuan".

## 3. Terjemahan ciri acuan → fitur mesin
| Ciri di acuan | Fitur mesin (`mesin.md`) |
|---|---|
| warna keseluruhan (terang/gelap, monokrom, hangat/dingin, kontras) | `KONFIG.grade` objek: `{ tint, kuat, saturasi, halftone, grain, vinyet, debu, garis, kontras }` (monokrom: saturasi .85–.95; vinyet kuat: .5–.6) |
| warna aksen | `KONFIG.palet` (`kuning` = aksen kata `*…*`, `merah` = stiker/cap) — ambil dari `ringkasan.json` palet |
| latar polos/gradasi + bentuk dekoratif bergerak (lengkungan, garis putus-putus, grid silang) | `latar: { pola: 'editorial', varian: 0–4, gelap, grid, warna, warnaTengah, warna2, warnaSabit, warnaPutus, sabit: false, putus: false, laju }` |
| kertas, grid biru, sinar, spiral | `pola` `kertas` / `grid` / `sinar` / `spiral` |
| latar unik yang tidak ada di daftar | benda `kustom` berukuran 20×20 di `x:540, y:960, z:.15, cek:false, blurGerak:false` yang menggambar ke seluruh layar (lihat `mesin.md` benda kustom) |
| dua gaya huruf (kecil miring di atas, besar tebal di bawah) | `gaya: 'serif'` + `gaya: 'tebal'`; sorotan kotak hitam `gaya: 'sorot'`; ubah semua sekaligus lewat `KONFIG.gayaTeks: { tebal: { font, gaya, warna, kapital }, serif: {...} }` |
| huruf kapital tebal berbayang, stiker, label, mesin ketik, tulisan tangan | `judul` / `padat` / `stiker` / `label` / `mesin` / `tangan` (+ `gayaTeks` untuk warna/font) |
| teks muncul per kata saat diucapkan | `anim: 'luncur', ikut: true` |
| kartu foto/video bersudut bulat berbayang | lapisan `gambar` + `bayangan`, atau `benda: kartu`; untuk sudut bulat persis: benda `kustom` (`K.bulat`) |
| polaroid di tali + jepitan, foto dalam lingkaran | `benda: kartu` + `coret: 'garis'` (tali), `bingkai: { bentuk: 'bulat' }`, atau benda `kustom` |
| UI aplikasi (chat, keyboard, notifikasi, layar HP) | `benda: hp/notif/balon`, atau benda `kustom` (contoh lengkap di `contoh/ai-mikir.konfig.js`: keyboard, menu chat, papan peluang) |
| benda 3D/ikon logo | potongan Flow latar hijau, gambar kiriman pengguna, atau ubin digambar kode; logo merek **hanya dari pengguna** |
| perpindahan (zoom tembus, geser, whip, kilat, glitch, lingkaran) | `dorong`/`tarik`/`geser`/`sentak`/`kilat`/`glitch`/`iris`/`bingkai`/`cocok` (`gaya.md` §4) |
| adegan sela gelap (jam digital, kalimat dramatis) | satu adegan `latar: { pola: 'editorial', gelap: true }` + teks terang |
| ritme (rata-rata bidikan dari `ringkasan.json`) | panjang adegan: ±rata-rata bidikan acuan (batas cek tetap berlaku) |

Bila ciri penting tidak bisa dibuat dengan fitur yang ada: buat benda `kustom` di konfig (tanpa mengubah mesin). Bila dipakai berulang di lebih dari satu video, pindahkan ke mesin (`assets/templat.html`), catat di `mesin.md`, rakit ulang `contoh/n250` + `contoh/ai-mikir` dan `cek` BERES.

## 4. Membangun
1. Isi bagian "Terjemahan ke mesin" di `gaya-acuan.md`, lalu tulis `konfig.js` (kepala konfig = kartu gaya acuan, bukan kartu tema).
2. Storyboard tetap dari naskah/topik pengguna; pilih benda yang membuktikan isi topik **dengan bahasa visual acuan** (mis. acuan memakai kartu foto bersudut bulat → data/foto topik ditampilkan dalam kartu seperti itu).
3. `rakit` → `cek` BERES → `kontak` → **bandingkan berdampingan** dengan `acuan/lembar-*.jpg` (latar, huruf, kartu, kepadatan, warna). Perbaiki sampai sekilas terasa satu keluarga, lalu pratinjau.
4. Di pesan Tahap 2 sebut: apa saja yang diikuti dari acuan, apa yang sengaja **tidak** ditiru, dan bagian yang belum bisa sama (beserta alasannya).

## 5. Jangan
- Jangan menyalin logo/watermark/nama akun/kalimat/footage/foto/tokoh/musik acuan; buat ulang gayanya saja.
- Jangan meniru wajah orang nyata dari acuan dengan Flow.
- Jangan mengorbankan data benar dan zona aman 9:16 demi kemiripan.
- Acuan untuk satu video tidak otomatis berlaku ke video berikutnya; tanyakan "pakai gaya acuan yang sama?" bila pengguna tidak menyebutnya (gaya acuan tersimpan di `_kerja/acuan/gaya-acuan.md` video lama).
