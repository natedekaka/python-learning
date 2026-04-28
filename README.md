# 🐍 Python Learning Hub

Koleksi materi pembelajaran Python untuk siswa SMA dan guru informatika.

## 📚 Modul Pembelajaran

- **[Kurikulum Python Lengkap](modules/kurikulum.html)** - 6 modul dari dasar hingga Flask
- **[Kurikulum Guru Informatika](modules/kurikulum-guru.html)** - Panduan untuk guru
- **[Bahan Ajar SMA](modules/bahan-ajar-sma.html)** - Materi untuk siswa SMA
- **[Tutorial File I/O](modules/file-io.html)** - Manipulasi file CSV & JSON
- **[Latihan Python](modules/latihan.html)** - Kumpulan latihan coding

## 🚀 Deploy ke GitHub Pages

### Opsi 1: Menggunakan GitHub CLI (Recommended)

```bash
# 1. Login ke GitHub
gh auth login

# 2. Create repo dan push
cd ~/projects/python_learning
gh repo create python-learning --public --source=. --push

# 3. Enable GitHub Pages
gh repo edit daniarsyah/python-learning --enable-pages --branch main
```

### Opsi 2: Manual via Web

```bash
# 1. Buat repo di https://github.com/new (nama: python-learning)
# 2. Push ke GitHub
cd ~/projects/python_learning
git remote add origin https://github.com/daniarsyah/python-learning.git
git push -u origin main
# 3. Buka Settings → Pages → Enable dari branch `main`
```

Website akan tersedia di: `https://daniarsyah.github.io/python-learning/`

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
