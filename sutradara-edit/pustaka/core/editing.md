# Editing fundamentals: pacing, ritme, potongan

> CORE · dipakai di langkah 6 (storyboard + shot), 10, 12, 15 · terkait: `../story/cerita.md`, `../short-form/short-form.md`, `../motion/transisi.md`, `../cinematic/kamera.md`, `../audio/musik.md`, `../audio/sound-design.md`

Prinsip inti:
1. **Potongan adalah kalimat.** Tiap potongan harus membawa informasi atau emosi baru; kalau tidak membawa apa-apa, potong lebih awal.
2. **Panjang potongan = waktu yang dibutuhkan otak untuk "mendapatkan" bingkai itu**, ditambah sedikit napas. Gambar sederhana 0,6–1,2 dtk, gambar padat/teks 2–3 dtk.
3. **Ritme dibuat dari variasi.** Cepat terasa cepat hanya karena ada yang lambat di dekatnya.
4. **Suara memimpin, gambar menyusul (atau sebaliknya) dengan sengaja.** Di repo ini narasi adalah tulang punggung; potongan menempel ke kata (`'L05.w4'`).
5. **Potongan yang bagus tidak terasa.** Potong di gerak, di kata kunci, di ketukan, atau di arah pandang; potong di tengah "diam" terasa seperti salah.

Patokan waktu (30 fps): 1 bingkai = 33 ms · 0,1 dtk = 3 bingkai · 0,2 dtk = 6 · 0,5 dtk = 15 · 1 dtk = 30.

---

## 1. Pacing (laju informasi)
- **Kapan**: menentukan kecepatan keseluruhan per babak (hook, konteks, ketegangan, payoff).
- **Kenapa**: pacing mengatur seberapa cepat penonton menerima informasi baru; terlalu cepat = bingung, terlalu lambat = geser.
- **Cara**: hitung "unit informasi" per babak (1 fakta, 1 angka, 1 aksi = 1 unit). Short 45 dtk: ±1 unit tiap 2–3 dtk (60–90 bingkai). Hook 1 unit per 0,8–1,5 dtk; konteks melambat (2–3 dtk); klimaks cepat lagi; payoff ditahan 2–3 dtk.
- **Hindari**: pacing rata dari awal sampai akhir; menumpuk 3 angka dalam satu kalimat; memperlambat hanya karena gambar habis.
- **Di mesin Kolase**: panjang adegan = jarak antar-rujukan `mulai`; cek memberi saran bila rata-rata > 3,2 dtk atau adegan > 4,5 dtk. Lihat tabel tempo §18.
- **Di editor lain**: tandai unit informasi dengan marker di timeline, lalu ukur jaraknya.

## 2. Ritme (pola panjang-pendek)
- **Kapan**: setelah pacing per babak ditetapkan; ritme mengatur urutan panjang tiap potongan.
- **Kenapa**: otak menangkap pola. Pola pendek-pendek-panjang memberi rasa "mendarat"; pola yang sama terus terasa mesin.
- **Cara**: pakai frasa ritme seperti musik: `pendek · pendek · panjang` (0,8 · 0,8 · 2,4 dtk = 24 · 24 · 72 bingkai) atau `panjang · pendek · pendek · tahan`. Ganti frasa tiap babak. Dua potongan berurutan jangan sama panjang (beda ≥ 20%).
- **Hindari**: semua adegan 2,5 dtk; semua potongan di ketukan musik (lihat §13).
- **Di mesin Kolase**: atur `mulai` adegan ke kata yang berbeda jaraknya; dalam adegan panjang, sisipkan "potongan dalam" lewat lapisan baru (`t`) atau gerak kamera keyframe.
- **Di editor lain**: lihat timeline dari jauh; blok klip yang seragam panjangnya = tanda ritme datar.

