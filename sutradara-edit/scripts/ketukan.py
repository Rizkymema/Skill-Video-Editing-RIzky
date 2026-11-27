"""Peta ketukan musik: BPM, ketukan, awal birama, energi, bagian (tenang/naik/puncak/turun), drop, hening,
dan SARAN titik potong yang bervariasi (ketukan -> tahan -> antisipasi -> hantam -> lepas), bukan semua di ketukan.

Pakai:
  python -X utf8 -I scripts/ketukan.py <musik.mp3|wav|mp4> [--keluar ketukan.json] [--kata kata.json]
                                       [--mulai S] [--sampai S] [--bpm-kira 100] [--konfig]
                                       [--potongan ringkasan.json|potongan.json]

  --kata      waktu kata narasi ([[mulai, akhir, "kata"], ...] dari jalankan.py suara/kata): hantaman diutamakan
              di sela narasi >= 0,25 dtk supaya bunyi/potongan keras tidak menimpa kata.
  --konfig    cetak `const KETUKAN = {...}` untuk ditempel di kepala konfig.js
              (waktu MUTLAK sejak video mulai; di dalam adegan kurangi a.mulai, lihat pustaka/audio/musik.md).
  --potongan  analisis acuan: daftar detik potongan (JSON list) atau ringkasan.json dari bedah_acuan.py;
              dicetak berapa persen potongan jatuh di ketukan / awal birama / tidak di ketukan.
  --mulai/--sampai  potong bagian musik yang dipakai (detik di berkas). Semua waktu keluaran dihitung dari --mulai.

Tanpa librosa: ffmpeg (PATH atau imageio_ffmpeg) + numpy. Deterministik.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np

SR = 22050
HOP = 512
NFFT = 2048
FPS_ENV = SR / HOP  # ±43 bingkai amplop per detik


def ffmpeg_exe():
    if shutil.which('ffmpeg'):
        return shutil.which('ffmpeg')
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        sys.exit('ffmpeg tidak ditemukan (pasang imageio-ffmpeg atau tambahkan ffmpeg ke PATH)')


def baca_audio(p, mulai=0.0, sampai=None):
    cmd = [ffmpeg_exe(), '-v', 'error']
    if mulai:
        cmd += ['-ss', str(mulai)]
    cmd += ['-i', str(p)]
    if sampai:
        cmd += ['-t', str(max(0.1, sampai - mulai))]
    cmd += ['-vn', '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-']
    raw = subprocess.run(cmd, capture_output=True).stdout
    x = np.frombuffer(raw, np.float32).astype(np.float64)
    if x.size < SR:
        sys.exit(f'audio terlalu pendek / tidak terbaca: {p}')
    return x


def stft_mag(x):
    """bingkai TERPUSAT: bingkai i berpusat di i*HOP (jadi waktu bingkai = i / FPS_ENV tanpa geser)"""
    x = np.pad(x, (NFFT // 2, NFFT // 2))
    win = np.hanning(NFFT)
    n = 1 + (len(x) - NFFT) // HOP
    idx = np.arange(NFFT)[None, :] + HOP * np.arange(n)[:, None]
    return np.abs(np.fft.rfft(x[idx] * win, axis=1)) / (win.sum() / 2)  # [bingkai, bin], sinus penuh ±1


def amplop_onset(mag):
    """spectral flux per pita log (40 Hz–10 kHz, 48 pita) dalam dB (lantai −80 dB dari puncak), disearah setengah
    gelombang, dirata-rata antar pita; versi bass (< 160 Hz) untuk kick/hentakan"""
    f = np.fft.rfftfreq(NFFT, 1 / SR)
    tepi = np.geomspace(40, 10000, 49)
    p = mag ** 2
    pita = np.stack([p[:, (f >= a) & (f < b)].sum(1) for a, b in zip(tepi[:-1], tepi[1:])], 1)
    db = 10 * np.log10(pita + 1e-12)
    db = np.maximum(db, db.max() - 80)
    d = np.maximum(0, np.diff(db, axis=0))
    d = np.vstack([np.zeros((1, d.shape[1])), d])
    bass = d[:, tepi[1:] <= 160].mean(1)
    full = d.mean(1)

    def norm(e):
        k = int(FPS_ENV * .5) | 1
        lok = np.convolve(e, np.ones(k) / k, 'same')
        e = np.maximum(0, e - lok)
        return e / (e.max() + 1e-9)
    return norm(full), norm(bass)


def tempo(env, bpm_kira=110.0):
    e = env - env.mean()
    ac = np.correlate(e, e, 'full')[len(e) - 1:]
    lag_min, lag_max = int(FPS_ENV * 60 / 200), int(FPS_ENV * 60 / 55)
    lags = np.arange(lag_min, min(lag_max, len(ac) - 1))
    bpm = 60 * FPS_ENV / lags
    prior = np.exp(-0.5 * (np.log2(bpm / bpm_kira) / 0.9) ** 2)  # condong ke bpm_kira, lebar ±1 oktaf
    skor = ac[lags] * prior
    i = int(np.argmax(skor))
    if 0 < i < len(lags) - 1:  # interpolasi parabola
        a, b, c = skor[i - 1], skor[i], skor[i + 1]
        geser = 0.5 * (a - c) / (a - 2 * b + c + 1e-12)
    else:
        geser = 0
    lag = lags[i] + geser
    return 60 * FPS_ENV / lag, lag


def lacak_ketukan(env, lag, ketat=100.0):
    """pelacak ketukan pemrograman dinamis (Ellis 2007)"""
    n = len(env)
    skor = env.copy()
    asal = -np.ones(n, int)
    p = lag
    for t in range(n):
        a, b = int(t - 2 * p), int(t - p / 2)
        if b <= 0:
            continue
        a = max(0, a)
        prev = np.arange(a, b)
        jarak = t - prev
        biaya = -ketat * (np.log(jarak / p)) ** 2
        k = skor[prev] + biaya
        j = int(np.argmax(k))
        skor[t] = env[t] + k[j]
        asal[t] = prev[j]
    akhir = int(np.argmax(skor[max(0, n - int(2 * p)):]) + max(0, n - int(2 * p)))
    ket = [akhir]
    while asal[ket[-1]] >= 0:
        ket.append(asal[ket[-1]])
    ket = np.array(ket[::-1])
    return ket[env[ket] > 0.02] if len(ket) > 8 else ket


def energi_db(x, langkah=0.25):
    n = int(SR * langkah)
    m = len(x) // n
    rms = np.sqrt((x[: m * n].reshape(m, n) ** 2).mean(1) + 1e-12)
    return 20 * np.log10(rms), langkah


def halus(v, k):
    k = max(1, int(k)) | 1
    pad = np.pad(v, (k // 2, k // 2), mode='edge')
    return np.convolve(pad, np.ones(k) / k, 'valid')


def db_halus(db, langkah, dtk):
    """kenyaringan rata-rata selama `dtk`: daya dirata-rata dulu, baru dB (tidak dikuasai lembah hening antar-ketukan)"""
    return 10 * np.log10(halus(10 ** (db / 10), dtk / langkah) + 1e-12)


def bagian(db, langkah, durasi):
    """label per blok 2 dtk: tenang / naik / puncak / turun; digabung, minimal 2 dtk"""
    h = db_halus(db, langkah, 2)
    p35, p75 = np.percentile(h, 35), np.percentile(h, 75)
    blok = max(1, int(2 / langkah))
    lab = []
    for i in range(0, len(h), blok):
        seg = h[i:i + blok]
        if len(seg) == 0:
            continue
        rata, miring = seg.mean(), (seg[-1] - seg[0]) if len(seg) > 1 else 0
        if rata >= p75:
            j = 'puncak'
        elif miring > 2.0:
            j = 'naik'
        elif miring < -2.0:
            j = 'turun'
        elif rata <= p35:
            j = 'tenang'
        else:
            j = 'naik' if miring > 0.8 else 'turun' if miring < -0.8 else 'tenang' if rata < (p35 + p75) / 2 else 'puncak'
        lab.append([round(i * langkah, 2), round(min(durasi, (i + blok) * langkah), 2), j])
    gabung = []
    for a, b, j in lab:
        if gabung and gabung[-1]['jenis'] == j:
            gabung[-1]['akhir'] = b
        else:
            gabung.append({'mulai': a, 'akhir': b, 'jenis': j})
    return gabung


def cari_drop(db, langkah, ketukan, birama, hening=()):
    """lonjakan energi: kenyaringan 2 dtk sesudah - 2 dtk sebelum > 6 dB dan sesudahnya termasuk keras;
    titiknya diperhalus ke blok 0,25 dtk dengan lompatan dB terbesar di sekitarnya"""
    pw = 10 ** (db / 10)
    w = int(2 / langkah)
    p70 = np.percentile(db_halus(db, langkah, 2), 70)
    calon = []
    for i in range(w, len(db) - w):
        pre, post = 10 * np.log10(pw[i - w:i].mean() + 1e-12), 10 * np.log10(pw[i:i + w].mean() + 1e-12)
        if post - pre > 5 and post >= p70:
            calon.append((post - pre, i))
    p60 = np.percentile(db_halus(db, langkah, 1), 60)
    for a, b in hening:  # hening lalu keras = hantaman (tahan napas -> impact), apa pun selisih rata-ratanya
        i = int(round(b / langkah))
        if i + int(1 / langkah) <= len(db) and 10 * np.log10(pw[i:i + int(1 / langkah)].mean() + 1e-12) >= p60:
            calon.append((99.0, i))
    calon.sort(reverse=True)
    pilih = []
    for _, i in calon:
        a, b = max(1, i - int(1 / langkah)), min(len(db) - 1, i + int(.5 / langkah))
        j = a + int(np.argmax(np.diff(db[a - 1:b + 1])[:b - a + 1]))  # blok pertama yang melompat paling tinggi
        t = j * langkah
        if all(abs(t - u) > 4 for u in pilih):
            pilih.append(t)
    acuan = birama if len(birama) else ketukan

    def jepret(t):  # ke awal birama/ketukan terdekat (dalam 0,35 dtk), else ketukan terdekat
        if len(acuan):
            j = acuan[np.argmin(np.abs(acuan - t))]
            if abs(j - t) < .35:
                return float(j)
        return float(ketukan[np.argmin(np.abs(ketukan - t))]) if len(ketukan) else t
    return sorted({round(jepret(t), 3) for t in pilih})


def cari_hening(db, langkah, min_dtk=0.3):
    ambang = max(np.percentile(db, 95) - 30, -55)
    out, a = [], None
    for i, v in enumerate(db):
        if v < ambang and a is None:
            a = i
        if (v >= ambang or i == len(db) - 1) and a is not None:
            b = i if v >= ambang else i + 1
            if (b - a) * langkah >= min_dtk:
                out.append([round(a * langkah, 2), round(b * langkah, 2)])
            a = None
    return out


def sela_narasi(kata, min_sela=0.25):
    if not kata:
        return []
    k = sorted(kata, key=lambda r: r[0])
    s = [[0.0, k[0][0]]] if k[0][0] >= min_sela else []
    for x, y in zip(k, k[1:]):
        if y[0] - x[1] >= min_sela:
            s.append([x[1], y[0]])
    return s


def di_sela(t, sela, toleransi=0.04):
    return any(a - toleransi <= t <= b + toleransi for a, b in sela)


def saran_potong(ketukan, birama, bag, drop, hening, sela):
    """ritme bervariasi: tenang = tiap 2 birama (tahan), naik = tiap ketukan/setengah birama (percepat),
    puncak = tiap birama, sebelum drop = antisipasi (+ tahan bila ada hening), drop = hantam, sesudahnya = lepas"""
    def jenis_di(t):
        for b in bag:
            if b['mulai'] <= t < b['akhir']:
                return b['jenis']
        return 'tenang'
    saran, terpakai = [], set()

    def tambah(t, peran, alasan):
        k = round(float(t), 3)
        if any(abs(k - u) < 0.12 for u in terpakai):
            return
        terpakai.add(k)
        if sela and peran == 'hantam' and not di_sela(k, sela):
            alasan += ' · menimpa kata narasi: geser ke sela terdekat atau kecilkan bunyi hantamnya'
        saran.append({'t': k, 'peran': peran, 'alasan': alasan})
    per = float(np.median(np.diff(ketukan))) if len(ketukan) > 1 else 0.5
    for d in drop:
        tambah(d, 'hantam', 'drop / lonjakan energi: potong keras, impact + bass, teks besar mendarat')
        sebelum = [h for h in hening if h[1] <= d + .05 and d - h[1] < 1.2]
        if sebelum:
            tambah(sebelum[-1][0], 'tahan', 'hening sebelum hantaman: bekukan gerak, tahan napas penonton')
        else:
            tambah(d - per, 'antisipasi', 'satu ketukan sebelum drop: riser berakhir, kamera mundur sedikit / tarik napas')
        tambah(d + 8 * per, 'lepas', 'dua birama sesudah hantaman: bidikan panjang, gerak melambat')
    bir = list(birama)
    for i, t in enumerate(bir):
        j = jenis_di(t)
        if j == 'tenang' and i % 2 == 0:
            tambah(t, 'tahan', 'bagian tenang: ganti adegan tiap 2 birama, biarkan gambar bernapas')
        elif j == 'puncak':
            tambah(t, 'ketukan', 'bagian puncak: ganti tiap birama')
        elif j == 'naik':
            tambah(t, 'ketukan', 'build-up: percepat, ganti tiap setengah birama')
            nx = bir[i + 1] if i + 1 < len(bir) else t + 4 * per
            tambah((t + nx) / 2, 'ketukan', 'build-up: setengah birama')
        elif j == 'turun' and i % 2 == 0:
            tambah(t, 'lepas', 'energi turun: transisi lembut, bidikan memanjang')
    saran.sort(key=lambda s: s['t'])
    return saran


def analisis_potongan(potongan, ketukan, birama, fps=30):
    tol = 2.5 / fps
    if not len(potongan):
        return None
    di_b = sum(1 for t in potongan if len(birama) and np.min(np.abs(birama - t)) <= tol)
    di_k = sum(1 for t in potongan if len(ketukan) and np.min(np.abs(ketukan - t)) <= tol)
    per = float(np.median(np.diff(ketukan))) if len(ketukan) > 1 else 0.5
    setengah = sum(1 for t in potongan if len(ketukan) and np.min(np.abs(ketukan - per / 2 - t)) <= tol)
    n = len(potongan)
    return {'jumlah': n, 'di_awal_birama': di_b, 'di_ketukan': di_k, 'di_setengah_ketukan': setengah,
            'persen_di_ketukan': round(100 * di_k / n, 1), 'persen_lepas_ketukan': round(100 * (n - di_k - setengah) / n, 1),
            'toleransi_dtk': round(tol, 3)}


def baca_potongan(p):
    d = json.loads(Path(p).read_text(encoding='utf-8'))
    if isinstance(d, list):
        return np.array([float(x) for x in d])
    if isinstance(d, dict) and d.get('video'):
        return np.array([float(x) for x in d['video'][0].get('potongan_detik', [])])
    return np.array([])


def opsi(arg, nama, bawaan=None, f=str):
    return f(arg[arg.index(nama) + 1]) if nama in arg else bawaan


def main():
    arg = sys.argv[1:]
    berpasangan = {'--keluar', '--kata', '--mulai', '--sampai', '--bpm-kira', '--potongan'}
    pos = [a for i, a in enumerate(arg) if not a.startswith('--') and (i == 0 or arg[i - 1] not in berpasangan)]
    if not pos:
        sys.exit(__doc__)
    src = Path(pos[0])
    mulai, sampai = opsi(arg, '--mulai', 0.0, float), opsi(arg, '--sampai', None, float)
    x = baca_audio(src, mulai, sampai)
    durasi = len(x) / SR
    mag = stft_mag(x)
    env, env_bass = amplop_onset(mag)
    bpm, lag = tempo(env, opsi(arg, '--bpm-kira', 110.0, float))
    kt = lacak_ketukan(env, lag)
    ketukan = kt / FPS_ENV
    # awal birama: fase (0..3) dengan hentakan bass terkuat, dihitung ulang per rangkaian ketukan
    # (rangkaian putus di jeda > 1,5 ketukan, mis. hening sebelum drop, supaya fase tidak bergeser)
    birama = []
    if len(kt) >= 4:
        putus = [0] + [i + 1 for i, g in enumerate(np.diff(kt)) if g > 1.5 * lag] + [len(kt)]
        for a, b in zip(putus, putus[1:]):
            run = kt[a:b]
            if len(run) < 4:
                birama += [float(run[0]) / FPS_ENV]
                continue
            # aksen = kenyaringan 80 md sesudah ketukan (dB) + hentakan bass; dibandingkan dengan tetangganya
            # supaya crescendo panjang tidak memenangkan fase terakhir
            n80 = int(.08 * SR)
            keras = np.array([10 * np.log10(np.mean(x[int(t * HOP):int(t * HOP) + n80] ** 2) + 1e-12) for t in run])
            keras = keras - halus(keras, 5)
            kuat = keras / 6 + env_bass[run]
            fase = int(np.argmax([kuat[f::4].mean() for f in range(4)]))
            birama += [float(t) / FPS_ENV for t in run[fase::4]]
    birama = np.array(birama if birama else ketukan[:1])
    db, langkah = energi_db(x)
    bag = bagian(db, langkah, durasi)
    hening = cari_hening(db, langkah)
    drop = cari_drop(db, langkah, ketukan, birama, hening)
    kata = json.loads(Path(opsi(arg, '--kata')).read_text(encoding='utf-8')) if '--kata' in arg else []
    sela = sela_narasi(kata)
    saran = saran_potong(ketukan, birama, bag, drop, hening, sela)
    hasil = {
        'sumber': src.name, 'mulai_di_berkas': mulai, 'durasi': round(durasi, 2), 'bpm': round(float(bpm), 1),
        'ketukan_dtk': round(60 / bpm, 3), 'ketukan': [round(float(t), 3) for t in ketukan],
        'birama': [round(float(t), 3) for t in birama],
        'energi': [[round(i * langkah, 2), round(float(v), 1)] for i, v in enumerate(db)],
        'bagian': bag, 'drop': drop, 'hening': hening, 'sela_narasi': sela, 'saran': saran,
    }
    if '--potongan' in arg:
        hasil['potongan_acuan'] = analisis_potongan(baca_potongan(opsi(arg, '--potongan')), ketukan, birama)
    keluar = opsi(arg, '--keluar')
    if keluar:
        Path(keluar).write_text(json.dumps(hasil, ensure_ascii=False, indent=1), encoding='utf-8')

    print(f'{src.name}: {durasi:.1f} dtk · {hasil["bpm"]} BPM (1 ketukan = {hasil["ketukan_dtk"]} dtk = {round(30 * 60 / bpm, 1)} bingkai @30fps) · '
          f'{len(ketukan)} ketukan · {len(birama)} birama')
    print('bagian :', ' | '.join(f'{b["mulai"]:.1f}-{b["akhir"]:.1f} {b["jenis"]}' for b in bag))
    print('drop   :', ', '.join(f'{t:.2f}' for t in drop) or '-')
    print('hening :', ', '.join(f'{a:.2f}-{b:.2f}' for a, b in hening) or '-')
    if sela:
        print('sela narasi >= 0,25 dtk:', len(sela))
    print('saran  :')
    for s in saran[:28]:
        print(f'  {s["t"]:7.2f}  {s["peran"]:<10} {s["alasan"]}')
    if len(saran) > 28:
        print(f'  … {len(saran) - 28} lagi (lihat --keluar)')
    if hasil.get('potongan_acuan'):
        p = hasil['potongan_acuan']
        print(f'potongan acuan: {p["jumlah"]} · di ketukan {p["di_ketukan"]} ({p["persen_di_ketukan"]}%) · di awal birama {p["di_awal_birama"]} · '
              f'di setengah ketukan {p["di_setengah_ketukan"]} · lepas ketukan {p["persen_lepas_ketukan"]}% (toleransi ±{p["toleransi_dtk"]} dtk)')
    if '--konfig' in arg:
        k = {kk: hasil[kk] for kk in ('bpm', 'ketukan', 'birama', 'drop', 'hening')}
        k['bagian'] = [[b['mulai'], b['akhir'], b['jenis']] for b in bag]
        print('\n/* tempel di kepala konfig.js — waktu MUTLAK (detik video); di dalam adegan: KETUKAN.drop[0] - <mulai adegan> */')
        print('const KETUKAN = ' + json.dumps(k, ensure_ascii=False, separators=(',', ':')) + ';')


if __name__ == '__main__':
    main()
