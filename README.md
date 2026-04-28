# 🐍 Python Learning Hub

Koleksi materi pembelajaran Python untuk siswa SMA dan guru informatika.

**Live Site:** [https://natedekaka.github.io/python-learning/](https://natedekaka.github.io/python-learning/)

## 📚 Modul Pembelajaran

- **[Kurikulum Python Lengkap](modules/kurikulum.html)** - 6 modul dari dasar hingga Flask
- **[Kurikulum Guru Informatika](modules/kurikulum-guru.html)** - Panduan untuk guru
- **[Bahan Ajar SMA](modules/bahan-ajar-sma.html)** - Materi untuk siswa SMA
- **[Tutorial File I/O](modules/file-io.html)** - Manipulasi file CSV & JSON
- **[Latihan Python](modules/latihan.html)** - Kumpulan latihan coding

## 🚀 Enable GitHub Pages

Repository sudah dipush ke: https://github.com/natedekaka/python-learning

**Langkah aktivasi:**
1. Buka: https://github.com/natedekaka/python-learning/settings/pages
2. Di "Build and deployment" → Source: pilih **"Deploy from a branch"**
3. Branch: pilih **"main"** dan folder **"/ (root)"**
4. Klik **Save**

Website akan tersedia di: `https://natedekaka.github.io/python-learning/`

> ⏳ Tunggu 1-2 menit setelah aktivasi untuk deployment selesai.

## 🛠️ Tools

### Generate Table of Contents
```bash
python3 scripts/generate_toc.py
```
Menghasilkan `toc.json` dan `toc.md` dari file HTML di `modules/`.

## 📂 Struktur Project

```
python_learning/
├── index.html          # Homepage
├── modules/           # HTML tutorial files
│   ├── kurikulum.html
│   ├── kurikulum-guru.html
│   ├── bahan-ajar-sma.html
│   ├── file-io.html
│   └── latihan.html
├── css/
│   └── style.css     # Shared styles
├── scripts/
│   └── generate_toc.py
└── python files/      # Practice files (variabel.py, list.py, etc.)
```

## 📊 Progress Tracking

Cek `toc.json` untuk statistik modul (word count, reading time, headings).

---

**Dibuat dengan ❤️ untuk pembelajaran Python** 🐍✨
