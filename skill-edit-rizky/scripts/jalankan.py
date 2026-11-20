"""Alat bantu Claude untuk skill skill-edit-rizky (salinan jalankan.py skill cerita-html + penanaman gambar/klip).

Videonya sendiri tetap SATU file HTML mandiri: animasi, cek kualitas, dan encoder MP4 (WebCodecs) ada di
dalam HTML, jadi pengguna cukup membukanya di Chrome/Edge lalu menekan "Ekspor MP4". Skrip ini merakit file
itu (konfig + gambar Flow + suara), membuat narasi (ElevenLabs / Edge TTS), dan "menekan tombolnya" di browser
tanpa layar (Playwright), supaya Claude bisa melihat bingkai sendiri dan mengunggah otomatis.

  rakit ... --gambar DIR [--maks 2400] [--klip nama=video.mp4[@12]]
            --gambar: semua .png/.jpg/.webp di DIR ditanam sebagai WebP (sisi terpanjang â‰¤ --maks px; PNG transparan
                      tetap transparan); di konfig dipakai sebagai { gambar: '<nama berkas tanpa ekstensi>' }
            --klip:   video pendek (mis. klip Flow) dipecah jadi urutan bingkai WebP 12 fps â†’ { urutan: 'nama' }
                      atau foto hidup { gambar: 'pelat', klip: { kode: 'nama', t } }; nama=klip.mp4@15:hijau = klip berlatar
                      hijau polos dibuang latarnya per bingkai (potongan bergerak, transparan); lihat references/klip.md

  suara     <naskah.txt> <folder_audio> [--edge] [--suara ID] [--model eleven_v3] [--stabil 0.5] [--perkiraan] [--tanpa-eja]
            (ElevenLabs: angka dieja Indonesia dan singkatan dibaca per huruf sebelum dikirim, supaya tidak berlogat Inggris)
            â†’ narasi.mp3 + kata.json (waktu tiap kata, relatif ke awal berkas) + ringkasan tempo
  kata      <naskah.txt> <rekaman.mp3|wav|m4a> <kata.json> [--model small]
            â†’ waktu tiap kata dari REKAMAN SENDIRI (Whisper lokal, disejajarkan ke naskah); pakai sebagai --kata di rakit
  rakit     <konfig.js> <keluar.html> [--naskah naskah.txt --narasi narasi.mp3 --kata kata.json] [--baris DIR]
            [--musik musik.mp3 --vol-musik 0.3] [--sfx DIR] [--rapatkan 0.4] [--laju-narasi 1.2] [--mulai 0.05]
            --laju-narasi: percepat tempo narasi tanpa mengubah nada (WSOLA di dalam HTML) bila TTS terlalu lambat
  cek       <film.html>                      cek kualitas + rumus cerita (JSON), kode keluar 0 = BERES
  kontak    <film.html> <keluar.jpg> [--n 24 | --t 1,2.5,4]
  bingkai   <film.html> <detik> <keluar.png>
  thumbnail <film.html> <keluar.png>
  ekspor    <film.html> <keluar.mp4> [--fps 30]

naskah.txt: satu baris narasi per baris ("L01 | Teks â€¦"); urutannya = urutan di rekaman. Baris berawalan # = catatan
            (sumber, arahan) dan tidak ikut dibaca; "# babak 3" menandai babak untuk baris-baris sesudahnya.
--baris DIR: berkas L01.mp3, L02.mp3, â€¦ (satu berkas per baris) dipasangkan ke id yang sama di naskah.
--sfx DIR:   semua berkas audio di DIR ditanam sebagai SFX berkas (nama = nama berkas tanpa ekstensi):
             di konfig dipakai sebagai sfx { t, berkas: 'tawa', vol, lama, ulang }.

Di PC Windows ini panggil dengan Python312 (alias "python" rusak):
  C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -X utf8 scripts\\jalankan.py â€¦
"""
import argparse, base64, io, json, mimetypes, os, re, sys, time, urllib.error, urllib.request
from pathlib import Path

AKAR = Path(__file__).resolve().parent.parent
TEMPLAT = AKAR / 'assets' / 'templat.html'
KUNCI_FILE = Path(r'D:\automation\Video AI\_elevenlabs\api_key.txt')
SUARA_BAWAAN = 'nPczCjzI2devNBz1zQrb'   # Brian (suara bawaan ElevenLabs; teruji bahasa Indonesia dengan eleven_v3)
EDGE_BAWAAN = 'id-ID-ArdiNeural'


def data_uri(berkas):
    p = Path(berkas)
    tipe = mimetypes.guess_type(p.name)[0] or 'audio/mpeg'
    return f'data:{tipe};base64,' + base64.b64encode(p.read_bytes()).decode('ascii')


