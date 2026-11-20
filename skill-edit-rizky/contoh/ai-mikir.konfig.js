/* ── Contoh Kolase 1.4: gaya mengikuti VIDEO ACUAN pengguna (references/acuan.md), topik AI. Dipakai sebagai contoh preset 'editorial monokrom'.
   Kartu identitas visual (gaya.md §0.3)
   gaya .......... editorial monokrom: latar abu-putih bervinyet, lengkungan abu besar + garis putus-putus yang bergerak,
                   huruf serif miring kecil di atas huruf tebal besar, kotak sorot hitam, kartu putih bersudut bulat berbayang
   pola cerita ... mitos · aksen: hitam (sorot) + merah #c8202e (NGGAK, halusinasi)
   benda khas .... menu chat AI + keyboard HP mode terang (benda kustom), 3 ubin logo kiriman pengguna
   tanda tangan .. `dorong` ke layar + `glitch` di "NGGAK" dan "HALUSINASI" (adegan gelap satu-satunya)
   beda dari video terakhir: bukan arsip/dosir, tanpa foto Flow, latar terang */
const aiPad = 60;
const T = { ink: '#151515', ink2: '#5a5a5a', ink3: '#9d9d9d', kartu: '#ffffff', layar: '#f4f4f6', tepi: '#dcdce0', isi2: '#ececef', rd: '#c8202e' };
const HB = '"KR Inter","Inter","Segoe UI",Arial,sans-serif', SERIF = 'Georgia,"Times New Roman","Liberation Serif",serif';
const aiR = (K, r) => K.ref(r) + K.a.mulai;
const aiFont = (K, uk, berat) => `${berat || 700} ${uk}px ${K.HURUF.teks}`;
function aiTeks(c, K, s, x, y, uk, warna, o) {
  o = o || {}; c.font = o.serif ? `italic 700 ${uk}px ${SERIF}` : aiFont(K, uk, o.berat); c.fillStyle = warna; c.textAlign = o.rata || 'left'; c.textBaseline = 'middle';
  if (o.maks) c.fillText(s, x, y, o.maks); else c.fillText(s, x, y);
}
function aiSpark(c, x, y, r, warna) { c.fillStyle = warna; c.beginPath(); for (let i = 0; i < 8; i++) { const a = i * Math.PI / 4 - Math.PI / 2, rr = i % 2 ? r * .3 : r; c.lineTo(x + Math.cos(a) * rr, y + Math.sin(a) * rr); } c.closePath(); c.fill(); }
function aiBayang(c, blur, oy, a) { c.shadowColor = `rgba(0,0,0,${a === undefined ? .2 : a})`; c.shadowBlur = blur; c.shadowOffsetY = oy; c.shadowOffsetX = 0; }
function aiTanpaBayang(c) { c.shadowColor = 'transparent'; c.shadowBlur = 0; c.shadowOffsetY = 0; c.shadowOffsetX = 0; }
function aiKartuDasar(x, K, CW, CH, r) {
  x.save(); x.translate(aiPad, aiPad); aiBayang(x, 44, 22, .24); x.fillStyle = T.kartu; K.bulat(x, 0, 0, CW, CH, r); x.fill(); aiTanpaBayang(x);
  x.strokeStyle = T.tepi; x.lineWidth = 3; K.bulat(x, 1.5, 1.5, CW - 3, CH - 3, r - 1); x.stroke(); x.restore();
}

/* ── gaya teks acuan: serif miring kecil + tebal besar + kotak sorot hitam ── */
const KECIL = (teks, o) => Object.assign({ teks, gaya: 'serif', ukuran: 50, lebar: 900, anim: 'luncur', ikut: true }, o);
const BESAR = (teks, o) => Object.assign({ teks, gaya: 'tebal', ukuran: 104, lebar: 900, anim: 'luncur', ikut: true }, o);
const SOROT = (teks, o) => Object.assign({ teks, gaya: 'sorot', ukuran: 66, masuk: 'sapu' }, o);

