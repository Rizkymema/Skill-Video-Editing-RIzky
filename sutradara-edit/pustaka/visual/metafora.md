# Metafora visual: konsep abstrak jadi gambar konkret

> VISUAL · dipakai di langkah 5 (dan setiap baris naskah yang abstrak) · terkait: `../story/cerita.md` §7, §12, `komposisi.md`, `../motion/kolase-editorial.md`, `../motion/ui-digital.md`, `../motion/transisi.md`

Prinsip inti:
1. **Metafora harus bergerak.** Benda diam hanya ilustrasi; perubahan pada benda itulah yang membawa makna (bohlam menyala = ide tidak cukup; bohlam berkedip lalu putus di kalimat "idenya mati" baru bercerita).
2. **Terbaca < 1 dtk tanpa narasi.** Kalau butuh penjelasan, metaforanya terlalu jauh.
3. **Dekat dengan penonton.** Benda sehari-hari Indonesia (kalender sobek, struk minimarket, angkot ngetem, kuota habis, warung) lebih cepat dipahami daripada simbol impor.
4. **Satu metafora per kalimat, satu metafora utama per video.** Metafora utama boleh berevolusi (§5).
5. **Metafora tidak menggantikan data.** Topik berdata tetap menampilkan angka/foto asli; metafora menjelaskan mekanismenya.

---

## 1. Metode 5 langkah
1. **Kata abstrak** → tulis satu kata intinya ("inflasi", bukan "harga-harga yang makin tinggi bikin susah").
2. **Sifat fisik** → apa yang terjadi kalau konsep itu benda: bertambah, berkurang, menyempit, menumpuk, retak, bercabang, berulang, menyebar, tertarik, memudar, mengeras, meledak.
3. **Benda/aksi** → cari 3–4 benda yang punya sifat itu secara alami. Pilih yang paling dekat dengan penonton dan paling mudah digambar di gaya video.
4. **Gerak yang membuktikan** → tentukan perubahan dari keadaan A ke B dalam 1–3 dtk (tas belanja menyusut saat struk memanjang). Inilah inti metaforanya.
5. **Bunyi** → bunyi benda itu sendiri (kertas struk, rantai, tetes) lebih kuat daripada musik dramatis.

Uji: tunjukkan bingkai tengah gerakannya ke orang lain tanpa suara; kalau mereka bisa menebak konsepnya dalam satu kata, metaforanya lolos.

- **Kapan**: setiap baris naskah yang tidak punya benda fisik untuk difoto.
- **Kenapa**: otak memahami konsep abstrak lewat tubuh dan benda (naik = baik, berat = beban); metafora memberi pegangan itu.
- **Hindari**: metafora yang bertentangan dengan nada (lucu di topik tragedi); metafora yang lebih menarik daripada isinya sehingga mengalihkan.
- **Di mesin Kolase**: sumber benda: potongan Flow berlatar hijau (`flow.md`), ikon 3D siap pakai `aset/ikon-3d/` (`robot`, `bohlam`, `topeng`, `kaca`, `target`, `stopwatch`, `gunting`), benda kode (`kartu`, `grafik`, `papan`, `label`, `cap`, `hp`, `notif`, `balon`, `kustom`), foto asli (`ambil_media.py`). Gerak: `gerak` keyframe, `rig` (`goyang`, `kibar`, `miring`), `cocok`, `angka`, `efek` (`partikel`, `kabut`, `sorot`).

## 2. Contoh pengguna, diperluas
### "Waktu terus berjalan"
| Visual | Gerak yang membuktikan | Di mesin Kolase |
|---|---|---|
| jam bergerak cepat | jarum berputar makin cepat, bayangan ruangan ikut bergeser | jam digambar `benda: { jenis: 'kustom' }` (`lukis` memutar jarum dari `t`, makin cepat) + `efek: cahaya` menyapu sebagai bayangan berpindah |
| progress bar | bilah merayap lalu melompat di kata "tiba-tiba" | `benda: { jenis: 'grafik', bentuk: 'progres' }` atau `kustom` |
| kalender berganti | lembar disobek beruntun makin rapat | lapisan `kartu`/`kustom` beruntun `t` makin rapat + `keluar: { gaya: 'lempar' }`, SFX `kertas` |
| tokoh berjalan, latar berubah | tokoh tetap di tengah, latar berganti kota–desa–malam | tokoh `rig: 'napas'` di `z: 1.4`, pelat latar beruntun di `z: .3` dengan `masuk: 'geser'` |
| timeline makin penuh | titik-titik peristiwa bertambah di garis | `kustom` garis + titik muncul per kata (`K.ref`) |