def baca_naskah(berkas):
    baris, babak = [], None
    for s in [x.strip() for x in Path(berkas).read_text(encoding='utf-8').splitlines()]:
        if not s:
            continue
        if s.startswith('#'):
            m = re.match(r'#\s*babak\s*(\d+)', s, re.I)
            if m:
                babak = int(m.group(1))
            continue
        m = re.match(r'^\s*([A-Za-z]{1,4}\d{1,3})\s*[|:]\s*(.+)$', s)
        b = {'id': m.group(1), 'teks': m.group(2).strip()} if m else {'id': f'L{len(baris) + 1:02d}', 'teks': s}
        if babak is not None:
            b['babak'] = babak
        baris.append(b)
    return baris


def teks_ucap(baris):
    """teks yang dibacakan: tanpa penanda *aksen*"""
    return ' '.join(b['teks'].replace('*', '') for b in baris)


# ---------------------------------------------------------------- ejaan untuk TTS (ElevenLabs)
# Suara bawaan (Brian) berlogat Inggris: angka dan singkatan bisa dibaca bahasa Inggris ("twelve", "em-pee-ar").
# Maka teks yang dikirim ke TTS dieja Indonesia (12 -> "dua belas", MPR -> "Em Pe Er"), dan waktu kata dikembalikan
# ke token ASLI naskah (subtitle dan rujukan L01.w3 tidak berubah).
_SATUAN = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
_HURUF = {'A': 'A', 'B': 'Be', 'C': 'Ce', 'D': 'De', 'E': 'E', 'F': 'Ef', 'G': 'Ge', 'H': 'Ha', 'I': 'I', 'J': 'Je', 'K': 'Ka', 'L': 'El', 'M': 'Em',
          'N': 'En', 'O': 'O', 'P': 'Pe', 'Q': 'Ki', 'R': 'Er', 'S': 'Es', 'T': 'Te', 'U': 'U', 'V': 'Ve', 'W': 'We', 'X': 'Eks', 'Y': 'Ye', 'Z': 'Zet'}
_BACA_SEBAGAI_KATA = {'ASEAN', 'NASA', 'UNESCO', 'COVID', 'SIM', 'OPEC', 'FIFA'}  # singkatan yang dibaca sebagai kata


def terbilang(n):
    if n < 10: return [_SATUAN[n]]
    if n == 10: return ['sepuluh']
    if n == 11: return ['sebelas']
    if n < 20: return [_SATUAN[n - 10], 'belas']
    if n < 100:
        t, r = divmod(n, 10); return [_SATUAN[t], 'puluh'] + ([_SATUAN[r]] if r else [])
    if n < 200: return ['seratus'] + (terbilang(n - 100) if n > 100 else [])
    if n < 1000:
        h, r = divmod(n, 100); return [_SATUAN[h], 'ratus'] + (terbilang(r) if r else [])
    if n < 2000: return ['seribu'] + (terbilang(n - 1000) if n > 1000 else [])
    if n < 1_000_000:
        k, r = divmod(n, 1000); return terbilang(k) + ['ribu'] + (terbilang(r) if r else [])
    if n < 1_000_000_000:
        j, r = divmod(n, 1_000_000); return terbilang(j) + ['juta'] + (terbilang(r) if r else [])
    return [_SATUAN[int(c)] for c in str(n)]


def eja_token(tok):
    """satu token naskah -> daftar kata yang diucapkan (tanda baca ikut di kata pertama/terakhir)"""
    m = re.match(r'^([^\w]*)(.*?)([^\w]*)$', tok, re.S)
    depan, inti, belakang = m.group(1), m.group(2), m.group(3)
    if inti.isdigit() and len(inti) <= 12 and not (len(inti) > 1 and inti[0] == '0'):
        kata = terbilang(int(inti))
    elif inti.isalpha() and inti.isupper() and 2 <= len(inti) <= 4 and inti not in _BACA_SEBAGAI_KATA:
        kata = [_HURUF[c] for c in inti if c in _HURUF]
    else:
        return [tok]
    kata[0] = depan + kata[0]; kata[-1] = kata[-1] + belakang
    return kata


def teks_eja(baris):
    """(teks untuk TTS, [(token asli, jumlah kata ucap)]); teks_ucap() = versi tanpa ejaan"""
    asli = teks_ucap(baris).split()
    ucap, grup = [], []
    for t in asli:
        k = eja_token(t); ucap.extend(k); grup.append((t, len(k)))
    return ' '.join(ucap), grup


def kembalikan_token(kata_ucap, grup):
    """kelompokkan kata ucap kembali ke token naskah asli (waktu = awal kata pertama .. akhir kata terakhir)"""
    if len(kata_ucap) != sum(n for _, n in grup):
        return kata_ucap  # tidak cocok: pakai apa adanya
    out, i = [], 0
    for tok, n in grup:
        seg = kata_ucap[i:i + n]; i += n
        out.append([seg[0][0], seg[-1][1], tok])
    return out