/* ── layar keyboard HP (mode terang) ─────────────────────────────────────────── */
const aiPeta = (() => {
  const p = {}, y0 = 760, h = 98, st = 110;
  [['qwertyuiop', 15], ['asdfghjkl', 61], ['zxcvbnm', 149]].forEach(([b, x0], r) => [...b].forEach((ch, i) => { p[ch] = { x: x0 + i * 92, y: y0 + r * st, w: 82, h }; }));
  p[','] = { x: 149, y: y0 + 3 * st, w: 82, h }; p[' '] = { x: 241, y: y0 + 3 * st, w: 440, h }; p['.'] = { x: 691, y: y0 + 3 * st, w: 82, h };
  p._shift = { x: 15, y: y0 + 2 * st, w: 124, h }; p._del = { x: 793, y: y0 + 2 * st, w: 132, h }; p._123 = { x: 15, y: y0 + 3 * st, w: 124, h }; p._enter = { x: 783, y: y0 + 3 * st, w: 142, h };
  return p;
})();
const aiKetik = [['selamat ', 'L03.w2', -.1], ['pagi, ', 'L03.w3', .02], ['apa ', 'L03.w4', 0]], aiLangkah = .05;
const aiKetikSeq = R => { const s = []; aiKetik.forEach(([tk, ref, off]) => [...tk].forEach((ch, i) => s.push({ ch, t: R(ref) + off + i * aiLangkah }))); return s; };
const aiSfxKetik = () => {
  const o = []; aiKetik.forEach(([tk, ref, off]) => [...tk].forEach((ch, i) => { const v = off + i * aiLangkah; if (ch !== ' ' && i % 2 === 0) o.push({ t: ref + (v >= 0 ? '+' : '') + v.toFixed(3), berkas: 'tuts', vol: .55 }); }));
  o.push({ t: 'L03.w9-0.12', berkas: 'pop', vol: .7 }); return o;
};
function aiDasarKeyboard(x, w, h, K) {
  const CW = 940, CH = 1260; aiKartuDasar(x, K, CW, CH, 78);
  x.save(); x.translate(aiPad, aiPad);
  x.fillStyle = T.layar; K.bulat(x, 18, 18, CW - 36, CH - 36, 62); x.fill();
  aiTeks(x, K, '09:41', 78, 64, 30, T.ink, { berat: 800 });
  for (let i = 0; i < 4; i++) { x.fillStyle = T.ink; K.bulat(x, 730 + i * 15, 76 - (8 + i * 6), 9, 8 + i * 6, 3); x.fill(); }
  x.strokeStyle = T.ink; x.lineWidth = 3; K.bulat(x, 806, 50, 58, 28, 8); x.stroke(); x.fillStyle = T.ink; K.bulat(x, 811, 55, 44, 18, 4); x.fill(); x.fillRect(866, 58, 5, 12);
  x.fillStyle = '#2b2b2b'; x.beginPath(); x.arc(86, 142, 34, 0, 7); x.fill(); aiTeks(x, K, 'D', 86, 144, 34, '#fff', { rata: 'center', berat: 800 });
  aiTeks(x, K, 'Dina', 140, 130, 36, T.ink, { berat: 800 }); aiTeks(x, K, 'aktif', 140, 166, 24, T.ink3, { berat: 600 });
  x.fillStyle = T.tepi; x.fillRect(18, 192, CW - 36, 2);
  x.fillStyle = T.isi2; K.bulat(x, 52, 232, 380, 92, 34); x.fill(); aiTeks(x, K, 'Udah bangun?', 88, 279, 40, T.ink, { berat: 600 });
  aiBayang(x, 16, 4, .12); x.fillStyle = '#ffffff'; K.bulat(x, 24, 520, 892, 88, 44); x.fill(); aiTanpaBayang(x);
  x.fillStyle = T.ink; x.beginPath(); x.arc(868, 564, 32, 0, 7); x.fill(); x.fillStyle = '#fff'; x.beginPath(); x.moveTo(853, 551); x.lineTo(887, 564); x.lineTo(853, 577); x.lineTo(859, 564); x.closePath(); x.fill();
  x.fillStyle = '#e3e4e8'; K.bulat(x, 15, 640, 910, 84, 20); x.fill(); x.fillStyle = '#c8cad0'; x.fillRect(15 + 303, 656, 2, 52); x.fillRect(15 + 606, 656, 2, 52);
  const khusus = { _shift: 1, _del: 1, _123: 1, _enter: 1 };
  for (const k in aiPeta) {
    const r = aiPeta[k]; x.fillStyle = '#b8bac1'; K.bulat(x, r.x, r.y + 4, r.w, r.h, 16); x.fill();
    x.fillStyle = k === '_enter' ? T.ink : khusus[k] ? '#d4d6dc' : '#ffffff'; K.bulat(x, r.x, r.y, r.w, r.h, 16); x.fill();
    const cx = r.x + r.w / 2, cy = r.y + r.h / 2;
    if (k.length === 1 && k !== ' ') aiTeks(x, K, k, cx, cy + 2, 44, T.ink, { rata: 'center', berat: 600 });
    else if (k === ' ') aiTeks(x, K, 'Indonesia', cx, cy, 26, T.ink3, { rata: 'center', berat: 600 });
    else if (k === '_123') aiTeks(x, K, '?123', cx, cy + 1, 32, T.ink, { rata: 'center', berat: 700 });
    else if (k === '_shift') { x.strokeStyle = T.ink; x.lineWidth = 5; x.lineJoin = 'round'; x.beginPath(); x.moveTo(cx, cy - 20); x.lineTo(cx + 22, cy + 2); x.lineTo(cx + 9, cy + 2); x.lineTo(cx + 9, cy + 20); x.lineTo(cx - 9, cy + 20); x.lineTo(cx - 9, cy + 2); x.lineTo(cx - 22, cy + 2); x.closePath(); x.stroke(); }
    else if (k === '_del') { x.strokeStyle = T.ink; x.lineWidth = 5; x.lineJoin = 'round'; x.beginPath(); x.moveTo(cx - 30, cy); x.lineTo(cx - 12, cy - 20); x.lineTo(cx + 28, cy - 20); x.lineTo(cx + 28, cy + 20); x.lineTo(cx - 12, cy + 20); x.closePath(); x.stroke(); x.beginPath(); x.moveTo(cx - 2, cy - 8); x.lineTo(cx + 16, cy + 8); x.moveTo(cx + 16, cy - 8); x.lineTo(cx - 2, cy + 8); x.stroke(); }
    else if (k === '_enter') { x.strokeStyle = '#fff'; x.lineWidth = 6; x.lineCap = 'round'; x.lineJoin = 'round'; x.beginPath(); x.moveTo(cx + 24, cy - 18); x.lineTo(cx + 24, cy + 6); x.lineTo(cx - 22, cy + 6); x.moveTo(cx - 8, cy - 8); x.lineTo(cx - 22, cy + 6); x.lineTo(cx - 8, cy + 20); x.stroke(); }
  }
  x.restore();
}
function aiLukisKeyboard(c, ly, t, K) {
  const E = K.E, tt = t + K.a.mulai, R = r => aiR(K, r); c.translate(aiPad, aiPad);
  const seq = aiKetikSeq(R), tap = R('L03.w9') - .12, tSel = tap + .14;
  const huruf = seq.filter(s => tt >= s.t).map(s => s.ch).join('') + (tt >= tSel ? 'kabar ' : '');
  if (tt >= R('L02.w4') && tt < R('L03.w2') - .2) { const pu = .5 + .5 * Math.sin(tt * 6); c.strokeStyle = `rgba(20,20,20,${.45 + .45 * pu})`; c.lineWidth = 5; c.setLineDash([16, 10]); K.bulat(c, 9, 634, 922, 96, 26); c.stroke(); c.setLineDash([]); }
  seq.forEach(s => {
    const u = tt - s.t; if (u < 0 || u > .16) return; const r = aiPeta[s.ch]; if (!r) return; const a = 1 - u / .16;
    c.save(); c.globalAlpha = a; c.fillStyle = '#b9bbc2'; K.bulat(c, r.x, r.y, r.w, r.h, 16); c.fill();
    if (s.ch !== ' ') { aiBayang(c, 18, 6, .25); c.fillStyle = '#ffffff'; K.bulat(c, r.x - 10, r.y - 92, r.w + 20, 92, 18); c.fill(); aiTanpaBayang(c); aiTeks(c, K, s.ch, r.x + r.w / 2, r.y - 44, 58, T.ink, { rata: 'center', berat: 800 }); }
    c.restore();
  });
  const fx = 64, fy = 565; c.save(); K.bulat(c, 24, 520, 840, 88, 44); c.clip();
  if (!huruf) aiTeks(c, K, 'Ketik pesan…', fx, fy, 44, T.ink3, { berat: 500 }); else aiTeks(c, K, huruf, fx, fy, 44, T.ink, { berat: 600 });
  const tw = huruf ? c.measureText(huruf).width : 0, aktif = seq.some(s => tt - s.t > -.05 && tt - s.t < .4);
  if (aktif || Math.floor(tt * 2.2) % 2 === 0) { c.fillStyle = T.ink; c.fillRect(fx + tw + 3, fy - 27, 4, 54); }
  c.restore();
  const cur = (!huruf || huruf.endsWith(' ')) ? '' : huruf.split(' ').pop(), prev = huruf.trim().split(' ').pop();
  const tLast = Math.max(0, ...seq.filter(s => tt >= s.t).map(s => s.t), tt >= tSel ? tSel : 0);
  let chips, tengah = true;
  if (!huruf) { chips = ['Halo', 'Hai', 'Oke']; tengah = false; }
  else if (cur) { const tg = ['selamat', 'pagi,', 'apa', 'kabar'].find(k => k.startsWith(cur)) || cur; chips = ['"' + cur + '"', tg.replace(',', ''), ({ selamat: 'selama', 'pagi,': 'paginya', apa: 'apakah' })[tg] || cur + 'a']; }
  else chips = ({ selamat: ['malam', 'pagi', 'siang'], 'pagi,': ['semua', 'apa', 'teman'], apa: ['yang', 'kabar', 'itu'], kabar: ['nih', 'kamu', 'hari ini'] })[prev] || ['', '', ''];
  const sorot = !cur && prev === 'apa' && tt >= R('L03.w5') && tt < tSel + .1, tekan = tt >= tap && tt < tSel + .1;
  chips.forEach((s, i) => {
    const mid = i === 1 && tengah; c.save(); c.translate(15 + 303 * i + 151.5, 682);
    let sk = i === 1 ? .78 + .22 * E.outBack(K.jepit((tt - tLast) / .3)) : 1; if (mid && tekan) sk *= .9; c.scale(sk, sk);
    if (mid && sorot) { c.fillStyle = T.ink; K.bulat(c, -140, -34, 280, 68, 22); c.fill(); }
    aiTeks(c, K, s, 0, 2, 40, mid ? (sorot ? '#fff' : T.ink) : T.ink2, { rata: 'center', berat: mid ? 800 : 600, maks: 270 });
    c.restore();
  });
  if (tt >= tap && tt < tap + .55) { const u = (tt - tap) / .55; c.save(); c.strokeStyle = `rgba(20,20,20,${1 - u})`; c.lineWidth = 6 * (1 - u) + 1; c.beginPath(); c.arc(15 + 303 * 1 + 151.5, 682, 36 + u * 170, 0, 7); c.stroke(); c.restore(); }
}

