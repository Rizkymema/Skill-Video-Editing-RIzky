# Alur produksi dengan AI

> AI · dipakai di semua langkah (terutama 1–6 dan produksi aset) · terkait: `../story/cerita.md`, `../visual/metafora.md`, `../style/gaya-visual.md`, `../motion/kolase-editorial.md`, `../audio/sound-design.md`, `../audio/musik.md`, `../polish/qc.md` · implementasi: `skill-edit-rizky/SKILL.md`, `references/flow.md`, `klip.md`, `data-media.md`, `riset.md`

Prinsip inti:
1. **AI mempercepat produksi, bukan menggantikan cerita.** Premis, sudut pandang, urutan emosi, dan apa yang tidak ditampilkan adalah keputusan editor. AI menghasilkan bahan; editor memilih dan menyusun.
2. **Keputusan dulu, generate kemudian.** Brief + storyboard selesai sebelum gambar pertama dibuat. Generate tanpa storyboard = tumpukan aset bagus yang tidak bercerita.
3. **Yang harus benar tidak diserahkan ke AI generatif.** Angka, tanggal, nama, teks di layar, wajah orang nyata, logo: ditulis mesin atau diambil dari sumber asli.
4. **Konsistensi adalah sistem, bukan keberuntungan.** Lembar karakter, gambar acuan, akhiran gaya tetap, latar hijau, dan grade mesin yang menyatukan.
5. **Kredit = uang.** Yang gratis dulu (gambar Flow, Edge TTS, musik sintesis), yang berbayar hanya sesudah disetujui di dialog persetujuan.

## 1. Pembagian kerja: AI vs editor
| Bagian | AI mengerjakan | Editor (Rizky + sutradara) memutuskan |
|---|---|---|
| Ide | 10–20 variasi sudut, cek kejenuhan, fakta pendukung | premis yang dipilih, kenapa penonton peduli, emosi target |
| Riset | mencari & merangkum sumber | fakta mana yang dipakai, mana yang meragukan, angka "±" |
| Naskah | draf, variasi hook, pemadatan kalimat | hook final, ritme kalimat, kalimat yang dibuang, vonis |
| Storyboard | usulan visual per beat, daftar aset | metafora yang dipakai, urutan, apa yang **tidak** ditampilkan |
| Gambar/klip | aset pelat, potongan, klip gerak | komposisi, apakah aset melayani beat, buang yang aneh |
| Suara | narasi, ejaan, waktu kata | narator, tempo, letak jeda, kata yang ditekan |
| Bunyi & musik | pencarian katalog, pemotongan | palet bunyi, titik hantam, hening, musik per babak |
| Edit | perakitan konfig, cek otomatis | timing akhir, kapan diam, rasa |
| QC | cek teknis (durasi, LUFS, zona aman, teks menimpa) | apakah ceritanya bekerja dan terasa manusia |

## 2. Pra-produksi
| Langkah | Alat di PC ini | Hasil | Catatan |
|---|---|---|---|
| Ide | Claude (+ `ide-anti-tiru` untuk niche jenuh) | 4 ide + hook + angka kunci | cek fakta inti tiap ide sebelum ditawarkan |
| Riset | WebSearch/WebFetch, agen `penulis-naskah` | `# sumber:` di `naskah.txt`, `KONFIG.sumber` | ≥ 2 sumber per angka kunci (`riset.md`) |
| Naskah | Claude / `penulis-naskah` | `Lxx \| kalimat` per baris | satu baris = satu kalimat, angka ditulis angka |
| Storyboard + shot list | Claude, `../../templat/storyboard.md` | tabel: waktu · visual · metafora · kamera · teks · transisi · SFX · musik | dirancang dari foto diam dulu; klip hanya bumbu |
| Referensi visual | `bedah_acuan.py` (video/gambar acuan pengguna), lembar bingkai, `../style/bahasa-earnedits.md` | `_kerja/acuan/gaya-acuan.md` | ambil prinsip, jangan salin isi |
| Brief sutradara | `../../templat/brief.md` | satu halaman keputusan | diisi sebelum aset pertama |