# ---------------------------------------------------------------- suara
def huruf_ke_kata(teks, mulai, akhir):
    """waktu per huruf (alignment ElevenLabs) â†’ [[mulai, akhir, kata], ...] dipisah spasi"""
    kata, cur, a, z = [], '', None, None
    for ch, s, e in zip(teks, mulai, akhir):
        if ch.isspace():
            if cur:
                kata.append([round(a, 3), round(z, 3), cur]); cur = ''
            continue
        if not cur:
            a = s
        cur += ch; z = e
    if cur:
        kata.append([round(a, 3), round(z, 3), cur])
    return kata


def ringkas_tempo(kata, label):
    if not kata:
        print(f'{label}: tanpa waktu kata'); return
    jeda = max((kata[i][0] - kata[i - 1][1], kata[i - 1][1]) for i in range(1, len(kata))) if len(kata) > 1 else (0, 0)
    dur = kata[-1][1] - kata[0][0]
    print(f'{label}: {len(kata)} kata, suara {kata[0][0]:.2f}â€“{kata[-1][1]:.2f} dtk ({dur:.1f} dtk), '
          f'{len(kata) / max(.1, dur / 60):.0f} kata/menit, jeda antar-kata terpanjang {jeda[0]:.2f} dtk di {jeda[1]:.2f} dtk')
    print('  (jeda â‰¤ Â±1 dtk masih bisa dirapatkan mesin ke 0,4 dtk; durasi video â‰ˆ suara + 0,3 dtk setelah rapat)')
    if dur > 64:
        print(f'  terlalu panjang untuk 55â€“65 dtk: rakit dengan --laju-narasi {dur / 60:.2f} (tempo dipercepat tanpa mengubah nada),'
              ' atau pendekkan naskah Â±' + str(round(len(kata) * (1 - 60 / dur))) + ' kata')


def suara_eleven(a, baris, keluar):
    teks, grup = (teks_ucap(baris), None) if a.tanpa_eja else teks_eja(baris)
    if a.perkiraan:
        print(f'perkiraan kredit ElevenLabs: Â±{len(teks)} karakter ({len(baris)} baris, {len(teks.split())} kata)'); return
    kunci = os.environ.get('ELEVENLABS_API_KEY') or (KUNCI_FILE.read_text(encoding='utf-8').strip() if KUNCI_FILE.exists() else '')
    if not kunci:
        sys.exit(f'kunci ElevenLabs tidak ada ({KUNCI_FILE} atau ELEVENLABS_API_KEY)')
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{a.suara or SUARA_BAWAAN}/with-timestamps?output_format=mp3_44100_128'
    badan = {'text': teks, 'model_id': a.model, 'language_code': 'id', 'voice_settings': {'stability': a.stabil, 'similarity_boost': .8}}
    if a.kecepatan:
        badan['voice_settings']['speed'] = a.kecepatan
    req = urllib.request.Request(url, data=json.dumps(badan).encode(), headers={'xi-api-key': kunci, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f'ElevenLabs menolak: {e.code} {e.read()[:400]!r}')
    (keluar / 'narasi.mp3').write_bytes(base64.b64decode(d['audio_base64']))
    al = d.get('alignment') or d.get('normalized_alignment') or {}
    kata = huruf_ke_kata(al.get('characters', []), al.get('character_start_times_seconds', []), al.get('character_end_times_seconds', []))
    if grup:
        kata = kembalikan_token(kata, grup)
    (keluar / 'kata.json').write_text(json.dumps(kata, ensure_ascii=False), encoding='utf-8')
    print(f'ok {keluar / "narasi.mp3"} Â· {len(teks)} karakter Â· model {a.model}')
    ringkas_tempo(kata, 'ElevenLabs')


def suara_edge(a, baris, keluar):
    import asyncio
    import edge_tts
    teks = teks_ucap(baris)

    async def jalan():
        kom = edge_tts.Communicate(teks, a.suara or EDGE_BAWAAN, rate=a.laju, boundary='WordBoundary')
        audio, kata = bytearray(), []
        async for ch in kom.stream():
            if ch['type'] == 'audio':
                audio.extend(ch['data'])
            elif ch['type'] == 'WordBoundary':
                m = ch['offset'] / 1e7
                kata.append([round(m, 3), round(m + ch['duration'] / 1e7, 3), ch['text']])
        return bytes(audio), kata
    audio, kata = asyncio.run(jalan())
    (keluar / 'narasi.mp3').write_bytes(audio)
    # Edge memecah tanda baca/angka berbeda dari naskah: samakan jumlah kata dengan naskah bila bisa
    kata_naskah = teks.split()
    if len(kata) != len(kata_naskah) or any(' ' in k[2] for k in kata):
        kata = samakan_kata(kata, kata_naskah)
    (keluar / 'kata.json').write_text(json.dumps(kata, ensure_ascii=False), encoding='utf-8')
    print(f'ok {keluar / "narasi.mp3"} Â· Edge {a.suara or EDGE_BAWAAN} Â· laju {a.laju}')
    ringkas_tempo(kata, 'Edge TTS')


def samakan_kata(kata, naskah):
    """sejajarkan waktu kata TTS ke kata naskah. Edge kadang menggabungkan token ("Agustus 1995", "55 menit") atau
    membaca angka/singkatan berbeda: token bergabung dipecah menurut panjang huruf, lalu dicocokkan dengan difflib
    (sama seperti perintah `kata`); kata naskah yang tak cocok mendapat rentang token pengganti atau diinterpolasi.
    (Versi lama yang rakus bergeser satu kata di setiap token gabungan; diganti 18 Nov 2026.)"""
    import difflib
    norm = lambda s: re.sub(r'[^0-9a-zÃ -Ã¿]', '', s.lower())
    pecah = []
    for a, z, s in kata:
        bag = s.split()
        if len(bag) > 1:
            tot, c = sum(max(1, len(b)) for b in bag), a
            for b in bag:
                d = (z - a) * max(1, len(b)) / tot; pecah.append([c, c + d, b]); c += d
        else:
            pecah.append([a, z, s])
    ref, hyp = [norm(k) for k in naskah], [norm(k[2]) for k in pecah]
    waktu = [None] * len(naskah)
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ref, hyp, autojunk=False).get_opcodes():
        if tag == 'equal':
            for d in range(i2 - i1):
                waktu[i1 + d] = (pecah[j1 + d][0], pecah[j1 + d][1])
        elif tag == 'replace':
            a0, a1 = pecah[j1][0], pecah[j2 - 1][1]
            bobot = [max(1, len(ref[i])) for i in range(i1, i2)]; tot = sum(bobot); c = a0
            for i, b in zip(range(i1, i2), bobot):
                waktu[i] = (c, c + (a1 - a0) * b / tot); c += (a1 - a0) * b / tot
    n, i = len(naskah), 0
    while i < n:
        if waktu[i] is None:
            j = i
            while j < n and waktu[j] is None:
                j += 1
            t0 = waktu[i - 1][1] if i > 0 else (pecah[0][0] if pecah else 0.0)
            t1 = waktu[j][0] if j < n else (pecah[-1][1] if pecah else t0)
            bobot = [max(1, len(ref[k])) for k in range(i, j)]; tot = sum(bobot); c = t0
            for k, b in zip(range(i, j), bobot):
                waktu[k] = (c, c + max(0.04, (t1 - t0) * b / tot)); c += (t1 - t0) * b / tot
            i = j
        else:
            i += 1
    hasil, akhir = [], 0.0
    for w_, (s, e) in zip(naskah, waktu):
        s = max(s, akhir); e = max(e, s + 0.04); hasil.append([round(s, 3), round(e, 3), w_]); akhir = e
    return hasil


