/* ── Kartu identitas visual (gaya.md §0.3)
   latar ......... navy #051D40 bergrid + kartu kertas retro (permintaan pengguna) · pola cerita: balik (salah → rumus → bukti)
   aksen ......... kuning #FFD23F + merah #E63946; warna unsur: PERAN kuning · KONTEKS biru · TUGAS hijau · FORMAT merah muda
   benda khas .... kartu prompt yang memanjang dengan stabilo per unsur (benda kustom) + tokoh 3D "Raka" (Flow, 6 pose)
   tanda tangan .. `dorong` ke kartu prompt + tombol ENTER ditekan
   bunyi ......... setiap teks/ikon muncul berbunyi (Epidemic; KONFIG.bunyiMuncul), silang = buzz, centang = sukses
*/
const pPad = 60;
const C = { navy: '#051D40', kertas: '#f3ead6', kertas2: '#e8dcc0', tinta: '#1c1a17', abu: '#6b6457', kuning: '#FFD23F', merah: '#E63946', biru: '#4CC9F0', hijau: '#7BE495', pink: '#FF8FA3' };
const UNSUR = [
  { kode: 'P', nama: 'PERAN', warna: C.kuning, tanya: 'Siapa dia?', teks: 'Bertindaklah sebagai copywriter spesialis F&B.', dari: 'L08.w2', sampai: 'L08.akhir' },
  { kode: 'K', nama: 'KONTEKS', warna: C.biru, tanya: 'Situasi & targetnya apa?', teks: 'Saya jual kopi susu gula aren Rp18.000 untuk pekerja kantoran yang ngantuk jam 2 siang.', dari: 'L10.w1', sampai: 'L10.akhir' },
  { kode: 'T', nama: 'TUGAS', warna: C.hijau, tanya: 'Minta apa secara spesifik?', teks: 'Buat 3 ide caption yang relatable dan bikin penasaran.', dari: 'L12.w1', sampai: 'L12.akhir' },
  { kode: 'F', nama: 'FORMAT', warna: C.pink, tanya: 'Mau disajikan bentuk apa?', teks: 'Tulis dalam bentuk tabel berisi hook, isi caption, dan CTA.', dari: 'L14.w1', sampai: 'L14.akhir' }
];
const pR = (K, r) => K.ref(r) + K.a.mulai;
function pTeks(c, K, s, x, y, uk, warna, o) {
  o = o || {}; c.font = o.font || `${o.berat || 700} ${uk}px ${K.HURUF[o.huruf || 'teks']}`; c.fillStyle = warna; c.textAlign = o.rata || 'left'; c.textBaseline = 'middle';
  if (o.maks) c.fillText(s, x, y, o.maks); else c.fillText(s, x, y);
}
function pBayang(c, b, oy, a) { c.shadowColor = `rgba(0,0,0,${a ?? .35})`; c.shadowBlur = b; c.shadowOffsetY = oy; c.shadowOffsetX = 0; }
function pPolos(c) { c.shadowColor = 'transparent'; c.shadowBlur = 0; c.shadowOffsetY = 0; c.shadowOffsetX = 0; }
function pKertas(c, K, x, y, w, h, r, warna) { // kartu kertas retro: bayangan, serat, pita selotip
  pBayang(c, 34, 16, .45); c.fillStyle = warna || C.kertas; K.bulat(c, x, y, w, h, r); c.fill(); pPolos(c);
  c.save(); K.bulat(c, x, y, w, h, r); c.clip(); for (let i = 0; i < 40; i++) { c.fillStyle = `rgba(120,95,50,${.03 + K.acak(i * 3.3) * .04})`; c.beginPath(); c.arc(x + K.acak(i) * w, y + K.acak(i + 9) * h, 10 + K.acak(i + 4) * 60, 0, 7); c.fill(); } c.restore();
  c.save(); c.translate(x + w / 2, y - 6); c.rotate(-.05); c.fillStyle = 'rgba(255,240,190,.75)'; c.fillRect(-70, -18, 140, 36); c.restore();
}
function pBungkus(K, s, font, maks) { return K.bungkus(s, font, maks); }

