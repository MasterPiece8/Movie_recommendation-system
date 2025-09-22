# app.py (Versi Perbaikan)

from flask import Flask, request, jsonify
import pickle
import pandas as pd

# --- 1. Inisialisasi Aplikasi Flask ---
app = Flask(__name__)

# --- 2. Muat Semua Aset (Model, Judul, dan Data Rating) SEKALI SAJA ---
print("Memuat model, judul, dan data rating...")
with open('recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('movie_titles.pkl', 'rb') as f:
    movie_titles = pickle.load(f)

# PERBAIKAN: Muat data rating di sini, bukan di dalam fungsi
ratings_df = pd.read_csv('u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])

print("Model dan data berhasil dimuat.")

# Buat daftar semua ID film untuk prediksi
all_movie_ids = list(movie_titles.keys())

# --- 3. Buat Fungsi untuk Memberikan Rekomendasi ---
def get_recommendations(user_id, n=10):
    # Dapatkan daftar film yang sudah ditonton oleh user dari DataFrame yang sudah dimuat
    watched_movies = ratings_df[ratings_df['user_id'] == user_id]['item_id'].tolist()

    # Prediksi rating untuk semua film yang BELUM ditonton
    predictions = []
    for movie_id in all_movie_ids:
        if movie_id not in watched_movies:
            pred = model.predict(uid=str(user_id), iid=str(movie_id))
            predictions.append((movie_id, pred.est))
            
    # Urutkan prediksi berdasarkan estimasi rating tertinggi
    predictions.sort(key=lambda x: x[1], reverse=True)
    
    # Ambil top N rekomendasi
    top_n_recs = predictions[:n]
    
    # Ubah ID film menjadi judul film
    recommended_movies = [{'title': movie_titles[movie_id], 'estimated_rating': round(rating, 2)} for movie_id, rating in top_n_recs]
    
    return recommended_movies

# --- 4. Buat Endpoint API ---
@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id', type=int)
    
    if user_id is None:
        return jsonify({'error': 'Parameter user_id tidak ditemukan'}), 400
        
    # Cek apakah user_id ada di dalam data
    if user_id not in ratings_df['user_id'].unique():
        return jsonify({'error': f'User dengan ID {user_id} tidak ditemukan di dalam dataset.'}), 404
        
    print(f"Memberikan rekomendasi untuk user_id: {user_id}")
    recommendations = get_recommendations(user_id)
    
    return jsonify(recommendations)

# --- 5. Jalankan Aplikasi ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)