# FinWise - AI Financial Advisor Chatbot

FinWise adalah aplikasi web chatbot interaktif yang berfungsi sebagai penasihat keuangan pribadi berbasis AI. Dibangun menggunakan Streamlit dan ditenagai oleh model bahasa canggih dari Google (Gemini-1.5-flash), aplikasi ini dirancang untuk membantu pengguna memahami dan mengelola keuangan mereka dengan lebih baik.

## 📜 Deskripsi Proyek

Tujuan utama dari proyek ini adalah menyediakan asisten virtual yang dapat menjawab berbagai pertanyaan seputar keuangan, mulai dari konsep dasar seperti budgeting dan menabung, hingga topik yang lebih kompleks seperti analisis investasi. Chatbot ini dapat berinteraksi secara dinamis dan memberikan jawaban yang relevan sesuai dengan konteks yang diberikan oleh pengguna, termasuk kemampuan untuk menganalisis data dari file yang diunggah.

## ✨ Fitur Utama

- **Antarmuka Interaktif**: Tampilan chat yang modern dan mudah digunakan berkat framework Streamlit.
- **Penasihat Keuangan AI**: Ditenagai oleh model `gemini-1.5-flash` dari Google untuk memberikan jawaban yang akurat dan relevan.
- **Analisis Dokumen**: Pengguna dapat mengunggah file dalam format `.txt`, `.csv`, atau `.pdf` (seperti laporan pengeluaran atau data keuangan) untuk dianalisis dan mendapatkan *insight*.
- **Peran & Perilaku Terpersonalisasi**: AI diprogram untuk bertindak sebagai penasihat keuangan profesional yang ramah, edukatif, dan menjaga privasi pengguna.
- **Manajemen State**: Menyimpan riwayat percakapan selama sesi berlangsung untuk menjaga kontinuitas obrolan.

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman**: Python
- **Framework Web**: Streamlit
- **Model AI**: Google Gemini-1.5-flash
- **Orkestrasi AI**: LangChain & LangGraph (khususnya `create_react_agent`)
- **Manajemen Environment**: `dotenv`
- **Manipulasi Data**: Pandas (untuk file `.csv`)
- **Ekstraksi Teks PDF**: PyPDF2 (untuk file `.pdf`)

## ⚙️ Instalasi & Konfigurasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini di lingkungan lokal Anda.

### 1. Clone Repository

```bash
git clone <URL_REPOSITORY_ANDA>
cd chatbot-streamlit
```

### 2. Buat dan Aktifkan Virtual Environment (Direkomendasikan)

- **Windows**:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instal Dependensi

Pastikan Anda sudah menginstal semua library yang dibutuhkan dengan menjalankan perintah berikut:

```bash
pip install -r requirements.txt
```
Aplikasi ini juga menggunakan `pandas` dan `PyPDF2` yang akan diimpor saat file `.csv` atau `.pdf` diunggah. Anda bisa menginstalnya terlebih dahulu:
```bash
pip install pandas PyPDF2
```

### 4. Konfigurasi Environment Variable

Aplikasi ini memerlukan kunci API dari Google untuk mengakses model Gemini.

- Buat file baru bernama `.env` di direktori root proyek.
- Salin konten dari `.env.example` ke dalam file `.env`.
- Ganti `Your API Key` dengan kunci API Google Anda yang valid.

**.env**
```
GOOGLE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

File `.gitignore` sudah dikonfigurasi untuk mengabaikan file `.env` agar kunci API Anda tidak terekspos ke repository.

## 🚀 Cara Menjalankan Aplikasi

Setelah semua langkah instalasi dan konfigurasi selesai, jalankan aplikasi Streamlit dengan perintah berikut di terminal Anda:

```bash
streamlit run react_chatbot.py
```

Aplikasi akan terbuka secara otomatis di browser default Anda dengan alamat lokal (biasanya `http://localhost:8501`).

## 📝 Cara Penggunaan

1. Buka aplikasi di browser Anda.
2. Anda akan disambut oleh FinWise.
3. (Opsional) Unggah file `.txt`, `.csv`, atau `.pdf` yang berisi data keuangan yang ingin Anda diskusikan.
4. Ketik pertanyaan Anda di kolom input chat dan tekan Enter.
5. AI akan memproses pertanyaan Anda (dan konten file jika ada) lalu memberikan respons.