## 3. Timing (kapan tepatnya)
- **Kapan**: setiap kali sesuatu muncul, berubah, atau dipotong.
- **Kenapa**: selisih 3–6 bingkai membedakan "pas" dan "telat". Penonton tidak bisa menyebutnya, tapi merasakannya.
- **Cara**: teks kata kunci muncul 0–2 bingkai sebelum kata diucapkan; benda yang disebut muncul 3–6 bingkai sebelum katanya (mata butuh waktu); hantaman (angka, cap) tepat di suku kata bertekanan; reaksi 6–12 bingkai sesudah pemicu.
- **Hindari**: teks muncul sesudah kata selesai diucapkan (terasa subtitle telat); semua lapisan muncul serentak di detik 0 adegan.
- **Di mesin Kolase**: `t: 'L05.w4-0.1'`; teks `ikut: true` menyamakan tiap kata dengan suara; lapisan beruntun `t` berjarak 0,15–0,3 dtk.
- **Di editor lain**: geser klip per bingkai (alt + panah) sambil memutar 50%.

## 4. Cutting (memilih titik potong)
- **Kapan**: setiap pergantian bidikan.
- **Kenapa**: titik potong yang tepat menyembunyikan potongan dan mendorong cerita.
- **Cara**: urutan prioritas titik potong: (1) di gerak (puncak kecepatan, benda melintas), (2) di kata yang menamai hal baru, (3) di ketukan musik yang kuat, (4) di arah pandang/menunjuk, (5) di akhir kalimat bila perlu jeda. Potong **sebelum** bidikan "habis": begitu penonton paham, keluar 4–10 bingkai kemudian.
- **Hindari**: potong saat kamera melambat ke diam (terasa tersendat); potong di tengah kata; potong keras tanpa alasan zaman/kejutan.
- **Di mesin Kolase**: perpindahan bermomentum (`dorong`, `tarik`, `sentak`, `putar`) memotong tepat di puncak kecepatan; potong keras dibatasi ≤ 3 per video (cek).
- **Di editor lain**: potong di bingkai dengan blur gerak terbesar.

## 5. Jump cut
- **Kapan**: talking head, tokoh menjelaskan, montase waktu berlalu, atau tekanan ("lalu… lalu… lalu…").
- **Kenapa**: membuang jeda sambil mempertahankan energi; sedikit lompatan skala memberi denyut.
- **Cara**: dua bidikan subjek sama, beda skala ≥ 12–20% atau posisi geser ≥ 8% bingkai; panjang tiap potongan 0,6–1,8 dtk (18–54 bingkai). Variasikan skala (dekat-jauh-dekat), jangan hanya makin dekat.
- **Hindari**: lompatan < 8% (terlihat seperti kesalahan); jump cut di adegan emosional yang butuh napas.
- **Di mesin Kolase**: dalam satu adegan, keyframe kamera bertangga: `kamera: [[0, { zoom: 1 }], [1.2, { zoom: 1.02 }, 'linear'], [1.22, { zoom: 1.18, x: 40 }, 'linear'], [2.4, { zoom: 1.2, x: 40 }, 'linear']]` (lompatan 0,02 dtk = 1 bingkai). Lebih aman dari `masuk: 'potong'` yang dihitung potong keras.
- **Di editor lain**: CapCut "Split" + skala 115% di klip kedua.

## 6. Match cut
- **Kapan**: menghubungkan dua tempat/zaman/gagasan yang punya kesamaan bentuk, gerak, warna, atau makna.
- **Kenapa**: transisi paling "pintar"; penonton merasakan hubungan sebab tanpa dijelaskan narasi.
- **Cara**: samakan posisi (dalam 10% bingkai), ukuran (±15%), dan arah gerak objek di bingkai terakhir A dan pertama B. Jenis: bentuk (bulan → koin), gerak (tangan melempar → bola mendarat), warna (merah darah → lampu merah), makna (kunci → pintu bank).
- **Hindari**: match yang dipaksa (bentuk tidak benar-benar mirip); match tanpa hubungan makna.
- **Di mesin Kolase**: `masuk: 'cocok'` dengan `cocok: { dari: 'idLama', ke: 'idBaru' }` (benda tetap, dunia berganti); `bingkai` (adegan jadi foto/layar di adegan berikut); match bentuk murni: letakkan objek B di `x, y` yang sama dengan objek A lalu `masuk: 'kilat'` atau `'fokus'`. Detail: `../motion/transisi.md`.
- **Di editor lain**: AE: samakan anchor point dan posisi, potong di bingkai yang sama gerak.

