# Klip gerak Flow + efek ala After Effects (Kolase 1.3)

Sejak 18 Nov 2026 (permintaan pengguna: "kombinasi dengan video dari Flow … hanya di bagian yang bagus saja, tapi juga bisa cuma foto", lalu "seolah saya mengedit langsung dari After Effects, kualitas bagus dan render cepat"). Video acuan @earn.edits ±90% gambar diam yang digerakkan kamera; gerak tubuh manusia di sana dari klip AI 1–3 dtk. Jadi klip hanya **bumbu** di momen yang memang butuh gerak, bukan pengganti foto.

## 1. Dua mode (ditanya di setup Tahap 1, pertanyaan "Gerak")
| Mode | Isi | Biaya |
|---|---|---|
| **Foto berlapis saja** | semua adegan dari gambar Flow/foto asli + kamera, rig, efek. Persis gaya acuan | 0 kredit |
| **Foto + klip Flow** | sama, ditambah 1–4 klip gerak 4 dtk di momen kunci (≤ 30% durasi video) | ±7 kredit per klip Omni 4 dtk (ditanya di dialog persetujuan Tahap 2) |

Pakai klip hanya bila geraknya membawa cerita dan tidak bisa dipalsukan kamera/rig: orang beraksi (menyerahkan, memukul palu, mengangkat jaring, berlari), air/ombak/api/asap yang bergerak, kendaraan melaju, kerumunan bergerak, momen puncak/hook. **Jangan** untuk tempat diam, benda diam, data, atau dokumen (kamera + efek sudah cukup). Satu klip dipakai 2–4 dtk saja; sisanya tetap foto.

## 2. Cara membuat (Tahap 2 rencana → Tahap 3 setelah disetujui)
1. Gambar awal sudah ada (pelat 2K atau potongan berlatar hijau dari Flow, 0 kredit). Klip dibuat **dari gambar itu** (`first_frame`), jadi bingkai pertama klip = foto di video: foto bisa "hidup" tanpa loncatan.
2. Tulis `aset.json["klip"]` (`flow_kolase.py` docstring): `kode`, `dari` (kode aset), `gerak` (SATU aksi berawal-berakhir, bahasa Inggris), `kamera` (satu gerak: `static locked-off` / `slow push-in`), `lama` 4, `model` `Omni 1.1 Flash` (Veo 3.1 - Fast ±20 kredit hanya bila wajah/tangan harus sangat realistis), `fps` 15.
3. `flow_kolase.py klip _kerja` → `flow_klip.json` + perkiraan kredit. Sebut daftar klip + total kredit di pesan Tahap 2 dan di opsi dialog persetujuan. **Tanpa persetujuan tidak ada klip** (video tetap jadi dari foto saja; adegannya sudah dirancang dari foto).
4. Sesudah disetujui: `flow_generate` dengan `project` + `scenes` dari `flow_klip.json` (sudah berisi `first_frame`, `download_quality: upscaled` 1080p, `max_credits`), `flow_wait`, lalu `flow_kolase.py ambil-klip _kerja` → `_kerja/klip/<kode>.mp4` + `klip/_cek-<kode>.jpg`.
5. **Periksa `_cek-<kode>.jpg` (8 bingkai/dtk)**: wajah/tangan/benda yang berubah bentuk di tengah gerak = jangan dipakai (potong pakai `klip.mulai`/hanya bagian awal, atau buang dan pakai foto). **Uji nyata pertama (18 Nov 2026, Omni 1.1 Flash 4 dtk, 7 kredit, 1080p)**: klip kerumunan berisi **potongan kamera mendadak di detik ±2,25** (tampilan melompat lebih dekat), padahal prompt "static locked-off". Awal klip (2,2 dtk) bagus, jadi dipangkas: `ffmpeg -i asli.mp4 -t 2.2 -c:v libx264 -crf 17 -pix_fmt yuv420p kode.mp4` (simpan yang asli sebagai `<kode>-asli.mp4`) dan dipakai dengan `klip: { tahan: true }` supaya berhenti di bingkai terakhir dan kembali jadi foto. Klip barisan atlet 4 dtk (kamera `slow push-in`, orang berjalan lurus) mulus penuh. Cari lompatan dengan membaca lembar periksa baris demi baris sebelum memutuskan.
6. `rakit … --klip <kode>=klip/<kode>.mp4@15` (klip dari potongan hijau: `@15:hijau`, latar dibuang per bingkai, transparan). Argumen siap salin dicetak `ambil-klip`.

