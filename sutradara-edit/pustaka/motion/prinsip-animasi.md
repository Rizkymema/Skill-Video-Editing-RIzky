# Prinsip Animasi + Mikro-Animasi & Polish

> Kategori **MOTION** · dipakai di langkah 8 (bahasa gerak) dan 14 (polish) · terkait: `transisi.md`, `../cinematic/kamera.md`, `../type/tipografi-kinetik.md`, `../audio/sound-design.md`, `../polish/qc.md`

Prinsip inti:
1. **Gerak = informasi.** Setiap gerak menjawab satu pertanyaan: menunjuk apa, mengungkap apa, menghubungkan apa, atau memberi rasa apa. Tidak ada jawaban → hapus.
2. **Tidak ada yang linear kecuali mesin.** Benda nyata selalu mempercepat dan melambat.
3. **Benda punya massa.** Ringan = cepat + overshoot besar; berat = lambat + mendarat keras + guncang.
4. **Satu pusat perhatian bergerak dalam satu waktu.** Sisanya diam atau hanya bernapas.
5. **Mikro-gerak menjaga hidup, bukan menarik perhatian.** Kalau penonton menyadarinya sebagai efek, terlalu besar.

---

## 1. Tes gerak bertujuan (sebelum menganimasi apa pun)
| Fungsi | Pertanyaan | Gerak yang cocok | Di mesin Kolase |
|---|---|---|---|
| Menunjuk | ke mana mata harus pergi? | masuk dari arah pandang, sorot, panah | `masuk: { gaya: 'geser', dari }`, `efek: sorot`, `coret: 'panah'` |
| Mengungkap | apa yang tadinya tersembunyi? | penutup bergeser, mundur, mask | `keluar` penutup, kamera `mundur`, `panel` + `gerak` |
| Menghubungkan | A berhubungan dengan B? | benda berpindah, gerak sepanjang garis | perpindahan `cocok`, `gerak` beberapa keyframe |
| Menekankan | apa yang paling penting? | overshoot, hantam, guncang kecil | `pop`/`tumbuh`/`jatuh`/`cap`, `efek: kilau` |
| Memberi rasa | suasana apa? | napas, melayang, partikel pelan | `rig: 'napas'`, `hidup`, `efek: partikel` |
| Memberi jeda | penonton perlu mencerna? | hampir diam | kamera `tenang`, tanpa masuk baru |

Tulis fungsi tiap gerak di kolom "motion" storyboard (`../../templat/storyboard.md`) dengan satu kata.

## 2. Anggaran gerak (motion budget)
- **Per bingkai**: 1 gerak primer (yang diikuti mata) + maks 2 sekunder; sisanya mikro (amplitudo ≤ 2% layar).
- **Per adegan 2–3 dtk**: maks 3 peristiwa masuk (benda/teks), jarak antar-masuk ≥ 0,25–0,4 dtk. Patokan kolase: sesuatu baru tiap ±1–1,5 dtk (`skill-edit-rizky/references/gaya.md` §3).
- **Saat perpindahan berjalan**: tidak ada masuk besar lain.
- **Saat teks dibaca**: kamera dan latar tenang (zoom ≤ 3–5% per adegan), teks sendiri diam.
- **Kamera besar dan benda besar** tidak bersamaan: pilih salah satu sebagai gerak primer.
- **Loop terus-menerus** (berputar, berdenyut) maks satu unsur per bingkai, dan amplitudonya kecil.

---

## 3. Tangga easing
Naiki tangga hanya sejauh yang dibutuhkan rasa geraknya.

| Anak tangga | Rasa | Kapan | Nama easing di mesin (`E`) |
|---|---|---|---|
| 1. Linear | mesin, konstan, tanpa nyawa | konveyor, jarum detik, gulir kredit, drift kamera sangat pelan, rotasi terus | `linear` |
| 2. Ease in (mempercepat) | pergi, jatuh, lepas | benda keluar layar, adegan lama menuju titik potong momentum | `inQuad` (lembut) · `inCubic` · `inExpo` (keras) |
| 3. Ease out (melambat) | datang, mendarat | **hampir semua masuk** | `outCubic` (bawaan) · `outQuart` (lebih tegas) · `outQuint` · `outExpo` (melesat lalu halus: UI, terbang) |
| 4. Ease in-out | pindah tempat di dalam layar | geser di dalam bingkai, keyframe kamera | `inOutSine` (paling halus) · `inOutCubic` (bawaan `gerak`) · `inOutQuart` · `inOutExpo` |
| 5. Kurva khusus | karakter merek/gaya | gerak tanda tangan video | fungsi sendiri di posisi easing: `[.6, { y: 0 }, x => 1 - (1 - x) ** 6]` (mesin menerima fungsi) |
| 6. Overshoot | hidup, tegas, ceria | pop ikon, teks hero, kartu mendarat | `outBack` (≈ 10% lewat) · `pegas` (≈ 8% + satu ayunan) · `outElastic` (≈ 35%, kartun saja) |
| 7. Settle | massa yang berhenti | setelah overshoot, benda berat | `pegas` sudah termasuk settle; manual: `[[0, { skala: 0 }], [.22, { skala: 1.08 }, 'outCubic'], [.34, { skala: .98 }, 'inOutSine'], [.44, { skala: 1 }, 'inOutSine']]` |