## 7. J-cut (suara mendahului gambar)
- **Kapan**: memasuki tempat/adegan baru, membangun antisipasi, atau menyambung babak.
- **Kenapa**: telinga sudah "masuk" duluan, jadi potongan gambar terasa diundang, bukan dipaksakan.
- **Cara**: ambience/SFX/kalimat adegan B mulai 6–15 bingkai (0,2–0,5 dtk) sebelum gambar B; untuk pergantian babak boleh 0,5–1,5 dtk.
- **Hindari**: J-cut lebih dari 1,5 dtk di short (penonton bingung sumber suaranya); suara B menabrak kata penting A.
- **Di mesin Kolase**: taruh bunyi adegan B di daftar `sfx` adegan A dengan rujukan ke awal adegan B: `sfx: [{ t: 'L06.w1-0.35', berkas: 'ambience-pasar', vol: .4 }]`. Narasi yang memimpin: adegan B `mulai` di kata kunci (bukan awal kalimat), jadi kalimat B sudah terdengar sebelum gambarnya (lihat §19).
- **Di editor lain**: tarik ujung audio klip B ke kiri melewati titik potong video.

## 8. L-cut (gambar bertahan setelah suaranya)
- **Kapan**: membiarkan emosi/pernyataan meresap, reaksi, atau saat narasi berikutnya masih "tentang" gambar ini.
- **Kenapa**: memberi napas tanpa jeda suara; penonton masih memproses gambar sementara cerita jalan.
- **Cara**: gambar A bertahan 0,3–1,0 dtk (9–30 bingkai) ke dalam kalimat berikutnya; ganti gambar di kata kunci pertama kalimat itu.
- **Hindari**: L-cut ke kalimat yang menyebut hal lain (gambar dan kata bertentangan).
- **Di mesin Kolase**: adegan B `mulai: 'L07.w3'` (bukan `'L07'`), jadi 2 kata pertama L07 masih di atas gambar A.
- **Di editor lain**: perpanjang video klip A melewati awal audio klip B.

## 9. Speed ramp
- **Kapan**: menuju potongan penting, menonjolkan satu momen aksi, atau transisi energik.
- **Kenapa**: perubahan kecepatan menandai "ini penting" dan memberi momentum yang bisa dibawa ke adegan berikut.
- **Cara**: normal → cepat (3–6 bingkai terakhir sebelum potong) → lambat (0,3–0,6 dtk sesudah) → normal. Kurva: ease-in ke titik potong, ease-out sesudahnya. Rasio lambat 30–50%.
- **Hindari**: ramp di setiap potongan; ramp linear (tanpa kurva) yang terasa patah.
- **Di mesin Kolase**: perpindahan momentum sudah berupa ramp kamera (keluar `inCubic`, masuk `outQuart`); untuk satu adegan: keyframe kamera dengan `'inExpo'` lalu `'outExpo'`; klip gerak: `klip: { laju: .5 }`. *Celah mesin*: laju klip tidak bisa berubah di tengah klip (akali: pecah jadi dua lapisan/adegan, laju 1 lalu .4).
- **Di editor lain**: CapCut Speed → Curve "Bullet"/kustom; AE time remap + graph editor.