/* ── menu chat: prompt 1 kalimat → jawaban klise ── */
const KLISE = 'Kopi enak dan nikmat! Harga terjangkau, rasa luar biasa. Yuk beli sekarang juga! #kopi #kopienak #promo';
function pChat(c, ly, t, K) {
  const tt = t + K.a.mulai, R = r => pR(K, r), E = K.E; c.translate(pPad, pPad);
  const W0 = 940, H0 = 900; pKertas(c, K, 0, 0, W0, H0, 40);
  c.fillStyle = C.tinta; K.bulat(c, 0, 0, W0, 110, 40); c.fill(); c.fillRect(0, 60, W0, 50);
  c.fillStyle = C.kuning; c.beginPath(); c.arc(64, 55, 26, 0, 7); c.fill(); pTeks(c, K, 'Asisten AI', 110, 56, 38, '#fff', { berat: 800 });
  // kolom ketik
  const prompt = 'Buatkan caption jualan kopi.', t0 = R('L02.w4') - .1, t1 = R('L02.w7') + .25, kirim = t1 + .2;
  const n = Math.floor(prompt.length * K.jepit((tt - t0) / (t1 - t0)));
  c.fillStyle = '#fffaf0'; K.bulat(c, 30, H0 - 120, W0 - 160, 84, 42); c.fill(); c.strokeStyle = 'rgba(0,0,0,.18)'; c.lineWidth = 2; K.bulat(c, 30, H0 - 120, W0 - 160, 84, 42); c.stroke();
  if (tt < kirim) { pTeks(c, K, n > 0 ? prompt.slice(0, n) : 'Ketik pesan…', 64, H0 - 78, 36, n > 0 ? C.tinta : '#9a917f', { berat: n > 0 ? 600 : 500 }); if (n > 0 && Math.floor(tt * 2.4) % 2 === 0) { c.font = `600 36px ${K.HURUF.teks}`; c.fillStyle = C.tinta; c.fillRect(66 + c.measureText(prompt.slice(0, n)).width, H0 - 100, 4, 44); } }
  c.fillStyle = C.tinta; c.beginPath(); c.arc(W0 - 74, H0 - 78, 40, 0, 7); c.fill(); c.fillStyle = '#fff'; c.beginPath(); c.moveTo(W0 - 92, H0 - 94); c.lineTo(W0 - 52, H0 - 78); c.lineTo(W0 - 92, H0 - 62); c.lineTo(W0 - 84, H0 - 78); c.closePath(); c.fill();
  // gelembung penanya
  if (tt >= kirim) { const u = E.outBack(K.jepit((tt - kirim) / .35)); c.save(); c.translate(W0 - 40, 190); c.scale(u, u); c.font = `700 40px ${K.HURUF.teks}`; const bw = c.measureText(prompt).width + 60; c.fillStyle = C.tinta; K.bulat(c, -bw, -45, bw, 90, 30); c.fill(); pTeks(c, K, prompt, -bw + 30, 0, 40, '#fff'); c.restore(); }
  // jawaban klise
  const tj = R('L03.w1') - .1;
  if (tt >= tj) {
    const f = `500 38px ${K.HURUF.teks}`, bs = pBungkus(K, KLISE, f, 700), m = Math.floor(KLISE.length * K.jepit((tt - tj) / 1.4)); let ct = 0;
    c.fillStyle = '#fff'; K.bulat(c, 30, 280, 790, bs.length * 56 + 60, 30); c.fill(); c.strokeStyle = 'rgba(0,0,0,.15)'; c.lineWidth = 2; K.bulat(c, 30, 280, 790, bs.length * 56 + 60, 30); c.stroke();
    bs.forEach((s, i) => { const k = Math.max(0, Math.min(s.length, m - ct)); ct += s.length + 1; if (k > 0) pTeks(c, K, s.slice(0, k), 64, 340 + i * 56, 38, C.tinta, { berat: 500 }); });
  }
}