Pendaratan benda jatuh memakai `outBounce` (memantul di bawah target, bukan melewati). Antisipasi otomatis: `inBack` (mundur ±10% sebelum berangkat).

### 3.1 Durasi patokan (30 fps)
| Besar gerak | Contoh | Bingkai | Detik |
|---|---|---|---|
| Mikro (≤ 5% layar) | ikon pop, kata pop, tombol | 6–10 | 0,2–0,33 |
| Kecil (5–20%) | teks luncur, label, notifikasi | 9–14 | 0,3–0,45 |
| Sedang (20–60%) | kartu masuk, panel tutup | 12–20 | 0,4–0,65 |
| Besar (layar penuh) | perpindahan, `terbang` | 15–24 | 0,5–0,8 |
| Sinematik pelan | judul elegan, pudar, tracking | 24–45 | 0,8–1,5 |

- **Overshoot**: 4–6% (korporat, mewah, editorial) · 8–12% (sosial, ceria, kartu) · > 15% hanya kartun/Y2K.
- **Settle**: 6–10 bingkai (0,2–0,33 dtk) sesudah puncak overshoot; maksimal 1–2 ayunan.
- **Stagger** (beberapa unsur berurutan): 2–4 bingkai (0,06–0,12 dtk) per unsur; > 6 bingkai terasa lambat.
- Gerak lebih cepat dari 4 bingkai tidak terbaca (kecuali whip dengan blur gerak).

---

## 4. Prinsip animasi (11)
Format: **Kapan** · **Kenapa** · **Cara** · **Hindari** · **Di mesin Kolase**.

### 4.1 Squash & stretch
- **Kapan**: benda lentur/ringan mendarat atau melesat (bola, ikon, karakter kartun, stiker); gaya ceria/kartu/Y2K. **Kenapa**: memberi kesan massa dan elastis. **Cara**: memanjang 8–15% searah gerak saat cepat, memipih 8–15% saat mendarat, volume tetap (lebar × tinggi konstan), kembali dalam 4–6 bingkai. **Hindari**: pada benda keras (dokumen, HP, gedung) dan pada foto realistis (terlihat rusak).
- **Di mesin**: *Celah mesin*: `gerak` hanya `skala` seragam. Akali: `masuk: 'jatuh'` (pantulan memberi kesan berat) + blur gerak; untuk ikon kartun gambar di benda `kustom` dengan `c.scale(sx, sy)`.

### 4.2 Anticipation (antisipasi)
- **Kapan**: sebelum gerak besar, hantaman, pembalik. **Kenapa**: otak bersiap, gerak utama terasa lebih kuat. **Cara**: gerak kecil berlawanan arah 3–6 bingkai (5–10% jarak gerak utama), atau jeda/diam 4–8 bingkai sebelum hantaman; di bunyi: riser 0,5–1,5 dtk sebelum hit. **Hindari**: antisipasi di setiap gerak kecil (lambat).
- **Di mesin**: easing `inBack` di keyframe keluar; momentum perpindahan sudah mengandung antisipasi (adegan lama dipercepat `inCubic` sampai titik potong); `sfx: [{ t, jenis: 'riser', lama: 1 }]` sebelum `kilau`.

### 4.3 Staging
- **Kapan**: selalu. **Kenapa**: penonton harus tahu ke mana melihat dalam 0,3 dtk. **Cara**: satu subjek, kontras tertinggi di subjek, latar lebih gelap/kabur, teks tidak bersaing dengan subjek, gerak primer satu. **Hindari**: dua hal penting masuk bersamaan; subjek di area tombol aplikasi.
- **Di mesin**: `efek: [{ jenis: 'sorot', titik }]`, `{ jenis: 'gelap' }`, `{ jenis: 'lensa' }`, `blur` pada latar, kamera `tenang`. Lihat `../visual/komposisi.md`.

### 4.4 Follow through
- **Kapan**: setelah benda berhenti (label tergantung, kertas mendarat, rambut/kain). **Kenapa**: bagian yang lentur tetap bergerak sesaat = nyata. **Cara**: ayunan teredam 2–3 kali dalam 0,6–1,2 dtk; overshoot + settle. **Hindari**: ayunan tanpa redam (seperti rusak).
- **Di mesin**: `ayun: { sudut: 10–14, periode: 1.1, redam: 1.4 }` (label harga, papan gantung), `rig: 'kibar'` (kertas/bendera), `tumbuh` (pegas).