def suara(a):
    baris = baca_naskah(a.naskah)
    keluar = Path(a.folder); keluar.mkdir(parents=True, exist_ok=True)
    (suara_edge if a.edge else suara_eleven)(a, baris, keluar)


def kata_dari_rekaman(a):
    """Waktu tiap kata dari REKAMAN SENDIRI: faster-whisper (lokal, offline) mentranskrip rekaman, lalu hasilnya disejajarkan
    ke kata naskah (difflib; kata yang tak terdengar/berbeda diinterpolasi). Keluaran = kata.json sama bentuknya dengan TTS."""
    import difflib, subprocess, wave
    import numpy as np
    import imageio_ffmpeg
    from faster_whisper import WhisperModel
    wav = Path(a.keluar).with_suffix('.16k.wav')
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error', '-i', str(a.rekaman), '-ac', '1', '-ar', '16000', str(wav)], check=True)
    with wave.open(str(wav)) as wf:
        audio = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    wav.unlink()
    try:
        model = WhisperModel(a.model, device='cpu', compute_type='int8', local_files_only=True)
    except Exception:
        model = WhisperModel(a.model, device='cpu', compute_type='int8')
    seg, _ = model.transcribe(audio, language='id', word_timestamps=True, vad_filter=False, beam_size=5)
    hyp = [(w.word.strip(), float(w.start), float(w.end)) for s in seg for w in s.words if w.word.strip()]
    if not hyp:
        sys.exit('Whisper tidak menemukan suara di rekaman itu.')
    naskah = teks_ucap(baca_naskah(a.naskah)).split()
    norm = lambda s: re.sub(r'[^0-9a-zÃ -Ã¿]', '', s.lower())
    refs, hyps = [norm(w) for w in naskah], [norm(h[0]) for h in hyp]
    sm = difflib.SequenceMatcher(None, refs, hyps, autojunk=False)
    waktu = [None] * len(naskah)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for d in range(i2 - i1):
                waktu[i1 + d] = (hyp[j1 + d][1], hyp[j1 + d][2])
        elif tag == 'replace':
            a0, a1 = hyp[j1][1], hyp[j2 - 1][2]
            bobot = [max(1, len(refs[i])) for i in range(i1, i2)]; tot = sum(bobot); c = a0
            for i, b in zip(range(i1, i2), bobot):
                waktu[i] = (c, c + (a1 - a0) * b / tot); c += (a1 - a0) * b / tot
    cocok = sum(b.size for b in sm.get_matching_blocks())
    # kata naskah yang tak terdengar: isi dengan interpolasi di celah antar-kata terdekat
    n, i = len(naskah), 0
    while i < n:
        if waktu[i] is None:
            j = i
            while j < n and waktu[j] is None:
                j += 1
            t0 = waktu[i - 1][1] if i > 0 else 0.0
            t1 = waktu[j][0] if j < n else hyp[-1][2]
            bobot = [max(1, len(refs[k])) for k in range(i, j)]; tot = sum(bobot); c = t0
            for k, b in zip(range(i, j), bobot):
                waktu[k] = (c, c + max(0.04, (t1 - t0) * b / tot)); c += (t1 - t0) * b / tot
            i = j
        else:
            i += 1
    kata, akhir = [], 0.0
    for w, (s, e) in zip(naskah, waktu):
        s = max(s, akhir); e = max(e, s + 0.04); kata.append([round(s, 3), round(e, 3), w]); akhir = e
    Path(a.keluar).write_text(json.dumps(kata, ensure_ascii=False), encoding='utf-8')
    print(f'ok {a.keluar} Â· {len(kata)} kata naskah, {len(hyp)} kata terdengar, cocok persis {cocok} ({cocok / max(1, len(naskah)) * 100:.0f}%)')
    ringkas_tempo(kata, 'Rekaman')
    if cocok / max(1, len(naskah)) < .7:
        print('  PERINGATAN: kurang dari 70% kata cocok â€” rekaman berbeda dari naskah? Waktu kata hasil interpolasi, cek lembar kontak lebih teliti.')