/* ── kartu rumus (nomor + nama + pertanyaan) ── */
function pKartuRumus(i, besar) {
  return (c, ly, t, K) => {
    const u = UNSUR[i], W0 = besar ? 900 : 420, H0 = besar ? 560 : 420; c.translate(pPad, pPad);
    pKertas(c, K, 0, 0, W0, H0, 34);
    c.fillStyle = u.warna; K.bulat(c, 0, 0, W0, besar ? 140 : 96, 34); c.fill(); c.fillRect(0, besar ? 90 : 60, W0, besar ? 50 : 36);
    c.fillStyle = C.tinta; c.beginPath(); c.arc(besar ? 90 : 62, besar ? 70 : 48, besar ? 50 : 34, 0, 7); c.fill(); pTeks(c, K, String(i + 1), besar ? 90 : 62, besar ? 72 : 50, besar ? 60 : 40, '#fff', { rata: 'center', huruf: 'judul', berat: 400 });
    pTeks(c, K, u.nama, besar ? 170 : 112, besar ? 72 : 50, besar ? 76 : 46, C.tinta, { huruf: 'judul', berat: 400 });
    if (besar) pTeks(c, K, u.tanya, W0 / 2, H0 - 70, 46, C.abu, { rata: 'center', huruf: 'tangan', berat: 700 });
    else pTeks(c, K, u.tanya, W0 / 2, H0 - 46, 30, C.abu, { rata: 'center', huruf: 'tangan', berat: 700, maks: W0 - 40 });
  };
}

/* ── kartu prompt yang memanjang + tombol ENTER ── */
function pPrompt(c, ly, t, K) {
  const tt = t + K.a.mulai, R = r => pR(K, r), E = K.E; c.translate(pPad, pPad);
  const W0 = 940, H0 = 1180; pKertas(c, K, 0, 0, W0, H0, 36, '#fbf6ea');
  pTeks(c, K, 'PROMPT KAMU', 40, 60, 34, C.abu, { huruf: 'judul', berat: 400 }); c.fillStyle = 'rgba(0,0,0,.15)'; c.fillRect(40, 96, W0 - 80, 3);
  let y = 150; const f = `600 44px ${K.HURUF.teks}`;
  UNSUR.forEach((u, i) => {
    const t0 = R(u.dari) - .15, t1 = R(u.sampai); if (tt < t0) return;
    const n = Math.floor(u.teks.length * K.jepit((tt - t0) / Math.max(.4, t1 - t0))), bs = pBungkus(K, u.teks, f, W0 - 120), e = E.outBack(K.jepit((tt - t0) / .35));
    c.save(); c.translate(40, y); c.scale(e, e); c.fillStyle = u.warna; K.bulat(c, 0, 0, 240, 58, 29); c.fill(); pTeks(c, K, u.nama, 120, 31, 32, C.tinta, { rata: 'center', berat: 800 }); c.restore();
    y += 76; let ct = 0;
    bs.forEach((s, j) => {
      const k = Math.max(0, Math.min(s.length, n - ct)); ct += s.length + 1; if (k <= 0) { y += 60; return; }
      c.font = f; const ww = c.measureText(s.slice(0, k)).width; c.fillStyle = u.warna + 'aa'; c.fillRect(56, y - 10, ww + 12, 54);
      pTeks(c, K, s.slice(0, k), 62, y + 18, 44, C.tinta, { berat: 600 }); y += 60;
    });
    y += 22;
  });
  // tombol ENTER
  const te = R('L14.akhir') + .05, u = K.jepit((tt - te) / .25), tekan = tt >= te && tt < te + .25;
  if (tt >= R('L13.w1')) { const kx = W0 - 250, ky = H0 - 130; c.save(); c.translate(kx, ky + (tekan ? 8 : 0)); c.fillStyle = '#5c544a'; K.bulat(c, 0, 12, 210, 96, 18); c.fill(); c.fillStyle = tt >= te ? C.hijau : '#fffaf0'; K.bulat(c, 0, tekan ? 8 : 0, 210, 96, 18); c.fill(); c.strokeStyle = C.tinta; c.lineWidth = 3; K.bulat(c, 0, tekan ? 8 : 0, 210, 96, 18); c.stroke(); pTeks(c, K, 'ENTER ↵', 105, (tekan ? 8 : 0) + 50, 34, C.tinta, { rata: 'center', berat: 800 }); c.restore();
    if (u > 0 && u < 1) { c.strokeStyle = `rgba(28,26,23,${1 - u})`; c.lineWidth = 6; c.beginPath(); c.arc(kx + 105, ky + 50, 60 + u * 140, 0, 7); c.stroke(); } }
}

