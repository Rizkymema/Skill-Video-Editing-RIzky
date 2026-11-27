# Gerak elemen: setiap gambar terdiri dari elemen yang bisa dihidupkan (Kolase 1.5)

Sejak 27 Nov 2026 (permintaan pengguna sesudah membedah reel @earn.edits `Del7Vohuw9D`: "tambahkan rigging, motion design, dan image animation ke flow yang sudah ada… setiap elemen visual di dalam gambar lebih hidup… rigging universal untuk karakter, produk, kendaraan, bangunan, objek, ilustrasi, environment"). Ini **bukan alur baru**: langkah 4c di Tahap 2 (`SKILL.md`), sesudah aset ada dan sebelum storyboard final. Alur 5 tahap, mesin satu HTML, dan semua aturan lama tetap.

Manfaat tambahan: **lebih hemat Google Flow**. Satu gambar (Flow, foto berlisensi `ambil_media.py`, kiriman pengguna, aset seri) bisa menghasilkan 3–6 gerakan berbeda, jadi jumlah aset per video turun dan foto asli yang tadinya "diam" ikut hidup.

## 1. Rantai animasi (sama dengan After Effects, dijalankan mesin Kolase)
`Adegan → Elemen → Lapisan → Rig/Transform → Keyframe → Gerak sekunder → Kamera → Efek → Hasil`

| Tahap | Di mesin | Catatan |
|---|---|---|
| Adegan | `ADEGAN[i]` | waktu dari narasi (`'L05.w4'`) |
| Elemen | `elemen: [...]` di lapisan gambar | wilayah dari gambar yang sama: `kotak` / `bulat` / `titik` (pecahan 0–1) |
| Lapisan | `lapis: [...]` dengan `z` | depan/tengah/belakang → parallax otomatis |
| Rig / transform | `poros`, `putar`, `skala`, `condong`, `alfa`, `rig` (mesh) | elemen berputar/miring di sekitar porosnya |
| Induk-anak | elemen = anak lapisan gambarnya; lapisan lain: `induk: 'id'` | anak ikut semua gerak induk + geraknya sendiri |
| Keyframe | `gerak: [[t, { x, y, putar, skala, condong, alfa, terang, blur }, ease], ...]` | `ease`: `outCubic` · `outBack` (overshoot) · `pegas` (settle) · fungsi sendiri |
| Gerak sekunder | `goyang` · `ombak` · `denyut` · `putaran` · `arus` · `kedip` | osilasi halus terus-menerus, beda `fase` per elemen = overlapping |
| Kamera | `kamera` preset/keyframe/fungsi + perpindahan bermomentum | gerak kamera ikut ke elemen (elemen anak lapisan) |
| Efek | `efek` (cahaya, kerucut, jendela, partikel…) + grade | dipakai hemat (`polish/qc.md` §6 di `sutradara-edit`) |
| Hasil | `cek`, `kontak`, pratinjau di HTML (real-time), ekspor MP4 | blur gerak otomatis di gerak cepat |

## 2. Identifikasi elemen (wajib dilihat, bukan ditebak)
1. `python -X utf8 -I scripts/elemen.py saran _kerja/gambar/<kode>.jpg` → usulan otomatis (titik cahaya/jendela/layar menyala, pita langit, bagian terpisah di PNG transparan) + `<kode>_saran.jpg`. Usulan bisa salah (kertas putih terbaca "cahaya"), jadi hanya titik awal.
2. `python -X utf8 -I scripts/elemen.py kisi _kerja/gambar/<kode>.jpg` → `<kode>_kisi.jpg` dengan kisi 0–1. **Lihat** gambar itu, tulis wilayah tiap elemen dan porosnya (sendi, engsel, pusat roda, pangkal batang).
3. Tulis `_kerja/elemen-<kode>.json` (daftar elemen), cek dengan `elemen.py uji _kerja/gambar/<kode>.jpg _kerja/elemen-<kode>.json` → lihat `<kode>_uji.jpg` (wilayah + poros bernomor). Perbaiki sampai pas, lalu salin daftarnya ke `elemen: [...]` lapisan di `konfig.js`.
4. Di tabel storyboard, kolom gambar ditulis dengan elemennya: "lab · layar osiloskop berkedip, lampu berdenyut".