# ---------------------------------------------------------------- gambar + klip
def gambar_uri(berkas, maks=1700, kualitas=86):
    from PIL import Image
    im = Image.open(berkas)
    im.load()
    alfa = im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info)
    im = im.convert('RGBA' if alfa else 'RGB')
    if alfa and im.getextrema()[3][0] >= 250:
        im = im.convert('RGB'); alfa = False
    s = min(1, maks / max(im.size))
    if s < 1:
        im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, 'WEBP', quality=kualitas, method=5)
    return 'data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode('ascii')


def kunci_hijau(berkas_bingkai, tol=1.0):
    """Klip berlatar hijau polos (Flow) -> bingkai RGBA transparan, dipangkas ke kotak gabungan semua bingkai
    (rumus sama dengan potong_latar.py, tapi warna kunci dari bingkai pertama dan tanpa pangkas per bingkai
    supaya subjek tidak bergeser-geser)."""
    import numpy as np
    from PIL import Image, ImageFilter
    def kroma(a):
        r, g, b = a[..., 0], a[..., 1], a[..., 2]
        return -0.168736 * r - 0.331264 * g + 0.5 * b, 0.5 * r - 0.418688 * g - 0.081312 * b
    a0 = np.asarray(Image.open(berkas_bingkai[0]).convert('RGB'), dtype=np.float32) / 255.0
    t = max(3, min(a0.shape[:2]) // 200)
    kunci = np.median(np.concatenate([a0[:t].reshape(-1, 3), a0[-t:].reshape(-1, 3), a0[:, :t].reshape(-1, 3), a0[:, -t:].reshape(-1, 3)]), axis=0)
    kcb, kcr = kroma(kunci); km = float(np.hypot(kcb, kcr))
    if km < 0.12:
        print('  peringatan: latar klip tidak hijau/biru polos; hasil kunci bisa memakan subjek')
    kc = int(np.argmax(kunci)); lain = [i for i in range(3) if i != kc]; ek = float(kunci[kc] - max(kunci[lain[0]], kunci[lain[1]]))
    hasil, kotak = [], None
    for f in berkas_bingkai:
        a = np.asarray(Image.open(f).convert('RGB'), dtype=np.float32) / 255.0
        cb, cr = kroma(a); d = np.hypot(cb - kcb, cr - kcr)
        al = np.clip((d - .2 * km * tol) / max(1e-6, .2 * km * tol), 0, 1); al = al * al * (3 - 2 * al)
        if ek > .3:
            lebih = a[..., kc] - np.maximum(a[..., lain[0]], a[..., lain[1]])
            ax = 1 - np.clip((lebih - .12 / tol) / max(1e-6, .55 * ek / tol - .12 / tol), 0, 1)
            al = np.minimum(al, ax * ax * (3 - 2 * ax))
        al[al < .03] = 0
        tm = (al > .02) & (al < .98); am = np.maximum(al[tm], .08)[:, None]
        a[tm] = np.clip((a[tm] - (1 - am) * kunci) / am, 0, 1)
        batas = np.maximum(a[..., lain[0]], a[..., lain[1]])
        a[..., kc] = np.where(al < .98, np.minimum(a[..., kc], batas + .02), a[..., kc])
        im = Image.fromarray((a * 255).astype(np.uint8), 'RGB'); im.putalpha(Image.fromarray((al * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.6)))
        bb = im.getchannel('A').point(lambda v: 255 if v > 12 else 0).getbbox()
        if bb:
            kotak = bb if kotak is None else (min(kotak[0], bb[0]), min(kotak[1], bb[1]), max(kotak[2], bb[2]), max(kotak[3], bb[3]))
        hasil.append(im)
    if kotak:
        w, h = hasil[0].size; p = int(.015 * max(w, h))
        kotak = (max(0, kotak[0] - p), max(0, kotak[1] - p), min(w, kotak[2] + p), min(h, kotak[3] + p))
        hasil = [im.crop(kotak) for im in hasil]
    return hasil


def pecah_klip(berkas, fps=12, maks=1700, hijau=False):
    import subprocess, tempfile
    import imageio_ffmpeg
    with tempfile.TemporaryDirectory() as d:
        subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error', '-i', str(berkas), '-vf', f'fps={fps},scale=\'min({maks},iw)\':-2',
                        str(Path(d) / 'b%04d.png')], check=True)
        bingkai = sorted(Path(d).glob('b*.png'))
        if hijau:
            for i, im in enumerate(kunci_hijau(bingkai)):
                im.save(Path(d) / f'k{i:04d}.png')
            bingkai = sorted(Path(d).glob('k*.png'))
        hasil = [gambar_uri(f, maks, 80) for f in bingkai]
    print(f'klip {Path(berkas).name}: {len(hasil)} bingkai @ {fps} fps{" · latar hijau dibuang" if hijau else ""}')
    return hasil


