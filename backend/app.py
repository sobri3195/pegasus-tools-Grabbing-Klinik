from flask import Flask, jsonify, request
from flask_cors import CORS
import math
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

MOCK_CLINICS = [
    {
        "id": 1,
        "nama_klinik": "Klinik Sehat Sentosa",
        "alamat": "Jl. Sudirman No. 123, Jakarta Pusat",
        "telepon": "021-12345678",
        "whatsapp": "6281234567890",
        "email": "info@sehatsentosa.com",
        "lat": -6.2088,
        "lng": 106.8456,
        "kategori": "Klinik Umum"
    },
    {
        "id": 2,
        "nama_klinik": "Klinik Medika Prima",
        "alamat": "Jl. Thamrin No. 45, Jakarta Pusat",
        "telepon": "021-87654321",
        "whatsapp": "6281234567891",
        "email": "contact@medikaprima.com",
        "lat": -6.1944,
        "lng": 106.8229,
        "kategori": "Klinik Spesialis"
    },
    {
        "id": 3,
        "nama_klinik": "Klinik Keluarga Sehat",
        "alamat": "Jl. Gatot Subroto No. 67, Jakarta Selatan",
        "telepon": "021-55512345",
        "whatsapp": "6281234567892",
        "email": "admin@keluargasehat.com",
        "lat": -6.2297,
        "lng": 106.8173,
        "kategori": "Klinik Keluarga"
    },
    {
        "id": 4,
        "nama_klinik": "Klinik Pratama Harapan",
        "alamat": "Jl. Rasuna Said No. 89, Jakarta Selatan",
        "telepon": "021-66678901",
        "whatsapp": "6281234567893",
        "email": "info@pratamaharapan.com",
        "lat": -6.2236,
        "lng": 106.8317,
        "kategori": "Klinik Pratama"
    },
    {
        "id": 5,
        "nama_klinik": "Klinik Cahaya Medika",
        "alamat": "Jl. HR Rasuna Said Kav. C-22, Jakarta Selatan",
        "telepon": "021-52901234",
        "whatsapp": "6281234567894",
        "email": "contact@cahayamedika.com",
        "lat": -6.2257,
        "lng": 106.8341,
        "kategori": "Klinik Umum"
    },
    {
        "id": 6,
        "nama_klinik": "Klinik Mitra Husada",
        "alamat": "Jl. Casablanca No. 88, Jakarta Selatan",
        "telepon": "021-29345678",
        "whatsapp": "6281234567895",
        "email": "info@mitrahusada.com",
        "lat": -6.2240,
        "lng": 106.8423,
        "kategori": "Klinik Umum"
    },
    {
        "id": 7,
        "nama_klinik": "Klinik Sejahtera Abadi",
        "alamat": "Jl. Kuningan Raya No. 12, Jakarta Selatan",
        "telepon": "021-83456789",
        "whatsapp": "6281234567896",
        "email": "admin@sejahteraabadi.com",
        "lat": -6.2382,
        "lng": 106.8304,
        "kategori": "Klinik Keluarga"
    },
    {
        "id": 8,
        "nama_klinik": "Klinik Griya Sehat",
        "alamat": "Jl. MT Haryono No. 34, Jakarta Timur",
        "telepon": "021-85567890",
        "whatsapp": "6281234567897",
        "email": "info@griyasehat.com",
        "lat": -6.2417,
        "lng": 106.8632,
        "kategori": "Klinik Umum"
    },
    {
        "id": 9,
        "nama_klinik": "Klinik Bina Husada",
        "alamat": "Jl. Tebet Raya No. 56, Jakarta Selatan",
        "telepon": "021-83901234",
        "whatsapp": "6281234567898",
        "email": "contact@binahusada.com",
        "lat": -6.2388,
        "lng": 106.8542,
        "kategori": "Klinik Pratama"
    },
    {
        "id": 10,
        "nama_klinik": "Klinik Permata Medika",
        "alamat": "Jl. Pancoran No. 78, Jakarta Selatan",
        "telepon": "021-79012345",
        "whatsapp": "6281234567899",
        "email": "admin@permatamedika.com",
        "lat": -6.2603,
        "lng": 106.8498,
        "kategori": "Klinik Spesialis"
    }
]

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    
    distance = R * c
    return round(distance, 2)

def format_clinic_data(clinic, user_lat=None, user_lng=None):
    formatted = {
        "id": clinic["id"],
        "nama_klinik": clinic["nama_klinik"],
        "alamat": clinic["alamat"],
        "telepon": clinic["telepon"],
        "whatsapp": clinic["whatsapp"],
        "email": clinic["email"],
        "kategori": clinic["kategori"],
        "maps_url": f"https://www.google.com/maps/search/?api=1&query={clinic['lat']},{clinic['lng']}"
    }
    
    if user_lat is not None and user_lng is not None:
        distance = calculate_distance(user_lat, user_lng, clinic["lat"], clinic["lng"])
        formatted["jarak_km"] = distance
    
    return formatted

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "API Pencari Klinik Terdekat",
        "endpoints": {
            "/search/clinic": "Cari klinik berdasarkan keyword",
            "/search/nearby": "Cari klinik terdekat berdasarkan lokasi"
        }
    })

@app.route('/search/clinic', methods=['GET'])
def search_clinic():
    keyword = request.args.get('keyword', '').lower()
    
    if not keyword:
        return jsonify({
            "status": "error",
            "message": "Parameter 'keyword' diperlukan"
        }), 400
    
    results = []
    for clinic in MOCK_CLINICS:
        if (keyword in clinic["nama_klinik"].lower() or 
            keyword in clinic["alamat"].lower() or
            keyword in clinic["kategori"].lower()):
            results.append(format_clinic_data(clinic))
    
    return jsonify({
        "status": "success",
        "total": len(results),
        "data": results
    })

@app.route('/search/nearby', methods=['GET'])
def search_nearby():
    try:
        lat = float(request.args.get('lat', 0))
        lng = float(request.args.get('lng', 0))
        radius = float(request.args.get('radius', 5))
    except ValueError:
        return jsonify({
            "status": "error",
            "message": "Parameter lat, lng, dan radius harus berupa angka"
        }), 400
    
    if lat == 0 or lng == 0:
        return jsonify({
            "status": "error",
            "message": "Parameter 'lat' dan 'lng' diperlukan"
        }), 400
    
    results = []
    for clinic in MOCK_CLINICS:
        distance = calculate_distance(lat, lng, clinic["lat"], clinic["lng"])
        if distance <= radius:
            clinic_data = format_clinic_data(clinic, lat, lng)
            results.append(clinic_data)
    
    results.sort(key=lambda x: x["jarak_km"])
    
    return jsonify({
        "status": "success",
        "total": len(results),
        "user_location": {
            "lat": lat,
            "lng": lng
        },
        "radius_km": radius,
        "data": results
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
