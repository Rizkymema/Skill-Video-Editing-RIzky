"""Sampul (cover/thumbnail) video skill-edit-rizky lewat Google Flow, desain mengikuti style video (references/sampul.md).

Sejak 28 Nov 2026 (permintaan pengguna): setiap video jadi disertai judul/deskripsi + sampul. Video 9:16 → sampul 9:16
(1080×1920), video 16:9 → sampul 16:9 (1280×720). Desain dibuat di Google Flow (0 kredit) seperti contoh pengguna
("7 Gembok Anti-Maling"): subjek 3D berekspresi di tengah, elemen pendukung mengambang berlapis, judul raksasa 3D,
kicker kecil di atas; bahan/palet/latar mengikuti tema video. Di cloud (tanpa Flow): kirim promptnya ke pengguna.

Pakai:
  python -X utf8 scripts/sampul.py rencana <_kerja>
      baca _kerja/sampul/isi.json (ditulis Claude; dibuat templatnya bila belum ada) + konfig.js (rasio, tema)
      → _kerja/sampul/flow_sampul.json (argumen flow_agent_images: project, aspect_ratio, scenes = 3 varian)
        + <folder video>/prompt-sampul.md (prompt siap tempel untuk Flow/Gemini, dipakai di cloud)
  python -X utf8 scripts/sampul.py ambil <_kerja> --dari <folder unduhan Flow>
      semua gambar di folder → _kerja/sampul/calon-N.jpg (ukuran pas) + _calon.jpg (besar + ukuran feed, untuk dipilih)
  python -X utf8 scripts/sampul.py pilih <_kerja> <N>
      calon-N → <folder video>/sampul.jpg (≤ 2 MB, batas thumbnail YouTube) + _kerja/sampul/sampul.jpg
  python -X utf8 scripts/sampul.py gaya            daftar style sampul per tema
"""
import argparse, json, re, sys
from pathlib import Path