/* ── menu chat AI (mode terang) ──────────────────────────────────────────────── */
const aiLangit = { tanya: 'Kenapa langit biru?', token: ['Langit', 'tampak', 'biru', 'karena', 'cahaya', 'biru', 'lebih', 'banyak'], kand: [['cahaya', 64], ['sinar', 12], ['udara', 9], ['warna', 5]] };
const aiTokWaktu = R => [R('L07.w6') + .02, R('L07.w7') + .02, R('L07.w8') + .02, R('L07.w10') - .02, R('L08.w9') + .4, R('L08.w9') + .85, R('L08.w9') + 1.3, R('L08.w9') + 1.75];
const aiBuku = { tanya: 'Ringkas novel "Kucing yang Menjaga Matahari" karya Bambang Soedarsono.', jawab: 'Novel ini bercerita tentang seekor kucing di Yogyakarta yang berjuang menjaga matahari. Terbit tahun 1998 dan meraih penghargaan sastra.' };
function aiDasarChat(x, w, h, K) {
  const CW = 940, CH = 980; aiKartuDasar(x, K, CW, CH, 56);
  x.save(); x.translate(aiPad, aiPad);
  x.fillStyle = '#f6f6f8'; K.bulat(x, 3, 3, CW - 6, 120, 54); x.fill(); x.fillRect(3, 60, CW - 6, 63);
  x.fillStyle = T.ink; K.bulat(x, 36, 32, 60, 60, 18); x.fill(); aiSpark(x, 66, 62, 22, '#fff');
  aiTeks(x, K, 'Asisten AI', 118, 62, 38, T.ink, { berat: 800 });
  x.fillStyle = '#2fa84f'; x.beginPath(); x.arc(CW - 128, 62, 7, 0, 7); x.fill(); aiTeks(x, K, 'online', CW - 40, 62, 26, T.ink2, { rata: 'right', berat: 600 });
  x.fillStyle = T.tepi; x.fillRect(3, 122, CW - 6, 2);
  // kolom tulis di bawah (menu chat)
  aiBayang(x, 14, 3, .1); x.fillStyle = '#ffffff'; K.bulat(x, 30, CH - 116, CW - 150, 80, 40); x.fill(); aiTanpaBayang(x); x.strokeStyle = T.tepi; x.lineWidth = 2; K.bulat(x, 30, CH - 116, CW - 150, 80, 40); x.stroke();
  aiTeks(x, K, 'Tanya apa saja…', 66, CH - 76, 32, T.ink3, { berat: 500 });
  x.fillStyle = T.ink; x.beginPath(); x.arc(CW - 70, CH - 76, 38, 0, 7); x.fill(); x.strokeStyle = '#fff'; x.lineWidth = 6; x.lineCap = 'round'; x.lineJoin = 'round'; x.beginPath(); x.moveTo(CW - 70, CH - 58); x.lineTo(CW - 70, CH - 94); x.moveTo(CW - 86, CH - 80); x.lineTo(CW - 70, CH - 96); x.lineTo(CW - 54, CH - 80); x.stroke();
  x.restore();
}
function aiBulatUser(c, K, E, teks, y, u) {
  if (u <= 0) return 0; const f = aiFont(K, 44, 700), maksW = 660; c.font = f; const bs = K.bungkus(teks, f, maksW), lw = Math.max(...bs.map(s => K.lebarTeks(s, f))), bw = lw + 64, bh = bs.length * 60 + 36, e = E.outBack(K.jepit(u));
  c.save(); c.globalAlpha = K.jepit(u * 3); c.translate(0, (1 - e) * 36);
  aiBayang(c, 18, 6, .18); c.fillStyle = T.ink; K.bulat(c, 940 - 30 - bw, y, bw, bh, 34); c.fill(); aiTanpaBayang(c);
  bs.forEach((s, i) => aiTeks(c, K, s, 940 - 30 - bw + 32, y + 18 + 30 + i * 60, 44, '#fff', { berat: 700 })); c.restore(); return bh;
}
function aiAvatar(c, K, x, y) { c.fillStyle = T.ink; c.beginPath(); c.arc(x, y, 32, 0, 7); c.fill(); aiSpark(c, x, y, 20, '#fff'); }
function aiPeluangBaris(c, K, E, tt, daftar, x, y, w, rh, t0, o) {
  o = o || {}; const maks = Math.max(...daftar.map(d => d[1])), lbl = o.lbl || 190, pct = o.pct || 110, uk = o.uk || 40;
  daftar.forEach(([k, p], i) => {
    const u = K.jepit((tt - (t0 + i * .1)) / .45); if (u <= 0) return; const e = E.outCubic(u), yy = y + i * rh, top = i === (o.pilih === undefined ? 0 : o.pilih);
    c.save(); c.globalAlpha = e; aiTanpaBayang(c);
    aiTeks(c, K, k, x, yy + rh / 2, uk, top ? T.ink : T.ink2, { berat: top ? 800 : 600, maks: lbl - 10 });
    const bx = x + lbl, bw = w - lbl - pct, bh = rh * .44, by = yy + rh / 2 - bh / 2;
    c.fillStyle = '#e7e7ea'; K.bulat(c, bx, by, bw, bh, bh / 2); c.fill();
    c.fillStyle = top ? T.ink : '#a9a9ae'; K.bulat(c, bx, by, Math.max(bh, bw * (p / maks) * e), bh, bh / 2); c.fill();
    aiTeks(c, K, Math.round(p * e) + '%', x + w, yy + rh / 2, uk, top ? T.ink : T.ink2, { rata: 'right', berat: 800 });
    c.restore();
  });
}
function aiChatLangit(c, K, E, tt, R) {
  const tTanya = R('L07.w3') - .05, hu = aiBulatUser(c, K, E, aiLangit.tanya, 168, (tt - tTanya) / .4);
  const wkt = aiTokWaktu(R), yA = 168 + hu + 36, bubX = 112, bubW = 800, tDot = R('L07.w4') + .3;
  const f = aiFont(K, 46, 700), tokens = aiLangit.token; c.font = f;
  let px = bubX + 28, py = yA + 28; const pos = [];
  tokens.forEach(s => { const wc = K.lebarTeks(s, f) + 44; if (px + wc > bubX + bubW - 20) { px = bubX + 28; py += 90; } pos.push({ s, x: px, y: py, w: wc }); px += wc + 14; });
  const nampak = pos.filter((p, i) => tt >= wkt[i]), nextIdx = nampak.length, baris = nextIdx ? Math.max(...nampak.map(p => p.y)) - (yA + 28) : 0, bubH = 28 + 76 + baris + 40;
  if (tt >= tDot - .1) {
    aiAvatar(c, K, 58, yA + 40);
    c.save(); c.globalAlpha = K.jepit((tt - tDot + .1) / .25); c.fillStyle = '#f2f2f4'; K.bulat(c, bubX, yA, bubW, bubH, 34); c.fill(); c.strokeStyle = T.tepi; c.lineWidth = 2; K.bulat(c, bubX, yA, bubW, bubH, 34); c.stroke(); c.restore();
    if (!nextIdx) for (let i = 0; i < 3; i++) { const b = Math.sin(tt * 8 - i * .8) * 7; c.fillStyle = T.ink3; c.beginPath(); c.arc(bubX + 56 + i * 30, yA + 42 + b, 8, 0, 7); c.fill(); }
  }
  nampak.forEach((p, i) => {
    const u = K.jepit((tt - wkt[i]) / .3), e = E.outBack(u);
    c.save(); c.translate(p.x + p.w / 2, p.y + 36); c.scale(.6 + .4 * e, .6 + .4 * e); c.globalAlpha = K.jepit(u * 3);
    aiBayang(c, 10, 3, .1); c.fillStyle = u < 1 ? T.ink : '#ffffff'; K.bulat(c, -p.w / 2, -36, p.w, 72, 22); c.fill(); aiTanpaBayang(c);
    c.strokeStyle = T.tepi; c.lineWidth = 2; K.bulat(c, -p.w / 2, -36, p.w, 72, 22); c.stroke();
    aiTeks(c, K, p.s, 0, 2, 46, u < 1 ? '#fff' : T.ink, { rata: 'center', berat: 700 }); c.restore();
  });
  const tP = R('L08.w3'), tPilih = R('L08.w9') - .05, tAkhirP = R('L08.w9') + .45;
  if (tt >= tP && tt < tAkhirP) {
    const u = E.outCubic(K.jepit((tt - tP) / .35)), out = 1 - K.jepit((tt - tPilih - .2) / .25), yp = yA + bubH + 30;
    c.save(); c.globalAlpha = u * out; c.translate(0, (1 - u) * 30);
    aiBayang(c, 30, 12, .18); c.fillStyle = '#ffffff'; K.bulat(c, 112, yp, 800, 420, 36); c.fill(); aiTanpaBayang(c); c.strokeStyle = T.tepi; c.lineWidth = 3; K.bulat(c, 112, yp, 800, 420, 36); c.stroke();
    aiTeks(c, K, 'kata berikutnya setelah “karena”?', 150, yp + 46, 32, T.ink2, { serif: true });
    aiPeluangBaris(c, K, E, tt, aiLangit.kand, 150, yp + 92, 724, 78, tP + .2, { lbl: 190, pct: 100, uk: 38 });
    if (tt >= R('L08.w8')) { c.strokeStyle = T.ink; c.lineWidth = 4; c.setLineDash([12, 8]); K.bulat(c, 138, yp + 96, 750, 72, 22); c.stroke(); c.setLineDash([]); }
    c.restore();
  }
}
function aiChatBuku(c, K, E, tt, R) {
  const tTanya = R('L09.w1') - .6, hu = aiBulatUser(c, K, E, aiBuku.tanya, 168, (tt - tTanya) / .4);
  const f = aiFont(K, 42, 500), bs = K.bungkus(aiBuku.jawab, f, 700), t0 = R('L09.w1') + .1, t1 = R('L09.w12') + .35, total = aiBuku.jawab.length;
  const n = Math.floor(total * K.jepit((tt - t0) / (t1 - t0)));
  const yA = 168 + hu + 36, bubH = bs.length * 60 + 50, salah = tt >= R('L09.w9');
  const aura = K.jepit((tt - R('L09.w4')) / .4) * (1 - K.jepit((tt - R('L09.w7')) / .4));
  aiAvatar(c, K, 58, yA + 40);
  c.save(); if (aura > 0) { c.shadowColor = `rgba(0,0,0,${.35 * aura})`; c.shadowBlur = 50 * aura; c.shadowOffsetY = 10 * aura; }
  c.fillStyle = '#f2f2f4'; K.bulat(c, 112, yA, 800, bubH, 34); c.fill(); aiTanpaBayang(c);
  c.strokeStyle = salah ? T.rd : (aura > 0 ? T.ink : T.tepi); c.lineWidth = salah ? 6 : 3; K.bulat(c, 112, yA, 800, bubH, 34); c.stroke(); c.restore();
  let ct = 0; bs.forEach((s, i) => { const k = Math.max(0, Math.min(s.length, n - ct)); ct += s.length + 1; if (k > 0) aiTeks(c, K, s.slice(0, k), 144, yA + 42 + i * 60, 42, T.ink, { berat: 500 }); });
  if (salah) { const u = E.outBack(K.jepit((tt - R('L09.w9')) / .35)); c.save(); c.translate(690, yA - 20); c.rotate(-.05); c.scale(u, u); c.fillStyle = T.rd; K.bulat(c, -230, -30, 460, 60, 14); c.fill(); aiTeks(c, K, 'BUKU INI TIDAK ADA', 0, 3, 32, '#fff', { rata: 'center', berat: 800 }); c.restore(); }
}
function aiLukisChat(c, ly, t, K, mode) {
  const E = K.E, tt = t + K.a.mulai, R = r => aiR(K, r); c.translate(aiPad, aiPad);
  if (mode === 'langit') aiChatLangit(c, K, E, tt, R); else aiChatBuku(c, K, E, tt, R);
  aiTeks(c, K, mode === 'langit' ? 'ilustrasi · peluang disederhanakan' : 'ilustrasi · buku dan jawaban karangan', 470, 830, 24, T.ink3, { rata: 'center', serif: true });
}