/* ── tabel hasil ── */
const TABEL = [
  ['Jam 2, mata tinggal 5 watt?', 'Kopi susu gula aren dingin, manisnya pas buat melek lagi.', 'Pesan sekarang, Rp18.000'],
  ['Ngantuk pas meeting?', 'Satu gelas gula aren, fokus balik sampai jam pulang.', 'Order lewat chat'],
  ['Lembur lagi malam ini?', 'Temani deadline-mu pakai kopi susu yang nggak bikin eneg.', 'Klik link di bio']
];
function pTabel(c, ly, t, K) {
  const tt = t + K.a.mulai, R = r => pR(K, r), E = K.E; c.translate(pPad, pPad);
  const W0 = 960, H0 = 900, col = [230, 460, 270], x0 = 0; pKertas(c, K, 0, 0, W0, H0, 30, '#fbf6ea');
  c.fillStyle = C.tinta; K.bulat(c, 0, 0, W0, 100, 30); c.fill(); c.fillRect(0, 60, W0, 40);
  let x = 0; ['HOOK', 'ISI CAPTION', 'CTA'].forEach((h, i) => { pTeks(c, K, h, x + 24, 52, 34, i === 0 ? C.kuning : i === 1 ? C.biru : C.pink, { huruf: 'judul', berat: 400 }); x += col[i]; });
  TABEL.forEach((row, r) => {
    const t0 = R('L15.w3') + r * .55, u = K.jepit((tt - t0) / .35); if (u <= 0) return; const e = E.outCubic(u), y0 = 120 + r * 255;
    c.save(); c.globalAlpha = u; c.translate((1 - e) * 60, 0);
    if (r % 2 === 0) { c.fillStyle = 'rgba(0,0,0,.05)'; c.fillRect(0, y0 - 10, W0, 250); }
    let xx = 0; row.forEach((s, i) => { const f = `${i === 0 ? 800 : 500} 30px ${K.HURUF.teks}`, bs = pBungkus(K, s, f, col[i] - 40); bs.slice(0, 5).forEach((q, j) => pTeks(c, K, q, xx + 22, y0 + 34 + j * 40, 30, C.tinta, { berat: i === 0 ? 800 : 500 })); xx += col[i]; });
    c.fillStyle = 'rgba(0,0,0,.18)'; c.fillRect(20, y0 + 236, W0 - 40, 2); c.restore();
  });
}

/* ── ikon simpan (bookmark) ── */
function pSimpan(c, ly, t, K) {
  const tt = t + K.a.mulai, R = r => pR(K, r); c.translate(pPad, pPad);
  const pu = 1 + .06 * Math.sin(tt * 6), on = tt >= R('L16.w1') + .1;
  c.save(); c.translate(110, 110); c.scale(pu, pu); pBayang(c, 30, 14, .45); c.fillStyle = '#fff'; K.bulat(c, -100, -100, 200, 200, 46); c.fill(); pPolos(c);
  c.fillStyle = on ? C.tinta : 'transparent'; c.strokeStyle = C.tinta; c.lineWidth = 12; c.lineJoin = 'round'; c.beginPath(); c.moveTo(-40, -58); c.lineTo(40, -58); c.lineTo(40, 62); c.lineTo(0, 30); c.lineTo(-40, 62); c.closePath(); if (on) c.fill(); c.stroke(); c.restore();
}

