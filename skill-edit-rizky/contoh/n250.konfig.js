const KONFIG = {
  judul: 'Indonesia Pernah Bikin Pesawat Sendiri',
  rasio: '9:16', fps: 30,
  durasiTarget: [35, 60],
  tema: 'arsip', // sejarah 1990-an: kertas krem, tint hangat, halftone (gaya.md §0)
  musik: { sintesis: 'dokumenter', bpm: 84, kunci: 98, vol: .42 },
  thumbnail: { t: 'L03.w3' },
  sumber: [
    { fakta: 'Terbang perdana 10 Agustus 1995; 50 penumpang; 2 prototipe; PA-2 terbang 19 Des 1996; uji terbang ±separuh dari ±1.400 jam; IMF (paket US$43 miliar); PA-1 di Museum Dirgantara Mandala', url: 'https://en.wikipedia.org/wiki/IPTN_N250' },
    { fakta: 'Terbang perdana 55 menit; 50 penumpang; fly by wire', url: 'https://rri.co.id/sudut-pandang/1954506/berkaca-pada-gatotkaca' },
    { fakta: 'LoI IMF 15 Januari 1998; IMF minta pendanaan IPTN dihentikan; fly-by-wire pertama di kelasnya', url: 'https://www.goodnewsfromindonesia.id/2026/05/25/n-250-dikubur-rupiah-diselamatkan-pengorbanan-terbesar-bj-habibie' },
    { fakta: 'Januari 1998 IMF meminta pemerintah berhenti membiayai IPTN, paket US$43 miliar', url: 'https://www.globalsecurity.org/military/world/indonesia/n250.htm' }
  ]
};