/* ── dua panel: keyboard HP = AI ──────────────────────────────────────────────── */
function aiLukisBanding(c, ly, t, K) {
  const E = K.E, tt = t + K.a.mulai, R = r => aiR(K, r); c.translate(aiPad, aiPad);
  const panel = (px, judul, t0, isi) => {
    const u = K.jepit((tt - t0) / .5); if (u <= 0) return; const e = E.outBack(u);
    c.save(); c.translate(px + 215, 280); c.scale(.7 + .3 * e, .7 + .3 * e); c.translate(-215, -280); c.globalAlpha = K.jepit(u * 2.5);
    aiBayang(c, 36, 16, .2); c.fillStyle = '#ffffff'; K.bulat(c, 0, 0, 430, 560, 40); c.fill(); aiTanpaBayang(c);
    c.strokeStyle = T.tepi; c.lineWidth = 3; K.bulat(c, 1.5, 1.5, 427, 557, 38); c.stroke();
    aiTeks(c, K, judul, 215, 62, 42, T.ink, { rata: 'center', berat: 800 });
    c.fillStyle = T.isi2; K.bulat(c, 24, 112, 382, 76, 38); c.fill(); aiTeks(c, K, 'selamat pagi, apa', 215, 151, 32, T.ink, { rata: 'center', berat: 600 });
    isi(); c.restore();
  };
  panel(0, 'Keyboard HP', R('L04.w2'), () => {
    c.fillStyle = '#e3e4e8'; K.bulat(c, 15, 250, 400, 84, 20); c.fill(); c.fillStyle = '#c8cad0'; c.fillRect(15 + 133, 266, 2, 52); c.fillRect(15 + 266, 266, 2, 52);
    const on = tt >= R('L04.w4');
    ['yang', 'kabar', 'itu'].forEach((s, i) => { if (i === 1 && on) { c.fillStyle = T.ink; K.bulat(c, 15 + 133 + 8, 258, 118, 68, 20); c.fill(); }
      aiTeks(c, K, s, 15 + 133 * i + 66.5, 293, 34, i === 1 && on ? '#fff' : (i === 1 ? T.ink : T.ink2), { rata: 'center', berat: i === 1 ? 800 : 600 }); });
    aiTeks(c, K, 'tebak kata berikutnya', 215, 500, 30, T.ink2, { rata: 'center', serif: true });
  });
  panel(510, 'AI', R('L04.w3'), () => {
    aiPeluangBaris(c, K, E, tt, [['kabar', 68], ['yang', 12], ['itu', 7]], 28, 228, 374, 82, R('L04.w5'), { lbl: 128, pct: 84, uk: 32 });
    aiTeks(c, K, 'tebak kata berikutnya', 215, 500, 30, T.ink2, { rata: 'center', serif: true });
  });
  const ue = K.jepit((tt - R('L04.w10') + .15) / .4);
  if (ue > 0) { const e = E.outBack(ue); c.save(); c.translate(470, 300); c.scale(e, e); aiTeks(c, K, '=', 0, 0, 130, T.ink, { rata: 'center', berat: 900 }); c.restore(); }
}
function aiLukisPeluang(c, ly, t, K) {
  const E = K.E, tt = t + K.a.mulai, R = r => aiR(K, r); c.translate(aiPad, aiPad);
  const CW = 940, CH = 840;
  aiBayang(c, 46, 22, .22); c.fillStyle = '#ffffff'; K.bulat(c, 0, 0, CW, CH, 48); c.fill(); aiTanpaBayang(c);
  c.strokeStyle = T.tepi; c.lineWidth = 3; K.bulat(c, 1.5, 1.5, CW - 3, CH - 3, 46); c.stroke();
  aiSpark(c, 62, 62, 26, T.ink); aiTeks(c, K, 'AI menebak kata berikutnya', 108, 62, 36, T.ink, { berat: 800 });
  c.fillStyle = T.isi2; K.bulat(c, 30, 112, 880, 76, 38); c.fill(); aiTeks(c, K, 'selamat pagi, apa', 70, 151, 38, T.ink, { berat: 600 });
  aiPeluangBaris(c, K, E, tt, [['kabar', 68], ['yang', 11], ['itu', 6], ['saja', 4], ['lagi', 3], ['nih', 2], ['ya', 2]], 40, 214, 860, 84, R('L04.w11'), { lbl: 200, pct: 120, uk: 42 });
  const u = K.jepit((tt - R('L04.w13')) / .5); if (u > 0) { c.globalAlpha = u; aiTeks(c, K, '… dan ribuan kata lain', CW / 2, 214 + 7 * 84 + 34, 34, T.ink2, { rata: 'center', serif: true }); c.globalAlpha = 1; }
}