### "Overthinking"
| Visual | Gerak | Di mesin Kolase |
|---|---|---|
| banyak tab browser terbuka | tab bertambah sampai judulnya tak terbaca, layar penuh | `benda: kustom` jendela browser, jumlah tab = fungsi waktu |
| kepala dipenuhi sticky notes | catatan kuning menempel satu per satu sampai wajah tertutup | `aset/raka-3d/tokoh-pusing.png` + lapisan catatan `masuk: 'pop'` beruntun, `putar` acak ±8° |
| animasi loop | gerak yang sama terulang 3× dengan teks yang sama | adegan pendek diulang dengan `bingkai` ke dirinya sendiri (adegan jadi foto di adegan berikut) |
| lorong tak berujung | kamera maju, pintu di ujung selalu sama | pelat lorong Flow + `masuk: 'dorong'` dengan `titikMasuk` di pintu, berulang 2× |
| benang kusut | benang makin rumit tiap kalimat | `kustom` kurva acak bertambah titik |

### "Growth"
| Visual | Gerak | Di mesin Kolase |
|---|---|---|
| progress bar | naik bertingkat, ada jeda (pertumbuhan nyata tidak mulus) | `grafik` `bentuk: 'progres'` dengan `lama` panjang |
| tanaman tumbuh | tunas → batang → daun, `goyang` pelan | 3 potongan Flow beruntun dengan `cocok`, `rig: 'goyang'` |
| tangga | tokoh naik satu anak tangga per poin | `gerak` keyframe `y` bertangga + `rig: 'napas'` |
| timeline berkembang | cabang baru muncul dari garis utama | `kustom` |
| cincin pohon | lingkaran bertambah dari dalam | `kustom` lingkaran per detik |

### "Distraction"
| Visual | Gerak | Di mesin Kolase |
|---|---|---|
| notifikasi bermunculan | menumpuk, menutupi isi layar utama | `benda: { jenis: 'notif' }` beruntun `masuk: { gaya: 'geser', dari: 'atas' }`, SFX `notif` bervariasi |
| layar terpecah | satu layar pecah jadi 4 lalu 9 panel | `panel` berlapis, tiap panel isinya beda |
| tokoh tertarik banyak objek | tokoh ditarik tali ke HP, TV, makanan | potongan tokoh + `coret: 'garis'` sebagai tali + `rig: { jenis: 'goyang', sudut: [[0, -6], [1, 7], [2, -8]] }` (miring bergantian ke arah tarikan) |
| kursor diseret ke mana-mana | kursor menuju tombol "Kerjakan" tapi belok ke iklan | `kustom` kursor (lihat `../motion/ui-digital.md`) |

## 3. Bank metafora (50 konsep)
Kolom "Hindari" = versi klise atau yang menyesatkan.