## 10. Montase
- **Kapan**: memadatkan waktu (bertahun-tahun, proses panjang), daftar contoh, atau puncak energi.
- **Kenapa**: 4–8 gambar cepat memberi kesan banyak/lama tanpa harus menjelaskan satu per satu.
- **Cara**: 3–8 bidikan 0,3–0,7 dtk (9–21 bingkai), satu benang merah (gerak searah, warna, objek sama, atau posisi sama), ditutup bidikan panjang 1,5–2,5 dtk sebagai "kesimpulan".
- **Hindari**: montase gambar acak tanpa benang merah; montase tanpa penutup (terasa terputus).
- **Di mesin Kolase**: satu adegan berisi lapisan gambar beruntun (`t`/`akhir` tiap 0,4 dtk) di posisi yang sama, ditutup lapisan yang bertahan; atau beberapa adegan pendek dengan `kilat`/`sentak` searah (perhatikan batas jenis perpindahan maks 3×).
- **Di editor lain**: beat markers lalu "auto cut" hanya di bagian montase.

## 11. Kontinuitas visual
- **Kapan**: sepanjang video, terutama antar-adegan yang menceritakan hal sama.
- **Kenapa**: kontinuitas membuat potongan cepat tetap terasa satu dunia; patah kontinuitas dipakai sengaja untuk kejutan.
- **Cara**: jaga 4 hal: (1) arah layar (gerak ke kanan tetap ke kanan), (2) posisi mata (lihat `../visual/komposisi.md` §Jejak mata), (3) warna/grade satu tema, (4) benda kunci tetap sama rupanya.
- **Hindari**: benda berubah rupa antar-adegan (gambar Flow beda), arah gerak berbalik tanpa alasan.
- **Di mesin Kolase**: satu `tema`/`grade` per video; `arahMasuk` konsisten per babak; benda kunci pindah dengan `cocok`; gambar Flow benda sama memakai `acuan` (`flow.md`).
- **Di editor lain**: adjustment layer grade tunggal di atas semua klip.

## 12. Progresi adegan
- **Kapan**: menyusun urutan adegan di storyboard.
- **Kenapa**: tiap adegan harus mengubah keadaan; kalau tidak ada yang berubah, cerita diam walaupun gambarnya bergerak.
- **Cara**: tulis untuk tiap adegan "yang berubah: …" (informasi, skala, tempat, emosi, waktu). Naikkan intensitas bertahap: skala makin dekat, kamera makin tegas, warna makin pekat, bunyi makin tebal; reset di awal babak baru.
- **Hindari**: dua adegan berurutan dengan fungsi sama; puncak visual di tengah video lalu menurun.
- **Di mesin Kolase**: kolom storyboard "berubah" (`../../templat/storyboard.md`); naikkan dari `kamera: 'tenang'` → `'dorong'` → `'dorong-kuat'` menuju klimaks.
- **Di editor lain**: beri warna marker per fungsi adegan; warna sama berurutan = curiga.

## 13. Sinkron ketukan (beat sync)
- **Kapan**: montase, puncak, pergantian babak, video tanpa narasi atau narasi tipis.
- **Kenapa**: potongan di ketukan terasa "pas" secara fisik; tapi kalau semua di ketukan, terasa templat.
- **Cara**: ambil peta ketukan dengan `../../scripts/ketukan.py`. Potong di ketukan kuat (birama/downbeat) hanya di 30–60% potongan; sisanya ikut kata. Pola: ketukan → tahan (lewati 2–4 ketukan) → antisipasi (riser/ramp) → hantam (drop) → lepas (adegan lambat). Hantaman visual boleh 1–2 bingkai **sebelum** ketukan (otak menyatukannya).
- **Hindari**: memaksa kata penting bergeser demi ketukan; potong di setiap ketukan 1/8.
- **Di mesin Kolase**: musik berkas `rakit --musik`; tempatkan efek/lapisan/SFX di detik ketukan (detik mutlak − detik mulai adegan). Detail: `../audio/musik.md`. *Celah mesin*: belum ada rujukan ketukan seperti `'B12'` (akali: hitung manual dari `ketukan.json`, atau `mulai` adegan angka mutlak).
- **Di editor lain**: CapCut "Beat" otomatis lalu hapus 40–60% markernya.