# ---------------------------------------------------------------- rakit
def rakit(a):
    tpl = TEMPLAT.read_text(encoding='utf-8')
    konfig = Path(a.konfig).read_text(encoding='utf-8')
    if '</script' in konfig.lower():
        sys.exit('konfig tidak boleh berisi </script>')
    awal = tpl.index('\n<script id="konfig">') + len('\n<script id="konfig">')
    akhir = tpl.index('</script>', awal)
    html = tpl[:awal] + '\n' + konfig.strip() + '\n' + tpl[akhir:]
    suara_ = None
    if a.naskah:
        suara_ = {'mulai': a.mulai, 'baris': baca_naskah(a.naskah)}
        if a.narasi:
            suara_['narasi'] = {'src': data_uri(a.narasi), 'mulai': a.mulai}
        if a.kata:
            suara_['kata'] = json.loads(Path(a.kata).read_text(encoding='utf-8'))
            suara_['kataRelatif'] = True
        if a.rapatkan is not None:
            suara_['rapatkan'] = a.rapatkan if a.rapatkan > 0 else False
        if a.laju_narasi:
            suara_['laju'] = a.laju_narasi
        if a.baris:
            d = Path(a.baris)
            for b in suara_['baris']:
                cocok = [f for f in d.iterdir() if f.stem.lower() == b['id'].lower()]
                if cocok:
                    b['src'] = data_uri(cocok[0])
    if a.musik:
        suara_ = suara_ or {}
        suara_['musik'] = {'src': data_uri(a.musik), 'vol': a.vol_musik}
    if a.sfx:
        suara_ = suara_ or {}
        suara_['sfxBerkas'] = {f.stem: data_uri(f) for f in sorted(Path(a.sfx).iterdir()) if f.suffix.lower() in ('.mp3', '.wav', '.ogg', '.m4a')}
    if suara_ is not None:
        blok = json.dumps(suara_, ensure_ascii=False).replace('</', '<\\/')
        html = re.sub(r'<script id="data-suara" type="application/json">.*?</script>',
                      lambda _: f'<script id="data-suara" type="application/json">{blok}</script>', html, count=1, flags=re.S)
    if a.gambar or a.klip:
        data = {}
        if a.gambar:
            for f in sorted(Path(a.gambar).iterdir()):
                if f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.webp') and not f.stem.startswith('_'):
                    data[f.stem] = gambar_uri(f, a.maks)
        for k in a.klip or []:
            nama, berkas = k.split('=', 1)
            hijau = berkas.endswith(':hijau')
            if hijau:
                berkas = berkas[:-len(':hijau')]
            fps = 12
            if '@' in berkas and berkas.rsplit('@', 1)[1].isdigit():
                berkas, fps = berkas.rsplit('@', 1); fps = int(fps)
            data[nama] = {'urutan': pecah_klip(berkas, fps, min(a.maks, 1920), hijau), 'fps': fps}
            if hijau:
                data[nama]['alfa'] = True
        blok = json.dumps(data).replace('</', '<\\/')
        html = re.sub(r'<script id="data-gambar" type="application/json">.*?</script>',
                      lambda _: f'<script id="data-gambar" type="application/json">{blok}</script>', html, count=1, flags=re.S)
        print(f'gambar tertanam: {len(data)} ({", ".join(list(data)[:30])})')
    judul = re.search(r"judul:\s*'([^']+)'", konfig)
    if judul:
        html = re.sub(r'<title>.*?</title>', lambda _: f'<title>{judul.group(1)}</title>', html, count=1)
    Path(a.keluar).write_text(html, encoding='utf-8')
    print(f'ok {a.keluar} ({len(html) / 1e6:.1f} MB)')