| Konsep | Visual konkret | Gerak yang membuktikan | Bunyi | Hindari |
|---|---|---|---|---|
| Prokrastinasi | tugas didorong ke kotak "besok" · tumpukan berkas makin tinggi · bola salju · pesawat kertas | tugas didorong keluar bingkai lalu kembali lebih besar | geser kertas, dum | tokoh tidur di kasur saja |
| Inflasi | tas belanja menyusut saat struk memanjang · label harga ditempel berlapis · uang sama, barang mengecil | label baru menutupi label lama, belanjaan mengempis | cetak struk, "tek" label | panah merah naik |
| Utang | bola besi di kaki · lubang makin dalam · tagihan menumpuk sendiri · bayangan mengikuti | bola terseret, tumpukan tumbuh tanpa disentuh | rantai, kertas | dompet kosong menganga |
| Kecanduan HP | tali dari layar ke tangan · jempol menggulir tanpa ujung · kail pancing · mata memantulkan layar | guliran loop, tokoh tertarik mendekat | swipe berulang | tokoh zombi |
| Burnout | lilin terbakar dua ujung · baterai merah · korek habis · mesin berasap | nyala mengecil, warna memudar ke abu | desis padam | tokoh berkeringat saja |
| Peluang | pintu terbuka sebentar · kereta berangkat · celah cahaya menyempit | celah menyempit di kata "terbatas" | pintu, peluit | kunci emas berkilau |
| Risiko | lantai es retak · menara jenga · tali tegang · dadu dilempar | retakan menjalar mengikuti langkah | es retak, kayu berderit | tanda seru kuning |
| Kepercayaan | jembatan papan · kaca retak sekali · gembok · tangan menangkap | satu papan retak, yang lain ikut goyah | kaca retak | jabat tangan generik |
| Informasi berlebih | air bah dari layar · kertas menimbun tokoh · corong meluap | volume melewati batas wadah | riuh kertas, air | otak meledak |
| Algoritma | tangan tak terlihat menyusun kartu feed · rel bercabang otomatis · mesin capit | kartu disusun ulang mengikuti arah tatapan tokoh | klik mesin | kode hijau "matrix" |
| Privasi | rumah berdinding kaca · jejak kaki digital · kamera di tiap benda · amplop terbuka | dinding berubah jadi kaca | rana kamera | gembok + perisai biru |
| Monopoli | papan permainan satu warna · ikan besar makan kecil · satu pipa ke semua rumah · gerbang tol tunggal | warna satu pemain menyebar menguasai peta | stempel beruntun | topi tinggi + cerutu |
| Krisis | tanah retak · air naik di ruangan · grafik jatuh menembus lantai | grafik jatuh keluar bingkai, kamera ikut jatuh | boom rendah | api di mana-mana |
| Kebiasaan | jalan setapak di rumput makin jelas · tali tipis jadi tambang · air mengikis batu | jejak makin dalam tiap ulangan | langkah berulang | kalender dicentang |
| Disiplin | metronom · bata disusun per hari · tetes air melubangi batu · kereta di rel | satu bata per detak, tanpa jeda | metronom | otot binaraga |
| Motivasi hilang | balon mengempis · korek padam · musik melambat · baterai turun | melambat + desaturasi | nada turun | awan hujan di atas kepala |
| Perbandingan sosial | jendela tetangga terang · feed orang lain berbingkai emas · timbangan dengan bayangan orang lain | tokoh mengecil saat feed orang lain membesar | swipe, sunyi | dua tokoh beda ukuran tanpa konteks |
| FOMO | pesta di balik kaca · pintu lift menutup · kerumunan menjauh | celah menutup, tokoh tertinggal | riuh teredam | jam alarm |
| Efek domino | domino · kartu ditarik menara runtuh · kerikil memicu longsor | reaksi berantai yang makin cepat | klik domino makin rapat | — (domino boleh bila iramanya bercerita) |
| Bunga majemuk | koin melahirkan koin · bola salju · sel membelah · pohon bercabang | tambahan datang dari dalam; lambat lalu meledak | koin makin rapat | grafik garis lurus naik |
| Rantai pasok | estafet tangan · ban berjalan · sungai berbendung · jaringan rel | satu mata rantai macet, semua tertahan | mesin berhenti | peta dunia + panah generik |
| Korupsi | pipa bocor di jalan · kue dipotong sebelum sampai · rayap di tiang | isi berkurang di tiap titik | tetes | tikus berdasi |
| Propaganda | megafon · cetakan (semua kepala sama) · kacamata berwarna · cermin cembung | kepala-kepala berubah warna mengikuti sumber | gema megafon | mata besar mengawasi |
| Memori | laci arsip · foto memudar · kaset · pita film | foto berubah sepia lalu luntur | proyektor, kaset | otak bercahaya |
| Lupa | tulisan pasir tersapu ombak · foto kehilangan wajah · bilah progres mundur | hilang bertahap dari tepi | ombak, angin | tanda tanya di kepala |
| Belajar | peta berkabut terbuka sedikit demi sedikit · neuron tersambung · gembok bertingkat | sambungan menyala satu per satu | klik terkunci | toga + buku |
| Keputusan | persimpangan jalan · koin di udara · dua pintu · tombol dua warna | kamera berhenti, lalu sentak ke satu arah | hening lalu klik | tokoh garuk kepala |
| Ketidakpastian | kabut · peta dengan bagian kosong · dadu berputar · lampu kuning berkedip | kabut menutup jalan di depan | angin, dengung | tanda tanya raksasa |
| Tekanan | dinding mendekat · teko mendidih · ban dipompa · batu bara jadi berlian | dinding bergerak masuk + getar | desis naik | tokoh berkeringat |
| Kebebasan | sangkar terbuka · layang-layang putus · rantai jatuh · jendela dibuka | tali putus lalu melayang | kepak, tali lepas | burung terbang generik |
| Isolasi | satu kursi di ruang kosong · pulau kecil · kaca tebal antar orang · mode pesawat | kamera mundur memperbesar ruang kosong | room tone kosong | tokoh duduk memeluk lutut |
| Koneksi | benang merah antar pin · colokan · jembatan · titik bercahaya | garis tersambung lalu menyala | klik colokan | tangan berjabat di atas globe |
| Skala besar | tokoh kecil di samping benda raksasa · dibandingkan lapangan bola · zoom keluar ke peta | `tarik` ekstrem dari detail | sub/boom | angka tanpa pembanding |
| Skala kecil | butir dalam genggaman · dibandingkan koin · mikroskop | `dorong` menembus ke detail | tik halus | kaca pembesar saja |
| Kecepatan | dunia buram, tokoh membeku · garis gerak · halaman membalik sendiri | blur + garis kecepatan | whoosh | roket kartun |
| Akumulasi | tetes ke gelas · tumpukan koin · stiker menumpuk · bata | menumpuk berirama lalu meluap | tetes berulang | grafik batang biasa |
| Keseimbangan | timbangan · batu bertumpuk · penyeimbang di tali | goyah lalu stabil | kayu berderit | simbol yin-yang |
| Konflik | tarik tambang · dua arus warna bertabrakan · bidak catur | garis tengah bergeser bolak-balik | tali tegang, hantaman | dua kepala beradu |
| Pertumbuhan eksponensial | kertas dilipat · beras di papan catur · sel membelah · kurva J | lambat-lambat-meledak | ketukan makin rapat | panah naik |
| Penurunan | tangga turun · bunga layu · tanah longsor · baterai | turun bertahap dengan jeda | nada turun | panah merah turun |
| "Sudah terlambat" | kereta sudah pergi · pintu menutup tepat di depan · es krim meleleh · pasir terakhir jatuh | tokoh tiba sedetik setelah | pintu menutup, hening | jam berdering |
| "Terlalu cepat" | buah dipetik masih hijau · produk di panggung tanpa penonton · halte kosong | sorot menyala ke panggung kosong | gema ruang kosong | roket meledak |
| Ilusi | topeng · panggung vs belakang panggung · cermin | kamera berputar ke balik layar | tirai | asap sihir |
| Nilai tersembunyi | gunung es · sinar-x · peti terkunci | air surut mengungkap bagian bawah | dengung bawah air | harta karun berkilau |
| Kerja tak terlihat | angsa tenang, kaki mengayuh di bawah air · belakang panggung | tilt turun menembus permukaan | air, kayuhan | tokoh lembur depan laptop |
| Biaya tersembunyi | struk memanjang · kabel kusut di balik meja · tarif kecil di bawah label | kamera turun mengungkap yang di bawah | cetak struk | tanda bintang (*) besar |
| Antre/menunggu | angkot ngetem · nomor antrean · loading bar macet | angka antrean tidak bergerak, jam bergerak | klakson jauh, tik | jam pasir |
| Sumber daya habis | kuota habis · bensin di garis merah · gelas tinggal ampas | indikator turun tepat di kata kunci | bip peringatan | tanda bahaya generik |
| Ketimpangan | satu piring penuh, sembilan kosong · tangga bawah ramai, atas lengang | proporsi dibuka bertahap (`tarik`) | hening + satu dentang | koin emas vs koin perunggu |
| Kemudahan palsu | tombol "1 klik" yang menarik tali panjang · pintu otomatis menuju labirin | kamera mundur mengungkap rumitnya | klik lalu mesin berderak | hadiah berpita |

