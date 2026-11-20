/* ── Kartu identitas visual — lanjutan seri "Kamu Salah Pakai AI" (aset dan gaya dipakai ulang atas permintaan pengguna)
   latar ......... navy #051D40 bergrid + kartu kertas retro · pola: angka (3 trik)
   aksen ......... kuning #FFD23F + merah #E63946; trik: POIN hijau · TABEL biru · 3 KALIMAT merah muda
   benda khas .... menu chat AI 4 tampilan (tembok teks → poin → tabel → 3 kalimat), tokoh 3D Raka
   tanda tangan .. tembok teks yang digunting / menyusut jadi kotak ringkas
   bunyi ......... setiap teks/ikon muncul berbunyi (Epidemic; KONFIG.bunyiMuncul)
*/
const pPad = 60;
const C = { tinta: '#1c1a17', abu: '#6b6457', kuning: '#FFD23F', merah: '#E63946', biru: '#4CC9F0', hijau: '#5BD17F', pink: '#FF8FA3' };
const pR = (K, r) => K.ref(r) + K.a.mulai;
function pTeks(c, K, s, x, y, uk, warna, o) {
  o = o || {}; c.font = `${o.berat || 700} ${uk}px ${K.HURUF[o.huruf || 'teks']}`; c.fillStyle = warna; c.textAlign = o.rata || 'left'; c.textBaseline = 'middle';
  if (o.maks) c.fillText(s, x, y, o.maks); else c.fillText(s, x, y);
}
function pBayang(c, b, oy, a) { c.shadowColor = `rgba(0,0,0,${a ?? .35})`; c.shadowBlur = b; c.shadowOffsetY = oy; c.shadowOffsetX = 0; }
function pPolos(c) { c.shadowColor = 'transparent'; c.shadowBlur = 0; c.shadowOffsetY = 0; c.shadowOffsetX = 0; }
function pKertas(c, K, x, y, w, h, r, warna) {
  pBayang(c, 34, 16, .45); c.fillStyle = warna || '#f3ead6'; K.bulat(c, x, y, w, h, r); c.fill(); pPolos(c);
  c.save(); K.bulat(c, x, y, w, h, r); c.clip(); for (let i = 0; i < 40; i++) { c.fillStyle = `rgba(120,95,50,${.03 + K.acak(i * 3.3) * .04})`; c.beginPath(); c.arc(x + K.acak(i) * w, y + K.acak(i + 9) * h, 10 + K.acak(i + 4) * 60, 0, 7); c.fill(); } c.restore();
  c.save(); c.translate(x + w / 2, y - 6); c.rotate(-.05); c.fillStyle = 'rgba(255,240,190,.75)'; c.fillRect(-70, -18, 140, 36); c.restore();
}
function pKepala(c, K, W0) { c.fillStyle = C.tinta; K.bulat(c, 0, 0, W0, 110, 40); c.fill(); c.fillRect(0, 60, W0, 50); c.fillStyle = C.kuning; c.beginPath(); c.arc(64, 55, 26, 0, 7); c.fill(); pTeks(c, K, 'Asisten AI', 110, 56, 38, '#fff', { berat: 800 }); }
function pBaris(c, K, s, x, y, uk, maks, warna, berat, lh) { const f = `${berat || 500} ${uk}px ${K.HURUF.teks}`, bs = K.bungkus(s, f, maks); bs.forEach((q, i) => pTeks(c, K, q, x, y + i * (lh || uk * 1.35), uk, warna || C.tinta, { berat: berat || 500 })); return bs.length * (lh || uk * 1.35); }
function pCentang(c, x, y, r, warna, k) { c.fillStyle = warna; c.beginPath(); c.arc(x, y, r, 0, 7); c.fill(); c.strokeStyle = '#fff'; c.lineWidth = r * .28; c.lineCap = 'round'; c.lineJoin = 'round'; c.beginPath(); c.moveTo(x - r * .45, y + r * .02); c.lineTo(x - r * .1, y + r * .38); if (k > .5) c.lineTo(x + r * .48, y - r * .35); c.stroke(); }

