# Komposisi dan staging: ke mana mata harus melihat

> VISUAL · dipakai di langkah 6 (storyboard + shot), 9, 14, 15 · terkait: `metafora.md`, `../core/editing.md` §11, `../cinematic/kamera.md`, `../type/tipografi-kinetik.md`, `../style/gaya-visual.md`

Prinsip inti:
1. **Satu titik fokus per bingkai.** Penonton harus tahu ke mana melihat dalam 0,3 dtk; kalau ada dua yang sama kuat, keduanya kalah.
2. **Hierarki dibuat dengan perbedaan**: ukuran, kontras, warna aksen, ketajaman, gerak. Unsur utama menang di minimal dua dari lima.
3. **Ruang kosong adalah unsur.** Ruang kosong memberi tempat teks, memberi bobot pada subjek, dan membuat video terasa mahal.
4. **Kedalaman membuat foto diam terasa ruang.** Depan, tengah, belakang yang bergerak beda kecepatan = parallax = hidup.
5. **9:16 punya area mati.** Tombol, caption, dan nama akun menutupi tepi kanan dan bawah; isi penting tidak boleh di sana.

---

## 1. Sepertiga vs tengah editorial
- **Kapan**: sepertiga untuk adegan bercerita (tempat + tokoh + ruang teks); tengah untuk hook, payoff, tokoh berbicara ke kamera, benda pahlawan, gaya editorial/minimal.
- **Kenapa**: komposisi tengah paling cepat dibaca di layar HP dan terasa tegas/simetris; sepertiga memberi arah dan ruang untuk teks atau gerak.
- **Cara**: 9:16 = 1080×1920. Garis sepertiga vertikal x 360/720, horizontal y 640/1280. Subjek sepertiga: mata di y ±640, ruang teks di sepertiga lain. Tengah editorial: subjek x 540, teks besar di atas (15–45% tinggi), ruang kosong simetris; patahkan simetri dengan satu unsur miring 2–4° supaya tidak kaku.
- **Hindari**: subjek tepat di tengah tanpa alasan di adegan konteks (terasa pas foto); semua adegan memakai komposisi yang sama.
- **Di mesin Kolase**: `x`, `y` lapisan; teks judul di `y` 288–864; `putar` kecil pada benda bertulisan (`gaya.md` §7).

## 2. Hierarki visual
- **Kapan**: setiap bingkai, terutama yang memuat teks + gambar + benda.
- **Kenapa**: tanpa hierarki, mata melompat-lompat dan informasi tidak masuk.
- **Cara**: susun 3 tingkat: **utama** (1 unsur, ukuran terbesar, kontras tertinggi, warna aksen, tajam), **pendukung** (1 unsur, 40–60% ukuran utama, tanpa aksen), **tekstur** (latar, label kecil, partikel; kontras rendah, boleh blur). Warna aksen hanya pada unsur utama atau kata kunci.
- **Hindari**: dua unsur sama besar dan sama terang; warna aksen di banyak tempat; teks pendukung lebih tebal dari teks utama.
- **Di mesin Kolase**: satu kata `*aksen*` per baris teks; latar `blur` 4–10 px atau `z` kecil; dua warna aksen per video (`palet`).
- **Di editor lain**: uji dengan memburamkan layar 10 px; yang masih terbaca = unsur utama.

## 3. Ruang kosong (negative space)
- **Kapan**: gaya editorial, minimal, luxury; adegan emosi; ruang napas.
- **Kenapa**: ruang kosong menaikkan bobot subjek dan memberi kesan sengaja/mahal; kepadatan terus-menerus terasa murahan.
- **Cara**: 30–50% bingkai kosong (latar polos, gradasi, langit, dinding) di adegan berbobot; subjek kecil di ruang besar untuk isolasi/skala. Pelat Flow dibuat dengan **ruang kosong di sepertiga atas** untuk judul (`flow.md` §1).
- **Hindari**: mengisi ruang kosong dengan partikel/ikon karena "terlalu sepi".
- **Di mesin Kolase**: latar `pola: 'polos'`/`'editorial'`, `kamera: 'mundur'` untuk memperbesar ruang kosong.

