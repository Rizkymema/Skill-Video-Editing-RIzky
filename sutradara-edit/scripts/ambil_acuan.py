"""Ambil + bedah video acuan untuk dijadikan RESEP GAYA (mode D, SKILL.md §4).

Pakai:
  python -X utf8 -I scripts/ambil_acuan.py <url|berkas.mp4> [...] --ke "<folder baru>" [--lewati-unduh]

Per video:
  1. URL -> unduh dengan yt-dlp TANPA cookie/login (video publik saja) ke <ke>/<id>.mp4 + <id>.info.json
     (ditolak = minta pengguna mengunduh MP4-nya sendiri, lalu jalankan lagi dengan path berkas)
  2. <ke>/bedah/<id>/acuan/  <- skill-edit-rizky/scripts/bedah_acuan.py (lembar bingkai, potongan, palet, ritme)
  3. <ke>/bedah/<id>/ketukan.json <- ketukan.py --potongan (BPM, persen potongan yang jatuh di ketukan)
Lalu <ke>/ringkasan-acuan.md: satu baris per video (durasi, potongan, rata bidikan, BPM, % di ketukan, kesan, palet, caption).
Langkah berikutnya: LIHAT semua lembar-*.jpg + potongan.jpg, lalu tulis resep dengan templat/resep-gaya.md.
"""
import json
import subprocess
import sys
from pathlib import Path

DI_SINI = Path(__file__).resolve().parent
PY = sys.executable


def cari_bedah():
    for p in (DI_SINI.parents[1] / 'skill-edit-rizky' / 'scripts' / 'bedah_acuan.py',
              Path.home() / '.claude' / 'skills' / 'skill-edit-rizky' / 'scripts' / 'bedah_acuan.py'):
        if p.exists():
            return p
    sys.exit('bedah_acuan.py (skill-edit-rizky) tidak ditemukan')


def ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return 'ffmpeg'


def unduh(url, ke):
    """yt-dlp tanpa cookie. Mengembalikan path mp4 atau None."""
    cmd = [PY, '-I', '-m', 'yt_dlp', '--no-playlist', '--no-progress', '--write-info-json', '--sleep-requests', '1',
           '--ffmpeg-location', ffmpeg(), '-o', str(ke / '%(id)s.%(ext)s'), '--print', 'after_move:filepath', url]
    r = subprocess.run(cmd, capture_output=True, text=True, errors='replace')
    jalur = [s for s in r.stdout.splitlines() if s.strip().lower().endswith(('.mp4', '.webm', '.mkv', '.mov'))]
    if r.returncode != 0 or not jalur:
        pesan = (r.stderr.strip().splitlines() or ['?'])[-1]
        print(f'GAGAL unduh {url}: {pesan}')
        if any(k in pesan.lower() for k in ('login', 'cookie', 'not a bot', 'rate', 'private')):
            print('  -> butuh login/ditolak: minta pengguna mengunduh MP4-nya sendiri (jangan memakai cookie pengguna)')
        return None
    return Path(jalur[-1].strip())


def main():
    arg = sys.argv[1:]
    if '--ke' not in arg:
        sys.exit(__doc__)
    ke = Path(arg[arg.index('--ke') + 1])
    item = [a for i, a in enumerate(arg) if not a.startswith('--') and arg[i - 1] != '--ke']
    if not item:
        sys.exit(__doc__)
    ke.mkdir(parents=True, exist_ok=True)
    bedah = cari_bedah()
    baris = []
    for it in item:
        if it.startswith('http'):
            mp4 = None
            if '--lewati-unduh' in arg:
                ada = sorted(ke.glob(f"{it.rstrip('/').split('/')[-1]}.mp4"))
                mp4 = ada[0] if ada else None
            mp4 = mp4 or unduh(it, ke)
            if not mp4:
                continue
        else:
            mp4 = Path(it)
            if not mp4.exists():
                print('LEWATI (tidak ada):', mp4)
                continue
        kerja = ke / 'bedah' / mp4.stem
        kerja.mkdir(parents=True, exist_ok=True)
        subprocess.run([PY, '-X', 'utf8', '-I', str(bedah), str(kerja), str(mp4)])
        ring_p = kerja / 'acuan' / 'ringkasan.json'
        subprocess.run([PY, '-X', 'utf8', '-I', str(DI_SINI / 'ketukan.py'), str(mp4), '--keluar', str(kerja / 'ketukan.json'),
                        '--potongan', str(ring_p)], capture_output=True)
        ring = json.loads(ring_p.read_text(encoding='utf-8')) if ring_p.exists() else {}
        v = (ring.get('video') or [{}])[0]
        kt_p = kerja / 'ketukan.json'
        kt = json.loads(kt_p.read_text(encoding='utf-8')) if kt_p.exists() else {}
        pa = kt.get('potongan_acuan') or {}
        info_p = mp4.with_suffix('.info.json')
        if not info_p.exists():
            info_p = next(iter(sorted(ke.rglob(f'{mp4.stem}.info.json'))), info_p)
        cap = ''
        if info_p.exists():
            cap = (json.loads(info_p.read_text(encoding='utf-8')).get('description') or '').replace('\n', ' ')[:120]
        st = v.get('statistik') or {}
        baris.append(f"| {mp4.stem} | {v.get('durasi', '-')} | {v.get('jumlah_potongan', '-')} | {v.get('rata_bidikan_dtk', '-')} | "
                     f"{kt.get('bpm', '-')} | {pa.get('persen_di_ketukan', '-')} | {st.get('kesan', '-')} | "
                     f"{' '.join(p['hex'] for p in (v.get('palet') or [])[:4])} | {cap} |")
        print(f'ok {mp4.stem}')
    teks = ['# Ringkasan acuan', '', 'Lihat `bedah/<id>/acuan/lembar-*.jpg` + `potongan.jpg` sebelum menulis resep (`templat/resep-gaya.md`).', '',
            '| id | durasi | potongan | rata bidikan (dtk) | BPM | % potongan di ketukan | kesan | palet | caption |',
            '|---|---|---|---|---|---|---|---|---|'] + baris
    (ke / 'ringkasan-acuan.md').write_text('\n'.join(teks) + '\n', encoding='utf-8')
    print('ringkasan:', ke / 'ringkasan-acuan.md')


if __name__ == '__main__':
    main()