/* ── konfigurasi ── */
const KONFIG = {
  judul: 'Kamu Salah Pakai AI Kalau Masih Nanya Cuma Satu Kalimat',
  rasio: '9:16', fps: 30,
  durasiTarget: [52, 66],
  tema: 'kartu',
  grade: { tint: '#f4e6c8', kuat: .05, saturasi: 1.02, halftone: .05, grain: .07, vinyet: .42, debu: .12, garis: 0, kontras: .1 },
  palet: { kuning: '#FFD23F', merah: '#E63946' },
  sfxPeta: { whoosh: 'whoosh', swish: 'swish', stempel: 'stempel', kertas: 'kertas', pop: 'pop' },
  bunyiMuncul: { teks: 'teks', gambar: 'ikon', benda: 'popup', vol: .5 },
  thumbnail: { t: 'L01.w4' },
  sumber: [
    { fakta: 'Panduan prompt Google Gemini for Workspace: empat area prompt efektif = Persona, Task, Context, Format; prompt paling berhasil rata-rata ±21 kata', url: 'https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf' },
    { fakta: 'Google: persona = sudut pandang, task = tindakan spesifik, context = latar belakang, format = bentuk hasil', url: 'https://blog.google/products/workspace/google-gemini-workspace-ai-prompt-tips/' }
  ]
};

const NAVY = { pola: 'grid', warna: '#051D40', warnaGaris: 'rgba(170,200,255,.13)', jarak: 72 };
const NAVY2 = { pola: 'grid', warna: '#06224a', warnaGaris: 'rgba(170,200,255,.11)', jarak: 90, putar: 1 };
const TOKOH = (kode, o) => Object.assign({ gambar: kode, z: 1.3, bayangan: .45, bunyi: 'swish', rig: ['napas', { jenis: 'goyang', sudut: { amp: 1, periode: 4 } }] }, o);
const KARTU = (i, besar, o) => Object.assign({ benda: { jenis: 'kustom', lebar: (besar ? 900 : 420) + 120, tinggi: (besar ? 560 : 420) + 120, lukis: pKartuRumus(i, besar) } }, o);
const PROMPT = o => Object.assign({ benda: { jenis: 'kustom', lebar: 1060, tinggi: 1300, lukis: pPrompt }, x: 540, y: 1110, skala: .92 }, o);
const JUDUL = (teks, o) => Object.assign({ teks, gaya: 'judul', ukuran: 84, y: 330, lebar: 900, anim: 'luncur' }, o);