### 4.5 Overlapping action
- **Kapan**: beberapa unsur satu kelompok (daftar ikon, kata, kartu). **Kenapa**: unsur yang tiba berurutan terasa organik, bukan blok. **Cara**: stagger 2–4 bingkai; unsur depan (z besar) sedikit lebih lambat dari belakang; bagian tubuh tokoh tiba tidak bersamaan. **Hindari**: stagger yang sama persis untuk semua kelompok di video (pola terbaca).
- **Di mesin**: `t: 'L06.w1+0.1'`, `'+0.18'`… per unsur, atau `tiap` pada teks; `rig: ['napas', { jenis: 'goyang', fase: .3 }]` pada tokoh.

### 4.6 Timing
- **Kapan**: menentukan durasi tiap gerak. **Kenapa**: jumlah bingkai = berat dan emosi. **Cara**: tabel §3.1; benda berat +30–50% bingkai; adegan serius lebih lambat; hook lebih cepat. **Hindari**: semua gerak berdurasi sama (0,5 dtk di mana-mana).
- **Di mesin**: `lama` di `masuk`/`keluar`, waktu keyframe `gerak`, `lamaMasuk` adegan.

### 4.7 Spacing
- **Kapan**: bersamaan dengan timing. **Kenapa**: jarak antar-posisi di tiap bingkai menentukan rasa (rapat = lambat, renggang = cepat). **Cara**: renggang di tengah gerak, rapat di ujung (ease out) = mendarat lembut; renggang di ujung (ease in) = pergi. **Hindari**: spasi rata (linear) untuk benda hidup.
- **Di mesin**: dipilih lewat nama easing; periksa dengan `kontak --t` rapat (0,05 dtk) di sekitar gerak.

### 4.8 Easing
- Lihat §3. **Hindari**: `outElastic`/`outBounce` di gaya serius; `linear` di masuk teks/benda.

### 4.9 Exaggeration
- **Kapan**: payoff, hook, pembalik; gaya sosial/kartun. **Kenapa**: kamera dan layar HP kecil "memakan" gerak; dilebihkan 10–20% supaya terbaca. **Cara**: lebih besar hanya di satu pose kunci, sisanya normal. **Hindari**: melebih-lebihkan semuanya (jadi norak) atau di topik tragedi.
- **Di mesin**: `cap` (skala 2,6 → 1), `efek: kilau`, `guncang kuat: .6–1`, `padat` raksasa.

### 4.10 Arcs
- **Kapan**: benda dilempar, tangan, kamera melayang, kartu terbang. **Kenapa**: gerak alami mengikuti lengkung, garis lurus terasa robotik. **Cara**: jalur lengkung dengan titik tengah 10–25% di luar garis lurus; putaran ringan searah lengkung. **Hindari**: lengkung pada UI (UI bergerak lurus).
- **Di mesin**: `masuk: 'lempar'`, `'terbang'`; manual `gerak` 3–4 keyframe dengan titik tengah menyimpang. *Celah mesin*: jalur bezier (antar-keyframe masih garis lurus).

### 4.11 Secondary action
- **Kapan**: saat aksi utama berlangsung tapi adegan perlu hidup (tokoh bernapas saat teks muncul, debu melayang). **Kenapa**: dunia terasa terus berjalan. **Cara**: amplitudo kecil, ritme lebih lambat dari aksi utama, tidak berbunyi. **Hindari**: aksi sekunder yang lebih menarik dari aksi utama.
- **Di mesin**: `rig: 'napas'`/`'angguk'`, `hidup: 4–6`, `efek: partikel debu`, `kilap` sekali.

---

