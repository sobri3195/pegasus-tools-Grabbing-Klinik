"""
Example implementation using Google Places API
Replace MOCK_CLINICS with real data from Google Places API

To use this:
1. Get API Key from Google Cloud Console
2. Enable Places API
3. Set environment variable: GOOGLE_PLACES_API_KEY
4. pip install requests
5. Replace app.py with this file (or copy the functions you need)
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import math
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

GOOGLE_API_KEY = os.environ.get('GOOGLE_PLACES_API_KEY', '')

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

def get_place_details(place_id):
    """Get detailed information about a place"""
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        'place_id': place_id,
        'fields': 'name,formatted_address,formatted_phone_number,website,geometry',
        'key': GOOGLE_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['status'] == 'OK':
            return data['result']
        return None
    except Exception as e:
        print(f"Error getting place details: {e}")
        return None

def format_google_place(place, user_lat=None, user_lng=None):
    """Format Google Places result to our clinic format"""
    
    place_id = place.get('place_id', '')
    name = place.get('name', 'Unknown')
    address = place.get('vicinity', place.get('formatted_address', ''))
    
    lat = place['geometry']['location']['lat']
    lng = place['geometry']['location']['lng']
    
    phone = 'N/A'
    email = 'N/A'
    whatsapp = 'N/A'
    
    details = get_place_details(place_id)
    if details:
        phone = details.get('formatted_phone_number', 'N/A')
        if phone != 'N/A':
            whatsapp = phone.replace('+', '').replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
            if whatsapp.startswith('0'):
                whatsapp = '62' + whatsapp[1:]
    
    formatted = {
        "id": place_id,
        "nama_klinik": name,
        "alamat": address,
        "telepon": phone,
        "whatsapp": whatsapp,
        "email": email,
        "kategori": "Klinik",
        "maps_url": f"https://www.google.com/maps/place/?q=place_id:{place_id}"
    }
    
    if user_lat is not None and user_lng is not None:
        distance = calculate_distance(user_lat, user_lng, lat, lng)
        formatted["jarak_km"] = distance
    
    return formatted

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "API Pencari Klinik Terdekat (Google Places)",
        "endpoints": {
            "/search/clinic": "Cari klinik berdasarkan keyword",
            "/search/nearby": "Cari klinik terdekat berdasarkan lokasi"
        },
        "note": "Requires GOOGLE_PLACES_API_KEY environment variable"
    })

@app.route('/search/clinic', methods=['GET'])
def search_clinic():
    keyword = request.args.get('keyword', '')
    location = request.args.get('location', '-6.2088,106.8456')
    
    if not keyword:
        return jsonify({
            "status": "error",
            "message": "Parameter 'keyword' diperlukan"
        }), 400
    
    if not GOOGLE_API_KEY:
        return jsonify({
            "status": "error",
            "message": "Google Places API Key not configured"
        }), 500
    
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': f"klinik {keyword}",
        'location': location,
        'radius': 50000,
        'type': 'health',
        'key': GOOGLE_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['status'] == 'OK':
            results = [format_google_place(place) for place in data['results']]
            
            return jsonify({
                "status": "success",
                "total": len(results),
                "data": results
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"Google Places API error: {data['status']}"
            }), 500
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error: {str(e)}"
        }), 500

@app.route('/search/nearby', methods=['GET'])
def search_nearby():
    try:
        lat = float(request.args.get('lat', 0))
        lng = float(request.args.get('lng', 0))
        radius = int(float(request.args.get('radius', 5)) * 1000)
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
    
    if not GOOGLE_API_KEY:
        return jsonify({
            "status": "error",
            "message": "Google Places API Key not configured"
        }), 500
    
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f"{lat},{lng}",
        'radius': radius,
        'type': 'health',
        'keyword': 'klinik',
        'key': GOOGLE_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['status'] == 'OK':
            results = [format_google_place(place, lat, lng) for place in data['results']]
            results.sort(key=lambda x: x.get("jarak_km", 999))
            
            return jsonify({
                "status": "success",
                "total": len(results),
                "user_location": {
                    "lat": lat,
                    "lng": lng
                },
                "radius_km": radius / 1000,
                "data": results
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"Google Places API error: {data['status']}"
            }), 500
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error: {str(e)}"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "google_api_configured": bool(GOOGLE_API_KEY)
    })

if __name__ == '__main__':
    if not GOOGLE_API_KEY:
        print("\n⚠️  WARNING: GOOGLE_PLACES_API_KEY not set!")
        print("This app requires Google Places API Key to function.")
        print("Get your API key from: https://console.cloud.google.com/")
        print("Then set: export GOOGLE_PLACES_API_KEY=your_key_here\n")
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
