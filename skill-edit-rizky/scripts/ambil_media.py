#!/usr/bin/env python3
"""Cari dan ambil foto/video NYATA untuk topik yang punya data (tokoh, tempat, benda, peristiwa), siap ditanam di skill-edit-rizky.

Disalin lalu disesuaikan dari visual-animasi-2d/scripts/ambil_footage.py (skill itu tidak diubah). Bedanya: hasilnya langsung
ke folder _kerja proyek kolase (gambar/<kode>.jpg dan klip/<kode>.mp4), kreditnya dicatat di _kerja/media.json, dan skrip
mencetak lapisan konfig siap tempel + kredit di layar + entri KONFIG.sumber + baris deskripsi.

Sumber, urut yang paling aman:
  wiki     foto yang dipakai artikel Wikipedia (id lalu en) + lisensinya          kueri = nama tokoh/benda/peristiwa
  commons  pencarian Wikimedia Commons (CC/domain publik, atribusi tercatat)
  nasa     NASA Image and Video Library (domain publik)
  youtube  calon video YouTube (berita/liputan/kanal resmi) -> hanya KUTIPAN pendek 3-8 dtk, total <= 20 dtk, kredit di layar
  berkas   foto/video yang dikirim pengguna (path lokal)

Pakai (Python312 di PC ini, selalu dengan -I):
  python -X utf8 -I ambil_media.py cari "N250 Gatotkaca" [--di wiki|commons|nasa|youtube|semua] [--jenis gambar|video]
                                     [--jumlah 8] [--bahasa id] [--cc] [--terbaru]
  python -X utf8 -I ambil_media.py ambil <url|berkas> <_kerja>
        tanpa --kode: unduh ke _kerja/_calon/ (+ lembar bingkai berstempel waktu untuk video) supaya bisa dipilih dulu
  python -X utf8 -I ambil_media.py ambil <url|berkas> <_kerja> --kode n250-terbang [--mulai 12 --sampai 17]
        [--buang-bawah 0.12] [--kredit "Foto: …"] [--lisensi "…"] [--potong]
        gambar -> _kerja/gambar/<kode>.jpg (sisi terpanjang <= 2400 px; --potong = latar dibuang rembg bila terpasang -> .png)
        video  -> _kerja/klip/<kode>.mp4 (bisu, H.264, <= 1080 px, segmen --mulai/--sampai) -> rakit --klip <kode>=klip/<kode>.mp4@12
  python -X utf8 -I ambil_media.py daftar <_kerja>      kredit semua media proyek (untuk deskripsi + cek lisensi)

Aturan (references/data-media.md): unduh hanya bila pengguna sudah setuju (pilihan "foto/video asli" di setup = izin);
lisensi non-bebas (fair use, logo, "all rights reserved") tidak dipakai kecuali kutipan berita pendek; kredit selalu tampil
di layar saat media muncul; wajah tokoh nyata hanya dari foto/video asli, tidak pernah dibuat AI.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

UA = {"User-Agent": "KolaseRetro/1.2 (video edukasi; media berlisensi)"}
BULAN = "Jan Feb Mar Apr Mei Jun Jul Agu Sep Okt Nov Des".split()
EKS_VIDEO = (".webm", ".ogv", ".mp4", ".mpg", ".mov", ".m4v", ".mkv", ".ogg")
EKS_GAMBAR = (".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".gif", ".bmp")
NONBEBAS = re.compile(r"non-?free|fair use|all rights reserved|copyright|hak cipta", re.I)


# ---------------------------------------------------------------- umum
def ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        exe = shutil.which("ffmpeg")
        if not exe:
            sys.exit("ffmpeg tidak ditemukan (pasang imageio-ffmpeg atau taruh ffmpeg di PATH)")
        return exe


def durasi_video(berkas):
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.count_frames_and_secs(str(berkas))[1]
    except Exception:
        keluar = subprocess.run([ffmpeg(), "-i", str(berkas)], capture_output=True, text=True, errors="replace").stderr
        m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", keluar)
        return int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3]) if m else 0


def json_url(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def unduh(url, tujuan, coba=4):
    import time
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    for i in range(coba):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180) as r, open(tujuan, "wb") as f:
                shutil.copyfileobj(r, f, 1 << 20)
            return
        except urllib.error.HTTPError as e:      # Wikimedia membatasi unduhan beruntun (429): tunggu lalu ulangi
            if e.code != 429 or i == coba - 1:
                raise
            tunggu = int(e.headers.get("Retry-After") or 0) or 15 * (i + 1)
            print(f"   dibatasi server (429), menunggu {tunggu} dtk lalu mencoba lagi")
            time.sleep(min(tunggu, 90))


def ytdlp(*a, tangkap=True):
    # --encoding utf-8: tanpa ini yt-dlp di Windows menulis judul dengan kode halaman lokal
    return subprocess.run([sys.executable, "-m", "yt_dlp", "--no-warnings", "--encoding", "utf-8", *a], check=True, text=True,
                          encoding="utf-8", errors="replace", capture_output=tangkap).stdout


def bersih(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


def detik(s):
    s = int(float(s or 0))
    return f"{s // 60}:{s % 60:02d}"


def tanda_lisensi(lis):
    if not lis:
        return "  [lisensi ?: cek halaman]"
    return "  [NON-BEBAS: jangan dipakai]" if NONBEBAS.search(lis) else ""


# ---------------------------------------------------------------- cari
def _cetak_imageinfo(halaman, jumlah, jenis):
    n = 0
    for p in sorted(halaman, key=lambda x: x.get("index", 0)):
        ii = (p.get("imageinfo") or [{}])[0]
        mime = ii.get("mime", "")
        if jenis == "gambar" and not mime.startswith("image/"):
            continue
        if jenis == "video" and not (mime.startswith("video/") or mime == "application/ogg"):
            continue
        if mime == "image/svg+xml" or (mime.startswith("image/") and (ii.get("width") or 0) < 500):
            continue                                                    # ikon/logo kecil tidak berguna untuk kolase
        m = ii.get("extmetadata", {})
        lis = bersih(m.get("LicenseShortName", {}).get("value"))
        oleh = bersih(m.get("Artist", {}).get("value"))[:60]
        tgl = bersih(m.get("DateTimeOriginal", {}).get("value"))[:10]
        dur = f" · {detik(ii.get('duration'))}" if ii.get("duration") else ""
        n += 1
        print(f"{n}. {p['title'].replace('File:', '').replace('Berkas:', '')} · {ii.get('width')}x{ii.get('height')}{dur} · "
              f"{tgl or '?'}\n   {lis or '?'} · {oleh or '?'}{tanda_lisensi(lis)}\n   {ii.get('descriptionurl')}")
        if n >= jumlah:
            break
    return n


def cari_commons(kueri, jumlah, jenis):
    ft = "filetype:video" if jenis == "video" else "filetype:bitmap"
    q = urllib.parse.urlencode({"action": "query", "format": "json", "generator": "search", "gsrnamespace": 6, "gsrlimit": jumlah * 2,
                                "gsrsearch": f"{kueri} {ft}", "prop": "imageinfo", "iiprop": "url|extmetadata|size|mime"})
    d = json_url("https://commons.wikimedia.org/w/api.php?" + q)
    print(f"== Wikimedia Commons: {kueri}")
    if not _cetak_imageinfo(d.get("query", {}).get("pages", {}).values(), jumlah, jenis):
        print("   (tidak ada; coba kata kunci bahasa Inggris)")


def cari_wiki(kueri, jumlah, jenis, bahasa):
    for lang in dict.fromkeys([bahasa, "en"]):
        api = f"https://{lang}.wikipedia.org/w/api.php?"
        hasil = json_url(api + urllib.parse.urlencode({"action": "query", "format": "json", "list": "search", "srsearch": kueri, "srlimit": 1}))
        top = (hasil.get("query", {}).get("search") or [{}])[0].get("title")
        if not top:
            continue
        q = urllib.parse.urlencode({"action": "query", "format": "json", "titles": top, "redirects": 1, "generator": "images",
                                    "gimlimit": 60, "prop": "imageinfo", "iiprop": "url|extmetadata|size|mime"})
        d = json_url(api + q)
        print(f"== Wikipedia {lang}: {top}  (https://{lang}.wikipedia.org/wiki/{urllib.parse.quote(top.replace(' ', '_'))})")
        if _cetak_imageinfo(d.get("query", {}).get("pages", {}).values(), jumlah, jenis):
            return
    print("   (artikel tanpa foto yang layak; coba --di commons)")


def cari_nasa(kueri, jumlah, jenis):
    d = json_url("https://images-api.nasa.gov/search?" + urllib.parse.urlencode({"q": kueri, "media_type": "video" if jenis == "video" else "image"}))
    print(f"== NASA: {kueri}")
    for i, it in enumerate(d.get("collection", {}).get("items", [])[:jumlah], 1):
        dt = (it.get("data") or [{}])[0]
        print(f"{i}. {dt.get('title')} · {dt.get('center', 'NASA')} · {str(dt.get('date_created', ''))[:10]} · domain publik NASA\n   {it.get('href')}")


def cari_youtube(kueri, jumlah, cc=False, terbaru=False):
    sp = "EgIwAQ%3D%3D" if cc else ("EgIIAw%3D%3D" if terbaru else None)   # saringan YouTube: Creative Commons / minggu ini
    sumber = f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(kueri)}&sp={sp}" if sp else f"ytsearch{jumlah}:{kueri}"
    print(f"== YouTube: {kueri}{' (Creative Commons)' if cc else ''}  -> kutipan 3-8 dtk, kredit di layar")
    try:
        keluar = ytdlp("--flat-playlist", "--playlist-end", str(jumlah), "--print",
                       "%(title)s\t%(channel)s\t%(duration)s\t%(upload_date)s\t%(url)s", sumber)
    except subprocess.CalledProcessError as e:
        print(f"   pencarian YouTube gagal ({bersih(e.stderr)[-160:]}); cari lewat browser bawaan lalu tempel tautannya")
        return
    for i, baris in enumerate(keluar.strip().splitlines(), 1):
        judul, kanal, dur, tgl, url = (baris.split("\t") + [""] * 5)[:5]
        dur = detik(dur) if dur not in ("", "NA", "None") else "?"
        print(f"{i}. {judul} · {kanal} · {dur} · {tgl if tgl not in ('NA', 'None') else '?'}\n   {url}")


# ---------------------------------------------------------------- siapkan sumber
def info_commons(url):
    """Halaman/berkas Commons atau berkas Wikipedia -> info + URL unduh (gambar diperkecil ke 2400 px oleh server)."""
    host = urllib.parse.urlparse(url).netloc
    nama = urllib.parse.unquote(url.split("#")[0].rsplit("/", 1)[-1])
    nama = re.sub(r"^(File|Berkas|Image|Gambar):", "", nama)
    api = f"https://{host}/w/api.php?" if host.endswith("wikipedia.org") else "https://commons.wikimedia.org/w/api.php?"
    q = urllib.parse.urlencode({"action": "query", "format": "json", "titles": "File:" + nama, "prop": "imageinfo",
                                "iiprop": "url|extmetadata|mime|size", "iiurlwidth": 1920})  # ukuran standar Wikimedia (ukuran lain sering 429)
    p = next(iter(json_url(api + q)["query"]["pages"].values()))
    if "imageinfo" not in p:
        sys.exit(f"berkas tidak ditemukan di Wikimedia: {nama}")
    ii = p["imageinfo"][0]
    m = ii.get("extmetadata", {})
    video = ii.get("mime", "").startswith("video/") or ii.get("mime") == "application/ogg"
    berkas = ii["url"] if video or (ii.get("width") or 0) <= 1920 else ii.get("thumburl") or ii["url"]
    return {"judul": os.path.splitext(nama)[0].replace("_", " "), "oleh": bersih(m.get("Artist", {}).get("value"))[:80],
            "tanggal": bersih(m.get("DateTimeOriginal", {}).get("value"))[:10], "tautan": ii.get("descriptionurl"),
            "lisensi": bersih(m.get("LicenseShortName", {}).get("value")), "asal": "Wikimedia Commons",
            "berkas_url": berkas, "jenis": "video" if video else "gambar"}


def berkas_nasa(url):
    daftar = json_url(url) if url.endswith(".json") else [url]
    for akhir in ("~orig.mp4", "~large.mp4", "~medium.mp4", "~large.jpg", "~orig.jpg"):
        for u in daftar:
            if u.endswith(akhir):
                return u.replace("http://", "https://")
    return daftar[0]


def siapkan(sumber, calon):
    """-> (info, berkas lokal). info: judul, oleh, tanggal, tautan, lisensi, asal, jenis, durasi."""
    calon.mkdir(parents=True, exist_ok=True)
    lokal = Path(sumber)
    if lokal.exists():
        jenis = "video" if lokal.suffix.lower() in EKS_VIDEO else "gambar"
        return {"judul": lokal.stem, "oleh": "", "tanggal": "", "tautan": "", "lisensi": "dari pengguna", "asal": "kiriman pengguna",
                "jenis": jenis}, lokal
    host = urllib.parse.urlparse(sumber).netloc
    if host.endswith("wikimedia.org") or host.endswith("wikipedia.org"):
        info = info_commons(sumber)
        eks = os.path.splitext(urllib.parse.urlparse(info["berkas_url"]).path)[1].lower() or ".jpg"
        berkas = calon / (re.sub(r"[^\w.-]", "_", info["judul"])[:80] + eks)
        if not berkas.exists():
            unduh(info.pop("berkas_url"), berkas)
        return info, berkas
    if "nasa.gov" in host:
        f = berkas_nasa(sumber)
        nid = f.rsplit("/", 2)[-2]
        berkas = calon / ("nasa_" + os.path.basename(f))
        if not berkas.exists():
            unduh(f, berkas)
        return {"judul": nid, "oleh": "NASA", "tanggal": "", "tautan": f"https://images.nasa.gov/details/{nid}",
                "lisensi": "domain publik (NASA)", "asal": "NASA", "jenis": "video" if f.endswith(".mp4") else "gambar"}, berkas
    # YouTube, Instagram, TikTok, situs berita: yt-dlp (video saja, bisu; suara asli tidak dipakai di kolase)
    try:
        info = json.loads(ytdlp("-J", "--no-playlist", sumber))
        berkas = calon / f"{info['id']}.mp4"
        if not berkas.exists():
            ytdlp("--no-playlist", "-f", "bv*[height<=1080][ext=mp4]/b[height<=1080][ext=mp4]/bv*[height<=1080]/b",
                  "--ffmpeg-location", ffmpeg(), "--remux-video", "mp4", "-o", str(berkas), sumber, tangkap=False)
    except subprocess.CalledProcessError as e:
        sys.exit("unduhan ditolak situsnya (YouTube/IG sering meminta login atau cek bot).\n"
                 "Jangan memakai cookie/login pengguna. Minta pengguna mengunduh MP4-nya sendiri, lalu:\n"
                 f"  ambil_media.py ambil <berkas.mp4> <_kerja> --kode … --kredit \"…\"\n({bersih(str(e.stderr or ''))[-200:]})")
    tgl = info.get("upload_date") or ""
    return {"judul": (info.get("title") or "").strip(), "oleh": (info.get("channel") or info.get("uploader") or "").strip(),
            "tanggal": f"{int(tgl[6:8])} {BULAN[int(tgl[4:6]) - 1]} {tgl[:4]}" if len(tgl) == 8 else tgl,
            "tautan": info.get("webpage_url") or sumber, "lisensi": info.get("license") or "standar (kutipan pendek)",
            "asal": info.get("extractor_key") or host, "jenis": "video", "durasi": info.get("duration")}, berkas


# ---------------------------------------------------------------- olah
def lembar_bingkai(berkas, keluar, durasi):
    """36 bingkai kecil berstempel waktu (PIL, tanpa drawtext ffmpeg) untuk memilih segmen."""
    from PIL import Image, ImageDraw, ImageFont
    jarak = max(1.0, float(durasi or 36) / 36)
    with tempfile.TemporaryDirectory() as d:
        subprocess.run([ffmpeg(), "-v", "error", "-y", "-i", str(berkas), "-vf", f"fps=1/{jarak:.3f},scale=320:-2",
                        str(Path(d) / "b%03d.jpg")], check=True)
        bingkai = sorted(Path(d).glob("b*.jpg"))[:36]
        if not bingkai:
            return None
        w, h = Image.open(bingkai[0]).size
        lembar = Image.new("RGB", (w * 6, h * ((len(bingkai) + 5) // 6)), "black")
        try:
            huruf = ImageFont.truetype("arial.ttf", 26)
        except OSError:
            huruf = ImageFont.load_default()
        for i, f in enumerate(bingkai):
            x, y = (i % 6) * w, (i // 6) * h
            lembar.paste(Image.open(f), (x, y))
            g = ImageDraw.Draw(lembar)
            g.rectangle([x + 4, y + 4, x + 96, y + 36], fill=(0, 0, 0))
            g.text((x + 10, y + 6), detik(i * jarak), fill=(255, 220, 0), font=huruf)
        lembar.save(keluar, quality=85)
    return keluar


def simpan_gambar(berkas, tujuan_dir, kode, potong):
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(berkas))
    if potong:
        try:
            from rembg import remove
        except ImportError:
            print("peringatan: rembg belum terpasang, latar tidak dibuang. Pakai bingkai (benda kartu / bayangan) atau minta izin\n"
                  "  pengguna untuk `pip install rembg` (mengunduh model ±170 MB). Foto TIDAK dipotong manual setengah jadi.")
            potong = False
        else:
            im = remove(im.convert("RGBA"))
            kotak = im.getbbox()
            if kotak:
                im = im.crop(kotak)
    im.thumbnail((2400, 2400))
    tujuan_dir.mkdir(parents=True, exist_ok=True)
    for lama in tujuan_dir.glob(f"{kode}.*"):
        lama.unlink()
    if potong:
        tujuan = tujuan_dir / f"{kode}.png"
        im.save(tujuan)
    else:
        tujuan = tujuan_dir / f"{kode}.jpg"
        im.convert("RGB").save(tujuan, quality=92)
    return tujuan, im.size


def simpan_klip(berkas, tujuan_dir, kode, mulai, sampai, bawah):
    tujuan_dir.mkdir(parents=True, exist_ok=True)
    tujuan = tujuan_dir / f"{kode}.mp4"
    vf = (f"crop=iw:trunc(ih*{1 - bawah}/2)*2:0:0," if bawah > 0 else "") + "scale='min(1080,iw)':-2"
    waktu = ["-ss", str(mulai)] + (["-to", str(sampai)] if sampai else [])
    subprocess.run([ffmpeg(), "-v", "error", "-y", *waktu, "-i", str(berkas), "-an", "-vf", vf, "-c:v", "libx264",
                    "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(tujuan)], check=True)
    return tujuan


def teks_kredit(info, jenis):
    asal, oleh, lis = info.get("asal", ""), info.get("oleh", ""), info.get("lisensi", "")
    kata = "Video" if jenis == "video" else "Foto"
    if asal == "kiriman pengguna":
        return ""
    if asal == "Wikimedia Commons":
        return f"{kata}: {oleh or info['judul']} / Wikimedia Commons, {lis}"
    if asal == "NASA":
        return f"{kata}: NASA"
    return f"Sumber: {oleh or asal}{' · ' + info['tanggal'] if info.get('tanggal') else ''}"


def ambil(a):
    kerja = Path(a.kerja)
    if not kerja.exists():
        sys.exit(f"folder _kerja tidak ada: {kerja}")
    info, berkas = siapkan(a.sumber, kerja / "_calon")
    jenis = info["jenis"]
    if a.lisensi:
        info["lisensi"] = a.lisensi
    peringatan = tanda_lisensi(info["lisensi"]).strip()
    if not a.kode:
        print(f"diunduh: {berkas}")
        if jenis == "video":
            dur = info.get("durasi") or durasi_video(berkas)
            ls = lembar_bingkai(berkas, kerja / "_calon" / f"{berkas.stem}_lembar.jpg", dur)
            print(f"durasi {detik(dur)} · lembar bingkai: {ls}")
        print(f"lisensi: {info['lisensi'] or '?'} · {info.get('oleh') or info.get('asal')} · {info.get('tautan') or '-'} {peringatan}")
        return
    if "NON-BEBAS" in peringatan:
        print(f"PERINGATAN: lisensi '{info['lisensi']}' bukan lisensi bebas; pakai hanya sebagai kutipan berita pendek dengan kredit.")
    if jenis == "video":
        mulai, sampai = a.mulai or 0.0, a.sampai
        if sampai is not None and sampai <= mulai:
            sys.exit("--sampai harus lebih besar dari --mulai")
        tujuan = simpan_klip(berkas, kerja / "klip", a.kode, mulai, sampai, a.buang_bawah)
        panjang = (sampai or durasi_video(tujuan) + mulai) - mulai
        if info["asal"] not in ("Wikimedia Commons", "NASA", "kiriman pengguna") and "Creative Commons" not in info["lisensi"] and panjang > 8:
            print(f"peringatan: kutipan {panjang:.1f} dtk; pakai 3-8 dtk per klip dan total <= 20 dtk per video")
        segmen = f"{detik(mulai)}-{detik(mulai + panjang)}"
        ukuran = None
    else:
        tujuan, ukuran = simpan_gambar(berkas, kerja / "gambar", a.kode, a.potong)
        segmen = ""
    kredit = a.kredit if a.kredit is not None else teks_kredit(info, jenis)
    catatan = kerja / "media.json"
    data = json.loads(catatan.read_text(encoding="utf-8")) if catatan.exists() else {}
    data[a.kode] = {"jenis": jenis, "berkas": str(tujuan.relative_to(kerja)).replace("\\", "/"), "segmen": segmen, "kredit": kredit,
                    **{k: info.get(k, "") for k in ("judul", "oleh", "tanggal", "tautan", "lisensi", "asal")}}
    catatan.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"siap: {tujuan}" + (f" ({ukuran[0]}x{ukuran[1]})" if ukuran else f" (segmen {segmen})") + f"\ndicatat: {catatan}")
    js = lambda s: str(s).replace("\\", "\\\\").replace("'", "\\'")
    label = f"{{ teks: '{js(kredit)}', gaya: 'label', ukuran: 28, y: 1330, lebar: 760, masuk: 'naik', t: .3 }}" if kredit else ""
    if jenis == "video":
        print(f"rakit: --klip {a.kode}=klip/{a.kode}.mp4@12")
        print(f"lapisan (layar miring di atas latar, tepi terlihat utuh):\n  {{ urutan: '{a.kode}', x: 540, y: 700, lebar: 940, z: 1.2, "
              f"bayangan: true, putar: -1.5, masuk: {{ gaya: 'geser', dari: 'bawah' }}, t: .05, cek: false }},")
    elif a.potong and tujuan.suffix == ".png":
        print(f"lapisan (potongan; tepi yang terpotong foto aslinya otomatis ditempel ke tepi layar):\n  {{ gambar: '{a.kode}', "
              f"x: 540, y: 1150, tinggi: 1200, z: 1.4, bayangan: true, masuk: 'terbang', rig: 'napas' }},")
    else:
        print(f"lapisan (pilih satu):\n  pelat penuh : {{ gambar: '{a.kode}' }},\n  kartu foto  : {{ benda: {{ jenis: 'kartu', gambar: "
              f"'{a.kode}', keterangan: '…', lebar: 620 }}, x: 540, y: 820, putar: -2.5, z: 1.2, bayangan: true, masuk: 'terbang' }},\n"
              f"  foto koran  : benda koran {{ foto: '{a.kode}' }}  ·  layar TV: benda tv {{ gambar: '{a.kode}' }}")
    if label:
        print(f"kredit di layar (wajib, selama media tampil):\n  {label},")
    if info.get("tautan"):
        print(f"KONFIG.sumber: {{ fakta: '{'Video' if jenis == 'video' else 'Foto'}: {js(info['judul'][:70])}', url: '{js(info['tautan'])}' }},")
    print(f"deskripsi: {kredit or 'kiriman pengguna'}{' – ' + info['tautan'] if info.get('tautan') else ''}")


def daftar(a):
    catatan = Path(a.kerja) / "media.json"
    if not catatan.exists():
        sys.exit("belum ada media.json")
    data = json.loads(catatan.read_text(encoding="utf-8"))
    for kode, m in data.items():
        print(f"{kode}: {m['berkas']} {m.get('segmen') or ''} · {m.get('lisensi') or '?'}{tanda_lisensi(m.get('lisensi'))}")
    baris = sorted({m["kredit"] + (f" ({m['tautan']})" if m.get("tautan") else "") for m in data.values() if m.get("kredit")})
    if baris:
        print("\nuntuk deskripsi:\n" + "\n".join(baris))


def main():
    import argparse
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest="perintah", required=True)
    c = s.add_parser("cari")
    c.add_argument("kueri")
    c.add_argument("--di", default="semua", choices=["wiki", "commons", "nasa", "youtube", "semua"])
    c.add_argument("--jenis", default="gambar", choices=["gambar", "video"])
    c.add_argument("--jumlah", type=int, default=8)
    c.add_argument("--bahasa", default="id")
    c.add_argument("--cc", action="store_true")
    c.add_argument("--terbaru", action="store_true")
    m = s.add_parser("ambil")
    m.add_argument("sumber")
    m.add_argument("kerja")
    m.add_argument("--kode")
    m.add_argument("--mulai", type=float)
    m.add_argument("--sampai", type=float)
    m.add_argument("--buang-bawah", type=float, default=0.0)
    m.add_argument("--kredit")
    m.add_argument("--lisensi")
    m.add_argument("--potong", action="store_true")
    d = s.add_parser("daftar")
    d.add_argument("kerja")
    a = p.parse_args()
    if a.perintah == "ambil":
        return ambil(a)
    if a.perintah == "daftar":
        return daftar(a)
    cari = {"wiki": lambda: cari_wiki(a.kueri, a.jumlah, a.jenis, a.bahasa), "commons": lambda: cari_commons(a.kueri, a.jumlah, a.jenis),
            "nasa": lambda: cari_nasa(a.kueri, a.jumlah, a.jenis), "youtube": lambda: cari_youtube(a.kueri, a.jumlah, a.cc, a.terbaru)}
    urut = ["wiki", "commons", "youtube"] if a.di == "semua" else [a.di]
    for k in urut:
        try:
            cari[k]()
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            print(f"== {k}: gagal ({e})")
        print()


if __name__ == "__main__":
    main()