# ---------------------------------------------------------------- style sampul per tema (bahasa Inggris untuk Flow)
# latar · subjek (perlakuan subjek utama) · props (benda khas style) · efek (cahaya/partikel) · judul1 (bahan baris biasa)
# · judul2 (bahan baris aksen) · kicker (warna kicker) · palet
GAYA = {
    'teknologi': dict(
        latar='deep navy-to-black gradient background with soft blue bokeh and tiny golden sparks',
        subjek='rendered as a glossy 3D object with a glowing cyan rim light; if it can have a face, give it simple glowing cartoon eyes and an expression that matches the hook',
        props='translucent frosted-glass interface cards with glowing edges floating at different depths, holographic cyan icons, a few gold accents',
        efek='a swirling stream of cyan digital particles around the subject, lens glow, cinematic rim light',
        judul1='polished chrome-silver 3D extruded letters with bevel and cool reflections', judul2='glossy metallic gold 3D extruded letters with warm glow',
        kicker='glowing cyan', palet='deep navy, electric cyan, chrome white, gold accent'),
    'kaca-gradien': dict(
        latar='clean bright studio with a soft white-to-pale-lavender gradient and a faint light grey grid floor, soft shadows',
        subjek='rendered as a glossy chrome or frosted-glass 3D object, soft studio reflections, gentle electric blue glow',
        props='frosted glass app buttons and rounded glass cards floating at different depths with electric blue highlights, chrome spheres, thin blue light lines',
        efek='soft electric blue glow, subtle light refraction through the glass, clean premium product-shot lighting',
        judul1='bold dark charcoal 3D letters with a glossy finish', judul2='glossy electric blue (#1f5cff) glass-like 3D letters with an inner glow',
        kicker='electric blue', palet='white, pale lavender, chrome, electric blue'),
    'sinema-kasus': dict(
        latar='dark blue-black cinematic night scene, wet reflections, light from computer monitors',
        subjek='lit by cold monitor light from one side and a thin red rim light, dramatic and tense, realistic',
        props='glowing screens with blurred data and maps behind the subject, a case folder, a red string line, police-style crime lighting, film grain',
        efek='cold blue haze, a single red accent glow, subtle film grain, anamorphic light streak',
        judul1='bold off-white 3D letters with a subtle metallic edge', judul2='glowing blood-red (#e0261b) 3D letters with a neon edge',
        kicker='soft red', palet='blue-black, cold steel blue, one red accent'),
    'legenda-gelap': dict(
        latar='dark charcoal night scene lit by a big blue full moon on one side and warm orange firelight on the other, a chalkboard texture in the background',
        subjek='mysterious, half lit by firelight and half by moonlight, slightly eerie but not gory',
        props='old polaroid photos pinned with red string, chalk drawings and symbols, drifting embers, old paper fragments',
        efek='floating embers and smoke, warm-vs-cold contrast lighting',
        judul1='aged cream carved 3D letters with a chalky texture', judul2='fiery golden-yellow (#f3c44a) 3D letters glowing like embers',
        kicker='warm cream', palet='charcoal, moon blue, fire orange, golden yellow'),
    'piksel-kertas': dict(
        latar='handmade olive-green paper craft diorama background with layered paper cut-outs and visible paper texture',
        subjek='made of layered paper cut-outs with soft drop shadows, a little playful',
        props='paper cut-out icons and metaphor objects, a red ribbon banner, small pixel-art details, washi tape',
        efek='soft studio light with crisp paper shadows, slight depth of field',
        judul1='cream uppercase 3D paper-cut letters with layered thickness and drop shadow', judul2='bold red (#d62a1e) paper-cut 3D letters on a red ribbon',
        kicker='cream', palet='olive green, cream paper, red ribbon, mustard'),
    'panggung-emas': dict(
        latar='deep bottle-green luxury stage with a golden spotlight and velvet texture',
        subjek='standing in front of a giant gold serif word so the subject overlaps the letters, regal and important',
        props='gold confetti, a podium or pedestal, laurel and ranking details, polished brass',
        efek='golden spotlight beams, sparkling gold dust, luxurious glow',
        judul1='giant elegant gold serif 3D letters (embossed, polished)', judul2='bright polished gold serif 3D letters with sparkle highlights',
        kicker='champagne gold', palet='bottle green, gold, ivory, a touch of crimson'),
    'arsip-pop': dict(
        latar='retro magazine advertisement page with a flat bold red background and halftone dot texture',
        subjek='shown as a black-and-white vintage photo cut-out with one element kept in full color (selective color)',
        props='torn paper labels in royal blue, vintage product illustrations, halftone circles, retro starbursts',
        efek='printed paper texture, slight ink misregistration, bold flat shadows',
        judul1='bold white 3D retro letters with a thick dark drop shadow', judul2='bright mustard-yellow (#f6c12a) 3D retro letters with a blue outline',
        kicker='royal blue on cream label', palet='flat red, cream, royal blue, mustard'),
    'panggung-korporat': dict(
        latar='dark corporate stage with a desaturated grey world, graph paper texture on a backdrop',
        subjek='the key object glowing in a single power color (orange) while everything else is grey, dramatic spotlight',
        props='a rising or crashing chart arrow drawn on graph paper, rival stage spotlights, boardroom chairs in silhouette',
        efek='hard spotlight from above, grey haze, one orange light accent',
        judul1='bold condensed white 3D letters (Anton-like)', judul2='bright orange (#ff7a00) 3D letters on an orange ribbon band, with a yellow number if any',
        kicker='warm yellow', palet='grey, charcoal, power orange, yellow'),
    'diorama-kreator': dict(
        latar='miniature toy diorama world made of voxel blocks on a dark stage, under a single soft spotlight',
        subjek='a toy-like miniature version of the subject on a small pedestal under the spotlight, cute and tactile',
        props='a glowing blue chat bubble screen, cream index cards with big numbers, tiny voxel props, miniature tools',
        efek='tilt-shift miniature depth of field, soft spotlight, gentle dust in the light beam',
        judul1='clean thin white 3D letters', judul2='hand-written red (#d11f1f) marker-style 3D word',
        kicker='soft white', palet='dark stage, warm spotlight, toy colors, chat blue, red marker'),
    'arsip': dict(
        latar='vintage cream paper collage background with halftone texture and old newspaper clippings',
        subjek='shown as a halftone black-and-white archival photo cut-out with a white paper edge',
        props='old newspaper fragments, a yellow highlighter stroke, postage stamps, paper clips, a red date stamp',
        efek='warm aged paper tone, dust, soft vignette',
        judul1='bold black condensed 3D letters printed on paper', judul2='bold red (#d7261e) 3D letters with a yellow highlighter swipe behind',
        kicker='dark brown', palet='cream paper, black ink, yellow highlighter, red'),
    'dosir': dict(
        latar='dark teal investigation room with a textured wall and a cork board',
        subjek='lit like an interrogation scene, harsh top light, mysterious',
        props='case documents, photos pinned to the wall, a red rubber stamp mark (no words), a magnifying glass, a keyhole shape',
        efek='harsh top light, dust in the air, teal-and-red contrast',
        judul1='bone-white 3D letters with a typewriter grit', judul2='deep red (#c1121f) stamped 3D letters',
        kicker='bone white', palet='dark teal, bone white, deep red'),
    'pasar': dict(
        latar='warm dark trading-desk scene with soft city lights and a glowing chart wall',
        subjek='dramatic and premium, warm key light',
        props='a glowing green rising chart line, price tags swinging, coins and banknotes (no real currency text), receipts',
        efek='warm golden light, green glow from the chart, sparkles on coins',
        judul1='bold white 3D letters with a subtle gold edge', judul2='bright lime-green (#a6f020) 3D letters with an orange (#ff7a00) shadow',
        kicker='lime green', palet='warm dark brown, lime green, orange, gold'),
    'tv': dict(
        latar='retro living room with a wooden TV set and a colorful sunburst pattern behind',
        subjek='playful and expressive, bright studio light',
        props='a vintage wooden TV, stickers, retro starbursts, scan lines, confetti',
        efek='scanline glow, cheerful saturated light',
        judul1='chunky white 3D retro letters with a thick outline', judul2='bright yellow (#ffde59) and pink (#ff3d7f) 3D retro letters',
        kicker='hot pink', palet='warm retro colors, yellow, pink, cream'),
    'modern': dict(
        latar='modern city at night with glass towers and neon reflections',
        subjek='realistic, cinematic, strong rim light',
        props='floating smartphone screens and news-style lower panels (only icons, no readable text), map pins, photo cards',
        efek='city bokeh, cinematic teal-and-orange grading',
        judul1='bold white 3D letters with a glossy finish', judul2='bright yellow (#ffd23f) 3D letters with a red (#e63946) shadow',
        kicker='yellow', palet='night blue, white, yellow, red'),
    'perang': dict(
        latar='dusty faded battlefield atmosphere with an old map texture and smoke',
        subjek='solemn, dust-covered, desaturated, respectful (no gore)',
        props='an old map with route lines, rubble silhouettes, document fragments, a red marker circle',
        efek='drifting dust and smoke, muted colors, low sun',
        judul1='stenciled bone-white 3D letters with worn edges', judul2='dark red (#b3261e) stenciled 3D letters',
        kicker='dusty beige', palet='dusty grey, beige, dark red'),
    'alam': dict(
        latar='dramatic natural landscape at golden hour with depth and atmosphere',
        subjek='vivid and alive, natural light, realistic',
        props='specimen cards, leaves or water droplets, a lens circle highlight, small field-guide sketches',
        efek='golden sunlight rays, floating pollen, shallow depth of field',
        judul1='bold white 3D letters with a natural soft shadow', judul2='warm golden (#ffd166) 3D letters',
        kicker='warm gold', palet='forest green, golden light, sky blue'),
    'editorial': dict(
        latar='light grey editorial background with soft vignette, big grey crescent arcs and thin dashed lines',
        subjek='black-and-white, clean studio cut-out with a soft shadow',
        props='white rounded cards, a black highlight box, minimal UI elements, thin dashed connector lines',
        efek='soft even studio light, minimal and premium',
        judul1='bold black 3D letters with a clean matte finish', judul2='white 3D letters inside a bold red (#c8202e) box',
        kicker='dark grey', palet='light grey, white, black, one red'),
    'kartu': dict(
        latar='navy blue (#051D40) background with a subtle light grid and retro paper cards',
        subjek='a friendly 3D cartoon character mascot in a clear pose (consistent series character), or the key object in 3D',
        props='retro paper cards taped with washi tape, chat bubbles, keyboard keys, small stickers',
        efek='soft studio light, playful pop shadows',
        judul1='bold white 3D letters with a navy outline', judul2='white letters on a red (#E63946) 3D sticker',
        kicker='yellow', palet='navy, white, red, yellow'),
}
ALIAS = {'acuan': 'teknologi'}


