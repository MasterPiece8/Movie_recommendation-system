# Movie_recommendation-system
A simple Movie Recommendation API using Python, Flask, and Singular Value Decomposition (SVD). 🎬

# Sistem Rekomendasi Film (Movie Recommendation System)

Sebuah mini-proyek untuk membangun dan mendeploy sistem rekomendasi film. Proyek ini menggunakan metode **Collaborative Filtering** dengan algoritma **Singular Value Decomposition (SVD)** untuk memberikan prediksi rating dan merekomendasikan film kepada pengguna.

Aplikasi ini dibungkus dalam sebuah **web API sederhana** menggunakan **Flask** dan siap untuk diuji coba.



[Image of a film reel and popcorn]


---

## 🚀 Teknologi yang Digunakan

* **Python**: Bahasa pemrograman utama.
* **Pandas**: Untuk manipulasi dan analisis data.
* **Scikit-surprise**: Library utama untuk membangun model sistem rekomendasi.
* **Flask**: Micro-framework untuk membuat web API.
* **Dataset**: MovieLens 100k.

---

## ✨ Fitur Utama

* **Prediksi Rating**: Mampu memprediksi rating yang mungkin diberikan oleh seorang pengguna pada film yang belum ia tonton.
* **Rekomendasi Top-N**: Memberikan daftar N film teratas yang paling direkomendasikan untuk pengguna.
* **Endpoint API**: Menyediakan endpoint `/recommend` yang mudah digunakan untuk mendapatkan hasil rekomendasi.

---

## ⚙️ Instalasi & Cara Menjalankan

1.  **Clone Repository**
    ```bash
    git clone [https://github.com/NAMA_USERNAME_ANDA/NAMA_REPO_ANDA.git](https://github.com/NAMA_USERNAME_ANDA/NAMA_REPO_ANDA.git)
    cd NAMA_REPO_ANDA
    ```

2.  **Install Dependencies**
    Pastikan Anda sudah menginstal semua library yang dibutuhkan.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan Aplikasi**
    Aplikasi Flask akan berjalan di `http://127.0.0.1:5000`.
    ```bash
    python app.py
    ```

---

## API Endpoint

Untuk mendapatkan rekomendasi, kirim permintaan `GET` ke endpoint berikut:

* **URL**: `/recommend`
* **Method**: `GET`
* **Parameter**: `user_id` (integer)

**Contoh Penggunaan:**
