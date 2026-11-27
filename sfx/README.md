# Pustaka SFX Edit Rizky

**Sumber utama SFX** untuk `/skill-edit-rizky` (permintaan pengguna 28 Nov 2026: "utamakan sfx dari folder ini… yang tidak cocok cari baru di Epidemic").
71 SFX Epidemic Sound: 61 dari koleksi `D:\Sound\Sound Effect` (sudah dipotong satu bunyi) + 10 unduhan baru untuk celah yang belum ada
(hantaman bersih/gelap, glitch pendek, koin, lampu neon, saklar, roda/kaset berputar, sapuan rendah, angin).

## Isi folder
```
sfx/
  katalog.json   nama → berkas, judul Epidemic asli, kapan dipakai, durasi, puncak (detik), keras; + peta bawaan mesin
  transisi/  muncul/  kertas/  ui/  angka/  tekanan/  latar/
```
- **Nama** = nama berkas tanpa `.mp3` (huruf kecil + tanda hubung), itu yang ditulis di konfig: `berkas: 'hit-bersih'`.
  Judul Epidemic lama (`'Swooshes, Whoosh, Soft, Clean'`) juga masih diterima.
- **Dirapikan 28 Nov 2026**: hening di depan dipotong, ekor dipudarkan 30 ms, keras disamakan per kategori
  (RMS maks: transisi −14, muncul/kertas/angka −16, ui −17, tekanan −9, latar −20 dBFS), puncak ≤ −1 dBFS (dulu 7 berkas lewat 0 dBFS).
  Berkas asli sebelum dirapikan: `C:\Users\ASUS\.claude\skills-cadangan\sfx-asli-2026-11-27\`.
- Audio tidak masuk git (`.gitignore`); yang di-commit hanya `README.md` + `katalog.json`.

## Otomatis di mesin (tanpa menulis apa pun)
`jalankan.py rakit` menemukan folder ini sendiri (`D:\automation\Skill-Video-Editing-Rizky\sfx`, lalu salinan terpasang
`~/.claude/skills/skill-edit-rizky/sfx`) dan:
1. **mengganti semua bunyi sintesis bawaan** (whoosh, swish, kertas, stempel, gulir, spidol, ketik, pop, kamera, glitch, boom/kilau, riser/cahaya, …)
   dengan berkas pustaka (kolom "Bawaan untuk"); perpindahan Kolase 1.5 punya bunyi sendiri: `sapu` → `whoosh-rendah`,
   `portal` → `whoosh-angin`, `lepas` → `kertas-geser`;
2. **meletakkan puncak bunyi tepat di kejadian**: whoosh/swish memuncak di titik potong perpindahan, hantaman/pop tepat saat lapisan muncul/mendarat
   (memakai `puncak` di katalog); bunyi berdurasi (gulir, spidol, ketik, loop) tetap mulai di awal kejadian dan dipotong sepanjang kejadiannya;
3. menanam **hanya yang dipakai** (peta bawaan ±1 MB + nama yang ditulis di konfig).

Matikan/ganti: `sfxPeta: { whoosh: 'whoosh-keras', 'masuk.sapu': 'swish' }` (per kunci), `sfxPeta: false` (bunyi sintesis lama),
`rakit --tanpa-pustaka-sfx`.

**Setiap teks/ikon yang muncul berbunyi cocok** (aturan pengguna 28 Nov 2026: "di setiap animasi baik teks atau icon yang muncul harus ada sfx-nya yang cocok"): otomatis, tanpa ditulis di konfig. Bunyinya dipilih dari jenis lapisan + gaya teks/animasi + gaya masuk (kata meluncur → `swish-cambuk`, angka/tahun jatuh → `pop-plop`, judul stiker → `stiker-lepas`, label/keterangan → `klik-ping`, teks ketik → `ketik-pendek` sepanjang ketikan, tulisan tangan → `pensil-coret`, ikon kecil → `ikon-kaca`, potongan → `pop-pencet`, foto/kartu → `foto-meluncur`, dokumen → `kertas-geser`, balon → `kartu-gelembung`, grafik → `slide-grafis`, HP/TV → `jendela-buka`, notifikasi → `notif-pesan`, cap → `stempel`, coretan → spidol/pensil, terbang dari lensa → `whoosh-mendarat`; aturan lengkap di `sfx/katalog.json` → `muncul`). Puncaknya jatuh saat lapisan tiba, nadanya sedikit beda tiap kemunculan, 5–10 dB di bawah narasi; yang muncul bersamaan digeser 0,07 dtk, yang jatuh di puncak perpindahan dilunakkan. `bunyi: '<nama>'` per lapisan untuk pilihan sendiri; `sfx: false` hanya untuk keheningan yang disengaja (cek memberi saran).
Ubah pilihannya di `katalog.json` → `muncul` (kunci paling khusus dulu: `teks.anim.<anim>` › `teks.<gaya>` › `masuk.<gaya masuk>` › `teks`; gambar `masuk.<gaya>` › `gambar.ikon|potongan|foto|pelat`; benda `benda.<jenis>`; coret `coret.<bentuk>`), lalu `pustaka_sfx.py cek`. Mati: `bunyiMuncul: false`. SFX khusus satu video tetap bisa: `rakit --sfx _kerja/audio/sfx` (menang atas pustaka bila namanya sama).

## Menulis bunyi pilihan
```js
// di lapisan (mengganti bunyi bawaannya); puncak otomatis di saat lapisan muncul
{ teks: 'BUKTI', gaya: 'stiker', t: 'L03.w2', bunyi: 'whoosh-mendarat' }
{ gambar: 'foto-arsip', x: 540, y: 900, lebar: 600, t: 'L04.w1', bunyi: { berkas: 'foto-meluncur', vol: .7 } }
{ coret: 'silang', x: 540, y: 340, lebar: 720, tinggi: 150, t: 'L04.w5', bunyi: 'salah-buzz' }
{ gambar: 'ikon-kecil', x: 300, y: 830, lebar: 170, sfx: false }            // lapisan tanpa bunyi

