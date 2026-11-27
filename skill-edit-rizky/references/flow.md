# Aset gambar Google Flow

Dari tutorial @earn.edits (reel 22 Okt 2026): inspirasi → prompt → gambar berlapis di Flow → buang latar hijau/mask → kamera 3D → tint + halftone. Di skill ini langkah 4–6 dikerjakan `flow_kolase.py` + mesin HTML.

## 1. Dua jenis aset
| Jenis | Isi | Hasil |
|---|---|---|
| `pelat` | latar penuh 9:16 (tempat, suasana) dengan **ruang kosong di sepertiga atas** untuk judul | `gambar/<kode>.jpg`, dipakai `{ gambar: 'kode' }` (otomatis menutup layar) |
| `potongan` | satu subjek/benda di **latar hijau polos #00FF00**, utuh dengan margin | `gambar/<kode>.png` transparan, dipakai dengan `x, y, lebar, z, bayangan` |

Tidak pernah ada teks di gambar Flow (prompt melarang); teks ditulis mesin. Satu video ±10–16 aset (N250: 9 pelat + 5 potongan). Pelat bisa dipakai ulang (foto di koran, kartu foto, isi TV).

## 2. Menulis aset.json
Lihat docstring `scripts/flow_kolase.py`. Tips isi (`isi`, bahasa Inggris):
- Sebut zaman, tempat, dan sudut pandang ("seen from behind", "from below", "wide shot"); orang dari belakang/jauh lebih aman dan lebih "arsip".
- Benda khas cerita digambarkan lengkap di setiap aset (warna, garis, bentuk), karena Flow tidak ingat antar-gambar. Untuk benda yang harus identik, beri `acuan` gambar (references).
- Potongan: subjek tunggal, tidak menyentuh tepi kecuali memang dipotong (tangan dari tepi, badan setengah). **Pilih salah satu dengan sengaja** (Kolase 1.2, keluhan pengguna: tangan berlengan terlihat terpotong di tengah layar): (a) **utuh**: "entire object fully visible, generous green margin on all sides" untuk benda yang melayang/dipindah (`cocok`, `terbang`); (b) **masuk dari tepi**: "arm entering from the bottom edge of the frame" untuk tangan, lengan, badan setengah, kerumunan; sisi itu otomatis ditempel ke tepi layar (`jangkar`), jadi letakkan lapisannya memang dekat tepi tersebut (`y` besar untuk tangan dari bawah).
- Potongan yang akan diberi `rig` (tokoh, tangan, bendera, tanaman): pose netral, sendi terlihat jelas (pergelangan, leher), tidak ada benda lain yang menempel di bagian yang bergerak.
- Gaya per aset boleh beda: `arsip` (bawaan), `modern` (masa kini), `gelap` (malam, dramatis). Grade mesin menyatukan warnanya.

## 3. Generate (0 kredit, tanpa izin terpisah)
```
python -X utf8 -I scripts/flow_kolase.py rencana <_kerja>
```
lalu panggil `flow_agent_images` dengan `project`, `aspect_ratio`, `scenes` (+ `references`, `scene_references`) dari `flow_batch.json`, kemudian `flow_wait` sampai `finished`. Bila belum ada proyek Flow terbuka: `flow_new_project` dengan judul video. Mode Agent kadang gagal lalu Flow membuat satu per satu (lebih lama, ±15 menit untuk 14 gambar, tetap 0 kredit).

## 4. Unduh 2K (wajib untuk hasil tajam)
Unduhan bawaan hanya 768×1376 (terlalu kecil untuk 1080×1920 + zoom kamera). Ambil versi besar gratis:
`flow_assets` (judul `<proyek>-scene-NN`) → `flow_download` `{ project: '<proyek>-2k', quality: 'upscaled', assets: [...urut] }` → `flow_wait` → lalu
```
python -X utf8 -I scripts/flow_kolase.py ambil <_kerja> --proyek <proyek>-2k
```
(`--proyek` membaca hasil dari folder itu; nama berkas `scene-NN` atau `<proyek>-scene-NN` sama-sama dikenali).

**`flow_download` bisa melapor gagal padahal berkasnya sudah ada** (uji 27 Nov 2026, video Kodak): status `failed` / `fetch failed`, tetapi ke-14 gambar 2K (1536×2752) sudah tersimpan sebagai `clip-01` … `clip-14` di `<proyek>-2k`. Jadi **sebelum mengulang, lihat dulu foldernya** (`ls … <proyek>-2k`, cek ukuran ±1,5–3,5 MB per berkas). Setiap pengulangan menambah salinan baru dengan nomor lanjutan (`clip-15`, `clip-16`, …), dan `ambil` memetakan nama ke kode menurut urutan, jadi salin hanya `clip-01` … `clip-NN` ke folder bersih (mis. `<proyek>-2k-bersih`) lalu `ambil <_kerja> --proyek <proyek>-2k-bersih`. Pratinjau Tahap 2 boleh memakai gambar resolusi biasa (`ambil … --proyek <proyek>`); versi 2K wajib sebelum render final.