## 4. Kontras skala
- **Kapan**: membandingkan, menekankan, atau membuat bingkai lebih dramatis.
- **Kenapa**: perbedaan ukuran adalah cara tercepat menunjukkan mana yang penting dan seberapa besar sesuatu.
- **Cara**: rasio utama:pendukung minimal 3:1 untuk hierarki tegas; tipografi raksasa (melebihi 70% lebar bingkai) di samping objek kecil; tokoh kecil di depan benda raksasa untuk skala.
- **Hindari**: semua unsur ukuran sedang.
- **Di mesin Kolase**: `lebar`/`skala` lapisan, `^kata^` (1,5×) dan `~kata~` di teks, `gaya: 'padat'` untuk angka raksasa.

## 5. Garis pengarah (leading lines)
- **Kapan**: mengarahkan mata ke subjek, angka, atau ke arah adegan berikutnya.
- **Kenapa**: mata mengikuti garis, tatapan, dan arah tunjuk tanpa sadar.
- **Cara**: jalan, rel, lengan menunjuk, arah pandang tokoh, berkas cahaya, panah coretan; semua mengarah ke unsur utama atau ke titik perpindahan berikutnya. Beri **ruang pandang** (lead room): tokoh menghadap kanan diletakkan di kiri.
- **Hindari**: garis yang membawa mata keluar bingkai tanpa alasan; tokoh menatap tepi terdekat.
- **Di mesin Kolase**: `coret: 'panah'`, `efek: { jenis: 'berkas', titik, sudut }`, `efek: sorot`, tokoh `aset/raka-3d/tokoh-tunjuk.png` dengan `balik` untuk arah.

## 6. Kedalaman: depan · tengah · belakang
- **Kapan**: hampir setiap adegan foto/kolase; wajib bila kamera bergerak.
- **Kenapa**: tiga bidang yang bergerak beda kecepatan membuat gambar diam terasa ruang 3D (parallax) dan membuat perpindahan bermomentum terasa melesat.
- **Cara**: **belakang** = pelat/tempat (kontras rendah, boleh sedikit blur); **tengah** = subjek (tajam, berbayangan); **depan** = benda dekat lensa (tangan, mik, kepala penonton, daun, bingkai pintu; besar, kabur, gelap, sebagian keluar bingkai). Depan hanya 1 benda, menutupi ≤ 20% bingkai, tidak menutupi wajah/teks.
- **Hindari**: lapisan depan tajam dan terang (bersaing dengan subjek); terlalu banyak bidang (> 4) yang membuat kacau.
- **Di mesin Kolase**: `z` mengatur parallax: latar pola `0`, pelat penuh `.3` (bawaan), subjek `1`, depan `1.6–2.4`; kerumunan bertingkat `.8 · 1.3 · 1.9` (`gaya.md` §4a). Lapisan depan `blur` 6–14 px, `jangkar` ke tepi bila terpotong. Teknik kamera: `../cinematic/kamera.md`.

## 7. Zona aman 9:16
- **Kapan**: setiap teks, angka, wajah, dan detail penting.
- **Kenapa**: antarmuka TikTok/Reels/Shorts menutupi kanan bawah (tombol suka/komentar/bagikan) dan bawah (caption, nama akun, musik).
- **Cara** (1080×1920):

| Area | Piksel | Aturan |
|---|---|---|
| Atas mati | y < 154 (8%) | tidak ada teks; jam/status HP |
| Zona judul | y 288–864 (15–45%) | teks utama, judul, angka |
| Zona isi | y 154–1344 (8–70%), x 54–940 | semua teks dan detail penting |
| Kolom tombol | x > 940, y > 806 (kanan, di bawah 42%) | tidak ada teks/wajah/angka |
| Bawah mati | y > 1459 (76%) | caption platform; hanya latar/tekstur |
- **Hindari**: angka penting di sepertiga bawah; wajah tokoh di kanan bawah; teks yang menyentuh tepi kiri < 54 px.
- **Di mesin Kolase**: `ZONA` mesin (atas 8%, bawah 70%, kiri 5%, kanan 87%); `cek` menolak teks di area tombol/keluar layar; teks di dalam benda `kustom` **tidak** dicek, jaga sendiri (`mesin.md` benda kustom). 16:9: atas 5%, bawah 80%.