## 5. Mikro-animasi & polish
| Detail | Angka patokan | Kapan | Hindari | Di mesin Kolase |
|---|---|---|---|---|
| Overshoot | 4–12%, 0,3–0,45 dtk | masuk ikon/teks hero | semua unsur | `pop`, `tumbuh`, easing `outBack`/`pegas` |
| Easing | tangga §3 | semua gerak | linear pada benda hidup | nama `E` di `gerak` |
| Antisipasi | 3–6 bingkai, 5–10% berlawanan | sebelum gerak besar | gerak kecil | `inBack`, momentum keluar |
| Follow-through | 2–3 ayunan teredam | benda tergantung/lentur | tanpa redam | `ayun`, `rig: 'kibar'` |
| Secondary motion | amplitudo ≤ 30% aksi utama | tokoh, latar | lebih ramai dari aksi utama | `rig`, `hidup` |
| Guncang kamera halus | 4–10 px, 0,25–0,4 dtk, meredam | hantaman, cap, angka jatuh | tiap potongan | `efek: { jenis: 'guncang', kuat: .2–.4, lama: .3 }`; otomatis pada `jatuh`/`cap` |
| Parallax mikro | beda `z` 0,3 / 1 / 1,8 + drift 3–9% | setiap adegan foto | z sama untuk semua | `z` per lapisan + kamera `dorong`/`tenang` |
| Melayang (floating) | 4–12 px, periode 3–6 dtk | ikon, kartu, benda di ruang kosong | benda yang seharusnya berat | `hidup: 4–8` |
| Bernapas (breathing) | skala ±0,8–1,5%, periode 3–4 dtk | tokoh, siluet | pada teks | `rig: 'napas'` (±1,2% / 3,6 dtk) |
| Variasi opasitas | kedip 2–6% | lampu, neon, layar, film | teks informasi | *Celah*: kedip; akali `gerak` alfa 3–4 keyframe, grade `garis` (tv) |
| Tekstur bergerak | grain berganti tiap bingkai, kertas geser 1–3 px/dtk | gaya analog/kertas | tekstur diam (terlihat tempelan) | grade `grain` (4 ubin bergantian tiap bingkai) dan `debu` (acak tiap bingkai); `halftone` diam |
| Noise halus (wiggle) | 1–3 px, 0,3–0,8 Hz | potongan foto, teks besar diam lama | pada UI presisi | `hidup: 2–3`; `kameraHidup` (±5 px, ±0,12°, bawaan) |
| Variasi skala kecil | 0,97–1,03 antar-unsur sejenis | daftar ikon, kolase | variasi yang terlihat acak berantakan | `lebar`/`skala` sedikit berbeda + `putar` ±1–4° |

### 5.1 Resep siap pakai
- **Ikon pop**: `masuk: 'pop'` + `bayangan: .3` + `hidup: 5` + bunyi pop halus; stagger 0,1 dtk antar-ikon.
- **Kartu mendarat**: `masuk: 'jatuh'` (guncang otomatis) + `putar: -3` + `bayangan: .5` + bunyi kertas/dum.
- **Teks hero hantam**: `teks` `padat` `ukuran: 220`, `masuk: 'tumbuh'` di downbeat, `efek: { jenis: 'garis', titik }`, kamera `tenang` 0,5 dtk sebelum (diam sebelum hantaman).
- **Tokoh hidup**: `rig: ['napas', { jenis: 'goyang', sudut: { amp: 1.2, periode: 4 }, fase: .3 }]` + `hidup: 3`.
- **Label harga**: `benda: { jenis: 'label' }` + `ayun: { sudut: 12 }`.
- **Benda penting menyala**: `kilap: { t }` sekali + `efek: { jenis: 'kilau', t, kuat: .6 }` hanya di payoff.

## Teknik modern
- **Spring physics (pegas) sebagai bawaan UI** · manfaat: gerak UI modern (iOS/Material) terasa mahal tanpa terlihat "efek" · kapan: gaya Futuristic UI, Corporate Premium, kartu data · cara: easing `pegas` untuk masuk kartu/ikon, `outExpo` untuk geser panel; satu jenis kurva per video.
- **Kurva tanda tangan per video** · manfaat: identitas gerak konsisten seperti merek · kapan: seri video · cara: definisikan satu fungsi easing di kepala `konfig.js` (`const KURVA = x => …`) dan pakai di semua `gerak`; catat di brief (`../../templat/brief.md`).
- **Gerak 2 lapis kecepatan (hold-then-snap)** · manfaat: rasa editorial modern: diam lama lalu pindah sangat cepat (6–8 bingkai `outExpo`) · kapan: gaya Editorial, Minimalist, Luxury · cara: keyframe datar lalu satu segmen pendek `outExpo`.

## Cek cepat
1. Setiap gerak punya fungsi satu kata (tabel §1)?
2. Satu gerak primer per bingkai; tidak ada kamera besar + benda besar bersamaan?
3. Tidak ada `linear` pada benda/teks hidup?
4. Durasi bervariasi sesuai besar gerak (bukan 0,5 dtk semua)?
5. Overshoot dalam rentang gaya (≤ 6% mewah/editorial, ≤ 12% sosial)?
6. Benda yang berhenti punya settle/follow-through, tidak berhenti mendadak?
7. Mikro-gerak tidak disadari sebagai efek (tidak ada yang berkedip/berdenyut mencolok)?
8. Teks diam saat dibaca, dan latar tenang saat teks panjang tampil?

## Celah mesin
- Skala tidak seragam (`skalaX`/`skalaY`) untuk squash & stretch dan deformasi.
- Jalur gerak lengkung (bezier) antar-keyframe untuk arcs.
- Kedip opasitas (flicker) per lapisan/efek.
- Wiggle frekuensi tinggi per lapisan (`hidup` hanya drift pelan).