// di adegan, tepat di kata narasi; puncak: true = puncak berkas jatuh tepat di t
sfx: [{ t: 'L06.w4', berkas: 'palu-sidang', vol: .9, puncak: true }]
sfx: [{ t: 'L02.w1', berkas: 'hit-bersih', puncak: true }, { t: 'L02.w1-1.8', berkas: 'riser-cepat', vol: .6 }]

// elemen hidup (Kolase 1.5): bunyi latar berulang selama benda bergerak
sfx: [{ t: 0, berkas: 'kaset-putar-loop', ulang: true, lama: 3.2, vol: .35 },        // roda kaset berputar
      { t: 'L05.w2', berkas: 'saklar-lampu', puncak: true },                        // lampu (elemen terang) menyala
      { t: 'L05.w2', berkas: 'neon-menyala', lama: 2.5, vol: .4 }]                    // layar/neon berkedip lalu berdengung
```
Aturan main: satu bunyi pilihan per kejadian (jangan ditumpuk dengan bawaannya); whoosh dimulai sebelum potongan (otomatis dari `puncak`);
hantaman tepat di bingkai mendarat; bunyi latar loop pelan (vol .25–.4) dan berhenti bersama bendanya; tidak semua teks perlu bunyi.

## Bila tidak ada yang cocok → cari di Epidemic, lalu tambahkan ke pustaka
1. `python -X utf8 scripts/pustaka_sfx.py lihat <kata>` (mis. `lihat kertas`, `lihat angin`) — pastikan memang belum ada.
2. Cari lewat konektor Epidemic (`SearchSoundEffects`), unduh pratinjau `lqmp3Url` dulu untuk melihat bentuk bunyinya
   (puncak di awal untuk hantaman, naik-turun untuk whoosh, rata untuk loop), lalu `DownloadSoundEffect` MP3 → curl ke folder kosong baru.
3. `python -X utf8 scripts/pustaka_sfx.py tambah "<unduhan>.mp3" --kategori <kategori> --nama <nama-pendek> --kapan "<kapan dipakai>" [--loop] [--potong 0 3] [--peta <jenis>]`
   → dipotong, disamakan kerasnya, disimpan di kategori, dicatat di `katalog.json` (judul Epidemic asli ikut tercatat).
4. `python -X utf8 scripts/pustaka_sfx.py cek` (harus BERES), lalu `pasang.ps1` supaya salinan terpasang ikut.

## Daftar per kategori (dibuat dari katalog.json)

### Transisi (perpindahan adegan, gerak cepat) — `transisi/`

| Nama (`berkas`) | Dtk | Puncak | Kapan dipakai | Bawaan untuk |
|---|---|---|---|---|
| `glitch-panjang` | 1,82 | 1,47 | glitch 1,9 dtk: berita/teknologi rusak, pakai dengan geser | — |
| `glitch-pendek` **baru** | 0,53 | 0,12 | perpindahan/efek glitch singkat (bawaan glitch) | `glitch` |
| `kilat-flash` | 1,47 | 0,1 | kilat putih | — |
| `mengecil` | 0,29 | 0,26 | lapisan mengecil/keluar | — |
| `piringan-mundur` | 1,22 | 0,29 | kilas balik, putar ulang | — |
| `putar-membesar` | 0,35 | 0,3 | lapisan membesar/berputar masuk | — |
| `riser-cepat` | 2,15 | 2,05 | build-up sebelum payoff, efek cahaya (bawaan riser) | `riser` |
| `slide-grafis` | 0,16 | 0,08 | elemen motion graphic meluncur | — |
| `swipe-panel` | 0,13 | 0,07 | panel/kartu digeser | — |
| `swish` | 0,54 | 0,21 | sentak/fokus/geser/lempar/strip (bawaan swish) | `swish` |
| `swish-cambuk` | 0,12 | 0,03 | sentak sangat cepat | — |
| `whoosh-angin` **baru** | 1,46 | 0,39 | masuk lewat jendela/pintu (bawaan portal), alam, ketinggian | `masuk.portal` |
| `whoosh-keras` | 0,86 | 0,51 | perpindahan keras, momen besar | — |
| `whoosh-lembut` | 1,92 | 0,77 | perpindahan dorong/tarik/putar/zoom/iris/lubang (bawaan whoosh) | `whoosh` |
| `whoosh-mendarat` | 0,91 | 0,23 | judul/kartu mendarat lembut | — |
| `whoosh-rendah` **baru** | 1,38 | 0,29 | benda gelap lewat dekat lensa (bawaan sapu) | `masuk.sapu` |
| `zoom-lensa` | 0,96 | 0,2 | kamera mendekat ke detail | — |

### Muncul (teks, ikon, kartu) — `muncul/`

| Nama (`berkas`) | Dtk | Puncak | Kapan dipakai | Bawaan untuk |
|---|---|---|---|---|
| `ikon-kaca` | 0,16 | 0,01 | gambar/ikon muncul (bunyiMuncul gambar) | `muncul.gambar` |
| `kartu-gelembung` | 0,25 | 0,03 | kartu/benda muncul (bunyiMuncul benda) | `muncul.benda` |
| `pesan-tips` | 0,83 | 0,18 | kotak tips/pesan muncul | — |
| `pop-pencet` | 0,35 | 0,26 | benda/stiker kecil muncul (bawaan pop) | `pop` |
| `pop-plop` | 0,08 | 0,03 | pop per kata, sangat pendek | — |
| `teks-muncul` | 0,24 | 0,15 | teks/judul muncul (bunyiMuncul teks) | `muncul.teks` |

### Kertas, kolase, arsip, dokumen — `kertas/`

| Nama (`berkas`) | Dtk | Puncak | Kapan dipakai | Bawaan untuk |
|---|---|---|---|---|
| `amplop-buka` | 0,47 | 0,23 | amplop/berkas dibuka | — |
| `foto-meluncur` | 0,5 | 0,12 | foto meluncur di meja | — |
| `halaman-dibalik` | 0,54 | 0,1 | halaman/dokumen dibalik | — |
| `kamera-jepret` | 0,25 | 0,07 | foto muncul, jepret (bawaan kamera/kilat) | `kamera` |
| `kartu-dibalik` | 0,78 | 0,48 | kartu/foto dibalik | — |
| `kertas-geser` | 1,5 | 0,79 | kertas digeser di meja; adegan terangkat (bawaan lepas) | `masuk.lepas` |
| `kertas-masuk` | 0,8 | 0,33 | kertas/kartu masuk, panel tutup/buka/kartu (bawaan kertas) | `kertas` |
| `kertas-sobek` | 0,92 | 0,65 | kertas disobek | — |
| `palu-sidang` | 0,5 | 0,01 | putusan, palu diketuk | — |
| `pensil-coret` | 1,14 | 0,09 | kata dicoret, tulisan tangan | — |
| `selotip-sobek` | 0,54 | 0,2 | foto ditempel selotip | — |
| `spidol-lingkar` | 2,48 | 1,09 | lingkaran/stabilo/coretan spidol (bawaan spidol, bunyiMuncul coret) | `spidol`, `muncul.coret` |
| `stempel` | 0,2 | 0,01 | cap/stempel (bawaan stempel) | `stempel` |
| `stiker-lepas` | 0,79 | 0,09 | stiker ditempel/dilepas | — |

### UI, HP, chat AI — `ui/`

| Nama (`berkas`) | Dtk | Puncak | Kapan dipakai | Bawaan untuk |
|---|---|---|---|---|
| `berhasil` | 0,76 | 0,14 | jawaban benar / berhasil (bawaan benar) | `benar` |
| `error-glitch` | 0,23 | 0,17 | error digital | — |
| `hud-muncul` | 0,56 | 0,24 | HUD/dasbor muncul | — |
| `jendela-buka` | 0,26 | 0,03 | jendela digital terbuka | — |
| `jendela-tutup` | 0,23 | 0,15 | jendela digital tertutup | — |
| `ketik-hp` | 4,04 | 0,84 | keyboard HP / chat AI | — |
| `ketik-panjang` | 2,18 | 0,07 | ketik panjang di keyboard | — |
| `ketik-pendek` | 1,06 | 0,38 | teks diketik singkat, papan kapur (bawaan ketik) | `ketik` |
| `klik` | 0,11 | 0,01 | kursor klik (bawaan klik) | `klik` |
| `klik-kembali` | 0,53 | 0,01 | tombol kembali | — |
| `klik-konfirmasi` | 0,53 | 0,01 | tombol ditekan / konfirmasi | — |
| `klik-ping` | 0,43 | 0,01 | opsi dipilih | — |
| `menu-buka` | 0,6 | 0,42 | menu/panel terbuka | — |
| `menu-tutup` | 0,2 | 0,01 | menu/panel tertutup | — |
| `notif-pesan` | 0,21 | 0,01 | pesan/notifikasi masuk (bawaan notif) | `notif` |
| `salah-buzz` | 0,42 | 0,33 | jawaban salah (bawaan salah) | `salah` |

### Angka, uang, waktu — `angka/`

| Nama (`berkas`) | Dtk | Puncak | Kapan dipakai | Bawaan untuk |
|---|---|---|---|---|
| `angka-gulir` | 3,63 | 1,98 | angka bergulir naik (bawaan gulir) | `gulir` |
| `ding-kilau` | 1,92 | 0,03 | kata/angka kunci menyala (bawaan ding) | `ding` |
| `jam-detik` | 0,21 | 0,06 | satu detik jam (bawaan tik) | `tik` |
| `kaching` | 1,63 | 0,38 | uang, harga (bawaan kaching) | `kaching` |
| `koin` **baru** | 1,08 | 0,14 | koin jatuh, recehan, partikel koin (bawaan koin) | `koin` |

### Penekanan dan tegang — `tekanan/`

| Nama (`berkas`) | Dtk | Puncak | Kapan dipakai | Bawaan untuk |
|---|---|---|---|---|
| `bass-turun` | 2,3 | 0,01 | drop bass sebelum fakta mengejutkan (bawaan sub) | `sub` |
| `boom-dalam` | 2,54 | 0,12 | puncak besar, efek kilau (bawaan boom) | `boom` |
| `dengung-naik` | 2,37 | 1,2 | BUKAN hantaman: dengung tebal yang naik 0,5 dtk lalu tertahan; latar tegang di bawah kalimat berat | — |
| `detak-jantung` | 1,7 | 1,26 | tegang, dua detak (bawaan jantung) | `jantung` |
| `dum-rendah` | 2,98 | 0,03 | hantaman rendah, benda mendarat (bawaan dum, ketukan) | `dum`, `ketukan` |
| `hit-bersih` **baru** | 2,83 | 0,06 | hantaman bersih di kata kunci (bawaan impact) | `impact` |
| `hit-gelap` **baru** | 1,5 | 0,11 | hantaman gelap: misteri, kriminal, horor | — |
| `kilau-kristal` | 0,85 | 0,1 | kilau halus, benda berkilap, ide muncul | — |

### Latar dan elemen hidup (loop, lampu, mesin) — `latar/`

| Nama (`berkas`) | Dtk | Puncak | Kapan dipakai | Bawaan untuk |
|---|---|---|---|---|
| `kaset-putar-loop` **baru** | 4,0 | 2,31 | kaset/pita/mesin berputar (elemen putaran; ulang: true) | — |
| `neon-menyala` **baru** | 4,82 | 1,4 | lampu neon/layar menyala berkedip lalu berdengung (elemen kedip/terang) | — |
| `proyektor-loop` | 7,0 | 0,2 | arsip film lama, bunyi latar (bawaan proyektor; ulang: true) | `proyektor` |
| `putar-klik-loop` **baru** | 4,0 | 3,38 | roda/gir/kipas/jarum berputar (elemen putaran; ulang: true) | — |
| `saklar-lampu` **baru** | 0,15 | 0,01 | saklar: lampu menyala/padam, efek kerucut/jendela muncul | — |

_"Puncak" = detik puncak bunyi di dalam berkas (dipakai mesin untuk menyelaraskan). **baru** = unduhan Epidemic 28 Nov 2026. `dengung-naik` (dulu "Cinematic Hit, Impact, Absolute Clean 04") ternyata dengung tebal yang tertahan, bukan hantaman; hantaman bersih sekarang `hit-bersih`._