## 14. Antisipasi (editing)
- **Kapan**: sebelum hantaman, pengungkapan, atau potongan besar.
- **Kenapa**: otak menikmati sesuatu yang "datang"; antisipasi membuat hantaman terasa 2× lebih kuat.
- **Cara**: 0,3–1,0 dtk sebelum momen: kamera mulai mempercepat, riser/whoosh naik, gambar sedikit menggelap atau zoom pelan, kalimat pendek "Tapi…". Lalu potong tepat di puncaknya.
- **Hindari**: antisipasi tanpa hantaman (penonton kecewa); antisipasi terlalu panjang (> 1,5 dtk di short).
- **Di mesin Kolase**: momentum keluar otomatis berfungsi sebagai antisipasi; tambah `sfx: [{ t: 'L08.w2-0.8', jenis: 'riser', lama: .8 }]`, `efek: [{ jenis: 'gelap', t, akhir, kuat: .3 }]`. Prinsip gerak: `../motion/prinsip-animasi.md`.
- **Di editor lain**: riser dari pustaka SFX berujung tepat di titik potong.

## 15. Timing reaksi
- **Kapan**: setelah fakta mengejutkan, punchline, atau aksi tokoh.
- **Kenapa**: reaksi memberi izin emosional pada penonton ("boleh kaget di sini") dan memberi jeda pemrosesan.
- **Cara**: reaksi muncul 6–12 bingkai (0,2–0,4 dtk) sesudah pemicu selesai; tahan 0,6–1,2 dtk. Reaksi lucu lebih cepat (4–6 bingkai), reaksi sedih lebih lambat (12–20 bingkai).
- **Hindari**: reaksi bersamaan dengan pemicu (tertutup); reaksi terlalu lama (terasa sinetron).
- **Di mesin Kolase**: pose tokoh (mis. `aset/raka-3d/tokoh-canggung.png`) `t: 'L04.akhir+0.25'`, `masuk: 'pop'`, `rig: 'angguk'`; SFX reaksi (`salah`, `ding`, `jantung`).
- **Di editor lain**: potong ke wajah reaksi 8 bingkai setelah kata terakhir.

## 16. Timing jeda
- **Kapan**: sebelum vonis/punchline, setelah angka besar, pergantian emosi.
- **Kenapa**: diam adalah tanda baca terkuat; jeda singkat memberi bobot pada kalimat berikutnya.
- **Cara**: jeda narasi 0,3–0,6 dtk (9–18 bingkai); gambar tetap hidup pelan (kamera `tenang`, napas), musik boleh turun/hilang 0,2–0,5 dtk sebelum hantaman.
- **Hindari**: jeda tanpa alasan; jeda dengan gambar benar-benar diam (cek mesin menolak gambar hampir diam > 1 dtk).
- **Di mesin Kolase**: jeda narasi > 0,6 dtk ditolak cek dan `KONFIG.rapatkan` merapatkan jeda alami. *Celah mesin*: belum ada pengecualian jeda sengaja per baris (akali: jeda ≤ 0,6 dtk + musik jatuh hening + `kamera: 'tenang'` sehingga terasa lebih panjang).
- **Di editor lain**: sisipkan 10–15 bingkai room tone sebelum punchline.

## 17. Ruang napas visual
- **Kapan**: setelah 3–4 adegan padat, sebelum babak baru, di momen emosi.
- **Kenapa**: kepadatan terus-menerus membuat mata lelah dan semua terasa sama penting.
- **Cara**: satu adegan 2,5–3,5 dtk dengan 1 subjek, ruang kosong ≥ 40%, gerak kamera pelan, teks maksimal satu baris atau tanpa teks; bunyi ambience, bukan SFX.
- **Hindari**: adegan napas yang benar-benar kosong informasi lebih dari 3,5 dtk di short.
- **Di mesin Kolase**: `kamera: 'tenang'`, lapisan sedikit, partikel halus (`partikel` `debu`, jumlah kecil) atau `rig: 'napas'` pada tokoh.
- **Di editor lain**: hapus semua overlay di satu klip dan biarkan musik bernapas.

---