## 3. Produksi aset
### Gambar (0 kredit)
- **Alat**: Google Flow lewat flow-mcp: `flow_agent_images` (batch, 0 kredit, tidak perlu ditanya) → `flow_wait` → unduh 2K `flow_assets` + `flow_download quality: 'upscaled'` → `flow_kolase.py ambil` (latar hijau dibuang otomatis, lembar kontak).
- **Struktur prompt gambar diam**: `[subjek + pose/aksi diam] + [tempat + zaman] + [sudut/komposisi: wide/close, dari belakang, dari bawah, ruang kosong sepertiga atas] + [cahaya: arah + suhu] + [akhiran gaya tetap] + [larangan: no text, no logos, no flags, no watermark]`. Potongan: `isolated on a flat pure green background (#00FF00), entire object fully visible with generous margin` **atau** `entering from the bottom edge of the frame` (pilih salah satu dengan sengaja, `flow.md` §2).
- **Akhiran gaya tetap**: satu paragraf pendek yang sama di semua prompt satu video (lensa, cahaya, palet, tekstur), disimpan di kepala `aset.json`. Contoh arsip: `archival documentary photograph, 1990s, soft overcast light, muted warm palette, subtle film grain`.

### Klip gerak (berbayar, tanya dulu)
- **Alat**: `flow_kolase.py klip` → `flow_klip.json` + perkiraan kredit → disetujui di dialog persetujuan → `flow_generate` → `flow_kolase.py ambil-klip` → periksa `klip/_cek-<kode>.jpg` (8 bingkai/dtk).
- **Model**: Omni 1.1 Flash ±7 kredit per 4 dtk (bawaan); Veo 3.1 Fast ±20 kredit hanya bila wajah/tangan harus sangat realistis.
- **Struktur prompt klip**: `[mulai dari gambar ini] + SATU aksi berawal-berakhir + SATU gerak kamera (static locked-off / slow push-in) + lama 4 dtk + no new objects appear, no text, background never changes`. Jangan: lempar/jatuh benda, tangan memindahkan barang, putar benda terbalik, dua aksi.
- **Pakai**: 1–4 momen aksi, ≤ 30% durasi; sisanya foto berlapis (`klip.md`).

### Suara
- **Pemandu gratis**: Edge TTS (`jalankan.py suara … --edge --laju=+12%`) untuk pratinjau dan timing.
- **Final**: ElevenLabs (`jalankan.py suara`, Brian `eleven_v3`, ejaan Indonesia otomatis) — **kredit, hanya sesudah persetujuan**; perkiraan `--perkiraan`. Agen `pengisi-suara` menangani narasi/dialog, rekaman pengguna, dan waktu kata.
- **Arah suara**: tulis emosi per baris di naskah (`# nada: datar → bisik di L07`), bukan membiarkan TTS menebak.