## 8. Teks di belakang subjek
- **Kapan**: judul hook, nama tempat/tokoh, kata besar editorial.
- **Kenapa**: teks yang terselip di antara lapisan terasa ada di ruang yang sama dengan subjek; tanda khas gaya editorial modern.
- **Cara**: urutan lapisan latar → teks besar → potongan subjek; subjek menutupi ≤ 25–30% huruf dan tidak menutupi huruf pertama kata kunci; teks tetap terbaca dalam 0,5 dtk.
- **Hindari**: subjek menutupi angka (angka harus utuh); dipakai di setiap adegan (jadi gimik).
- **Di mesin Kolase**: urutan `lapis` menentukan tumpukan: pelat, lalu `{ teks, gaya: 'padat' }`, lalu `{ gambar: 'tokoh', z: 1.2 }` (`gaya.md` §4a "teks di antara lapisan"). Potongan harus bersih tepinya (`flow.md` §5).

## 9. Jejak mata antar-potongan (eye-trace)
- **Kapan**: setiap potongan, terutama di montase dan potongan cepat.
- **Kenapa**: bila subjek bidikan B berada di tempat mata penonton berakhir di bidikan A, potongan terasa mulus walau isinya berbeda; bila jauh, potongan terasa menyentak.
- **Cara**: catat titik fokus akhir A; letakkan subjek B dalam jarak ±1/3 bingkai dari titik itu untuk potongan halus. Untuk kejutan, sengaja lompat ke sisi berlawanan (dipadukan whip/sentak). Gerak keluar A ke kanan → subjek B masuk dari kiri atau berada di kanan.
- **Hindari**: lompatan fokus kiri-kanan bergantian di montase cepat (melelahkan).
- **Di mesin Kolase**: `titikMasuk` = titik fokus di adegan lama (`dorong`/`tarik`/`iris`); `cocok` menjaga benda di jalurnya; `arahMasuk` searah gerak keluar. Lihat `../motion/transisi.md`.

## 10. Jumlah unsur per bingkai
- **Kapan**: menilai lembar kontak.
- **Kenapa**: unsur berlebih adalah tanda paling cepat video terlihat seperti templat/AI (`../polish/qc.md` §6).
- **Cara**: maksimal **5 unit**: 1 utama + 1 pendukung + ≤ 3 tekstur/label. Teks: ≤ 2 blok sekaligus, ≤ 7 kata total. Warna aksen ≤ 2 per video. Efek berlangsung ≤ 1 per bingkai (partikel ATAU bokeh ATAU kabut).
- **Hindari**: ikon + teks + stiker + partikel + garis + label bersamaan.
- **Di mesin Kolase**: lapisan lama diberi `akhir`/`keluar` sebelum yang baru menumpuk; efek 1–2 per adegan (`klip.md` §4).

## 11. Staging per jenis beat
| Beat | Komposisi | Kamera | Unsur | Hindari |
|---|---|---|---|---|
| Hook | tengah, dekat, subjek besar + teks besar, kontras tinggi | sudah bergerak di bingkai 0 (`dorong-kuat`, `terbang`) | ≤ 3 unit | latar ramai, subjek kecil |
| Konteks | lebar, tempat terbaca, subjek di sepertiga, ruang teks atas | pelan (`dorong`, `kiri`/`kanan`) | tempat + subjek + 1 label | close-up tanpa tempat |
| Data/angka | angka dominan (≥ 3× pendukung), benda bukti di sampingnya | stabil/pelan supaya angka terbaca | 1 angka + 1 benda + sumber kecil | dua angka bersaing |
| Ketegangan | rapat, subjek dekat tepi, miring 1–3°, vinyet gelap | `guling`, `dorong` makin cepat | sedikit, gelap | terang dan simetris |
| Emosi | close-up atau subjek kecil di ruang besar, ruang kosong ≥ 40% | `tenang`, napas | 1–2 unit | teks banyak, SFX ramai |
| Payoff | tengah/simetris, cahaya pahlawan (sorot/kilau), ditahan | melambat lalu diam-hidup (`tenang`) | benda payoff + 1 kalimat | unsur baru yang belum ditanam |
| Loop | sama dengan bingkai hook | berakhir di keadaan kamera adegan 1 | sama dengan hook | fade ke hitam |