const ADEGAN = [
  // 1 hook
  { id: 'hook', mulai: 0, akhir: 'L02', latar: NAVY, kamera: 'dorong-kuat', efek: [{ jenis: 'kilat', t: 'L01.w2', lama: .25, kuat: .6 }],
    lapis: [
      TOKOH('tokoh-stop', { x: 560, y: 1230, tinggi: 1250, masuk: { gaya: 'terbang', dari: 'bawah' }, t: .05, jangkar: 'bawah' }),
      { teks: 'SALAH PAKAI AI', gaya: 'stiker', ukuran: 92, y: 330, putar: -3, masuk: 'pop', t: 'L01.w2', bunyi: 'salah' },
      { teks: 'kalau cuma *1 kalimat*', gaya: 'label', ukuran: 46, y: 470, masuk: 'naik', t: 'L01.w8' }
    ] },
  // 2 prompt satu kalimat
  { id: 'ketik', mulai: 'L02', akhir: 'L03', masuk: 'dorong', titikMasuk: [540, 900], latar: NAVY2, kamera: 'dorong',
    sfx: [...Array(9)].map((_, i) => ({ t: 'L02.w4+' + (i * .14).toFixed(2), berkas: 'tuts', vol: .5 })).concat([{ t: 'L02.w7+0.45', berkas: 'notif', vol: .6 }]),
    lapis: [
      { benda: { jenis: 'kustom', lebar: 1060, tinggi: 1020, lukis: pChat }, x: 540, y: 1080, skala: .95, masuk: { gaya: 'naik' }, t: .05 },
      JUDUL('Prompt *1 kalimat*', { t: 'L02.w1', y: 300 })
    ] },
  // 3 jawaban kaku
  { id: 'kaku', mulai: 'L03', akhir: 'L04', masuk: 'geser', arahMasuk: 'atas', latar: NAVY2, kamera: [[0, { zoom: 1.05, y: -40 }], [4, { zoom: 1.15, y: -80 }, 'inOutSine']],
    lapis: [
      { benda: { jenis: 'kustom', lebar: 1060, tinggi: 1020, lukis: pChat }, x: 540, y: 1080, skala: .95 },
      { benda: { jenis: 'cap', teks: 'KAKU', ukuran: 96, warna: '#E63946' }, x: 260, y: 930, putar: -10, masuk: 'cap', t: 'L03.w3' },
      { benda: { jenis: 'cap', teks: 'KLISE', ukuran: 96, warna: '#E63946' }, x: 760, y: 1010, putar: 8, masuk: 'cap', t: 'L03.w4' },
      TOKOH('robot', { x: 830, y: 1380, lebar: 330, putar: 6, masuk: 'pop', t: 'L03.w8-0.1', bunyi: 'salah', rig: { jenis: 'goyang', sudut: { amp: 3, periode: 1.2 } } }),
      JUDUL('= jawaban *robot*', { t: 'L03.w6', y: 300 })
    ] },
  // 4 bukan AI-nya
  { id: 'bukan', mulai: 'L04', akhir: 'L05', masuk: 'tutup', arahMasuk: 'bawah', latar: NAVY, kamera: 'dorong',
    lapis: [
      TOKOH('tokoh-bingung', { x: 520, y: 1330, tinggi: 1000, masuk: { gaya: 'terbang', dari: 'bawah' }, t: .05, jangkar: 'bawah' }),
      JUDUL('Bukan AI-nya yang *kurang pintar*', { t: 'L04.w1', ikut: true, y: 300, ukuran: 74 }),
      { coret: 'silang', x: 540, y: 340, lebar: 720, tinggi: 150, warna: 'merah', tebal: 12, t: 'L04.w5+0.1', lama: .4, bunyi: 'salah' },
      { teks: 'tapi *arahannya* kurang lengkap', gaya: 'label', ukuran: 50, y: 520, lebar: 860, masuk: 'naik', t: 'L04.w6' }
    ] },
  // 5 aha
  { id: 'aha', mulai: 'L05', akhir: 'L06', masuk: 'sentak', arahMasuk: 'kanan', latar: NAVY2, kamera: 'mundur',
    efek: [{ jenis: 'kilau', t: 'L05.w8', lama: .9, kuat: .7, titik: [790, 720], sinar: 14, sfx: false }],
    lapis: [
      TOKOH('tokoh-aha', { x: 420, y: 1300, tinggi: 1150, masuk: { gaya: 'terbang', dari: 'kiri' }, t: .05, jangkar: 'bawah' }),
      TOKOH('bohlam', { x: 800, y: 760, lebar: 300, masuk: 'pop', t: 'L05.w6', bunyi: 'ide', hidup: 10, rig: { jenis: 'goyang', poros: [.5, 0], sudut: { amp: 4, periode: 2 } } }),
      JUDUL('Rumus *4 elemen*', { t: 'L05.w8', y: 330, ukuran: 96 })
    ] },
  // 6 empat kartu
  { id: 'empat', mulai: 'L06', akhir: 'L07', masuk: 'tarik', latar: NAVY, kamera: 'dorong',
    lapis: [
      JUDUL('RUMUS PROMPT', { t: .05, y: 300, ukuran: 90 }),
      KARTU(0, false, { x: 300, y: 800, putar: -4, masuk: 'pop', t: 'L06.w1' }),
      KARTU(1, false, { x: 780, y: 820, putar: 3, masuk: 'pop', t: 'L06.w2' }),
      KARTU(2, false, { x: 300, y: 1270, putar: 2, masuk: 'pop', t: 'L06.w3' }),
      KARTU(3, false, { x: 780, y: 1290, putar: -3, masuk: 'pop', t: 'L06.w5' }),
      { gambar: 'topeng', x: 300, y: 830, lebar: 170, putar: -4, masuk: 'pop', t: 'L06.w1+0.1', sfx: false, bayangan: .3 },
      { gambar: 'kaca', x: 780, y: 850, lebar: 180, putar: 3, masuk: 'pop', t: 'L06.w2+0.1', sfx: false, bayangan: .3 },
      { gambar: 'target', x: 300, y: 1300, lebar: 170, putar: 2, masuk: 'pop', t: 'L06.w3+0.1', sfx: false, bayangan: .3 }
    ] },
  // 7 peran
  { id: 'peran', mulai: 'L07', akhir: 'L08', masuk: 'kartu', latar: NAVY2, kamera: 'dorong',
    lapis: [
      KARTU(0, true, { x: 540, y: 820, putar: -2, masuk: 'pop', t: .05 }),
      { gambar: 'topeng', x: 540, y: 830, lebar: 300, putar: -6, masuk: 'pop', t: 'L07.w2', bayangan: .35, hidup: 6 },
      TOKOH('tokoh-tunjuk', { x: 330, y: 1500, tinggi: 820, masuk: { gaya: 'terbang', dari: 'bawah' }, t: 'L07.w3', jangkar: 'bawah' }),
      { teks: 'sebagai *siapa*?', gaya: 'tangan', ukuran: 76, x: 690, y: 1190, putar: -6, masuk: 'pop', t: 'L07.w8-0.2' }
    ] },
  { id: 'peran-isi', mulai: 'L08', akhir: 'L09', masuk: 'dorong', titikMasuk: [540, 820], latar: NAVY, kamera: 'dorong', sfx: [{ t: 'L08.w2', berkas: 'tuts', vol: .4 }, { t: 'L08.w4', berkas: 'tuts', vol: .4 }],
    lapis: [PROMPT({ masuk: { gaya: 'naik' }, t: .05 }), JUDUL('1. *PERAN*', { t: 'L08.w1', y: 270, ukuran: 80 })] },
  // 8 konteks
  { id: 'konteks', mulai: 'L09', akhir: 'L10', masuk: 'sentak', arahMasuk: 'bawah', latar: NAVY2, kamera: 'dorong',
    lapis: [
      KARTU(1, true, { x: 540, y: 820, putar: 2, masuk: 'pop', t: .05 }),
      { gambar: 'kaca', x: 560, y: 840, lebar: 320, putar: 8, masuk: 'pop', t: 'L09.w2', bayangan: .35, hidup: 6 },
      TOKOH('tokoh-tunjuk', { x: 330, y: 1500, tinggi: 820, masuk: { gaya: 'terbang', dari: 'bawah' }, t: 'L09.w3', jangkar: 'bawah' })
    ] },
  { id: 'konteks-isi', mulai: 'L10', akhir: 'L11', masuk: 'tutup', arahMasuk: 'kanan', latar: NAVY, kamera: [[0, { zoom: 1.0, y: 0 }], [6, { zoom: 1.1, y: 60 }, 'inOutSine']], sfx: [{ t: 'L10.w1', berkas: 'tuts', vol: .4 }, { t: 'L10.w7', berkas: 'tuts', vol: .4 }],
    lapis: [PROMPT({}), JUDUL('2. *KONTEKS*', { t: .05, y: 270, ukuran: 80 })] },
  // 9 tugas
  { id: 'tugas', mulai: 'L11', akhir: 'L12', masuk: 'geser', arahMasuk: 'kiri', latar: NAVY2, kamera: 'dorong',
    lapis: [
      KARTU(2, true, { x: 540, y: 820, putar: -2, masuk: 'pop', t: .05 }),
      { gambar: 'target', x: 560, y: 840, lebar: 320, putar: -4, masuk: 'pop', t: 'L11.w2', bayangan: .35, hidup: 6 },
      TOKOH('tokoh-tunjuk', { x: 330, y: 1500, tinggi: 820, masuk: { gaya: 'terbang', dari: 'bawah' }, t: 'L11.w3', jangkar: 'bawah' })
    ] },
  { id: 'tugas-isi', mulai: 'L12', akhir: 'L13', masuk: 'dorong', titikMasuk: [540, 820], latar: NAVY, kamera: [[0, { zoom: 1.05, y: 80 }], [4, { zoom: 1.14, y: 140 }, 'inOutSine']], sfx: [{ t: 'L12.w1', berkas: 'tuts', vol: .4 }, { t: 'L12.w5', berkas: 'tuts', vol: .4 }],
    lapis: [PROMPT({}), JUDUL('3. *TUGAS*', { t: .05, y: 270, ukuran: 80, z: .3 })] },
  // 10 format
  { id: 'format', mulai: 'L13', akhir: 'L14', masuk: 'sentak', arahMasuk: 'kanan', latar: NAVY2, kamera: 'dorong',
    lapis: [
      KARTU(3, true, { x: 540, y: 820, putar: 2, masuk: 'pop', t: .05 }),
      { benda: { jenis: 'kustom', lebar: 380, tinggi: 300, lukis: (c, ly, t, K) => { c.translate(30, 30); c.fillStyle = '#fff'; K.bulat(c, 0, 0, 320, 240, 18); c.fill(); c.strokeStyle = C.tinta; c.lineWidth = 6; K.bulat(c, 0, 0, 320, 240, 18); c.stroke(); c.fillStyle = C.tinta; c.fillRect(0, 0, 320, 56); for (let i = 1; i < 4; i++) { c.fillRect(0, 56 + i * 46, 320, 3); } c.fillRect(106, 0, 4, 240); c.fillRect(212, 0, 4, 240); } }, x: 540, y: 840, putar: 4, masuk: 'pop', t: 'L13.w2' },
      TOKOH('tokoh-tunjuk', { x: 330, y: 1500, tinggi: 820, masuk: { gaya: 'terbang', dari: 'bawah' }, t: 'L13.w3', jangkar: 'bawah' })
    ] },
  { id: 'format-isi', mulai: 'L14', akhir: 'L15', masuk: 'tutup', arahMasuk: 'bawah', latar: NAVY, kamera: [[0, { zoom: 1.08, y: 140 }], [4.5, { zoom: 1.18, y: 220 }, 'inOutSine']],
    sfx: [{ t: 'L14.w1', berkas: 'tuts', vol: .4 }, { t: 'L14.w6', berkas: 'tuts', vol: .4 }, { t: 'L14.akhir+0.05', berkas: 'konfirm', vol: .8 }],
    lapis: [PROMPT({}), JUDUL('4. *FORMAT*', { t: .05, y: 270, ukuran: 80, z: .25 })] },
  // 11 hasil
  { id: 'hasil', mulai: 'L15', akhir: 'L16', masuk: 'iris', titikMasuk: [790, 1080], latar: NAVY2, kamera: 'dorong',
    efek: [{ jenis: 'kilau', t: 'L15.w5', lama: .8, kuat: .45, titik: [540, 900], sinar: 12, sfx: false }],
    sfx: [{ t: 'L15.w3', berkas: 'popup', vol: .5 }, { t: 'L15.w3+0.55', berkas: 'popup', vol: .45 }, { t: 'L15.w3+1.1', berkas: 'popup', vol: .45 }],
    lapis: [
      { benda: { jenis: 'kustom', lebar: 1080, tinggi: 1020, lukis: pTabel }, x: 540, y: 900, skala: .96, masuk: { gaya: 'naik' }, t: .05 },
      { teks: 'SIAP PAKAI!', gaya: 'stiker', ukuran: 90, y: 330, putar: -3, masuk: 'pop', t: 'L15.w4', bunyi: 'benar' },
      TOKOH('tokoh-jempol', { x: 880, y: 1700, tinggi: 640, masuk: { gaya: 'terbang', dari: 'kanan' }, t: 'L15.w9', jangkar: 'bawah' })
    ] },
  // 12 save
  { id: 'simpan', mulai: 'L16', masuk: 'buka', arahMasuk: 'atas', latar: NAVY, kamera: 'mundur',
    lapis: [
      TOKOH('tokoh-save', { x: 430, y: 1250, tinggi: 1150, balik: true, masuk: { gaya: 'terbang', dari: 'kiri' }, t: .05, jangkar: 'bawah' }),
      { benda: { jenis: 'kustom', lebar: 340, tinggi: 340, lukis: pSimpan }, x: 830, y: 1240, masuk: 'pop', t: 'L16.w1', bunyi: 'konfirm' },
      { teks: 'SAVE VIDEO INI', gaya: 'stiker', ukuran: 88, y: 330, putar: -2, masuk: 'pop', t: 'L16.w1' },
      { teks: 'buat contekan prompt', gaya: 'label', ukuran: 46, y: 470, masuk: 'naik', t: 'L16.w7' },
      { teks: 'coba praktekkin *sekarang!*', gaya: 'tangan', ukuran: 76, y: 620, putar: -4, masuk: 'pop', t: 'L17.w1' }
    ] }
];