## 3. Apa yang bisa hidup, dan dengan cara apa
Pilih cara **paling ringan yang cukup**. Rig mesh hanya bila benda harus melentur; jangan memasang rig di semua elemen.

| Jenis | Elemen | Cara (kunci mesin) | Nilai awal yang terasa alami |
|---|---|---|---|
| Manusia | kepala | `goyang` (poros leher) atau `rig: 'angguk'` | 1,5–3° / 2,5–4 dtk |
| | dada/badan | `rig: 'napas'` | bawaan |
| | tangan menunjuk/melambai | `gerak` putar di poros siku/bahu + `outBack`; pergelangan `rig: 'tekuk'` | 6–15° sekali, lalu `goyang` 1° |
| | rambut, pakaian, syal | `rig: { jenis: 'kibar', dari: 'kiri' }` | amp .015–.03 |
| | ekspresi/mata | potongan wajah terpisah dari Flow, ganti `alfa` | — |
| Kendaraan | roda, baling-baling, kipas | `putaran` (bulat, poros = pusat roda) | 180–720 °/dtk (sesuai kecepatan cerita) |
| | bodi | `ombak { y: 2–4 }` (getar mesin) | periode .2–.4 |
| | lampu depan/rem | `kedip` atau `gerak` `terang` (menyala) | kuat .2–.5 |
| | kaca | `kilap` pada lapisan, atau elemen `terang` sekali | — |
| Produk | tutup botol/kemasan | `gerak` `y` + `putar` (membuka), `outBack` | 10–40 px |
| | tombol | `denyut` atau `gerak skala` .92 → 1 (ditekan) | — |
| | label/stiker | `goyang` kecil, `rig: 'miring'` | 1–2° |
| Bangunan | jendela/lampu ruangan | `kedip` (terang) beda `laju` tiap jendela | kuat .2–.45, laju 2–9 |
| | pintu/daun jendela | `gerak` `condong`/`skala` x (membuka), poros di engsel | — |
| | papan nama/bendera | `rig: 'kibar'` / `goyang` | — |
| Alam | awan | `arus { x: 4–10 }` (px/dtk) atau `ombak { x: 6 }` | sangat pelan |
| | daun/pohon/rumput | `goyang` poros di pangkal (+ `tambal` bila geraknya besar) | 1–2° / 3–4 dtk |
| | air, asap, kabut | `ombak` + `denyut`; asap: `arus { y: -12, skala: .03, pudar: .2 }` | — |
| | cahaya | `kedip` pelan (`laju` 1–2) atau efek `cahaya`/`kerucut` | — |
| Objek | jarum jam/meteran | `putaran` di poros jarum | detik: 6 °/dtk |
| | layar (TV, HP, osiloskop) | `kedip` cepat (`laju` 6–12) + konten `hp.lukis` bila perlu | — |
| | kertas di meja | `rig: 'kibar'` lemah / `ombak` | — |
| Latar | depan/tengah/belakang | pisahkan jadi lapisan dengan `z` 0,3 / 1 / 1,8 (pelat + potongan Flow) | parallax otomatis |
| Ilustrasi | tiap bentuk terpisah | `elemen` per bentuk, atau PNG bagian (`saran` mendeteksi bagian terpisah) | — |

**Kapan elemen dari satu gambar tidak cukup** (minta potongan Flow terpisah / foto lain): gerak besar yang memperlihatkan belakang benda (pintu terbuka lebar, orang berjalan, tangan mengambil barang), benda keluar dari bingkainya, atau bagian yang tertutup benda lain. Elemen dari satu gambar cocok untuk gerak di tempat (putar, kedip, goyang, ayun, ombak kecil).

