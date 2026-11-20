# Aset siap pakai

Gambar PNG berlatar transparan (latar hijau Flow sudah dibuang `scripts/potong_latar.py`). Dipakai ulang lewat `rakit --gambar <folder>` setelah disalin ke `_kerja\gambar\` video baru. **Tanpa video, audio, atau logo pihak lain.**

## `raka-3d/` — tokoh tetap seri tips AI
Raka: pria muda Indonesia gaya animasi 3D (Pixar-like), rambut hitam pendek rapi, kulit sawo matang, sweter rajut kuning mustard di atas kemeja putih berkerah. Dibuat di Google Flow (0 kredit, satu per satu) dengan `_acuan-raka.jpeg` sebagai gambar acuan (`reference_images`) supaya wajah dan baju tetap sama.

| Berkas | Pose |
|---|---|
| `tokoh-stop.png` | kaget, telapak tangan ke kamera (stop) |
| `tokoh-bingung.png` | bingung |
| `tokoh-aha.png` | dapat ide |
| `tokoh-tunjuk.png` | menunjuk |
| `tokoh-jempol.png` | jempol |
| `tokoh-save.png` | menyimpan / puas |
| `tokoh-pusing.png` | pusing di balik laptop, gulungan kertas panjang |
| `tokoh-gunting.png` | menggunting pita kertas panjang |
| `tokoh-kopi.png` | santai pegang kopi + jempol |

**Pose baru** (pakai `_acuan-raka.jpeg` sebagai referensi):
```
Pixar-style 3D animation, waist-up: the same 3D cartoon young Indonesian man (short black hair, mustard-yellow knit sweater over white collared shirt) <POSE / AKSI>, isolated on a flat pure green background, whole figure visible with margin, soft studio light, no readable text, no logos
```
Prompt pertama (pembentuk tokoh): `3D animated cartoon character in Pixar-style 3D animation, waist-up: a friendly young Indonesian man, short neat black hair, warm brown skin, big expressive eyes, wearing a mustard-yellow knit sweater over a white collared shirt, … soft subsurface skin, soft studio lighting, isolated on a flat pure green background, … no text, no logos`.

## `ikon-3d/` — benda 3D
`robot`, `bohlam`, `topeng`, `kaca` (kaca pembesar), `target`, `stopwatch`, `gunting`. Prompt:
```
Pixar-style 3D render of <BENDA>, entire object fully visible with a generous margin, isolated on a flat pure green background, soft studio light, no text, no logos
```

Aset baru yang bagus dari video berikutnya disalin ke sini (gambar saja), lalu tabel di atas diperbarui.