## 4. Memilih dari bank
1. Pilih baris yang cocok dengan **gaya video** (`../style/gaya-visual.md`): gaya arsip/editorial → benda nyata dan kertas; gaya dark tech → UI dan cahaya; gaya kolase → potongan foto dan kertas sobek.
2. Pilih visual yang **bisa dibuat dengan aset yang ada** (ikon 3D, Flow, benda kode). Metafora yang butuh 6 aset baru untuk satu kalimat terlalu mahal.
3. Tulis di storyboard kolom "metafora": konsep → benda → perubahan A→B.

## 5. Metafora berlapis (satu benda berevolusi sepanjang video)
- **Kapan**: video 30–60 dtk dengan satu gagasan besar.
- **Kenapa**: satu benda yang berubah keadaan di tiap babak menjadi tulang visual; penonton mengikuti benda itu tanpa sadar, dan payoff terasa utuh.
- **Cara**: tentukan benda di hook; tulis 4–5 keadaannya (sehat → retak → diperbaiki → lebih kuat); tiap babak mengubah keadaannya; payoff = keadaan terakhir, dekat dengan bingkai awal untuk loop. Contoh: N250 — pesawat di landasan → foto di koran → diselimuti terpal → foto di museum. Bunga majemuk — satu koin → tumpukan → bola salju → longsor koin.
- **Hindari**: mengganti benda utama di tengah; keadaan yang tidak berubah antar-babak.
- **Di mesin Kolase**: benda pindah antar-adegan dengan `masuk: 'cocok'` (`cocok: { dari, ke }`, gambar beda saling melebur), `bingkai` (adegan jadi foto di adegan berikut), gambar tiap keadaan dibuat dengan `acuan` yang sama di Flow supaya rupanya konsisten.