## 4. Prinsip gerak (bukan sekadar digeser)
- **Easing**: masuk `outCubic`/`outQuart`, aksi tegas `outBack` (overshoot 4–10%), mendarat `pegas` (settle). Linear hanya untuk benda mekanis (roda, jarum).
- **Antisipasi + follow-through**: aksi sekali (tangan menunjuk, pintu terbuka) memakai 3 keyframe: mundur sedikit → aksi → lewat sedikit lalu kembali.
- **Overlapping**: elemen sejenis tidak boleh serempak; beri `fase` berbeda (0, .3, .55) dan `laju` berbeda untuk lampu.
- **Sekunder halus**: amplitudo kecil (tabel §3). Kalau gerak terlihat sebagai "efek", terlalu besar.
- **Kedalaman**: elemen ikut `z` lapisannya; kamera bergerak pelan terus (napas kamera bawaan) supaya parallax terasa.
- **Motion blur** otomatis pada gerak cepat (perpindahan, `terbang`, putaran cepat); jangan menambah blur manual di gerak lambat.
- **Anggaran**: 2–5 elemen bergerak per adegan; satu elemen "bintang" yang paling terlihat, sisanya sekunder. Tiap elemen punya fungsi (menunjukkan hidup, menarik mata ke subjek, menjelaskan aksi). Hukum Sutradara tetap berlaku.

## 5. Tambal lubang
Elemen yang bergeser dari tempatnya (pohon bergoyang besar, papan berayun) memperlihatkan piksel aslinya di bawah. `tambal: true` menutup wilayah aslinya dengan warna sekitar yang sangat kabur, jadi tidak ada "bayangan ganda". Tidak perlu untuk gerak di tempat (putaran roda, kedip, denyut kecil).

## 6. Teknologi
Mesin tetap **Canvas 2D + JavaScript dalam satu HTML** (deterministik, ekspor MP4 di browser, tanpa server). Kedalaman, parallax, kamera, perspektif (`rig: 'miring'`), deformasi (mesh rig), cahaya (efek), dan blur gerak sudah tersedia di Canvas. Three.js/WebGL **tidak ditambahkan** ke skill ini: tidak dibutuhkan oleh gaya kolase 2,5D dan akan memperlambat ekspor. Untuk huruf 3D bervolume dan kamera 3D sungguhan, pakai skill `teks-kinetik-3d` (sudah memakai Three.js).

## 7. Kinerja
- Potongan elemen (tepi lembut + tambalan) dibuat **sekali** per gambar lalu dipakai ulang tiap bingkai.
- Filter terang/blur hanya pada potongan kecil. Rig mesh: maks ±4 elemen ber-rig per adegan.
- Pratinjau real-time tetap di HTML (tombol putar); `kontak --t` rapat untuk memeriksa gerak.

## 7a. Uji (27 Nov 2026)
Konfig uji 5 adegan tanpa gambar Flow baru: layar osiloskop berkedip (selisih piksel wilayah 33,9 vs 6,9 di dinding pembanding), roda kaset berputar (38,6 vs 13,3), pohon bergoyang dengan kamera diam (12,0 vs 2,4), label ikut kaset (`induk`), poros + condong, 4 transisi baru. Video Kodak yang dirakit ulang dengan mesin 1.5 identik piksel demi piksel dengan mesin 1.4 (fitur baru tidak mengubah konfig lama).

## 8. Cek cepat
- [ ] Tiap gambar utama sudah dibaca elemennya (`saran` + `kisi` dilihat)
- [ ] 2–5 elemen bergerak per adegan, satu jadi pusat perhatian
- [ ] Elemen sejenis beda fase/laju (tidak serempak)
- [ ] Poros di sendi/engsel/pusat yang benar (`elemen.py uji` dilihat)
- [ ] Tidak ada bayangan ganda (pakai `tambal` bila elemen bergeser)
- [ ] Gerak tetap halus; tidak ada yang terlihat seperti efek tempelan