/* ── data mengalir ke model ────────────────────────────────────────────────────── */
function aiBukuIkon(c, w, h, w1) {
  const cols = ['#2b2b2b', '#8e1c24', '#6a6a6a', '#b4b4b4', '#444444']; c.fillStyle = cols[w1 % 5]; c.beginPath(); c.roundRect(-w / 2, -h / 2, w, h, 9); c.fill();
  c.fillStyle = 'rgba(0,0,0,.28)'; c.fillRect(-w / 2, -h / 2, 15, h); c.fillStyle = 'rgba(255,255,255,.85)'; c.fillRect(-w / 2 + 28, -h / 2 + 24, w - 48, 8); c.fillRect(-w / 2 + 28, -h / 2 + 42, w - 70, 7);
  c.fillStyle = '#f2efe8'; c.fillRect(w / 2 - 8, -h / 2 + 5, 6, h - 10);
}
function aiArtikelIkon(c, w, h) {
  c.fillStyle = '#ffffff'; c.beginPath(); c.roundRect(-w / 2, -h / 2, w, h, 8); c.fill(); c.fillStyle = '#222'; c.fillRect(-w / 2 + 12, -h / 2 + 14, w - 24, 12);
  c.fillStyle = '#9a9a9a'; c.fillRect(-w / 2 + 12, -h / 2 + 36, w * .42, w * .32); for (let i = 0; i < 5; i++) { c.fillStyle = '#cfcfcf'; c.fillRect(-w / 2 + 12 + (i < 3 ? w * .46 : 0), -h / 2 + 36 + (i < 3 ? i * 14 : (i - 3) * 14 + w * .3), i < 3 ? w * .34 : w - 24, 7); }
}
function aiWebIkon(c, w, h) {
  c.fillStyle = '#ffffff'; c.beginPath(); c.roundRect(-w / 2, -h / 2, w, h, 10); c.fill(); c.fillStyle = '#1e1e1e'; c.beginPath(); c.roundRect(-w / 2, -h / 2, w, 24, [10, 10, 0, 0]); c.fill();
  ['#e0e0e0', '#bdbdbd', '#9a9a9a'].forEach((k, i) => { c.fillStyle = k; c.beginPath(); c.arc(-w / 2 + 14 + i * 14, -h / 2 + 12, 4, 0, 7); c.fill(); });
  c.fillStyle = '#5a5a5a'; c.fillRect(-w / 2 + 10, -h / 2 + 34, w - 20, 16); c.fillStyle = '#d6d6d6'; for (let i = 0; i < 3; i++) c.fillRect(-w / 2 + 10 + i * ((w - 20) / 3), -h / 2 + 58, (w - 20) / 3 - 6, h - 70);
}
function aiTeksIkon(c, w) { for (let i = 0; i < 3; i++) { c.fillStyle = `rgba(30,30,30,${.75 - i * .18})`; c.beginPath(); c.roundRect(-w / 2, -24 + i * 18, w * (1 - i * .18), 9, 5); c.fill(); } }
function aiLukisAliran(c, ly, t, K) {
  const E = K.E, tt = t + K.a.mulai, R = r => aiR(K, r), acak = K.acak; const cx = 540, cy = 720;
  const t0 = R('L05.w2'), tb = R('L05.w8'), ta = R('L05.w9'), tw = R('L05.w10'), te = R('L06.w2') - .05, N = 60, jalan = 1.0;
  const items = []; let energi = 0;
  for (let i = 0; i < N; i++) {
    const sp = t0 + (te - t0 - 1.1) * Math.pow(i / N, .85) - .05; let tipe = 'teks';
    if (sp >= tb) { const lst = sp < ta ? ['buku'] : sp < tw ? ['buku', 'artikel'] : ['buku', 'artikel', 'web']; tipe = lst[i % lst.length]; }
    const q = (tt - sp) / jalan; if (q > 0 && q < 1) items.push({ i, q, tipe }); if (q >= 1) energi += Math.exp(-(tt - sp - jalan) * 5);
  }
  energi = Math.min(energi, 2.4);
  const r0 = 130 + energi * 10;
  c.save(); c.translate(cx, cy); c.rotate(tt * .5); c.strokeStyle = 'rgba(30,30,30,.5)'; c.lineWidth = 4; c.setLineDash([22, 18]); c.beginPath(); c.arc(0, 0, r0 + 62, 0, 7); c.stroke(); c.rotate(-tt * 1.1); c.setLineDash([8, 22]); c.beginPath(); c.arc(0, 0, r0 + 108, 0, 7); c.stroke(); c.restore();
  aiBayang(c, 60, 30, .35); const g = c.createRadialGradient(cx - 46, cy - 52, 10, cx, cy, r0); g.addColorStop(0, '#6e6e6e'); g.addColorStop(.45, '#262626'); g.addColorStop(1, '#050505'); c.fillStyle = g; c.beginPath(); c.arc(cx, cy, r0, 0, 7); c.fill(); aiTanpaBayang(c);
  c.fillStyle = 'rgba(255,255,255,.22)'; c.beginPath(); c.ellipse(cx - 40, cy - 60, r0 * .5, r0 * .22, -.5, 0, 7); c.fill();
  aiSpark(c, cx, cy, 58 + energi * 8, '#ffffff');
  items.sort((a, b) => a.q - b.q).forEach(it => {
    const ang = acak(it.i * 3.7 + 1) * Math.PI * 2, R0 = 760, sx = cx + Math.cos(ang) * R0, sy = cy + Math.sin(ang) * R0 * .95;
    const perp = ang + Math.PI / 2, bend = (acak(it.i + 9) - .5) * 520, mx = (sx + cx) / 2 + Math.cos(perp) * bend, my = (sy + cy) / 2 + Math.sin(perp) * bend;
    const q = E.inQuad(it.q) * .85 + it.q * .15, x = (1 - q) * (1 - q) * sx + 2 * (1 - q) * q * mx + q * q * cx, y = (1 - q) * (1 - q) * sy + 2 * (1 - q) * q * my + q * q * cy;
    const sc = 1.4 - 1.05 * q, al = it.q > .86 ? (1 - it.q) / .14 : 1;
    c.save(); c.translate(x, y); c.rotate((acak(it.i + 5) - .5) * 1.2 + q * 2.4); c.scale(sc, sc); c.globalAlpha = al; aiBayang(c, 16, 8, .25);
    if (it.tipe === 'buku') aiBukuIkon(c, 100, 134, it.i); else if (it.tipe === 'artikel') aiArtikelIkon(c, 104, 138); else if (it.tipe === 'web') aiWebIkon(c, 168, 120); else aiTeksIkon(c, 130);
    c.restore();
  });
}

/* ── pola kata berurutan ──────────────────────────────────────────────────────── */
function aiBarisPola(c, K, E, tt, a, b, t0, y, umum) {
  const u = K.jepit((tt - t0) / .6); if (u <= 0) return; const e1 = E.outCubic(K.jepit(u * 2)), e2 = E.outBack(K.jepit(u * 2 - 1));
  c.save(); c.globalAlpha = K.jepit(u * 3); c.translate((1 - e1) * -70, 0);
  if (!umum) { aiBayang(c, 18, 6, .15); c.fillStyle = '#ffffff'; K.bulat(c, 20, y, 330, 100, 50); c.fill(); aiTanpaBayang(c); }
  c.strokeStyle = umum ? T.ink2 : T.tepi; c.lineWidth = 3; if (umum) c.setLineDash([12, 10]); K.bulat(c, 20, y, 330, 100, 50); c.stroke(); c.setLineDash([]);
  aiTeks(c, K, a, 185, y + 52, 46, T.ink, { rata: 'center', berat: 700, serif: umum }); c.restore();
  c.save(); c.strokeStyle = T.ink; c.lineWidth = umum ? 8 : 5; c.lineCap = 'round'; c.lineJoin = 'round';
  const xa = 375, xb = 375 + 190 * e1; c.beginPath(); c.moveTo(xa, y + 50); c.lineTo(xb, y + 50); c.stroke(); if (e1 > .85) { c.beginPath(); c.moveTo(xb - 24, y + 28); c.lineTo(xb + 2, y + 50); c.lineTo(xb - 24, y + 72); c.stroke(); } c.restore();
  if (e2 > 0) { c.save(); c.translate(755, y + 50); c.scale(e2, e2); c.globalAlpha = K.jepit(e2 * 2);
    if (umum) { c.strokeStyle = T.ink; c.lineWidth = 3; c.setLineDash([12, 10]); K.bulat(c, -165, -50, 330, 100, 50); c.stroke(); c.setLineDash([]); }
    else { aiBayang(c, 18, 6, .2); c.fillStyle = T.ink; K.bulat(c, -165, -50, 330, 100, 50); c.fill(); aiTanpaBayang(c); }
    aiTeks(c, K, b, 0, 3, 46, umum ? T.ink : '#ffffff', { rata: 'center', berat: 800, serif: umum }); c.restore(); }
}
function aiLukisPola(c, ly, t, K) {
  const E = K.E, tt = t + K.a.mulai, R = r => aiR(K, r); c.translate(aiPad, aiPad);
  [['terima', 'kasih', R('L06.w4')], ['selamat', 'pagi', R('L06.w5') + .2], ['apa', 'kabar', R('L06.w7') - .1], ['sampai', 'jumpa', R('L06.w9') + .05]].forEach(([a, b, t0], i) => aiBarisPola(c, K, E, tt, a, b, t0, 20 + i * 140, false));
  aiBarisPola(c, K, E, tt, 'kata A', 'kata B', R('L06.w11') - .05, 20 + 4 * 140 + 40, true);
}