def gaya_untuk(tema):
    return GAYA.get(tema) or GAYA.get(ALIAS.get(tema, '')) or GAYA['teknologi']


def baca_konfig(kerja):
    k = (Path(kerja) / 'konfig.js').read_text(encoding='utf-8')
    rasio = re.search(r"rasio:\s*'([\d:]+)'", k); tema = re.search(r"tema:\s*'([\w-]+)'", k); judul = re.search(r"judul:\s*'([^']+)'", k)
    return (rasio.group(1) if rasio else '9:16'), (tema.group(1) if tema else 'teknologi'), (judul.group(1) if judul else Path(kerja).parent.name)


TEMPLAT_ISI = {
    'judul': ['BARIS PERTAMA', 'BARIS AKSEN'],
    'aksen': 1,
    'kicker': 'konteks singkat · 2-5 kata (boleh kosong)',
    'subjek': 'subjek utama dalam bahasa Inggris, mis. a modern smartphone with a worried cartoon face',
    'pendukung': ['3-6 elemen pendukung dari isi video, bahasa Inggris'],
    'tambahan': '',
    'tema': '',
}


def prompt_sampul(isi, rasio, tema, varian=0):
    g = dict(gaya_untuk(isi.get('tema') or tema)); g.update(isi.get('gaya') or {})
    potret = rasio == '9:16'
    baris = [b.strip() for b in isi['judul'] if b.strip()]
    aksen = isi.get('aksen', len(baris) - 1)
    teks_judul = '; '.join(f'line {i + 1} "{b}" in {g["judul2"] if i == aksen else g["judul1"]}' for i, b in enumerate(baris))
    semua = [*baris] + ([isi['kicker']] if isi.get('kicker') else [])
    if potret:
        tata = (f'Vertical 9:16 poster, YouTube Shorts / Reels cover, 1080x1920. The subject ({isi["subjek"]}) is the hero in the center of the frame, '
                f'{g["subjek"]}. The huge title sits in the lower third, spanning almost the full width (about 85% of the width), stacked in {len(baris)} lines: {teks_judul}; '
                'heavy geometric sans-serif (or the serif named above), perfectly kerned, slight perspective, strong depth and glow so it reads at thumbnail size. '
                + (f'At the top, a small single line of text "{isi["kicker"]}" in {g["kicker"]}. ' if isi.get('kicker') else '')
                + 'Keep the title and the subject inside the central safe area; nothing important in the outer 6% of the frame.')
    else:
        tata = (f'Horizontal 16:9 YouTube thumbnail, 1280x720. The subject ({isi["subjek"]}) is large on the right side, {g["subjek"]}. '
                f'The huge title fills the left 55-60% of the frame, stacked in {len(baris)} lines: {teks_judul}; heavy geometric sans-serif (or the serif named above), '
                'perfectly kerned, strong depth and glow so it reads at small size. '
                + (f'Above the title, a small single line of text "{isi["kicker"]}" in {g["kicker"]}. ' if isi.get('kicker') else '')
                + 'Keep the bottom-right corner free of important details (video timestamp area).')
    pendukung = ', '.join(isi.get('pendukung') or [])
    var = ['', ' Camera slightly lower and closer to the subject for a more heroic, dramatic angle.',
           ' Alternative composition: the subject slightly off-center with more breathing room around the title, stronger contrast between background and title.'][varian % 3]
    return (f'{tata} Background: {g["latar"]}. Around the subject, floating at different depths (some in front, some behind, a few blurred in the foreground corners): '
            f'{pendukung}{", " if pendukung else ""}{g["props"]}. Lighting and effects: {g["efek"]}. Color palette: {g["palet"]}. '
            + (f'{isi["tambahan"]} ' if isi.get('tambahan') else '')
            + 'Premium, polished, high-detail digital poster art, cinematic lighting, high contrast, sharp focus on the subject and the title, '
            'clean readable composition with one clear focal point.' + var
            + f' The only text in the image is exactly: {", ".join(chr(34) + s + chr(34) for s in semua)} - spelled exactly as written, every letter correct. '
            'Any interface cards or screens show only icons, toggles, bars and simple shapes, no small readable words, no gibberish text. '
            'No watermark, no logos, no real brand marks, no real person\'s face, no signature, no frame border.')