/* ── tampilan A: tembok teks yang digulir ── */
const TEMBOK = 'Inflasi adalah kondisi ketika harga barang dan jasa secara umum naik terus-menerus dalam jangka waktu tertentu. Untuk memahami inflasi, kita perlu melihat sejarah ekonomi, teori permintaan dan penawaran, peran bank sentral, kebijakan fiskal, hingga perilaku konsumen di berbagai negara. Pada dasarnya ada beberapa jenis inflasi, misalnya inflasi tarikan permintaan, inflasi dorongan biaya, dan inflasi bawaan, yang masing-masing memiliki penyebab dan dampak berbeda. Selain itu, para ekonom juga membedakan inflasi ringan, sedang, berat, dan hiperinflasi berdasarkan besarnya kenaikan harga. Dalam konteks Indonesia, inflasi dipantau oleh Badan Pusat Statistik setiap bulan dan dikendalikan bersama oleh pemerintah dan Bank Indonesia melalui berbagai instrumen kebijakan. Dengan demikian, dapat disimpulkan bahwa inflasi merupakan fenomena yang kompleks dan memerlukan pemahaman menyeluruh dari banyak sudut pandang.';
function pChatPanjang(c, ly, t, K) {
  const tt = t + K.a.mulai, R = r => pR(K, r); c.translate(pPad, pPad);
  const W0 = 940, H0 = 1000; pKertas(c, K, 0, 0, W0, H0, 40); pKepala(c, K, W0);
  c.save(); K.bulat(c, 0, 112, W0, H0 - 112, 0); c.clip();
  const gulir = Math.max(0, tt - R('L02.w6')) * 260 + Math.max(0, tt - R('L03.w1')) * 260;
  c.translate(0, -gulir);
  c.font = `700 38px ${K.HURUF.teks}`; const q = 'Apa itu inflasi?', bw = c.measureText(q).width + 60; c.fillStyle = C.tinta; K.bulat(c, W0 - 40 - bw, 150, bw, 84, 30); c.fill(); pTeks(c, K, q, W0 - 40 - bw + 30, 193, 38, '#fff');
  let y = 290; for (let r = 0; r < 3; r++) { c.fillStyle = '#fff'; const h = pBaris(c, K, TEMBOK, 64, y + 40, 32, 790, C.tinta, 500, 44) + 40; c.globalCompositeOperation = 'destination-over'; K.bulat(c, 30, y, 850, h, 26); c.fill(); c.globalCompositeOperation = 'source-over'; y += h + 24; }
  c.restore();
  const tinggi = 860, pos = Math.min(1, gulir / 2200); c.fillStyle = 'rgba(0,0,0,.25)'; K.bulat(c, W0 - 22, 140 + pos * (H0 - 340), 10, 180, 5); c.fill();
}

