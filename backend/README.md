# Backend API - Clinic Grabber

API Python Flask untuk mengambil data klinik terdekat tanpa database.

## Instalasi

```bash
pip install -r requirements.txt
```

## Menjalankan Server

```bash
python app.py
```

Server akan berjalan di `http://localhost:5000`

## Endpoints

### 1. GET /search/clinic
Cari klinik berdasarkan keyword

**Parameters:**
- `keyword` (required): Kata kunci pencarian

**Example:**
```
GET /search/clinic?keyword=sehat
```

### 2. GET /search/nearby
Cari klinik terdekat berdasarkan lokasi GPS

**Parameters:**
- `lat` (required): Latitude posisi user
- `lng` (required): Longitude posisi user
- `radius` (optional): Radius pencarian dalam km (default: 5)

**Example:**
```
GET /search/nearby?lat=-6.2088&lng=106.8456&radius=10
```

## Deployment

### Deploy ke Heroku, Railway, atau Render

1. Pastikan file `requirements.txt` sudah ada
2. Deploy menggunakan platform pilihan Anda
3. Set environment variable `PORT` jika diperlukan

## Integrasi Google Places API (Opsional)

Untuk menggunakan data real dari Google Places API:

1. Dapatkan API Key dari [Google Cloud Console](https://console.cloud.google.com/)
2. Aktifkan Google Places API
3. Tambahkan environment variable `GOOGLE_PLACES_API_KEY`
4. Modifikasi fungsi search untuk menggunakan Google Places API

## CORS

CORS sudah diaktifkan untuk semua origin. Untuk production, sebaiknya batasi origin yang diizinkan.