def rencana(a):
    kerja = Path(a.kerja); d = kerja / 'sampul'; d.mkdir(parents=True, exist_ok=True); f = d / 'isi.json'
    rasio, tema, judul_video = baca_konfig(kerja)
    if not f.exists():
        t = dict(TEMPLAT_ISI); t['tema'] = tema
        f.write_text(json.dumps(t, ensure_ascii=False, indent=1), encoding='utf-8')
        sys.exit(f'isi sampul belum ada: templat dibuat di {f}. Isi judul (2-4 kata per baris, maks 2 baris), aksen, kicker, subjek, pendukung, lalu jalankan lagi.')
    isi = json.loads(f.read_text(encoding='utf-8'))
    if any('BARIS' in b for b in isi['judul']):
        sys.exit(f'isi.json masih templat: {f}')
    tema = isi.get('tema') or tema
    scenes = [prompt_sampul(isi, rasio, tema, i) for i in range(3)]
    proyek = 'sampul-' + re.sub(r'[^a-z0-9]+', '-', judul_video.lower()).strip('-')[:40]
    (d / 'flow_sampul.json').write_text(json.dumps({'project': proyek, 'aspect_ratio': '9:16' if rasio == '9:16' else '16:9', 'scenes': scenes}, ensure_ascii=False, indent=1), encoding='utf-8')
    video = kerja.parent
    ukuran = '1080×1920 (9:16, potret)' if rasio == '9:16' else '1280×720 (16:9, lanskap)'
    md = [f'# Prompt sampul — {judul_video}', '',
          f'Rasio sampul: **{ukuran}**, mengikuti rasio video. Style: **{tema}** (`references/sampul.md`). Teks di sampul: '
          + ' / '.join(f'**{b}**' for b in isi['judul']) + (f' · kicker "{isi["kicker"]}"' if isi.get('kicker') else '') + '.', '',
          'Cara pakai: buka Google Flow (gambar, 0 kredit; atau Gemini / Nano Banana), tempel salah satu prompt, pilih rasio yang sama, buat 2-4 hasil, '
          'pilih yang ejaan judulnya benar dan terbaca di ukuran kecil, lalu simpan sebagai `sampul.jpg` di folder video ini.', '']
    for i, s in enumerate(scenes, 1):
        md += [f'## Varian {i}', '```', s, '```', '']
    (video / 'prompt-sampul.md').write_text('\n'.join(md), encoding='utf-8')
    print(f'ok 3 prompt -> {d / "flow_sampul.json"} (flow_agent_images: project={proyek}, aspect_ratio={"9:16" if rasio == "9:16" else "16:9"}) + {video / "prompt-sampul.md"}')