# ---------------------------------------------------------------- browser tanpa layar
def buka(html, lebar=600, tinggi=1000):
    from playwright.sync_api import sync_playwright
    pw = sync_playwright().start()
    br = None
    for opsi in ({}, {'channel': 'chrome'}, {'channel': 'msedge'}, {'executable_path': '/opt/pw-browsers/chromium'}):
        try:
            br = pw.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'], **opsi)
            break
        except Exception:
            continue
    if br is None:
        sys.exit('Browser tidak ditemukan. Buka file HTML-nya di Chrome/Edge lalu tekan tombol di bawah video.')
    pg = br.new_page(viewport={'width': lebar, 'height': tinggi})
    pg.set_default_timeout(0)
    log = []
    pg.on('console', lambda m: m.type in ('error', 'warning') and log.append(f'[{m.type}] {m.text}'))
    pg.on('pageerror', lambda e: log.append(f'[galat] {e}'))
    pg.goto(Path(html).resolve().as_uri() + '?render')
    try:
        pg.wait_for_function('window.SIAP === true', timeout=120000)
    except Exception:
        print('\n'.join(log) or 'Halaman tidak siap (cek galat JavaScript di blok konfig).')
        raise
    return pw, br, pg, log


def tutup(pw, br, log):
    if log:
        print('\n'.join(log[:20]))
    br.close(); pw.stop()


def ambil_kanvas(pg, t):
    d = pg.evaluate("t => { seek(t); return document.getElementById('kanvas').toDataURL('image/png') }", t)
    from PIL import Image
    return Image.open(io.BytesIO(base64.b64decode(d.split(',')[1]))).convert('RGB')


def cek(a):
    pw, br, pg, log = buka(a.html)
    r = pg.evaluate('hasilCek()')
    print(json.dumps(r, ensure_ascii=False, indent=1))
    print('BERES' if r['beres'] else 'BELUM BERES')
    tutup(pw, br, log)
    sys.exit(0 if r['beres'] else 1)