/* ── kartu 3 batasan ── */
const TRIK = [{ nama: 'POIN-POIN', warna: C.hijau, sub: 'Tulis dalam 5 poin' }, { nama: 'TABEL', warna: C.biru, sub: 'Cocok buat banding' }, { nama: 'MAKS. 3 KALIMAT', warna: C.pink, sub: 'Padat, langsung inti' }];
function pIkonTrik(c, i, x, y, s) {
  c.save(); c.translate(x, y); c.scale(s, s); c.strokeStyle = C.tinta; c.fillStyle = C.tinta; c.lineWidth = 9; c.lineCap = 'round';
  if (i === 0) for (let k = 0; k < 3; k++) { c.beginPath(); c.arc(-50, -40 + k * 40, 9, 0, 7); c.fill(); c.beginPath(); c.moveTo(-26, -40 + k * 40); c.lineTo(60, -40 + k * 40); c.stroke(); }
  else if (i === 1) { c.strokeRect(-62, -52, 124, 104); c.beginPath(); c.moveTo(-62, -18); c.lineTo(62, -18); c.moveTo(-62, 17); c.lineTo(62, 17); c.moveTo(-20, -52); c.lineTo(-20, 52); c.moveTo(22, -52); c.lineTo(22, 52); c.stroke(); }
  else { c.font = `400 120px ${'"KR Anton","Anton",Impact,sans-serif'}`; c.textAlign = 'center'; c.textBaseline = 'middle'; c.fillText('3', 0, 6); }
  c.restore();
}
function pKartuTrik(i, besar) {
  return (c, ly, t, K) => {
    const u = TRIK[i], W0 = besar ? 900 : 300, H0 = besar ? 560 : 400; c.translate(pPad, pPad); pKertas(c, K, 0, 0, W0, H0, 30);
    const hb = besar ? 140 : 84; c.fillStyle = u.warna; K.bulat(c, 0, 0, W0, hb, 30); c.fill(); c.fillRect(0, hb - 40, W0, 40);
    c.fillStyle = C.tinta; c.beginPath(); c.arc(besar ? 90 : 46, hb / 2, besar ? 48 : 28, 0, 7); c.fill(); pTeks(c, K, String(i + 1), besar ? 90 : 46, hb / 2 + 2, besar ? 58 : 34, '#fff', { rata: 'center', huruf: 'judul', berat: 400 });
    pTeks(c, K, u.nama, besar ? 165 : 86, hb / 2 + 2, besar ? 66 : (i === 2 ? 26 : 34), C.tinta, { huruf: 'judul', berat: 400, maks: W0 - (besar ? 190 : 100) });
    if (i < 2 || besar === false) pIkonTrik(c, i, W0 / 2, besar ? 300 : 225, besar ? 1.5 : 1);
    pTeks(c, K, u.sub, W0 / 2, H0 - (besar ? 60 : 40), besar ? 46 : 30, C.abu, { rata: 'center', huruf: 'tangan', berat: 700, maks: W0 - 30 });
  };
}

