# Musik dan sinkron ketukan

> AUDIO · dipakai di langkah 12 (struktur di langkah 3, dicek di 15) · terkait: `sound-design.md`, `../core/editing.md`, `../story/cerita.md`, `../short-form/short-form.md`, `../type/tipografi-kinetik.md`

Prinsip inti:
1. **Musik adalah peta emosi, bukan karpet.** Bagian musik (tenang, naik, puncak, turun) dipetakan ke beat cerita, bukan diputar rata dari awal sampai akhir.
2. **Jangan semua potongan di ketukan.** Pola yang hidup: **ketukan → tahan → antisipasi → hantam → lepas**. Potongan rata di setiap ketukan terasa seperti templat slideshow.
3. **Hening adalah alat paling kuat.** Musik berhenti 0,2–1 dtk sebelum pengungkapan membuat hantaman berikutnya dua kali lebih besar.
4. **Narasi menang.** Untuk video bernarasi, musik melayani kejelasan kata: tanpa vokal, tidak padat di frekuensi tengah, diredam saat orang bicara.
5. **Satu video, satu arah musik.** Ganti lagu hanya di titik balik cerita (babak baru), dan gantinya di batas birama.

## 1. Memilih musik
| Jenis video | Tempo | Suasana | Contoh folder lokal `D:\Sound\Backsound\` |
|---|---|---|---|
| Explainer/edukasi bernarasi | 80–110 BPM | ambient, pulsa ringan, tanpa vokal | `Documentary`, `Corporate Tech`, `Quirky Curious`, `Chill Lofi` |
| Sejarah/arsip/misteri | 70–95 | drone, piano rendah, string | `Documentary`, `Dark Suspense`, `Cinematic Epic` |
| Horor/psikologis | 60–80 atau tanpa tempo | drone, denyut, ruang | `Horror`, `Dark Suspense` |
| Motivasi/transformasi | 90–120 | membangun, drum masuk di babak 2 | `Inspiring Motivational`, `Cinematic Epic` |
| Tips/santai/lucu | 95–120 | petikan, marimba, ukulele | `Upbeat Happy`, `Funny Comedy`, `Quirky Curious` |
| Montase tanpa narasi / edit beat | 120–150 (atau 140–160 phonk) | drum jelas, drop | `Hip Hop Beat`, `Phonk`, `Action Sport`, `Game Chiptune` |
| Emosional | 60–85 | piano, akustik | `Sad Emotional`, `Romantic Acoustic` |
| Budaya/tradisi | bebas | instrumen lokal | `Asian Traditional` |

Sumber, urut: (1) Epidemic Sound lewat konektor (`SearchRecordings`: tanpa vokal, mood, BPM, durasi 60–200 dtk; tampilkan 2–3 pilihan + tautan pratinjau di dialog persetujuan; `DownloadRecording` sesudah disetujui, tautan kedaluwarsa ±5 menit); (2) musik milik pengguna di `D:\Sound\Backsound\` atau kiriman; (3) musik sintesis mesin (§6) bila tidak ada yang cocok. Agen `penata-musik` mengerjakan pemilihan per babak + angka redam + kredit.

Syarat untuk video bernarasi: **tanpa vokal berlirik**, tidak ada lead melodi yang menonjol di 1–4 kHz (bertabrakan dengan konsonan), punya bagian yang jelas berubah (supaya bisa dipetakan ke cerita). Uji: putar musik di −20 dB di bawah narasi; bila kata masih sulit ditangkap, ganti musik, bukan naikkan narasi.

## 2. Struktur musik ↔ struktur cerita
| Bagian musik | Beat cerita (`../story/cerita.md`, `../short-form/short-form.md`) | Perlakuan visual |
|---|---|---|
| Intro / tanpa drum | HOOK + CONTEXT | potongan tidak di ketukan; gerak kamera pelan; teks hook mendarat di kata, bukan di ketukan |
| Verse / pulsa stabil | DEVELOPMENT (fakta 1–2–3) | sebagian pergantian di ketukan kuat (1 dan 3), sebagian di kata kunci |
| Build-up / riser | TENSION (masalah, "tapi…") | potongan makin rapat (2 ketukan → 1 ketukan), kamera `dorong-kuat`, teks makin besar |
| **Hening sebelum drop** | detik sebelum pengungkapan | gambar ditahan / layar gelap / satu kata |
| Drop / puncak | PAYOFF / pengungkapan / angka besar | hantaman: potong + kilau + boom tepat di drop |
| Breakdown / turun | refleksi, vonis, "hari ini" | potongan panjang, ruang napas, musik tipis |
| Outro / ending resolusi | LOOP / CTA | akhiri di akord tuntas atau hit tunggal; atau potong mati untuk loop |

Bila musik tidak punya bagian yang pas dengan cerita: potong/sambung musiknya (§4), jangan memaksa cerita mengikuti musik.

## 3. Teknik
### Deteksi ketukan (beat detection) dan penanda (beat markers)
- **Kapan**: sebelum storyboard final, setiap kali memakai musik berkas.
- **Kenapa**: posisi ketukan, birama, drop, dan hening harus diketahui dalam detik supaya bisa diputuskan mana yang diikuti dan mana yang sengaja dilawan.
- **Cara**: jalankan `scripts/ketukan.py` (bagian §7). Tandai di tabel storyboard kolom "Musik": nomor birama, `D` (drop), `H` (hening), `B` (build).
- **Hindari**: menebak BPM dari judul lagu; menempatkan pergantian dengan mata di timeline tanpa angka.

### Potong di ketukan (beat cutting)
- **Kapan**: montase, daftar cepat (3 hal), bagian build-up, video tanpa narasi.
- **Kenapa**: otak menikmati keselarasan pendengaran dan penglihatan; potongan terasa "benar".
- **Cara**: potong di **ketukan kuat** (1 dan 3 birama 4/4) untuk pergantian adegan; ketukan lemah (2, 4) untuk pergantian kecil dalam adegan (teks, benda). Potong **1–2 bingkai sebelum** ketukan: mata butuh sedikit waktu, jadi potongan yang tepat di ketukan terasa sedikit telat. Variasikan panjang: 4 ketukan → 4 → 2 → 2 → 1 → 1 → tahan 8.
- **Hindari**: potong di setiap ketukan sepanjang video; memotong di tengah kata narasi demi ketukan (kata menang).

### Animasi berirama (rhythm-based animation)
- **Kapan**: teks muncul per kata dalam daftar, ikon bermunculan, grafik naik, denyut latar.
- **Kenapa**: gerak kecil yang selaras ketukan membuat video terasa "satu instrumen".
- **Cara**: tiap butir muncul di ketukan atau setengah ketukan; denyut skala 2–4% di ketukan kuat untuk elemen latar (bukan teks yang sedang dibaca). Pakai ketukan sebagai **kisi**, lalu geser 1–3 butir keluar kisi supaya tidak mekanis.
- **Hindari**: semua elemen berdenyut bersamaan (seperti visualizer musik); teks yang sedang dibaca bergoyang.

### Transisi digerakkan musik (music-driven transitions)
- **Kapan**: pergantian babak, pengungkapan, perubahan dunia (`../motion/transisi.md`).
- **Kenapa**: transisi besar paling meyakinkan bila dipicu peristiwa musik (hit, drop, akhir frase).
- **Cara**: transisi besar (`bingkai`, `putar`, `dorong-kuat`) di **awal frase** (tiap 4 atau 8 birama); transisi kecil (`geser`, `fokus`) di dalam frase. Whoosh transisi memuncak di ketukan.
- **Hindari**: transisi besar di tengah frase musik (terasa tersandung).

### Bass impact dan drop sync
- **Kapan**: angka besar, judul, vonis, payoff.
- **Kenapa**: drop adalah titik energi tertinggi; menaruh informasi terpenting di situ membuat informasi itu "terasa" penting.
- **Cara**: susun mundur dari drop: drop = bingkai pengungkapan (potong + teks besar + kilau + boom/sub). 0,2–0,5 dtk sebelum drop = hening atau riser berhenti. Narasi kalimat pengungkapan selesai **sebelum** drop atau kata kuncinya jatuh **tepat** di drop (`--kata` di `ketukan.py` membantu mencari jeda narasi).
- **Hindari**: drop yang datang saat narasi sedang menjelaskan hal kecil; drop tanpa perubahan visual.

### Build-up dan ketegangan musik
- **Kapan**: babak TENSION, hitung mundur, kronologi menuju kejadian.
- **Kenapa**: musik yang menahan resolusi (akord menggantung, riser, drum makin rapat) membuat penonton menunggu.
- **Cara**: potongan dirapatkan bertahap mengikuti build (4 → 2 → 1 ketukan), kamera makin cepat, warna makin kontras, teks makin besar. Bisa diperkuat riser SFX dan `jantung` di bawah.
- **Hindari**: build-up yang lebih panjang dari 4–6 dtk di video pendek; build-up yang berakhir antiklimaks.

### Hening sebelum hantaman (silence before impact)
- **Kapan**: satu kali per video, di titik terpenting.
- **Kenapa**: kontras dinamis; telinga "menahan napas".
- **Cara**: musik dan SFX berhenti 0,2–1 dtk (room tone tetap), gambar ditahan atau gelap, lalu hantaman + musik masuk kembali di ketukan 1.
- **Hindari**: hening berkali-kali (kehilangan daya); hening nol mutlak tanpa room tone.

### Pola variasi: ketukan → tahan → antisipasi → hantam → lepas
| Tahap | Lama patokan | Gambar | Bunyi |
|---|---|---|---|
| Ketukan | 2–4 potongan di ketukan | ganti cepat, berirama | musik penuh |
| Tahan | 1–2 birama | satu gambar ditahan, kamera pelan | musik tetap, tanpa SFX |
| Antisipasi | 0,5–2 dtk | dorong-kuat, teks menahan diri, layar menggelap | riser / musik menipis |
| Hantam | 1 bingkai | potong + teks besar + kilau | hening 0,2 dtk → impact/boom di ketukan 1 |
| Lepas | 1–3 dtk | gambar lega, gerak melambat | ekor boom + musik bagian baru |

## 4. Menyunting musik
- Potong dan sambung **di garis birama** (awal ketukan 1), silang-pudar 2–4 ketukan (±1–2 dtk), atau potong keras tepat di transient drum.
- Memperpendek: buang kelipatan 4 atau 8 birama dari tengah verse; jangan memotong build-up.
- Mengakhiri: berhenti di **akord tuntas** atau **satu hit akhir** pada bingkai terakhir; untuk video loop, potong mati di ketukan 1 supaya putaran ulang menyambung (`../short-form/short-form.md` §Loop).
- Mulai dari tengah lagu (mis. langsung dari drop): potong berkasnya dulu, `ffmpeg -ss 24.0 -i lagu.mp3 -c:a libmp3lame -q:a 2 lagu-dari-drop.mp3`, lalu jalankan `ketukan.py` pada berkas hasil potongan.
- Musik lebih panjang dari video: mesin memudarkan musik di 1,2 dtk terakhir; tetap pastikan akhir video jatuh di ujung frase.

## 5. Ducking dan campuran
- Musik berkas: `rakit … --musik audio/epidemic/<lagu>.mp3 --vol-musik 0.3` (bawaan 0,3). Mesin meredam musik ke 30% saat tiap baris narasi berbunyi (mulai 0,12 dtk sebelum baris, pulih 0,15 dtk sesudah), memudar di akhir, lalu seluruh campuran dinormalkan ke −14 LUFS.
- Musik sintesis (`KONFIG.musik`) diredam ke 32–40% saat narasi.
- Patokan: musik terdengar jelas di jeda narasi, nyaris tidak disadari saat orang bicara. Bila narasi rapat tanpa jeda, turunkan `--vol-musik` ke 0,2–0,25 dan pilih musik lebih tipis.
- Ukur: `jalankan.py cek` (LUFS) lalu sesudah ekspor `ffmpeg -i <mp4> -af ebur128=peak=true -f null -` (−14 ±1 LUFS, puncak < 0 dBFS). Agen `penata-musik` mengukur kejelasan dialog dan memberi angka redam.

## 6. Di mesin Kolase
- **Musik sintesis** (`KONFIG.musik`): `{ sintesis: 'dokumenter' | 'misteri' | 'tegang' | 'pad' | 'pulsa' | 'ceria' | 'jenaka', bpm, kunci (Hz), akord, vol, mulai, akhir }`; variasi akord/nada otomatis dari `benih` (beda tiap judul). **Daftar segmen** untuk mengubah musik per babak: `musik: [{ sintesis: 'pad', mulai: 0, akhir: 'L06' }, { sintesis: 'tegang', mulai: 'L06', akhir: 'L09.akhir', bpm: 96 }, { sintesis: 'dokumenter', mulai: 'L10' }]` — jeda antar-segmen = hening (pakai untuk "hening sebelum hantaman").
- **Musik berkas**: `rakit --musik <berkas> --vol-musik 0.3`; mulai di detik 0 timeline, berulang bila lebih pendek dari video.
- **Hantaman di ketukan**: hit, boom, sub, impact lewat `KONFIG.sfx` dengan `t` **detik mutlak** (cocok untuk waktu dari `ketukan.py`), atau `sfx` adegan dengan `t` **detik sejak adegan mulai** / rujukan narasi.
- **Pergantian adegan di ketukan**: `mulai` adegan boleh angka detik mutlak (`mulai: KETUKAN.birama[6]`) atau rujukan narasi (`'L05.w4'`). Utamakan rujukan narasi untuk adegan yang membawa kalimat; pakai angka ketukan untuk adegan montase/tanpa narasi atau saat kata kunci dan ketukan berdekatan (< 0,15 dtk: geser ke ketukan).

## 7. Alat: `scripts/ketukan.py`
```
python -X utf8 -I scripts/ketukan.py <musik.mp3|wav|mp4> [--keluar ketukan.json] [--kata _kerja/audio/eleven/kata.json] [--mulai S] [--sampai S] [--konfig] [--potongan ringkasan.json]
```
Keluaran JSON (waktu = detik dihitung dari `--mulai`; tanpa `--mulai` = dari awal berkas). Karena `rakit --musik` selalu memutar berkas dari detik 0, cara paling aman: potong lagunya dulu dengan ffmpeg (§4), lalu jalankan `ketukan.py` pada **berkas hasil potong** tanpa `--mulai`, sehingga waktu keluaran = waktu timeline video.
| Kunci | Isi | Dipakai untuk |
|---|---|---|
| `bpm` | tempo perkiraan | memilih panjang potongan (1 ketukan = 60/bpm dtk) |
| `ketukan` | `[t, …]` semua ketukan | kisi animasi berirama, potong kecil |
| `birama` | `[t, …]` perkiraan awal birama | pergantian adegan, sambung/potong musik |
| `energi` | `[[t, dB], …]` tiap 0,25 dtk | melihat naik-turun lagu |
| `bagian` | `[{ mulai, akhir, jenis: tenang\|naik\|puncak\|turun }]` | memetakan musik ke beat cerita (§2) |
| `drop` | `[t, …]` lonjakan energi terbesar | payoff/pengungkapan |
| `hening` | `[[a, b], …]` jeda sepi di musik | titik "tahan" alami |
| `saran` | `[{ t, peran: hantam\|ketukan\|antisipasi\|tahan\|lepas, alasan }]` | usulan pola variasi §3 |

- `--kata <kata.json>`: memprioritaskan titik **hantam** yang jatuh di jeda narasi ≥ 0,25 dtk (hantaman tidak menutupi kata).
- `--mulai/--sampai`: membatasi rentang analisis (untuk mencoba bagian lagu; waktu keluaran dihitung dari `--mulai`).
- `--potongan <ringkasan.json>`: untuk membedah acuan: berapa persen potongan video acuan (dari `bedah_acuan.py`) jatuh di ketukan, di awal birama, di setengah ketukan, atau lepas ketukan. Hasil 8 reel @earn.edits: video bercerita 0–25%, promosi 23–56% (`../style/resep/README.md`).
- Diuji 27 Nov 2026: trek sintetis 120 BPM dengan hening 15–16 dtk → BPM 119,8, ketukan dan awal birama tepat ±1 bingkai, drop 15,97 dtk, "tahan" di 15,00; musik sinematik nyata (60 dtk) terbaca 129,5 BPM. Awal birama tetap perkiraan: cek dengan telinga sebelum memasang potongan penting.
- `--konfig`: mencetak `const KETUKAN = {...}` untuk ditempel **di atas** `konfig.js`, lalu dipakai:
```js
const KETUKAN = { bpm: 96, birama: [0.42, 2.92, 5.42, /* … */], drop: [21.9], /* … */ };
const KONFIG = { /* … */,
  sfx: [{ t: KETUKAN.drop[0] - 0.9, jenis: 'riser', lama: .85 }, { t: KETUKAN.drop[0], jenis: 'boom' }] };   // detik mutlak