Aturan prompt klip (playbook Flow): satu aksi yang jelas, satu gerak kamera, tidak ada benda dilempar/jatuh/muncul, tidak ada teks, tidak ada putar benda terbalik, tangan tidak memindahkan barang. Klip hijau: "background never changes, no shadows, camera locked off" (sudah ditambah otomatis).

## 3. Cara tampil di konfig
| Pola | Konfig | Kapan |
|---|---|---|
| **Foto hidup** | `{ gambar: 'nelayan', klip: { kode: 'nelayan-hidup', t: 'L08.w9', lebur: .25 } }` | foto diam beberapa saat, lalu mulai bergerak tepat di kata kunci (paling mirip acuan) |
| Klip penuh | `{ urutan: 'ombak-hidup' }` (tanpa x/y = menutup layar) | adegan gerak penuh |
| Klip di benda | `benda: { jenis: 'hp', urutan: 'kode' }` · `benda: { jenis: 'tv', gambar: 'kode' }` (kode klip) | rekaman di layar HP/TV |
| Klip di kartu/panel | `{ urutan: 'kode', x, y, lebar, putar, bayangan: true, hitamPutih: true }` atau `panel: [...]` | arsip film, layar terbelah |
| **Potongan bergerak** | `{ urutan: 'kode-hijau', x, y, tinggi, z: 1.4, bayangan: .4 }` (rakit `:hijau`) | tokoh/benda bergerak di atas foto latar; `jangkar` tepi tetap berlaku |

Kontrol putar per lapisan: `klip: { mulai (detik di dalam video), laju (.5 = gerak lambat), ulang, pantul (maju-mundur, cocok untuk klip pendek di adegan panjang), tahan (berhenti di bingkai terakhir = kembali jadi foto) }`. `hitamPutih` dan blur gerak berlaku juga untuk klip.

## 4. Efek ala After Effects (murah: gradien/bentuk canvas, tanpa filter berat per bingkai)
Satu adegan maks 1–2 efek; satu efek "tanda tangan" boleh berulang 2–3× per video. Lihat `mesin.md` untuk opsi lengkap.
| Efek | Konfig | Pakai untuk |
|---|---|---|
| Cahaya bocor | `efek: [{ jenis: 'cahaya', t, lama: 1.4, dari: 'kiri' }]` | pembuka, kenangan, "dulu…", tema hangat |
| Film terbakar | `{ jenis: 'bakar', t, lama: .8 }` | akhir babak / sebelum lompatan zaman (arsip, perang) |
| Glitch | `{ jenis: 'glitch', t, lama: .45 }` · perpindahan `masuk: 'glitch'` | fakta mengejutkan, teknologi, berita |
| Garis gerak | `{ jenis: 'garis', t, titik: [x, y] }` | angka/teks mendarat keras |
| Partikel | `{ jenis: 'partikel', gaya: 'debu'\|'abu'\|'salju'\|'hujan'\|'gelembung'\|'kunang'\|'konfeti'\|'koin', t, akhir }` | suasana (debu arsip, hujan, bawah air, uang) |
| Bokeh / berkas / kabut | `{ jenis: 'bokeh' }` · `{ jenis: 'berkas', titik, sudut }` · `{ jenis: 'kabut', y }` | kedalaman, cahaya dramatis |
| Sorot | `{ jenis: 'sorot', titik, keTitik, r }` | menunjuk satu tokoh/benda |
| Kilau / kilat | (sudah ada) | puncak, potong di ketukan |
| Kilap | lapisan `kilap: { t }` | kartu foto, HP, cap, koin berkilat sekali |
| Miring 3D | lapisan `rig: { jenis: 'miring', y: [[0, -25], [2.5, 15, 'inOutSine']], x: 6 }` | kartu/foto berputar 3D seperti kamera AE |
| Coretan | lapisan `{ coret: 'lingkar'\|'panah'\|'garis'\|'silang'\|'centang'\|'kotak', x, y, lebar, tinggi, warna, t }` | menandai wajah/angka/benda di foto (ala acuan) |
| HP / notifikasi / balon | `benda: { jenis: 'hp', gambar\|urutan, notif: {...} }` · `benda: { jenis: 'notif', judul, teks, waktu }` · `benda: { jenis: 'balon', teks, gaya: 'bicara'\|'pikir'\|'teriak', ekor }` | berita viral, chat, komentar, kutipan |