/* ── tampilan B/C/D: prompt tambahan + hasil rapi ── */
const MODE = {
  poin: { tanya: 'Apa itu inflasi?', tambah: 'Tulis dalam 5 poin singkat tanpa pembukaan.', dari: 'L06.w3', sampai: 'L06.akhir', hasil: 'L07.w1', warna: C.hijau,
    isi: ['Harga barang & jasa naik terus-menerus', 'Nilai uang turun, daya beli melemah', 'Pemicu: permintaan melebihi pasokan', 'Bisa juga karena biaya produksi naik', 'Dikendalikan lewat suku bunga'] },
  tabel: { tanya: 'Bandingkan 3 laptop buat kuliah.', tambah: 'Sajikan dalam bentuk tabel berisi kelebihan, kekurangan, dan harga.', dari: 'L09.w8', sampai: 'L09.w12', hasil: 'L09.w13', warna: C.biru,
    isi: [['Laptop A', 'Ringan, baterai awet', 'Layar kecil', '±Rp7 jt'], ['Laptop B', 'Layar besar, kencang', 'Berat', '±Rp10 jt'], ['Laptop C', 'Murah', 'RAM kecil', '±Rp5 jt']] },
  kalimat: { tanya: 'Jelaskan apa itu blockchain.', tambah: 'Jelaskan konsep ini maksimal dalam 3 kalimat sederhana.', dari: 'L12.w2', sampai: 'L12.akhir', hasil: 'L13.w1', warna: C.pink,
    isi: 'Blockchain adalah buku catatan digital yang disimpan bersama oleh banyak komputer. Setiap transaksi dicatat dalam blok yang saling terhubung. Karena salinannya tersebar, catatan itu sulit diubah diam-diam.' }
};
function pChatTrik(mode) {
  return (c, ly, t, K) => {
    const m = MODE[mode], tt = t + K.a.mulai, R = r => pR(K, r), E = K.E; c.translate(pPad, pPad);
    const W0 = 940, H0 = 1140; pKertas(c, K, 0, 0, W0, H0, 40); pKepala(c, K, W0);
    // gelembung penanya + kalimat tambahan yang diketik (stabilo warna trik)
    const f = `700 36px ${K.HURUF.teks}`, t0 = R(m.dari) - .1, t1 = R(m.sampai), n = Math.floor(m.tambah.length * K.jepit((tt - t0) / Math.max(.4, t1 - t0)));
    const bTanya = K.bungkus(m.tanya, f, 700), bTambah = K.bungkus(m.tambah, f, 700), lh = 50, bh = (bTanya.length + bTambah.length) * lh + 40;
    c.fillStyle = C.tinta; K.bulat(c, 70, 140, W0 - 110, bh, 30); c.fill();
    bTanya.forEach((s, i) => pTeks(c, K, s, 100, 140 + 44 + i * lh, 36, '#fff'));
    let ct = 0; bTambah.forEach((s, i) => { const k = Math.max(0, Math.min(s.length, n - ct)); ct += s.length + 1; if (k <= 0) return; c.font = f; const ww = c.measureText(s.slice(0, k)).width, yy = 140 + 44 + (bTanya.length + i) * lh; c.fillStyle = m.warna; c.fillRect(94, yy - 24, ww + 12, 46); pTeks(c, K, s.slice(0, k), 100, yy, 36, C.tinta); });
    const y0 = 140 + bh + 40, th = R(m.hasil) - .15;
    if (mode === 'kalimat') { // teks panjang abu menyusut jadi kotak ringkas
      const u = E.inOutCubic(K.jepit((tt - (th - .2)) / .8));
      if (u < 1) { c.save(); c.globalAlpha = 1 - u; c.translate(W0 / 2, y0 + 260); c.scale(1 - .5 * u, 1 - .5 * u); for (let i = 0; i < 12; i++) { c.fillStyle = '#c9bfa8'; c.fillRect(-400, -250 + i * 42, 800 - (i % 3) * 90, 18); } c.restore(); }
      if (u > .4) { const a = K.jepit((u - .4) / .6); c.save(); c.globalAlpha = a; pBayang(c, 22, 8, .25); c.fillStyle = '#fff'; K.bulat(c, 40, y0 + 40, W0 - 80, 420, 28); c.fill(); pPolos(c); c.strokeStyle = m.warna; c.lineWidth = 8; K.bulat(c, 40, y0 + 40, W0 - 80, 420, 28); c.stroke();
        const kal = m.isi.split('. ').map((s, i, a) => i < a.length - 1 ? s + '.' : s); let yy = y0 + 90; kal.forEach((s, i) => { const k2 = K.jepit((tt - th - .3 - i * .45) / .3); if (k2 <= 0) return; c.globalAlpha = a * k2; pTeks(c, K, String(i + 1), 82, yy + 4, 34, m.warna === C.pink ? '#c2185b' : C.tinta, { huruf: 'judul', berat: 400 }); yy += pBaris(c, K, s, 120, yy, 36, W0 - 220, C.tinta, 600, 48) + 18; }); c.restore(); }
      return;
    }
    if (tt < th) return;
    if (mode === 'poin') m.isi.forEach((s, i) => { const k = K.jepit((tt - th - i * .32) / .3); if (k <= 0) return; const e = E.outBack(k), yy = y0 + 40 + i * 120; c.save(); c.globalAlpha = K.jepit(k * 3); c.translate((1 - e) * 50, 0); pBayang(c, 14, 5, .18); c.fillStyle = '#fff'; K.bulat(c, 40, yy, W0 - 80, 100, 22); c.fill(); pPolos(c); pCentang(c, 100, yy + 50, 30, C.hijau, k); pTeks(c, K, s, 150, yy + 52, 34, C.tinta, { berat: 700, maks: W0 - 230 }); c.restore(); });
    if (mode === 'tabel') { const col = [190, 250, 240, 180], hd = ['', 'KELEBIHAN', 'KEKURANGAN', 'HARGA'];
      c.save(); pBayang(c, 18, 6, .2); c.fillStyle = '#fff'; K.bulat(c, 30, y0 + 30, W0 - 60, 470, 22); c.fill(); pPolos(c); c.fillStyle = C.tinta; K.bulat(c, 30, y0 + 30, W0 - 60, 80, 22); c.fill(); c.fillRect(30, y0 + 80, W0 - 60, 30);
      let x = 30; hd.forEach((h, i) => { pTeks(c, K, h, x + 18, y0 + 72, 28, i === 1 ? C.hijau : i === 2 ? C.pink : C.kuning, { huruf: 'judul', berat: 400 }); x += col[i]; });
      m.isi.forEach((row, r) => { const k = K.jepit((tt - th - r * .4) / .3); if (k <= 0) return; c.globalAlpha = k; const yy = y0 + 120 + r * 125; if (r % 2 === 0) { c.fillStyle = 'rgba(76,201,240,.12)'; c.fillRect(30, yy, W0 - 60, 125); } let xx = 30; row.forEach((s, i) => { pBaris(c, K, s, xx + 18, yy + 42, 28, col[i] - 28, C.tinta, i === 0 || i === 3 ? 800 : 500, 36); xx += col[i]; }); c.globalAlpha = 1; });
      c.restore(); }
  };
}