## 6. Saringan klise
Metafora klise boleh dipakai **hanya bila geraknya menambah makna baru**. Tanyakan:
- Apakah benda ini muncul di 100 video lain dengan makna yang sama? (bohlam = ide, jam pasir = waktu, panah naik = sukses, otak bercahaya = pintar, globe + jabat tangan = kerja sama)
- Kalau ya: apakah **gerak**nya baru? Bohlam yang berkedip lalu putus di kata "idenya ditolak" = boleh; bohlam menyala biasa = ganti. Jam pasir yang dibalik terus oleh tangan yang lelah = boleh; jam pasir diam = ganti.
- Apakah ada versi lokal yang lebih segar? (jam pasir → angkot ngetem; panah naik → antrean sembako memendek)
- Apakah metafora cocok dengan nada? Topik tragedi tidak memakai metafora lucu.
- Apakah metafora menyesatkan fakta? (inflasi bukan "uang dicuri"; jangan menyiratkan pelaku bila sumber tidak menyebut).

## Cek cepat
- Setiap kalimat abstrak di naskah punya benda + perubahan A→B di storyboard.
- Bingkai tengah gerak metafora bisa ditebak konsepnya tanpa suara.
- Tidak ada metafora klise yang dipakai tanpa gerak bermakna baru.
- Maksimal satu metafora per kalimat; satu metafora utama per video.
- Metafora utama (bila ada) berubah keadaan di tiap babak dan muncul di payoff.
- Metafora tidak menggantikan angka/foto asli pada topik berdata.

## Celah mesin
- **Benda metafora berulang** (kalender sobek, tab browser, sticky note, progress bar bertingkat, domino) saat ini harus digambar ulang sebagai `kustom` per video. Usulan: pustaka `benda` siap pakai di mesin (`kalender`, `tab`, `catatan`, `domino`, `struk`) dengan parameter jumlah + waktu.
- **Loop rekursif** (lorong tak berujung / bingkai di dalam bingkai berkali-kali) hanya bisa dengan `bingkai` berulang antar-adegan; belum ada efek Droste dalam satu adegan.

## Teknik modern
- **Metafora harfiah surealis (literal visual)** · manfaat: hook visual ganjil yang langsung menghentikan jempol · kapan: hook dan payoff · cara: ambil ungkapan sehari-hari secara harfiah ("gaji numpang lewat" → gaji berupa kereta yang lewat di depan rumah tanpa berhenti), buat sebagai pelat/potongan Flow realistis, satu per video.
- **Objek persisten lintas dunia** · manfaat: kontinuitas cerita kuat dengan sedikit narasi · kapan: metafora berlapis · cara: `cocok` antar-adegan + gambar dari `acuan` sama; catat keadaan benda di kolom storyboard.