## 18. Peta tempo short 45 dtk
| Babak | Detik | Panjang bidikan target | Catatan |
|---|---|---|---|
| Hook | 0–3 | 0,8–1,5 dtk (24–45 bingkai) | bingkai 0 sudah ada subjek + teks + gerak |
| Konteks | 3–9 | 2–2,5 dtk | melambat supaya dunia dipahami |
| Ketegangan | 9–16 | 2 → 1,5 dtk (makin pendek) | antisipasi di ujung |
| Pengembangan | 16–34 | 2–3 dtk, satu napas 3–3,5 dtk | re-hook kecil di ±25 dtk |
| Klimaks/payoff | 34–42 | 0,8–1,2 dtk cepat lalu tahan 2–3 dtk | hantaman + tahan |
| Penutup/loop | 42–45 | 2–3 dtk | bingkai akhir menyambung ke awal (`../short-form/short-form.md` §Loop) |
Rata-rata ±2,4–2,8 dtk (17–19 adegan), sesuai contoh N250 (17 adegan / 46,5 dtk). Durasi lain: kalikan proporsinya, hook tetap ≤ 3 dtk.

## 19. Editing yang dipimpin narasi (logika J/L-cut di repo ini)
Narasi rekaman/TTS adalah garis waktu; adegan menempel ke kata (`mulai: 'L05.w4'`). Aturan:
1. **Gambar mengikuti kata benda.** Ganti adegan di kata yang menamai hal baru ("…krisis **datang**" → potong di "krisis"), bukan di awal kalimat. Hasilnya otomatis J-cut: awal kalimat terdengar di atas gambar lama.
2. **L-cut untuk resapan.** Setelah kalimat berbobot (vonis, angka besar), mulai adegan berikut 2–3 kata ke dalam kalimat baru (`'L09.w3'`).
3. **Bunyi mendahului gambar.** Whoosh/ambience adegan baru mulai 0,15–0,4 dtk sebelum potongan supaya puncaknya jatuh di titik potong (`'L06.w1-0.25'`).
4. **Teks mengikuti suara, benda sedikit mendahului.** Teks `ikut: true`; benda/foto yang disebut muncul 0,1–0,2 dtk sebelum katanya.
5. **Kalimat pendek = potongan pendek.** Kalimat ≤ 4 kata ("Tapi lalu, krisis datang.") layak jadi adegan/kartu sendiri.
6. **Napas pembicara = napas gambar.** Jeda alami narasi adalah tempat potongan paling halus; jangan memotong di tengah frasa kecuali kata kuncinya di sana.

## Cek cepat
- Tidak ada dua potongan berurutan dengan panjang hampir sama (beda < 20%) lebih dari 3 kali berturut-turut.
- Setiap potongan jatuh di gerak, kata kunci, ketukan, atau arah pandang (bisa disebutkan alasannya).
- Hook ≤ 3 dtk dan bidikan pertama ≤ 1,5 dtk.
- Ada minimal satu ruang napas di video > 30 dtk.
- Potongan di ketukan musik ≤ 60% dari total potongan.
- Reaksi muncul 0,2–0,4 dtk setelah pemicu, tidak bersamaan.
- Arah layar dan benda kunci konsisten antar-adegan (kecuali disengaja).
- Setiap adegan punya "yang berubah" yang bisa ditulis satu kata.

## Celah mesin
- **Rujukan ketukan musik** (`mulai: 'B16'`) belum ada: akali dengan angka dari `ketukan.json`. Usulan: `KONFIG.ketukan` dibaca dari `ketukan.py`, rujukan `'B<n>'` dan `'D<n>'` (downbeat).
- **Laju klip berubah dalam satu klip** (speed ramp sejati) belum ada: akali dengan dua lapisan/adegan beda `laju`. Usulan: `klip.laju` menerima keyframe.
- **Jeda sengaja** > 0,6 dtk ditolak cek: usulan `KONFIG.jedaSengaja: ['L07']` untuk mengecualikan satu jeda dramatis.
- **Jump cut** hanya lewat keyframe kamera bertangga: usulan preset `kamera: 'lompat'` (2–3 lompatan skala dalam satu adegan).