## 12. Bobot dan arah
- **Kapan**: menata gerak masuk dan posisi tokoh.
- **Kenapa**: penonton Indonesia membaca kiri ke kanan; gerak ke kanan terasa maju/masa depan, ke kiri terasa mundur/masa lalu; bawah terasa berat, atas ringan.
- **Cara**: kronologi maju = gerak/perpindahan ke kanan (`arahMasuk: 'kanan'` berarti adegan baru datang dari kanan, kamera bergerak ke kanan); kilas balik = ke kiri; penurunan/krisis = jatuh ke bawah; harapan = naik.
- **Hindari**: arah acak antar-adegan dalam satu babak.

## 13. Bingkai di dalam bingkai
- **Kapan**: arsip (foto di koran, layar TV), UI (layar HP), menandai "ini bukti", atau memindahkan adegan jadi benda.
- **Kenapa**: bingkai kedua memfokuskan mata dan memberi lapisan makna ("ini rekaman", "ini kenangan", "ini yang dilihat tokoh").
- **Cara**: bingkai dalam menempati 45–70% lebar layar, miring 1–4°, berbayangan; isi bingkai lebih terang/kontras dari sekelilingnya; beri label kecil (sumber/tanggal) di bawahnya.
- **Hindari**: bingkai di dalam bingkai di dalam bingkai tanpa alasan; bingkai terlalu kecil sehingga isinya tak terbaca.
- **Di mesin Kolase**: `benda: kartu`/`tv`/`hp`/`koran { foto }`, `masuk: 'bingkai'` (adegan lama jadi foto/layar di adegan baru), `bayangan: true`, label kredit `gaya: 'label'`.

## 14. Simetri dan asimetri
- **Kapan**: simetri untuk otoritas, payoff, kemewahan, ketegangan dingin; asimetri untuk gerak, cerita, dan rasa alami.
- **Kenapa**: simetri terasa disengaja dan stabil; asimetri terasa hidup. Simetri sempurna di setiap bingkai terasa seperti templat.
- **Cara**: simetri: subjek di x 540, unsur pendukung berpasangan; asimetri: berat visual 60/40, satu unsur besar diimbangi ruang kosong. Selingi: maksimal 2 adegan simetris berurutan.
- **Hindari**: simetri yang "hampir" (subjek meleset 20–40 px dari tengah terlihat seperti kesalahan, bukan pilihan).

## Cek cepat
- Tiap bingkai lembar kontak punya satu unsur utama yang jelas (uji blur).
- Tidak ada teks/angka/wajah di kolom tombol kanan bawah atau di bawah 70% tinggi.
- Maksimal 5 unit dan 2 blok teks per bingkai.
- Adegan dengan kamera bergerak punya ≥ 2 bidang kedalaman (`z` berbeda).
- Lapisan depan kabur dan tidak menutupi wajah/teks.
- Subjek bidikan berikut berada dekat titik fokus akhir bidikan sebelumnya (kecuali potongan kejutan).
- Komposisi berganti mengikuti jenis beat (tidak semua tengah, tidak semua sepertiga).

## Celah mesin
- **Uji hierarki otomatis** belum ada: usulan `cek` menghitung jumlah lapisan aktif per bingkai dan memberi saran bila > 6 unsur atau > 2 blok teks.
- **Zona aman benda `kustom`** tidak dicek: usulan `K.zona` (kotak aman) dan pendaftaran teks kustom ke `cek` lewat `K.catatTeks`.
- **Fokus kedalaman otomatis** (blur sesuai `z` jauh dari bidang fokus) belum ada; sekarang `blur` ditulis manual per lapisan. Usulan: `KONFIG.fokus: { z: 1, kuat }` → blur otomatis lapisan jauh/dekat.

## Teknik modern
- **Teks di belakang subjek (depth-sorted type)** · manfaat: tampilan editorial 3D tanpa render 3D · kapan: hook, judul tempat/tokoh · cara: potongan subjek bersih dari Flow/`ambil_media.py --potong`, urutan lapis latar → teks → subjek (§8).
- **Komposisi "UI-aware"** · manfaat: tidak ada informasi tertutup tombol platform · kapan: semua 9:16 · cara: pakai tabel §7 saat menulis `x/y`, cek lembar kontak dengan bingkai tombol di kepala.