/* ── gulungan kata ────────────────────────────────────────────────────────────── */
const aiGulung = ['kabar', 'pagi', 'makan', 'hujan', 'kopi', 'siang', 'bola', 'mobil', 'buku', 'hari', 'malam', 'teman', 'cepat', 'pintar', 'hebat', 'jago'];
function aiLukisGulung(c, ly, t, K) {
  const E = K.E, tt = t + K.a.mulai, R = r => aiR(K, r); c.translate(aiPad, aiPad);
  const CW = 820, CH = 400, t0 = R('L11.w6'), t1 = R('L11.w13') + .1, u = K.jepit((tt - t0) / (t1 - t0)), N = aiGulung.length - 1, off = N * E.outCubic(u), fin = u >= .999;
  aiBayang(c, 40, 20, .24); c.fillStyle = '#ffffff'; K.bulat(c, 0, 0, CW, CH, 44); c.fill(); aiTanpaBayang(c);
  c.save(); K.bulat(c, 0, 0, CW, CH, 44); c.clip();
  c.fillStyle = fin ? T.ink : '#efeff1'; c.fillRect(0, CH / 2 - 62, CW, 124);
  aiGulung.forEach((s, i) => { const d = i - off, ad = Math.abs(d); if (ad > 2.2) return; const y = CH / 2 + d * 124, sk = 1 - Math.min(.45, ad * .22), al = 1 - Math.min(.9, ad * .42);
    c.save(); c.globalAlpha = al; c.translate(CW / 2, y); c.scale(sk, sk); aiTeks(c, K, s, 0, 0, 84, i === N && fin ? '#ffffff' : T.ink, { rata: 'center', berat: 800 }); c.restore(); });
  const g = c.createLinearGradient(0, 0, 0, CH); g.addColorStop(0, 'rgba(255,255,255,.95)'); g.addColorStop(.28, 'rgba(255,255,255,0)'); g.addColorStop(.72, 'rgba(255,255,255,0)'); g.addColorStop(1, 'rgba(255,255,255,.95)'); c.fillStyle = g; c.fillRect(0, 0, CW, CH);
  c.restore(); c.strokeStyle = T.tepi; c.lineWidth = 3; K.bulat(c, 1.5, 1.5, CW - 3, CH - 3, 43); c.stroke();
  c.fillStyle = T.ink; c.beginPath(); c.moveTo(-6, CH / 2); c.lineTo(22, CH / 2 - 16); c.lineTo(22, CH / 2 + 16); c.closePath(); c.fill(); c.beginPath(); c.moveTo(CW + 6, CH / 2); c.lineTo(CW - 22, CH / 2 - 16); c.lineTo(CW - 22, CH / 2 + 16); c.closePath(); c.fill();
}

/* ── cek ulang + ikon teknologi lain ──────────────────────────────────────────── */
function aiLukisCek(c, ly, t, K) {
  const E = K.E, tt = t + K.a.mulai, R = r => aiR(K, r); c.translate(aiPad, aiPad);
  [['Cek sumber resmi', R('L12.w2')], ['Bandingkan dengan sumber lain', R('L12.w4')]].forEach(([s, t0], i) => {
    const u = K.jepit((tt - t0) / .5); if (u <= 0) return; const e = E.outCubic(u), y = i * 170; c.save(); c.globalAlpha = K.jepit(u * 3); c.translate((1 - e) * 80, y);
    aiBayang(c, 30, 12, .18); c.fillStyle = '#ffffff'; K.bulat(c, 0, 0, 860, 140, 40); c.fill(); aiTanpaBayang(c); c.strokeStyle = T.tepi; c.lineWidth = 3; K.bulat(c, 1.5, 1.5, 857, 137, 38); c.stroke();
    c.fillStyle = T.ink; c.beginPath(); c.arc(86, 70, 40, 0, 7); c.fill();
    const k = K.jepit((u - .35) / .5); c.strokeStyle = '#ffffff'; c.lineWidth = 11; c.lineCap = 'round'; c.lineJoin = 'round'; c.beginPath(); const pts = [[66, 72], [82, 88], [110, 54]]; c.moveTo(pts[0][0], pts[0][1]);
    if (k > 0) { const a = Math.min(1, k * 2), b = Math.max(0, k * 2 - 1); c.lineTo(pts[0][0] + (pts[1][0] - pts[0][0]) * a, pts[0][1] + (pts[1][1] - pts[0][1]) * a); if (b > 0) c.lineTo(pts[1][0] + (pts[2][0] - pts[1][0]) * b, pts[1][1] + (pts[2][1] - pts[1][1]) * b); } c.stroke();
    aiTeks(c, K, s, 154, 72, 44, T.ink, { berat: 700, maks: 680 }); c.restore();
  });
}
function aiIkonTek(c, jenis) {
  c.strokeStyle = T.ink; c.fillStyle = T.ink; c.lineWidth = 11; c.lineCap = 'round'; c.lineJoin = 'round';
  if (jenis === 'wifi') { for (let i = 1; i <= 3; i++) { c.beginPath(); c.arc(0, 38, i * 28, -Math.PI * .8, -Math.PI * .2); c.stroke(); } c.beginPath(); c.arc(0, 38, 7, 0, 7); c.fill(); }
  else if (jenis === 'lokasi') { c.beginPath(); c.moveTo(0, 56); c.bezierCurveTo(-52, 6, -46, -52, 0, -52); c.bezierCurveTo(46, -52, 52, 6, 0, 56); c.stroke(); c.beginPath(); c.arc(0, -12, 14, 0, 7); c.stroke(); }
  else if (jenis === 'kamera') { c.beginPath(); c.roundRect(-52, -30, 104, 76, 14); c.stroke(); c.beginPath(); c.arc(0, 8, 22, 0, 7); c.stroke(); c.beginPath(); c.moveTo(-18, -30); c.lineTo(-10, -46); c.lineTo(12, -46); c.lineTo(20, -30); c.stroke(); }
  else if (jenis === 'baterai') { c.beginPath(); c.roundRect(-52, -26, 94, 56, 12); c.stroke(); c.fillRect(48, -10, 10, 24); c.fillRect(-40, -14, 52, 32); }
  else { c.beginPath(); c.arc(-8, -8, 30, 0, 7); c.stroke(); c.beginPath(); c.moveTo(14, 14); c.lineTo(48, 48); c.stroke(); }
}
function aiLukisIkon(c, ly, t, K) {
  const E = K.E, tt = t + K.a.mulai, R = r => aiR(K, r); c.translate(aiPad, aiPad);
  ['wifi', 'lokasi', 'kamera', 'baterai', 'cari'].forEach((j, i) => {
    const t0 = R('L13.w6') + i * .22 - .1, u = K.jepit((tt - t0) / .45); if (u <= 0) return; const e = E.outBack(u);
    c.save(); c.translate(180 + i * 180, 100); c.scale(e, e); c.globalAlpha = K.jepit(u * 3);
    aiBayang(c, 26, 12, .2); c.fillStyle = '#ffffff'; K.bulat(c, -78, -78, 156, 156, 38); c.fill(); aiTanpaBayang(c); c.strokeStyle = T.tepi; c.lineWidth = 3; K.bulat(c, -77, -77, 154, 154, 37); c.stroke();
    aiIkonTek(c, j); c.restore();
  });
}