/* ── ikon simpan ── */
function pSimpan(c, ly, t, K) {
  const tt = t + K.a.mulai, R = r => pR(K, r); c.translate(pPad, pPad);
  const pu = 1 + .06 * Math.sin(tt * 6), on = tt >= R('L15.w1') + .1;
  c.save(); c.translate(110, 110); c.scale(pu, pu); pBayang(c, 30, 14, .45); c.fillStyle = '#fff'; K.bulat(c, -100, -100, 200, 200, 46); c.fill(); pPolos(c);
  c.strokeStyle = C.tinta; c.fillStyle = C.tinta; c.lineWidth = 12; c.lineJoin = 'round'; c.beginPath(); c.moveTo(-40, -58); c.lineTo(40, -58); c.lineTo(40, 62); c.lineTo(0, 30); c.lineTo(-40, 62); c.closePath(); if (on) c.fill(); c.stroke(); c.restore();
}

/* ── konfigurasi ── */
const KONFIG = {
  judul: 'Jawaban AI Kepanjangan? Pakai Trik Ini',
  rasio: '9:16', fps: 30,
  durasiTarget: [50, 66],
  tema: 'kartu',
  grade: { tint: '#f4e6c8', kuat: .05, saturasi: 1.02, halftone: .05, grain: .07, vinyet: .42, debu: .12, garis: 0, kontras: .1 },
  palet: { kuning: '#FFD23F', merah: '#E63946' },
  sfxPeta: { whoosh: 'whoosh', swish: 'swish', stempel: 'stempel', kertas: 'kertas', pop: 'pop' },
  bunyiMuncul: { teks: 'teks', gambar: 'ikon', benda: 'popup', vol: .5 },
  thumbnail: { t: 'L01.w3' },
  sumber: [
    { fakta: 'Google Gemini for Workspace: format adalah salah satu unsur prompt; minta bentuk hasil seperti poin, tabel, batas panjang', url: 'https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf' },
    { fakta: 'OpenAI: jelaskan format keluaran dan panjang yang diinginkan secara spesifik', url: 'https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api' },
    { fakta: 'Anthropic: beri instruksi yang jelas dan langsung, termasuk bentuk keluaran', url: 'https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct' }
  ]
};