def target(rasio):
    return (1080, 1920) if rasio == '9:16' else (1280, 720)


def pas(im, w, h):
    from PIL import Image
    s = max(w / im.width, h / im.height); im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def ambil(a):
    from PIL import Image, ImageDraw, ImageFont
    kerja = Path(a.kerja); d = kerja / 'sampul'; d.mkdir(parents=True, exist_ok=True)
    rasio, _, _ = baca_konfig(kerja); w, h = target(rasio)
    calon = sorted([f for f in Path(a.dari).iterdir() if f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.webp')], key=lambda f: f.name)
    if not calon: sys.exit('tidak ada gambar di ' + a.dari)
    for f in d.glob('calon-*.jpg'): f.unlink()
    ims = []
    for i, f in enumerate(calon, 1):
        im = pas(Image.open(f).convert('RGB'), w, h); im.save(d / f'calon-{i}.jpg', quality=92); ims.append(im)
        print(f'calon-{i}: {f.name} ({Image.open(f).size[0]}×{Image.open(f).size[1]})')
    # lembar pilih: tiap calon besar + ukuran feed (± lebar 150 px potret / 240 px lanskap) supaya keterbacaan judul terlihat
    besar = 420 if rasio == '9:16' else 640; kecil = 150 if rasio == '9:16' else 240
    hb = round(besar * h / w); hk = round(kecil * h / w)
    lembar = Image.new('RGB', (len(ims) * (besar + kecil + 40) + 20, hb + 70), (24, 24, 28)); dr = ImageDraw.Draw(lembar)
    try: fn = ImageFont.truetype('arialbd.ttf', 26)
    except OSError: fn = ImageFont.load_default()
    for i, im in enumerate(ims):
        x = 20 + i * (besar + kecil + 40)
        lembar.paste(im.resize((besar, hb), Image.LANCZOS), (x, 50)); lembar.paste(im.resize((kecil, hk), Image.LANCZOS), (x + besar + 10, 50))
        dr.text((x, 12), f'calon-{i + 1}  (kanan: ukuran feed)', fill=(255, 220, 90), font=fn)
    lembar.save(d / '_calon.jpg', quality=88)
    print(f'lihat {d / "_calon.jpg"}: cek ejaan judul, keterbacaan di ukuran feed, tidak ada teks acak/logo/wajah orang nyata; lalu `pilih`.')


def pilih(a):
    from PIL import Image
    kerja = Path(a.kerja); d = kerja / 'sampul'; src = d / f'calon-{a.n}.jpg'
    if not src.exists(): sys.exit(f'{src} tidak ada (jalankan ambil dulu)')
    im = Image.open(src).convert('RGB'); video = kerja.parent
    for q in (92, 88, 84, 80, 75):
        out = video / 'sampul.jpg'; im.save(out, quality=q, optimize=True, progressive=True)
        if out.stat().st_size <= 2 * 1024 * 1024: break
    im.save(d / 'sampul.jpg', quality=q, optimize=True)
    print(f'ok {out} ({im.width}×{im.height}, {out.stat().st_size / 1e6:.2f} MB, kualitas {q})')


def daftar(a):
    for k, g in GAYA.items():
        print(f'{k:18} {g["palet"]}  |  judul: {g["judul1"][:40]} / {g["judul2"][:40]}')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='perintah', required=True)
    q = sub.add_parser('rencana'); q.add_argument('kerja'); q.set_defaults(f=rencana)
    q = sub.add_parser('ambil'); q.add_argument('kerja'); q.add_argument('--dari', required=True); q.set_defaults(f=ambil)
    q = sub.add_parser('pilih'); q.add_argument('kerja'); q.add_argument('n', type=int); q.set_defaults(f=pilih)
    q = sub.add_parser('gaya'); q.set_defaults(f=daftar)
    a = ap.parse_args(); a.f(a)


if __name__ == '__main__':
    main()