/* ── konfigurasi ──────────────────────────────────────────────────────────────── */
const KONFIG = {
  judul: 'AI Sebenarnya Nggak Mikir Kayak Manusia',
  rasio: '9:16', fps: 30,
  durasiTarget: [44, 57],
  tema: 'teknologi',
  grade: { tint: '#ffffff', kuat: 0, saturasi: .9, halftone: 0, grain: .06, vinyet: .55, debu: .05, garis: 0, kontras: .08 },
  palet: { kuning: '#c8202e', merah: '#c8202e' },
  sfxPeta: { whoosh: 'whoosh', swish: 'swish', stempel: 'stempel', kertas: 'kertas', pop: 'pop' },
  thumbnail: { t: 'L01.w12+0.25' },
  sumber: [
    { fakta: 'Model bahasa besar = mesin prediksi statistik yang berulang memprediksi kata berikutnya; dilatih dari data raksasa (situs web, artikel, buku)', url: 'https://www.ibm.com/think/topics/large-language-models' },
    { fakta: 'Halusinasi = pernyataan masuk akal tetapi salah yang dihasilkan model bahasa', url: 'https://openai.com/index/why-language-models-hallucinate/' },
    { fakta: 'Why Language Models Hallucinate (Kalai dkk., 2025): pelatihan dan penilaian mendorong model menebak daripada mengaku tidak tahu', url: 'https://arxiv.org/abs/2509.04664' },
    { fakta: 'Survei halusinasi pada model bahasa besar', url: 'https://arxiv.org/abs/2311.05232' },
    { fakta: 'Keyboard HP (Gboard) memakai model bahasa untuk menebak kata', url: 'https://research.google/blog/the-machine-intelligence-behind-gboard/' }
  ]
};

const KARTU_KEYBOARD = { jenis: 'kustom', lebar: 1060, tinggi: 1380, dasar: aiDasarKeyboard, lukis: aiLukisKeyboard };
const KARTU_CHAT = mode => ({ jenis: 'kustom', lebar: 1060, tinggi: 1100, dasar: aiDasarChat, lukis: (c, ly, t, K) => aiLukisChat(c, ly, t, K, mode) });