const NAVY = { pola: 'grid', warna: '#051D40', warnaGaris: 'rgba(170,200,255,.13)', jarak: 72 };
const NAVY2 = { pola: 'grid', warna: '#06224a', warnaGaris: 'rgba(170,200,255,.11)', jarak: 90, putar: 1 };
const TOKOH = (kode, o) => Object.assign({ gambar: kode, z: 1.3, bayangan: .45, bunyi: 'swish', rig: ['napas', { jenis: 'goyang', sudut: { amp: 1, periode: 4 } }] }, o);
const JUDUL = (teks, o) => Object.assign({ teks, gaya: 'judul', ukuran: 84, y: 310, lebar: 860, anim: 'luncur' }, o);
const KARTU = (i, besar, o) => Object.assign({ benda: { jenis: 'kustom', lebar: (besar ? 900 : 300) + 120, tinggi: (besar ? 560 : 400) + 120, lukis: pKartuTrik(i, besar) } }, o);
const CHAT = (mode, o) => Object.assign({ benda: { jenis: 'kustom', lebar: 1060, tinggi: 1260, lukis: pChatTrik(mode) }, x: 540, y: 1090, skala: .92 }, o);

const ADEGAN = [
  // 1 hook
  { id: 'hook', mulai: 0, akhir: 'L02', latar: NAVY, kamera: 'dorong-kuat',
    lapis: [
      TOKOH('tokoh-pusing', { x: 540, y: 1250, tinggi: 1200, masuk: { gaya: 'terbang', dari: 'bawah' }, t: .05, jangkar: 'bawah' }),
      { teks: 'JAWABAN AI KEPANJANGAN?', gaya: 'stiker', ukuran: 70, y: 320, lebar: 860, putar: -3, masuk: 'pop', t: 'L01.w1', bunyi: 'salah' },
      { teks: 'pakai *trik ini!*', gaya: 'label', ukuran: 50, y: 500, masuk: 'naik', t: 'L01.w4' }
    ] },
  // 2 tembok teks
  { id: 'tembok', mulai: 'L02', akhir: 'L03', masuk: 'dorong', titikMasuk: [540, 900], latar: NAVY2, kamera: 'dorong', sfx: [{ t: 'L02.w2', berkas: 'notif', vol: .5 }, { t: 'L02.w6', berkas: 'swish', vol: .45 }],
    lapis: [
      { benda: { jenis: 'kustom', lebar: 1060, tinggi: 1120, lukis: pChatPanjang }, x: 540, y: 1100, skala: .94, masuk: { gaya: 'naik' }, t: .05 },
      JUDUL('nanya *singkat* =', { t: 'L02.w2', y: 260, ukuran: 70 })
    ] },
  { id: 'skripsi', mulai: 'L03', akhir: 'L04', masuk: 'geser', arahMasuk: 'atas', latar: NAVY2, kamera: [[0, { zoom: 1.08, y: 60 }], [4, { zoom: 1.2, y: 120 }, 'inOutSine']], sfx: [{ t: 'L03.w1', berkas: 'swish', vol: .45 }],
    lapis: [
      { benda: { jenis: 'kustom', lebar: 1060, tinggi: 1120, lukis: pChatPanjang }, x: 540, y: 1100, skala: .94 },
      { benda: { jenis: 'cap', teks: 'KAYAK SKRIPSI', ukuran: 84, warna: '#E63946' }, x: 540, y: 980, putar: -8, masuk: 'cap', t: 'L03.w3' },
      { teks: 'harus ngerangkum *sendiri*', gaya: 'label', ukuran: 48, y: 300, lebar: 820, masuk: 'naik', t: 'L03.w6', z: .3 }
    ] },
  // 4 solusi: gunting + 3 batasan
  { id: 'gunting', mulai: 'L04', akhir: 'L04.w11', masuk: 'sentak', arahMasuk: 'kanan', latar: NAVY, kamera: 'mundur',
    lapis: [
      TOKOH('tokoh-gunting', { x: 540, y: 1250, tinggi: 1200, masuk: { gaya: 'terbang', dari: 'bawah' }, t: .05, jangkar: 'bawah' }),
      JUDUL('kunci *panjang* & *bentuk*', { t: 'L04.w6', ikut: false, y: 300, ukuran: 76 }),
      { gambar: 'gunting', x: 860, y: 640, lebar: 280, putar: 18, masuk: 'pop', t: 'L04.w5', bunyi: 'ide', hidup: 8 }
    ] },
  { id: 'tiga', mulai: 'L04.w11', akhir: 'L05', masuk: 'tarik', latar: NAVY2, kamera: 'dorong',
    lapis: [
      JUDUL('KUNCI FORMAT AI', { t: .05, y: 300, ukuran: 86 }),
      KARTU(0, false, { x: 205, y: 960, putar: -4, masuk: 'pop', t: 'L04.w15' }),
      KARTU(1, false, { x: 540, y: 1000, putar: 2, masuk: 'pop', t: 'L04.w15+0.25' }),
      KARTU(2, false, { x: 875, y: 960, putar: 4, masuk: 'pop', t: 'L04.w15+0.5' })
    ] },
  // trik 1
  { id: 'trik1', mulai: 'L05', akhir: 'L06', masuk: 'kartu', latar: NAVY, kamera: 'dorong',
    lapis: [ KARTU(0, true, { x: 540, y: 820, putar: -2, masuk: 'pop', t: .05 }), TOKOH('tokoh-tunjuk', { x: 330, y: 1500, tinggi: 820, masuk: { gaya: 'terbang', dari: 'bawah' }, t: 'L05.w2', jangkar: 'bawah' }) ] },
  { id: 'trik1-isi', mulai: 'L06', akhir: 'L07', masuk: 'dorong', titikMasuk: [540, 820], latar: NAVY2, kamera: [[0, { zoom: 1.0, y: 0 }], [6, { zoom: 1.08, y: 60 }, 'inOutSine']],
    sfx: [{ t: 'L06.w3', berkas: 'tuts', vol: .4 }, { t: 'L06.w6', berkas: 'tuts', vol: .4 }, { t: 'L07.w1-0.15', berkas: 'benar', vol: .45 }],
    lapis: [ CHAT('poin'), JUDUL('1. *POIN-POIN*', { t: .05, y: 250, ukuran: 76 }) ] },
  { id: 'trik1-hasil', mulai: 'L07', akhir: 'L08', masuk: 'fokus', latar: NAVY, kamera: [[0, { zoom: 1.12, y: 180 }], [3, { zoom: 1.2, y: 220 }, 'inOutSine']],
    lapis: [ CHAT('poin'), JUDUL('buang *basa-basi*', { t: 'L07.w4', y: 260, ukuran: 78, z: .25 }) ] },
  // trik 2
  { id: 'trik2', mulai: 'L08', akhir: 'L09', masuk: 'sentak', arahMasuk: 'bawah', latar: NAVY, kamera: 'dorong',
    lapis: [ KARTU(1, true, { x: 540, y: 820, putar: 2, masuk: 'pop', t: .05 }), TOKOH('tokoh-aha', { x: 300, y: 1500, tinggi: 820, masuk: { gaya: 'terbang', dari: 'kiri' }, t: 'L08.w2', jangkar: 'bawah' }) ] },
  { id: 'trik2-isi', mulai: 'L09', akhir: 'L10', masuk: 'tutup', arahMasuk: 'kanan', latar: NAVY2, kamera: [[0, { zoom: 1.0, y: 0 }], [7, { zoom: 1.08, y: 80 }, 'inOutSine']],
    sfx: [{ t: 'L09.w8', berkas: 'tuts', vol: .4 }, { t: 'L09.w12', berkas: 'tuts', vol: .4 }, { t: 'L09.w13-0.15', berkas: 'benar', vol: .45 }],
    lapis: [ CHAT('tabel'), JUDUL('2. *TABEL*', { t: .05, y: 250, ukuran: 76 }) ] },
  { id: 'trik2-hasil', mulai: 'L10', akhir: 'L11', masuk: 'zoom', titikMasuk: [540, 1250], latar: NAVY, kamera: [[0, { zoom: 1.12, y: 220 }], [3, { zoom: 1.18, y: 250 }, 'inOutSine']],
    lapis: [ CHAT('tabel'), JUDUL('sekali lirik *paham*', { t: 'L10.w1', y: 270, ukuran: 64, lebar: 800, z: .2 }) ] },
  // trik 3
  { id: 'trik3', mulai: 'L11', akhir: 'L12', masuk: 'geser', arahMasuk: 'kiri', latar: NAVY, kamera: 'dorong',
    lapis: [ KARTU(2, true, { x: 540, y: 820, putar: -2, masuk: 'pop', t: .05 }), { gambar: 'stopwatch', x: 540, y: 860, lebar: 300, putar: -6, masuk: 'pop', t: 'L11.w2', bayangan: .35, hidup: 6 }, TOKOH('tokoh-tunjuk', { x: 330, y: 1500, tinggi: 820, masuk: { gaya: 'terbang', dari: 'bawah' }, t: 'L11.w3', jangkar: 'bawah' }) ] },
  { id: 'trik3-isi', mulai: 'L12', akhir: 'L13', masuk: 'dorong', titikMasuk: [540, 820], latar: NAVY2, kamera: [[0, { zoom: 1.0, y: 0 }], [6, { zoom: 1.08, y: 60 }, 'inOutSine']],
    sfx: [{ t: 'L12.w2', berkas: 'tuts', vol: .4 }, { t: 'L12.w6', berkas: 'tuts', vol: .4 }, { t: 'L13.w1-0.3', berkas: 'whoosh', vol: .45 }],
    lapis: [ CHAT('kalimat'), JUDUL('3. *MAKS. 3 KALIMAT*', { t: .05, y: 250, ukuran: 70 }) ] },
  { id: 'trik3-hasil', mulai: 'L13', akhir: 'L14', masuk: 'kilat', latar: NAVY, kamera: [[0, { zoom: 1.08, y: 120 }], [3, { zoom: 1.16, y: 160 }, 'inOutSine']],
    lapis: [ CHAT('kalimat'), JUDUL('paham dalam *detik*', { t: 'L13.w4', y: 260, ukuran: 76, z: .25 }) ] },
  // hasil
  { id: 'hasil', mulai: 'L14', akhir: 'L15', masuk: 'tutup', arahMasuk: 'bawah', latar: NAVY, kamera: 'mundur',
    lapis: [
      TOKOH('tokoh-kopi', { x: 540, y: 1260, tinggi: 1150, masuk: { gaya: 'terbang', dari: 'bawah' }, t: .05, jangkar: 'bawah' }),
      JUDUL('lebih *rapi*', { t: 'L14.w4', y: 290, ukuran: 90 }),
      { teks: 'hemat waktu baca', gaya: 'label', ukuran: 50, y: 440, masuk: 'naik', t: 'L14.w6', bunyi: 'benar' }
    ] },
  // save
  { id: 'simpan', mulai: 'L15', masuk: 'buka', arahMasuk: 'atas', latar: NAVY2, kamera: 'mundur',
    lapis: [
      TOKOH('tokoh-save', { x: 430, y: 1250, tinggi: 1150, balik: true, masuk: { gaya: 'terbang', dari: 'kiri' }, t: .05, jangkar: 'bawah' }),
      { benda: { jenis: 'kustom', lebar: 340, tinggi: 340, lukis: pSimpan }, x: 830, y: 1240, masuk: 'pop', t: 'L15.w1', bunyi: 'konfirm' },
      { teks: 'SAVE VIDEO INI', gaya: 'stiker', ukuran: 88, y: 330, putar: -2, masuk: 'pop', t: 'L15.w1' },
      { teks: 'biar nggak lupa *triknya!*', gaya: 'label', ukuran: 46, y: 470, masuk: 'naik', t: 'L15.w6' }
    ] }
];