Catatan: `ambil` memetakan `scene-NN`/`clip-NN` ke kode lewat **urutan di `flow_batch.json`**. Bila yang diunduh berbeda dari batch awal (aset dibuat ulang, hanya sebagian diunduh), samakan urutan `aset.json` dengan urutan unduhan lalu jalankan `rencana` lagi sebelum `ambil`; kalau tidak, nama berkas tertukar. Bendera, lambang, dan bangunan khas (gedung pengadilan, ruang sidang) sering salah di Flow (bendera Denmark di ruang sidang, gedung mirip Mahkamah Agung AS): periksa dengan zoom, tulis "no flags, no emblems" bila bendera tak perlu.

## 5. Periksa
- `gambar/_kontak.jpg`: semua aset; `gambar/potong/potong_cek.jpg`: potongan di atas kotak-kotak dan latar gelap.
- `PERIKSA … menyentuh tepi`: wajar untuk tangan/setengah badan yang masuk dari tepi layar; untuk benda utuh, buat ulang.
- Sisa hijau di tepi (awan, rambut): `ambil --toleransi 1.3`.
- Ulang sebagian: `rencana --hanya kode1,kode2` → generate → `ambil` (hanya kode itu yang ditimpa).
- `rakit --gambar <_kerja>/gambar` menanam semua gambar sebagai WebP (sisi terpanjang ≤ 1700 px); berkas berawalan `_` dan subfolder tidak ikut.

## 6. Klip gerak (opsional, berbayar)
Alurnya di `klip.md` (`aset.json["klip"]` → `flow_kolase.py klip` → tanya kredit → `flow_generate` → `ambil-klip` → `rakit --klip …[:hijau]`, foto hidup/potongan bergerak). Klip selalu berbayar, jadi **tanya dulu**; tanpa klip, gerak cukup dari kamera + lapisan. (Catatan lama yang menggandakan isi `klip.md` dihapus 27 Nov 2026.)

## 7. Bahan dari pengguna: foto dan klip asli (berita/tokoh nyata)
Foto/video nyata dari internet (Wikipedia, Commons, NASA, kutipan YouTube) diambil dengan `scripts/ambil_media.py`; aturannya di `data-media.md`. Bagian ini untuk bahan yang dikirim pengguna (`ambil_media.py ambil <berkas> <_kerja> --kode … --kredit "…"` mencatatnya juga).
- **Foto tokoh yang dikirim pengguna**: simpan di `gambar/` (resolusi kecil dibesarkan Lanczos ×4, wajah tidak diubah), pakai sebagai `benda: kartu` hitam-putih (`hitamPutih: true`), jangan latar penuh. Wajah tokoh lain tidak dibuat Flow; tampilkan dari belakang/siluet atau tulisan.
- **Klip video asli** (mis. pernyataan resmi di YouTube): `yt-dlp` sering ditolak ("Sign in to confirm you're not a bot"); jangan memakai cookie browser pengguna tanpa izin. Cara aman: pengguna menaruh MP4 (mis. `Downloads\…mp4`), potong 4–6 dtk bisu ke `_kerja/klip/<nama>.mp4` (`ffmpeg -ss <mulai> -t <lama> -an`), lalu `rakit --klip <nama>=klip/<nama>.mp4@12` dan pakai lapisan `{ urutan: '<nama>', lebar: 960, bayangan: true, cek: false }`. Cantumkan kredit di layar (`Sumber: <kanal> (YouTube)`) dan di `KONFIG.sumber`.
- **Poin penting dari video** tanpa mengunduh: buka di browser Claude, putar muted dengan `playbackRate` 3, baca `.ytp-caption-segment` tiap 150 ms (teks otomatis, cocokkan lagi dengan subtitle di klip sebelum dikutip). Kutipan dari tokoh ditulis sebagai kutipan dan diatribusikan ("menurut …"); klaim tokoh tentang dirinya tidak dipakai sebagai fakta.
- **Berita terkini**: minimal 2 sumber per angka; bila sumber berbeda (jam, jumlah), tulis rentang atau jangan tampilkan; narasi hanya melaporkan, tanpa menilai; kategori YouTube `25`.