### Bunyi dan musik
- Epidemic Sound lewat konektor (`SearchRecordings`, `SearchSoundEffects`, unduh sesudah disetujui), pustaka lokal `D:\Sound\`, musik sintesis mesin; agen `penata-sfx` dan `penata-musik` (`../audio/sound-design.md`, `../audio/musik.md`). Analisis ketukan: `scripts/ketukan.py`.

### Media nyata (bukti)
- `ambil_media.py cari|ambil|daftar` (Wikipedia/Commons/NASA/YouTube CC + lisensi + kredit, `data-media.md`). Wajah tokoh nyata hanya dari media asli. YouTube/IG yang menolak tanpa login: minta pengguna mengunduh MP4, jangan memakai cookie pengguna.

## 4. Pasca-produksi
| Bagian | Alat | Keputusan editor |
|---|---|---|
| Edit / perakitan | mesin Kolase (`konfig.js` → `rakit`), agen `penyusun-video` | timing per bingkai, kapan diam, transisi bermotivasi |
| Compositing | `flow_kolase.py ambil` / `potong_latar.py` (kunci hijau), lapisan `z`, `bayangan`, `jangkar`, grade | potongan menyatu dengan pelat (cahaya, bayangan, tepi) |
| Motion graphics | mesin (teks kinetik, benda, efek, rig) | bahasa gerak satu keluarga (`../motion/prinsip-animasi.md`) |
| Sound design | `sfxPeta`, `--sfx`, `penata-sfx` | hanya bunyi yang berfungsi |
| Color grading | `KONFIG.tema` / `grade` (menyatukan aset AI + foto asli) | satu grade per video, dua aksen |
| Caption | teks kinetik mesin (bukan subtitle bawaan) | kata yang ditekan, posisi (`../type/tipografi-kinetik.md`) |
| Polish + QC | `jalankan.py cek`, `kontak`, agen `pemeriksa-video`, `../polish/qc.md` | apakah video terasa manusia dan ceritanya sampai |

## 5. Konsistensi antar-gambar
- **Lembar karakter + gambar acuan**: tokoh seri punya satu gambar acuan resmi (mis. `aset/raka-3d/_acuan-raka.jpeg`) yang selalu dilampirkan sebagai `reference_images`, dan satu kalimat deskripsi tetap (rambut, kulit, baju, gaya render) yang disalin persis ke setiap prompt (`aset/README.md`). Pose baru dibuat satu per satu dari acuan itu.
- **Benda kunci**: deskripsikan lengkap di setiap prompt (warna, bentuk, tanda), atau lampirkan gambar benda sebagai acuan; Flow tidak mengingat antar-gambar.
- **Model dan pengaturan sama** untuk satu set; jangan mencampur model berbeda dalam satu video kecuali sengaja.
- **Latar hijau untuk semua potongan**, lalu grade mesin + bayangan mesin menyamakan cahaya. Lebih konsisten daripada meminta Flow membuat seluruh komposisi.
- **Ulang hanya yang melenceng** (`flow_kolase.py rencana --hanya kode1,kode2`), jangan generate ulang seluruh set.
- **Simpan aset bagus** ke `aset/<seri>/` (gambar saja) supaya video berikutnya tidak membuat ulang.

## 6. QC artefak AI (sebelum aset dipakai)
| Artefak | Cek | Tindakan |
|---|---|---|
| Tangan | jumlah jari, jari menyatu, pegangan benda tidak masuk akal | buat ulang, atau potong dari tepi/sembunyikan di balik benda |
| Wajah | asimetri, gigi, mata tidak sejajar, wajah mirip orang terkenal | buat ulang; tampilkan dari belakang/jauh |
| Teks tak sengaja | huruf acak di papan, kaos, koran | buat ulang dengan `no text`; teks ditulis mesin |
| Bendera, lambang, gedung khas | bendera negara salah, lambang palsu, gedung mirip negara lain | `no flags, no emblems`; periksa dengan zoom |
| Fisika | arah bayangan bertabrakan, benda melayang, pantulan salah | pilih yang konsisten dengan pelat; tambah `bayangan` mesin |
| Klip | wajah/tangan berubah bentuk, kamera melompat di tengah klip | pangkas ke bagian mulus (`klip.mulai`, `tahan`) atau buang |
| Gaya melenceng | satu aset terlalu bersih/jenuh dibanding lainnya | ulang dengan akhiran gaya tetap; grade mesin |
| Kemulusan "AI" | kulit lilin, cahaya terlalu sempurna, simetri | tambahkan grain/tekstur, potong lebih dekat, kurangi glow (`../polish/qc.md` §6) |

## 7. Etika dan label
- Gambar realistis buatan AI tentang kejadian nyata: tandai konten sintetis di YouTube (`synthetic: true`, `kemasan.md`); jangan menulis "foto asli" untuk ilustrasi.
- Tidak membuat wajah tokoh nyata, logo merek, atau media nyata dengan AI.
- Tidak menyalin karya, nama, kalimat, musik, atau file proyek kreator acuan; yang diambil hanya prinsip.

## 8. Kendali biaya
| Sumber | Biaya | Aturan |
|---|---|---|
| Gambar Flow (`flow_agent_images`, unduh 2K) | 0 kredit | bebas, tanpa bertanya |
| Klip Flow | ±7 kredit/4 dtk (Omni), ±20 (Veo Fast) | perkiraan dari `flow_kolase.py klip`, disetujui di dialog Tahap 2 |
| ElevenLabs narasi | kredit per huruf | perkiraan `--perkiraan`; pemandu Edge sampai disetujui |
| Epidemic Sound | langganan | unduh sesudah pilihan disetujui |
| Waktu render | menit | `cek` dan `kontak` dulu; ekspor final sekali |

## Teknik modern
- **Transisi morph bingkai awal + akhir** (Frames to Video: klip dibuat dari gambar A menuju gambar B). Manfaat: transisi mulus "dunia berubah" yang tidak bisa dipalsukan kamera (wajah jadi foto arsip, kota siang jadi malam). Kapan: satu transisi tanda tangan per video. Alur: dua pelat sudah jadi → klip 2–4 dtk dengan bingkai awal A dan akhir B (bila model di Flow mendukung bingkai akhir; berbayar) → `rakit --klip` → adegan `{ urutan: 'morph' }` diapit potongan biasa (`../motion/transisi.md`).
- **Parallax dari peta kedalaman (depth map)**: perkiraan kedalaman satu foto memisahkan depan/tengah/belakang. Manfaat: foto tunggal (termasuk foto arsip asli) jadi 2,5D. Alur: buat peta kedalaman di luar mesin, potong 2–3 lapisan PNG menurut ambang kedalaman (isi celah belakang dengan Flow edit/inpaint), lalu tumpuk dengan `z` berbeda (`../cinematic/kamera.md`). *Celah mesin*: tidak ada displacement berbasis peta kedalaman.
- **Relight AI**: menyamakan arah dan warna cahaya potongan dengan pelat ("same subject, relit with warm window light from the left"). Manfaat: compositing tidak terlihat tempelan. Kapan: potongan tokoh di atas pelat yang cahayanya kuat. Alur: edit gambar di Flow dengan gambar potongan sebagai acuan, lalu ambil lagi lewat `flow_kolase.py ambil`.
- **Desain suara (voice design)**: suara narator baru dari deskripsi (umur, warna, logat). Manfaat: identitas suara seri yang konsisten dan tidak dipakai channel lain. Alur: konektor ElevenLabs (desain suara dari deskripsi + kalimat contoh dari pengguna) → simpan → pakai ID-nya di `jalankan.py suara --suara <id>`; berbayar, tanya dulu.

## Cek cepat
- [ ] Brief + storyboard selesai sebelum aset pertama dibuat.
- [ ] Angka, nama, tanggal, dan teks di layar ditulis mesin dari sumber, bukan oleh AI generatif.
- [ ] Semua aset satu video memakai akhiran gaya tetap dan model yang sama; tokoh seri memakai gambar acuan.
- [ ] Tiap aset lolos QC artefak (tangan, wajah, teks, bendera, klip melompat).
- [ ] Klip ≤ 30% durasi dan masing-masing membawa aksi yang tidak bisa dipalsukan kamera.
- [ ] Kredit berbayar (klip, ElevenLabs, unduhan) hanya sesudah persetujuan.
- [ ] Label sintetis diisi untuk gambar realistis tentang kejadian nyata.

## Celah mesin
- **Displacement dari peta kedalaman** tidak ada. Akali: pecah foto jadi 2–3 PNG berlapis lalu `z` berbeda. Usulan: lapisan `kedalaman: 'kode-depth'` yang menggeser piksel menurut peta saat kamera bergerak.
- **Morph antar-gambar tanpa klip** tidak ada. Akali: `cocok` dengan dua gambar yang saling melebur, atau klip Flow bingkai awal-akhir (berbayar).