const ADEGAN = [
  // ── babak 1: hook
  { id: 'hook', mulai: 0, akhir: 'L02+0.5', latar: { pola: 'editorial', varian: 0 }, kamera: [[0, { zoom: 1.0, y: 0 }], [6, { zoom: 1.05, y: -30 }, 'inOutSine']],
    efek: [{ jenis: 'glitch', t: 'L01.w12-0.05', lama: .45, sfx: false }],
    sfx: [{ t: 'L01.w12-0.05', berkas: 'glitch', vol: .8 }],
    lapis: [
            KECIL('Kamu pikir', { y: 300, t: 'L01.w1' }),
      BESAR('mikir kayak manusia?', { y: 420, ukuran: 92, t: 'L01.w8' }),
      { gambar: 'logo-chatgpt', x: 190, y: 930, lebar: 300, putar: -5, masuk: 'pop', t: 'L01.w3', bayangan: .45, hidup: 8 },
      SOROT('ChatGPT', { ukuran: 40, x: 195, y: 1110, masuk: 'naik', t: 'L01.w3+0.12' }),
      { gambar: 'logo-gemini', x: 515, y: 930, lebar: 300, putar: 3, masuk: 'pop', t: 'L01.w4', bayangan: .45, hidup: 8 },
      SOROT('Gemini', { ukuran: 40, x: 515, y: 1110, masuk: 'naik', t: 'L01.w4+0.12' }),
      { gambar: 'logo-claude', x: 840, y: 930, lebar: 300, putar: -3, masuk: 'pop', t: 'L01.w6', bayangan: .45, hidup: 8 },
      SOROT('Claude', { ukuran: 40, x: 835, y: 1110, masuk: 'naik', t: 'L01.w6+0.12' }),
      { teks: '?', gaya: 'elegan', gayaTeks: { warna: '#141414', bayang: false }, ukuran: 210, x: 195, y: 650, masuk: 'pop', t: 'L01.w9', akhir: 'L01.w12', keluar: { gaya: 'susut' }, hidup: 10 },
      { teks: '?', gaya: 'elegan', gayaTeks: { warna: '#141414', bayang: false }, ukuran: 240, x: 515, y: 630, masuk: 'pop', t: 'L01.w10', akhir: 'L01.w12', keluar: { gaya: 'susut' }, hidup: 10 },
      { teks: '?', gaya: 'elegan', gayaTeks: { warna: '#141414', bayang: false }, ukuran: 210, x: 835, y: 650, masuk: 'pop', t: 'L01.w10+0.18', akhir: 'L01.w12', keluar: { gaya: 'susut' }, hidup: 10 },
      { benda: { jenis: 'cap', teks: 'NGGAK', ukuran: 190, warna: '#c8202e' }, x: 515, y: 930, putar: -9, masuk: 'cap', t: 'L01.w12-0.05' }
    ] },
  // ── babak 2: keyboard HP
  { id: 'hp1', mulai: 'L02+0.5', akhir: 'L03', masuk: 'dorong', titikMasuk: [540, 930], latar: { pola: 'editorial', varian: 1 }, kamera: 'dorong',
    lapis: [
            { benda: KARTU_KEYBOARD, skala: .98, x: 540, y: 1130, masuk: { gaya: 'terbang', dari: 'bawah' }, t: .05, hidup: 5 },
      KECIL('mirip fitur', { y: 250, t: 'L02.w3' }),
      BESAR('tebak kata', { y: 360, t: 'L02.w5' })
    ] },
  { id: 'hp2', mulai: 'L03', akhir: 'L04', masuk: 'fokus', latar: { pola: 'editorial', varian: 1 }, kamera: [[0, { zoom: 1.04, y: 40 }], [5.2, { zoom: 1.16, y: 110 }, 'inOutSine']],
    sfx: aiSfxKetik(),
    lapis: [
            { benda: KARTU_KEYBOARD, skala: .98, x: 540, y: 1130, hidup: 5 },
      KECIL('keyboard langsung', { y: 260, t: 'L03.w6', z: .25 }),
      SOROT('nebak', { y: 370, ukuran: 84, t: 'L03.w8', z: .25 })
    ] },
  // ── babak 3: cara kerja
  { id: 'sama', mulai: 'L04', akhir: 'L04.w10+0.45', masuk: 'tarik', titikMasuk: [540, 1000], latar: { pola: 'editorial', varian: 2 }, kamera: 'dorong',
    sfx: [{ t: 'L04.w10-0.15', berkas: 'pop', vol: .6 }],
    lapis: [
            KECIL('melakukan', { y: 270, t: 'L04.w7' }),
      BESAR('hal yang sama', { y: 380, ukuran: 96, t: 'L04.w8' }),
      { gambar: 'logo-chatgpt', x: 270, y: 640, lebar: 215, putar: -4, masuk: 'pop', t: 'L04.w3', bayangan: .45, hidup: 6 },
      { gambar: 'logo-gemini', x: 540, y: 640, lebar: 215, putar: 3, masuk: 'pop', t: 'L04.w4', bayangan: .45, hidup: 6 },
      { gambar: 'logo-claude', x: 810, y: 640, lebar: 215, putar: -3, masuk: 'pop', t: 'L04.w6', bayangan: .45, hidup: 6 },
      { benda: { jenis: 'kustom', lebar: 1060, tinggi: 700, lukis: aiLukisBanding }, x: 540, y: 1230, masuk: { gaya: 'naik' }, t: .05 }
    ] },
  { id: 'canggih', mulai: 'L04.w10+0.45', akhir: 'L05.w2', masuk: 'sentak', arahMasuk: 'kanan', latar: { pola: 'editorial', varian: 3 }, kamera: 'dorong-kuat',
    lapis: [
            KECIL('tapi jauh lebih', { y: 250, t: 'L04.w11' }),
      SOROT('canggih', { y: 360, ukuran: 90, t: 'L04.w14' }),
      { benda: { jenis: 'kustom', lebar: 1060, tinggi: 960, lukis: aiLukisPeluang }, x: 540, y: 1110, skala: .95, masuk: { gaya: 'geser', dari: 'bawah' }, t: .05 }
    ] },
  { id: 'data', mulai: 'L05.w2', akhir: 'L06.w2', masuk: 'tutup', arahMasuk: 'bawah', latar: { pola: 'editorial', varian: 4 }, kamera: 'dorong',
    lapis: [
            { benda: { jenis: 'kustom', lebar: 1080, tinggi: 1500, lukis: aiLukisAliran }, x: 540, y: 1000, cek: false },
      KECIL('dilatih dari teks dalam jumlah', { y: 250, t: 'L05.w2' }),
      BESAR('raksasa', { y: 360, ukuran: 112, t: 'L05.w7' }),
      SOROT('buku', { ukuran: 50, x: 200, y: 1340, putar: -3, masuk: 'pop', t: 'L05.w8' }),
      SOROT('artikel', { ukuran: 50, x: 470, y: 1340, putar: 2, masuk: 'pop', t: 'L05.w9' }),
      SOROT('website', { ukuran: 50, x: 765, y: 1340, putar: -2, masuk: 'pop', t: 'L05.w10' })
    ] },
  { id: 'pola', mulai: 'L06.w2', akhir: 'L07', masuk: 'buka', arahMasuk: 'atas', latar: { pola: 'editorial', varian: 2 }, kamera: 'dorong',
    lapis: [
            KECIL('mereka belajar', { y: 250, t: 'L06.w3' }),
      BESAR('pola', { y: 360, ukuran: 120, t: 'L06.w5' }),
      SOROT('setelah kata apa', { y: 480, ukuran: 46, t: 'L06.w11' }),
      { benda: { jenis: 'kustom', lebar: 1060, tinggi: 940, lukis: aiLukisPola }, x: 540, y: 1120, masuk: { gaya: 'naik' }, t: .05 }
    ] },
  { id: 'tanya', mulai: 'L07', akhir: 'L08', masuk: 'geser', arahMasuk: 'kiri', latar: { pola: 'editorial', varian: 0 }, kamera: 'dorong',
    sfx: [{ t: 'L07.w3-0.05', berkas: 'notif', vol: .55 }, { t: 'L07.w6+0.02', berkas: 'pop', vol: .45 }, { t: 'L07.w7+0.02', berkas: 'pop', vol: .45 }, { t: 'L07.w8+0.02', berkas: 'pop', vol: .45 }, { t: 'L07.w10-0.02', berkas: 'pop', vol: .45 }],
    lapis: [
            KECIL('AI menyusun jawaban', { y: 250, t: 'L07.w5' }),
      BESAR('sepotong demi sepotong', { y: 370, ukuran: 84, t: 'L07.w8' }),
      { benda: KARTU_CHAT('langit'), x: 540, y: 1090, masuk: { gaya: 'terbang', dari: 'bawah' }, t: .05, hidup: 4 }
    ] },
  { id: 'pilih', mulai: 'L08', akhir: 'L09', masuk: 'dorong', titikMasuk: [520, 1050], latar: { pola: 'editorial', varian: 0 }, kamera: [[0, { zoom: 1.0, y: 0 }], [3, { zoom: 1.08, y: 60 }, 'inOutSine']],
    sfx: [{ t: 'L08.w9+0.32', berkas: 'pop', vol: .5 }, { t: 'L08.w9+0.77', berkas: 'pop', vol: .4 }],
    lapis: [
            KECIL('memilih kata berikutnya', { y: 260, t: 'L08.w4' }),
      SOROT('yang paling cocok', { y: 370, ukuran: 70, t: 'L08.w7' }),
      { benda: KARTU_CHAT('langit'), x: 540, y: 1090, hidup: 4 }
    ] },
  // ── babak 4: twist
  { id: 'yakin', mulai: 'L09', akhir: 'L10', masuk: 'tutup', arahMasuk: 'kanan', latar: { pola: 'editorial', varian: 3 }, kamera: 'dorong',
    sfx: [{ t: 'L09.w1-0.6', berkas: 'notif', vol: .5 }],
    lapis: [
            KECIL('terdengar pintar banget,', { y: 240, t: 'L09.w4' }),
      BESAR('tapi kadang salah', { y: 340, ukuran: 84, t: 'L09.w7' }),
      SOROT('dengan sangat yakin', { y: 450, ukuran: 54, t: 'L09.w10' }),
      { benda: KARTU_CHAT('buku'), x: 540, y: 1100, masuk: { gaya: 'terbang', dari: 'bawah' }, t: .05, hidup: 4 }
    ] },
  { id: 'halusinasi', mulai: 'L10', akhir: 'L11.w3', masuk: 'glitch', latar: { pola: 'editorial', varian: 1, gelap: true }, kamera: 'dorong-kuat',
    efek: [{ jenis: 'guncang', t: 'L10.w2', lama: .35, kuat: 1 }, { jenis: 'glitch', t: 'L10.w2-0.1', lama: .35, sfx: false }],
    sfx: [{ t: 'L10.w2-0.1', berkas: 'glitch', vol: .85 }],
    lapis: [
            { benda: KARTU_CHAT('buku'), x: 540, y: 1100, alfa: .18, blur: 8, z: .5 },
      KECIL('Istilahnya:', { y: 420, t: 'L10.w1', gayaTeks: { warna: '#f2f2f2', bayang: false } }),
      { benda: { jenis: 'cap', teks: 'HALUSINASI', ukuran: 122, warna: '#e0303d' }, x: 540, y: 660, putar: -6, masuk: 'cap', t: 'L10.w2-0.12' },
      SOROT('masuk akal, tapi salah', { y: 880, ukuran: 46, t: 'L10.w2+0.25', gayaTeks: { kotak: '#f2f2f2', warna: '#111111' } })
    ] },
  // ── babak 5: kesimpulan + penutup
  { id: 'otak', mulai: 'L11.w3', akhir: 'L12', masuk: 'tarik', latar: { pola: 'editorial', varian: 4 }, kamera: 'dorong',
    sfx: [{ t: 'L11.w13+0.1', berkas: 'pop', vol: .6 }],
    lapis: [
            BESAR('OTAK', { y: 440, ukuran: 240, anim: 'muncul', ikut: false, masuk: 'pop', t: 'L11.w5' }),
      { coret: 'silang', x: 540, y: 450, lebar: 600, tinggi: 260, warna: 'merah', tebal: 18, t: 'L11.w5+0.2', lama: .5 },
      KECIL('tapi', { y: 640, t: 'L11.w6' }),
      SOROT('mesin penebak kata', { y: 740, ukuran: 70, t: 'L11.w7' }),
      { benda: { jenis: 'kustom', lebar: 940, tinggi: 520, lukis: aiLukisGulung }, x: 540, y: 1150, masuk: { gaya: 'naik' }, t: 'L11.w6' }
    ] },
  { id: 'cek', mulai: 'L12', akhir: 'L13', masuk: 'geser', arahMasuk: 'bawah', latar: { pola: 'editorial', varian: 2 }, kamera: 'dorong',
    lapis: [
            KECIL('Tetap', { y: 300, t: 'L12.w1' }),
      BESAR('cek ulang', { y: 410, ukuran: 112, t: 'L12.w2' }),
      { benda: { jenis: 'kustom', lebar: 980, tinggi: 360, lukis: aiLukisCek }, x: 540, y: 960, masuk: { gaya: 'naik' }, t: .05 },
      { coret: 'centang', x: 540, y: 1260, lebar: 340, tinggi: 260, warna: 'hitam', tebal: 22, t: 'L12.w4+0.1', lama: .55 }
    ] },
  { id: 'follow', mulai: 'L13', masuk: 'sentak', arahMasuk: 'bawah', latar: { pola: 'editorial', varian: 3 }, kamera: 'dorong',
    lapis: [
            KECIL('cara kerja', { y: 330, t: 'L13.w4' }),
      BESAR('teknologi lain', { y: 440, ukuran: 100, t: 'L13.w6' }),
      { teks: 'FOLLOW', gaya: 'stiker', ukuran: 118, y: 740, masuk: 'pop', t: 'L13.w1', putar: -3 },
      { benda: { jenis: 'kustom', lebar: 1080, tinggi: 280, lukis: aiLukisIkon }, x: 540, y: 1120, t: .05 }
    ] }
];