def kontak(a):
    from PIL import Image, ImageDraw
    pw, br, pg, log = buka(a.html)
    dur = pg.evaluate('DURATION')
    waktu = [float(x) for x in a.t.split(',')] if a.t else [dur * (i + .5) / a.n for i in range(a.n)]
    ubin = []
    for t in waktu:
        im = ambil_kanvas(pg, t)
        lb = 300 if im.height > im.width else 480
        im = im.resize((lb, round(im.height * lb / im.width)))
        ImageDraw.Draw(im).text((8, 6), f'{t:.1f}s', fill=(255, 255, 0))
        ubin.append(im)
    w, h = ubin[0].size
    kol = min(6 if h > w else 4, len(ubin)); bar = (len(ubin) + kol - 1) // kol
    L = Image.new('RGB', (w * kol, h * bar), (17, 17, 17))
    for i, im in enumerate(ubin):
        L.paste(im, ((i % kol) * w, (i // kol) * h))
    L.save(a.keluar, quality=86)
    print('ok', a.keluar, f'durasi {dur:.2f} dtk')
    tutup(pw, br, log)


def bingkai(a):
    pw, br, pg, log = buka(a.html)
    ambil_kanvas(pg, float(a.detik)).save(a.keluar)
    print('ok', a.keluar)
    tutup(pw, br, log)


def thumbnail(a):
    pw, br, pg, log = buka(a.html)
    d = pg.evaluate('thumbnail()')
    Path(a.keluar).write_bytes(base64.b64decode(d.split(',')[1]))
    print('ok', a.keluar)
    tutup(pw, br, log)


def ekspor(a):
    pw, br, pg, log = buka(a.html)
    t0 = time.time()
    tipe, isi = pg.evaluate("""async fps => {
      const blob = await eksporMP4({ fps: fps || undefined });
      const buf = new Uint8Array(await blob.arrayBuffer()); let s = '';
      for (let i = 0; i < buf.length; i += 0x8000) s += String.fromCharCode.apply(null, buf.subarray(i, i + 0x8000));
      return [blob.type, btoa(s)];
    }""", a.fps)
    keluar = Path(a.keluar)
    keluar.parent.mkdir(parents=True, exist_ok=True)
    if 'webm' in tipe:
        keluar = keluar.with_suffix('.webm')
    keluar.write_bytes(base64.b64decode(isi))
    print(f'ok {keluar} ({keluar.stat().st_size / 1e6:.1f} MB, {time.time() - t0:.0f} dtk, {tipe})')
    tutup(pw, br, log)
    if keluar.suffix == '.mp4':
        periksa_awal_audio(keluar)


def periksa_awal_audio(berkas, detik=0.6):
    """Encoder AAC bawaan Windows pernah menghasilkan LEDAKAN di 0,1 dtk pertama (18 Nov 2026, "Siaran TV Pertama Indonesia":
    sampel sampai 24x batas maksimum tepat saat narasi mulai, padahal campuran audio sebelum encode aman ±0,89).
    Setelah ekspor, beberapa ratus ms pertama didekode; bila ada sampel > 1,3 (batas wajar overshoot AAC), bagian itu
    dibisukan sampai sebelum sampel wajar pertama + fade-in 25 ms, dan audio dikodekan ulang (gambar disalin)."""
    import subprocess, tempfile
    import numpy as np
    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    with tempfile.TemporaryDirectory() as d:
        mentah = Path(d) / 'awal.f32'
        subprocess.run([ff, '-v', 'error', '-y', '-i', str(berkas), '-vn', '-t', str(detik), '-f', 'f32le', '-ac', '2', '-ar', '48000', str(mentah)], check=True)
        a = np.fromfile(mentah, dtype='<f4')
        if not len(a):
            return
        buruk = np.flatnonzero(np.abs(a) > 1.3)
        if not len(buruk):
            print(f'audio awal aman (puncak {np.abs(a).max():.2f})')
            return
        akhir = (buruk[-1] // 2) / 48000 + 0.015        # detik terakhir yang rusak (+ 15 ms)
        print(f'PERINGATAN: ledakan audio di awal (puncak {np.abs(a).max():.1f}x, sampai {akhir:.3f} dtk) — memperbaiki otomatis')
        asli = berkas.with_name(berkas.stem + '-asli' + berkas.suffix)
        berkas.replace(asli)
        subprocess.run([ff, '-v', 'error', '-y', '-i', str(asli), '-c:v', 'copy', '-af',
                        f"volume=enable='lt(t,{akhir:.3f})':volume=0,afade=t=in:st={akhir:.3f}:d=0.025", '-c:a', 'aac', '-b:a', '192k',
                        '-movflags', '+faststart', str(berkas)], check=True)
        print(f'ok audio diperbaiki: {berkas} (salinan asli: {asli.name}; hapus bila sudah dicek)')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='perintah', required=True)
    p = sub.add_parser('suara'); p.add_argument('naskah'); p.add_argument('folder')
    p.add_argument('--edge', action='store_true'); p.add_argument('--suara'); p.add_argument('--model', default='eleven_v3')
    p.add_argument('--stabil', type=float, default=0.5); p.add_argument('--kecepatan', type=float)
    p.add_argument('--laju', default='+8%'); p.add_argument('--perkiraan', action='store_true'); p.add_argument('--tanpa-eja', action='store_true'); p.set_defaults(f=suara)
    p = sub.add_parser('kata'); p.add_argument('naskah'); p.add_argument('rekaman'); p.add_argument('keluar'); p.add_argument('--model', default='small'); p.set_defaults(f=kata_dari_rekaman)
    p = sub.add_parser('rakit'); p.add_argument('konfig'); p.add_argument('keluar')
    p.add_argument('--naskah'); p.add_argument('--narasi'); p.add_argument('--kata'); p.add_argument('--baris'); p.add_argument('--mulai', type=float, default=0.05)
    p.add_argument('--rapatkan', type=float); p.add_argument('--laju-narasi', type=float); p.add_argument('--sfx')
    p.add_argument('--musik'); p.add_argument('--vol-musik', type=float, default=0.3)
    p.add_argument('--gambar'); p.add_argument('--maks', type=int, default=2400); p.add_argument('--klip', action='append'); p.set_defaults(f=rakit)
    p = sub.add_parser('cek'); p.add_argument('html'); p.set_defaults(f=cek)
    p = sub.add_parser('kontak'); p.add_argument('html'); p.add_argument('keluar'); p.add_argument('--n', type=int, default=24); p.add_argument('--t'); p.set_defaults(f=kontak)
    p = sub.add_parser('bingkai'); p.add_argument('html'); p.add_argument('detik'); p.add_argument('keluar'); p.set_defaults(f=bingkai)
    p = sub.add_parser('thumbnail'); p.add_argument('html'); p.add_argument('keluar'); p.set_defaults(f=thumbnail)
    p = sub.add_parser('ekspor'); p.add_argument('html'); p.add_argument('keluar'); p.add_argument('--fps', type=int, default=0); p.set_defaults(f=ekspor)
    a = ap.parse_args()
    a.f(a)


if __name__ == '__main__':
    main()