const ADEGAN = [ /* … */,
  { id: 'ungkap', mulai: KETUKAN.drop[0], masuk: 'kilat', lapis: [
      { teks: '^381^ MILIAR', gaya: 'padat', t: 0 },                                   // t = detik sejak adegan mulai
      { teks: 'dalam satu tahun', gaya: 'serif', t: KETUKAN.ketukan[40] - KETUKAN.drop[0] } ] } ];
```
Waktu dari `ketukan.py` berlaku langsung bila musik mulai di detik 0 timeline (bawaan `--musik`). Bila narasi digeser `rakit --mulai`, musik tidak ikut bergeser.

Alur: pilih musik → `ketukan.py … --kata … --konfig` → tandai birama/drop/hening di storyboard → letakkan pengungkapan di drop, jeda tahan di `hening`/`tenang` → rakit → dengar → geser per 1–2 bingkai bila terasa telat.

## Teknik modern
- **Edit berirama dengan speed ramp** (velocity edit): klip/gerak kamera dipercepat menuju ketukan lalu melambat sesudahnya. Manfaat: energi tanpa menambah potongan. Kapan: montase, intro, payoff tanpa narasi. Alur: adegan dimulai satu ketukan sebelum ketukan sasaran, lalu kamera keyframe (detik sejak adegan mulai) `kamera: [[0, { zoom: 1 }], [b, { zoom: 1.25 }, 'inExpo'], [b + .4, { zoom: 1.3 }, 'outQuart']]` dengan `b = 60 / KETUKAN.bpm` (`../cinematic/kamera.md`).
- **Stem / lapisan musik terpisah** (drum, bas, pad): Epidemic menyediakan stem untuk banyak lagu. Manfaat: bisa "membisukan drum" saat narasi padat lalu memasukkan drum di payoff. Alur: unduh stem lewat konektor Epidemic bila tersedia, tanam stem sebagai berkas `--sfx` dan atur dengan `sfx: [{ t, berkas, dari, lama, vol }]` per babak (stem lewat `sfx` tidak diredam otomatis oleh narasi, jadi turunkan `vol`).
- **Musik adaptif lewat segmen sintesis**: ganti `sintesis`/`bpm` per babak dalam daftar segmen supaya musik mengikuti cerita tanpa mencari lagu baru.

## Cek cepat
- [ ] Musik tanpa vokal berlirik; kata narasi jelas di speaker HP.
- [ ] Bagian musik terpetakan ke beat cerita (hook, tegang, payoff, penutup).
- [ ] Tidak semua potongan di ketukan; ada pola tahan → antisipasi → hantam → lepas.
- [ ] Ada satu momen hening/menipis sebelum hantaman terpenting.
- [ ] Payoff/pengungkapan jatuh di drop atau awal frase, tidak di tengah frase.
- [ ] Sambungan musik di garis birama; akhir video di akord tuntas, hit, atau potong loop yang bersih.
- [ ] LUFS −14 ±1, puncak < 0 dBFS.

## Celah mesin
- **Musik berkas tidak bisa dimulai dari tengah berkas** (`--musik` selalu dari detik 0 berkas). Akali: potong dengan ffmpeg (§4), atau tanam bagian lagu sebagai berkas `--sfx` dan pakai `{ t, berkas, dari, lama }` (tanpa redam narasi otomatis).
- **Tidak ada keyframe volume musik / jendela bisu** (untuk hening sebelum drop). Akali: musik sintesis bersegmen dengan jeda, atau edit berkas musik: `ffmpeg -i lagu.mp3 -af "volume=enable='between(t,21.4,21.9)':volume=0" lagu-hening.mp3`.
- **Hanya satu musik berkas** per video. Akali: gabung dua lagu dengan silang-pudar di garis birama lewat ffmpeg (`acrossfade=d=1.5`) sebelum `rakit`.
- **Tidak ada penanda ketukan di pemutar mesin** (tanda adegan saja). Akali: baca `ketukan.json`; usulan: tampilkan `KETUKAN.birama` sebagai garis di bilah waktu pemutar.