const ADEGAN = [
  // ── babak 1: dunia yang dikenal → pembalik
  { id: 'kini', mulai: 0, akhir: 'L02', kamera: 'dorong-kuat',
    lapis: [
      { gambar: 'bandara-kini' },
      { teks: 'Pesawat mudikmu?', gaya: 'stiker', ukuran: 58, y: 300, putar: -3, masuk: 'pop', t: .15 },
      { teks: 'buatan *luar negeri*', gaya: 'judul', ukuran: 96, y: 470, lebar: 820, anim: 'luncur', t: 'L01.w8', ikut: true }
    ] },
  { id: 'tahun', mulai: 'L02', akhir: 'L02.w5', masuk: 'sentak', arahMasuk: 'bawah', latar: { pola: 'grid', warna: '#1d3f9e', putar: 2 }, kamera: 'guling',
    lapis: [
      { gambar: 'awan', x: 900, y: 1500, lebar: 560, z: 1.8, alfa: .9, hidup: 10, gerak: [[0, { x: 1020 }], [2.5, { x: 820 }]] },
      { teks: 'padahal', gaya: 'judul', ukuran: 64, y: 520, anim: 'luncur', t: 0 },
      { teks: '1995', gaya: 'padat', ukuran: 300, y: 820, anim: 'jatuh', t: 'L02.w3-0.15', tiap: .07 }
    ] },
  { id: 'koran', mulai: 'L02.w5', akhir: 'L03', masuk: 'tutup', arahMasuk: 'bawah', latar: { pola: 'kertas', warna: '#4a3220', tua: 1 }, kamera: [[0, { zoom: 1.0, y: 80 }], [3, { zoom: 1.2, y: -20 }, 'inOutSine']],
    lapis: [
      { benda: { jenis: 'koran', nama: 'HARIAN NUSANTARA', tanggal: 'Jumat, 11 Agustus 1995', judul: 'N250 Gatotkaca Mengudara', sub: 'Pesawat rancangan IPTN terbang perdana 55 menit di Bandung', foto: 'n250-lepas', tinggiFoto: .62, lebar: 780,
          isi: 'Pesawat N250 Gatotkaca buatan IPTN terbang perdana di Bandung pada 10 Agustus 1995 selama 55 menit. Pesawat baling-baling berkapasitas 50 penumpang ini memakai kendali fly by wire, yang pertama di kelasnya.',
          sorot: [{ baris: 'judul', t: 'L02.w8', lama: .5 }] }, y: 900, putar: -2.5, bayangan: true, hidup: 3 },
      { gambar: 'tangan-pena', x: 960, y: 1500, lebar: 520, putar: -20, z: 1.6, masuk: { gaya: 'geser', dari: 'kanan' }, t: .5, bayangan: true, sfx: false }
    ] },
  // ── babak 2: pengenalan + 3 fakta
  { id: 'hangar', mulai: 'L03', akhir: 'L03.w4', masuk: 'dorong', titikMasuk: [540, 900], kamera: 'naik',
    lapis: [
      { gambar: 'hangar-luar' },
      { teks: 'N250 ^Gatotkaca^', gaya: 'judul', ukuran: 86, y: 360, lebar: 840, anim: 'pop', t: 'L03.w2', besar: 1.35 }
    ] },
  { id: 'rakit', mulai: 'L03.w4', akhir: 'L04', masuk: 'fokus', kamera: 'kiri',
    lapis: [
      { gambar: 'hangar-dalam', z: .5 },
      { gambar: 'insinyur', x: 300, y: 1430, tinggi: 980, z: 1.5, masuk: { gaya: 'terbang', dari: 'kiri' }, t: .05, bayangan: .35,
        rig: ['napas', { jenis: 'goyang', sudut: { amp: 1.2, periode: 4 } }] }, // badan setengah: tepi bawah otomatis ditempel ke tepi layar (jangkar)
      { teks: 'IPTN · Bandung', gaya: 'stiker', ukuran: 62, x: 560, y: 420, putar: -4, masuk: 'pop', t: 'L03.w5' }
    ] },
  { id: 'penonton', mulai: 'L04', akhir: 'L04.w5', masuk: 'sentak', arahMasuk: 'kanan', kamera: 'mundur',
    lapis: [
      { gambar: 'penonton' },
      { teks: '10 Agustus', gaya: 'judul', ukuran: 80, y: 330, anim: 'luncur', t: 'L04', ikut: true },
      { teks: '1995', gaya: 'padat', ukuran: 190, y: 520, anim: 'jatuh', t: 'L04.w3-0.1' }
    ] },
  { id: 'terbang', mulai: 'L04.w5', akhir: 'L05', masuk: 'geser', arahMasuk: 'atas', kamera: [[0, { zoom: 1.05, y: 200 }], [3, { zoom: 1.16, y: -60 }, 'outCubic']],
    efek: [{ jenis: 'kilau', t: 'L04.w8+0.75', lama: .7, kuat: .4, titik: [540, 420], sinar: 10 }], // angka sampai 55: kilau di puncak
    lapis: [
      { gambar: 'n250-lepas', z: .4 },
      { gambar: 'awan', x: 160, y: 1350, lebar: 780, z: 2.2, gerak: [[0, { x: 320 }], [3, { x: -60 }]], alfa: .95 },
      { angka: { dari: 0, ke: 55, lama: 1.1, akhir: ' MENIT' }, gaya: 'padat', ukuran: 170, y: 420, t: 'L04.w8-0.3', aksenBaru: false },
      { teks: 'terbang perdana', gaya: 'label', ukuran: 46, y: 580, masuk: 'naik', t: 'L04.w6' }
    ] },
  { id: 'kabin', mulai: 'L05', akhir: 'L05.w4', masuk: 'dorong', kamera: 'dorong-kuat',
    lapis: [
      { gambar: 'kabin' },
      { angka: { dari: 0, ke: 50, lama: .9 }, gaya: 'padat', ukuran: 260, y: 440, t: 'L05.w2-0.25', aksenBaru: false },
      { teks: 'penumpang', gaya: 'judul', ukuran: 70, y: 640, anim: 'luncur', t: 'L05.w3', ikut: true }
    ] },
  { id: 'blueprint', mulai: 'L05.w4', akhir: 'L06', masuk: 'tarik', latar: { pola: 'grid', warna: '#1f45b5', putar: -1.5 }, kamera: 'dorong',
    lapis: [
      { gambar: 'pesawat', x: 540, y: 960, lebar: 1050, z: 1, hitamPutih: true, campur: 'luminosity', alfa: .35, gerak: [[0, { x: 520 }], [3, { x: 560 }]] },
      { gambar: 'pesawat', x: 540, y: 960, lebar: 980, z: 1.3, masuk: { gaya: 'terbang', dari: 'kiri', skala: 1.1 }, t: .1, bayangan: .5, hidup: 5 },
      { teks: 'fly-by-wire', gaya: 'stiker', ukuran: 64, x: 380, y: 520, putar: -6, masuk: 'pop', t: 'L05.w6' },
      { teks: 'pertama di ^kelasnya^', gaya: 'judul', ukuran: 72, y: 330, lebar: 860, anim: 'luncur', t: 'L05.w10', ikut: true }
    ] },
  { id: 'prototipe', mulai: 'L06', akhir: 'L07', masuk: 'kartu', latar: { pola: 'kertas', warna: '#dccfb1' }, kamera: 'dorong',
    lapis: [
      { benda: { jenis: 'kartu', gambar: 'n250-lepas', keterangan: 'PA-1 · 10 Agustus 1995', lebar: 470, tinggiFoto: 560 }, x: 330, y: 860, putar: -7, bayangan: true, masuk: { gaya: 'lempar', dari: 'kiri' }, t: 0 },
      { benda: { jenis: 'kartu', gambar: 'hangar-dalam', keterangan: 'PA-2 · 19 Desember 1996', lebar: 470, tinggiFoto: 560 }, x: 740, y: 950, putar: 6, bayangan: true, masuk: { gaya: 'lempar', dari: 'kanan' }, t: 'L06.w3' },
      { teks: 'Desember 1996', gaya: 'tahun', ukuran: 92, y: 330, anim: 'luncur', t: 'L06', ikut: true }
    ] },
  // ── babak 3: masalah → konsekuensi
  { id: 'krisis', mulai: 'L07', akhir: 'L08', masuk: 'putar', latar: { pola: 'grid', warna: '#8e1b14', putar: 2.5 }, kamera: 'guling',
    lapis: [
      { teks: 'Tapi lalu, ^krisis^ datang', gaya: 'judul', ukuran: 84, y: 760, lebar: 880, anim: 'luncur', t: 'L07', ikut: true, besar: 1.6 },
      { gambar: 'uang', x: 820, y: 330, lebar: 420, putar: 18, z: 1.7, masuk: { gaya: 'jatuh' }, t: 'L07.w4', bayangan: .5 }
    ] },
  { id: 'antre', mulai: 'L08', akhir: 'L08.w4', masuk: 'kilat', kamera: 'kanan', efek: [{ jenis: 'warna', t: 0, warna: '#a3241a', kuat: .55 }],
    lapis: [
      { gambar: 'antre-bank' },
      { teks: 'Januari 1998', gaya: 'judul', ukuran: 84, y: 360, lebar: 760, anim: 'luncur', t: 'L08', ikut: true }
    ] },
  { id: 'loi', mulai: 'L08.w4', akhir: 'L09', masuk: 'tutup', arahMasuk: 'bawah', latar: { pola: 'kertas', warna: '#3d2a1b', tua: 1 }, kamera: [[0, { zoom: 1.05, y: -40 }], [3.5, { zoom: 1.22, y: 80 }, 'inOutSine']],
    lapis: [
      { benda: { jenis: 'dokumen', kop: 'Catatan', nomor: '15 Jan 1998', judul: 'Indonesia — IMF', lebar: 900, baris: ['Letter of Intent ditandatangani.', 'Paket bantuan: US$43 miliar.', 'Syarat: dana untuk IPTN dihentikan.'],
          sorot: [{ baris: 0, t: 'L08.w5', lama: .5 }, { baris: 1, t: 'L08.w9', lama: .5 }] }, y: 860, putar: 1.5, bayangan: true },
      { gambar: 'tangan-pena', x: 830, y: 760, lebar: 540, putar: -28, z: 1.5, masuk: { gaya: 'geser', dari: 'kanan' }, t: .15, keluar: { gaya: 'geser', ke: 'kanan' }, akhir: 'L08.w9', bayangan: .5 },
      { gambar: 'uang', x: 300, y: 1330, lebar: 470, putar: -12, z: 1.4, masuk: { gaya: 'jatuh' }, t: 'L08.w11-0.2', bayangan: .5 }
    ] },
  { id: 'syarat', mulai: 'L09', akhir: 'L10', masuk: 'dorong', latar: { pola: 'kertas', warna: '#3d2a1b', tua: 1 }, kamera: [[0, { zoom: 1.5, y: 130 }], [3, { zoom: 1.62, y: 150 }, 'linear']],
    lapis: [
      { benda: { jenis: 'dokumen', kop: 'Catatan', nomor: '15 Jan 1998', judul: 'Indonesia — IMF', lebar: 900, baris: ['Letter of Intent ditandatangani.', 'Paket bantuan: US$43 miliar.', 'Syarat: dana untuk IPTN dihentikan.'],
          sorot: [{ baris: 0, t: -1, lama: .01 }, { baris: 1, t: -1, lama: .01 }, { baris: 2, t: 'L09.w4', lama: .6, warna: 'merah' }] }, y: 860, putar: 1.5, bayangan: true },
      { benda: { jenis: 'cap', teks: 'Dihentikan', ukuran: 66 }, x: 500, y: 1010, putar: -11, masuk: 'cap', t: 'L09.w6', z: 1 }
    ] },
  { id: 'gelap', mulai: 'L10', akhir: 'L11', masuk: 'buka', arahMasuk: 'bawah', kamera: 'dorong', efek: [{ jenis: 'lensa', t: 0, r: .52 }],
    lapis: [
      { gambar: 'hangar-gelap' },
      { benda: { jenis: 'grafik', judul: 'Uji terbang', data: [700], maks: 1400, bentuk: 'progres', t: 'L10.w5', lama: 1.1, labelMaks: 'dari ±1.400 jam', format: v => '±' + Math.round(v / 14) + '%' }, x: 540, y: 1000, skala: .78, putar: -3, masuk: { gaya: 'geser', dari: 'kanan' }, t: 'L10.w2', bayangan: true }
    ] },
  // ── babak 4: hari ini + vonis
  { id: 'museum', mulai: 'L11', akhir: 'L12', masuk: 'tarik', kamera: 'mundur',
    lapis: [
      { gambar: 'museum' },
      { teks: 'Hari ini', gaya: 'judul', ukuran: 84, y: 330, anim: 'luncur', t: 'L11', ikut: true },
      { teks: 'Museum Dirgantara Mandala · Yogyakarta', gaya: 'label', ukuran: 40, y: 470, lebar: 900, masuk: 'naik', t: 'L11.w6' }
    ] },
  { id: 'vonis', mulai: 'L12', masuk: 'bingkai', bingkai: { lapis: 'foto' }, latar: { pola: 'kertas', warna: '#3d2a1b', tua: 1 }, kamera: [[0, { zoom: 1.0 }], ['L12.akhir', { zoom: 1.05, y: 30 }, 'inOutSine']],
    lapis: [
      { id: 'foto', gambar: 'museum', x: 560, y: 1000, lebar: 500, putar: -4, tepi: .035, hitamPutih: true, bayangan: true },
      { teks: 'Pesawatnya sudah jadi.', gaya: 'judul', ukuran: 62, y: 290, lebar: 900, anim: 'luncur', t: 'L12', ikut: true },
      { teks: 'Yang tidak siap, *^zamannya.^*', gaya: 'judul', ukuran: 62, y: 430, lebar: 900, anim: 'luncur', t: 'L12.w4', ikut: true, besar: 1.5 }
    ] }
];
