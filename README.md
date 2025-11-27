# 🏥 Clinic Grabber - Pencari Klinik Terdekat

Sistem pencarian klinik terdekat dengan informasi kontak lengkap (telepon, WhatsApp, email) tanpa menggunakan database. Backend Python menyediakan data secara real-time, dan frontend React dapat di-deploy ke Netlify.

## 👨‍⚕️ Author

**Lettu Kes dr. Muhammad Sobri Maulana, S.Kom, CEH, OSCP, OSCE**

- 🌐 GitHub: [github.com/sobri3195](https://github.com/sobri3195)
- 📧 Email: [muhammadsobrimaulana31@gmail.com](mailto:muhammadsobrimaulana31@gmail.com)
- 🌍 Website: [muhammadsobrimaulana.netlify.app](https://muhammadsobrimaulana.netlify.app)
- 🛒 Toko Online: [Pegasus Shop](https://pegasus-shop.netlify.app)

### 📱 Social Media

- 🎥 YouTube: [@muhammadsobrimaulana6013](https://www.youtube.com/@muhammadsobrimaulana6013)
- 📱 TikTok: [@dr.sobri](https://www.tiktok.com/@dr.sobri)
- ✈️ Telegram: [winlin_exploit](https://t.me/winlin_exploit)
- 💬 WhatsApp Group: [Join Here](https://chat.whatsapp.com/B8nwRZOBMo64GjTwdXV8Bl)

### 💰 Support & Donation

Jika project ini bermanfaat, Anda dapat mendukung pengembangan lebih lanjut melalui:

- 💳 Lynk: [lynk.id/muhsobrimaulana](https://lynk.id/muhsobrimaulana)
- ☕ Trakteer: [trakteer.id/g9mkave5gauns962u07t](https://trakteer.id/g9mkave5gauns962u07t)
- 🎨 Gumroad: [maulanasobri.gumroad.com](https://maulanasobri.gumroad.com/)
- 💝 KaryaKarsa: [karyakarsa.com/muhammadsobrimaulana](https://karyakarsa.com/muhammadsobrimaulana)
- 🎁 Nyawer: [nyawer.co/MuhammadSobriMaulana](https://nyawer.co/MuhammadSobriMaulana)
- 🌐 Sevalla: [muhammad-sobri-maulana-kvr6a.sevalla.page](https://muhammad-sobri-maulana-kvr6a.sevalla.page/)

---

## 📋 Fitur Utama

✅ **Tanpa Database** - Data diambil secara real-time setiap request  
✅ **Pencarian Keyword** - Cari klinik berdasarkan nama atau lokasi  
✅ **Pencarian Terdekat** - Gunakan GPS untuk menemukan klinik terdekat  
✅ **Informasi Kontak Lengkap** - Telepon, WhatsApp, Email, dan Maps  
✅ **Tombol Aksi Langsung** - Call, WhatsApp, Email, dan buka Maps  
✅ **Responsive Design** - Tampilan optimal di semua perangkat (Mobile, Tablet, Desktop)  
✅ **Deploy ke Netlify** - Frontend 100% statis, siap deploy  

## 🏗️ Struktur Project

```
clinic-grabber/
├── src/                     # React source files
│   ├── components/         # React components
│   ├── App.jsx             # Main app component
│   ├── App.css             # App styles
│   ├── index.css           # Global styles
│   └── main.jsx            # Entry point
│
├── backend/                # Python Flask API
│   ├── app.py              # Main application
│   ├── requirements.txt    # Python dependencies
│   └── README.md           # Backend documentation
│
├── public/                 # Static assets
├── dist/                   # Build output (generated)
├── index.html              # HTML template
├── package.json            # Node dependencies
├── vite.config.js          # Vite configuration
├── netlify.toml            # Netlify configuration
└── README.md               # This file
```

## 🚀 Quick Start

### Backend Setup

1. Navigate to backend folder:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   python app.py
   ```

   Server akan berjalan di `http://localhost:5000`

### Frontend Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Run development server:
   ```bash
   npm run dev
   ```

   Frontend akan berjalan di `http://localhost:5173`

3. Build for production:
   ```bash
   npm run build
   ```

   Build output akan ada di folder `dist/`

## 📡 API Endpoints

### 1. Search by Keyword

```
GET /search/clinic?keyword={keyword}
```

**Parameters:**
- `keyword` (required): Kata kunci pencarian

**Response:**
```json
{
  "status": "success",
  "total": 2,
  "data": [
    {
      "id": 1,
      "nama_klinik": "Klinik Sehat Sentosa",
      "alamat": "Jl. Sudirman No. 123, Jakarta Pusat",
      "telepon": "021-12345678",
      "whatsapp": "6281234567890",
      "email": "info@sehatsentosa.com",
      "kategori": "Klinik Umum",
      "maps_url": "https://www.google.com/maps/search/?api=1&query=-6.2088,106.8456"
    }
  ]
}
```

### 2. Search Nearby

```
GET /search/nearby?lat={lat}&lng={lng}&radius={radius}
```

**Parameters:**
- `lat` (required): Latitude posisi user
- `lng` (required): Longitude posisi user
- `radius` (optional): Radius pencarian dalam km (default: 5)

**Response:**
```json
{
  "status": "success",
  "total": 3,
  "user_location": {
    "lat": -6.2088,
    "lng": 106.8456
  },
  "radius_km": 10,
  "data": [
    {
      "id": 1,
      "nama_klinik": "Klinik Sehat Sentosa",
      "alamat": "Jl. Sudirman No. 123, Jakarta Pusat",
      "telepon": "021-12345678",
      "whatsapp": "6281234567890",
      "email": "info@sehatsentosa.com",
      "kategori": "Klinik Umum",
      "maps_url": "https://www.google.com/maps/search/?api=1&query=-6.2088,106.8456",
      "jarak_km": 0.5
    }
  ]
}
```

## 🌐 Deployment

### Deploy Backend

**Option 1: Heroku**
```bash
cd backend
heroku create your-clinic-api
git subtree push --prefix backend heroku main
```

**Option 2: Railway**
1. Connect repository di Railway.app
2. Set root directory ke `backend`
3. Railway akan auto-detect Python

**Option 3: Render**
1. Connect repository di Render.com
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `gunicorn app:app`

### Deploy Frontend ke Netlify

**Option 1: Netlify CLI**
```bash
npm run build
netlify deploy --prod
```

**Option 2: Git Auto-Deploy (Recommended)**
1. Push ke GitHub/GitLab
2. Connect repository di Netlify
3. Netlify akan otomatis detect build settings dari `netlify.toml`
4. Add environment variable di Netlify dashboard:
   - `VITE_API_URL`: URL backend API Anda
5. Deploy akan otomatis berjalan setiap push ke main branch

**Option 3: Manual Upload**
```bash
npm run build
# Upload folder 'dist' ke Netlify dashboard
```

**Konfigurasi Otomatis:**
- Build command: `npm run build` (dari netlify.toml)
- Publish directory: `dist` (dari netlify.toml)
- Redirects untuk SPA sudah dikonfigurasi

## ⚙️ Konfigurasi

### Backend CORS

Edit `backend/app.py` untuk membatasi CORS origins di production:

```python
from flask_cors import CORS

# Development - allow all
CORS(app)

# Production - specific origins
CORS(app, resources={
    r"/*": {
        "origins": ["https://your-app.netlify.app"]
    }
})
```

### Frontend API URL

Edit `.env.production`:

```env
VITE_API_URL=https://your-backend-api.herokuapp.com
```

Atau set via Netlify Dashboard (Recommended):
1. Site settings → Environment variables
2. Add `VITE_API_URL` dengan URL backend Anda
3. Redeploy site untuk apply perubahan

## 🔧 Integrasi Google Places API (Opsional)

Untuk menggunakan data real dari Google Places:

1. **Dapatkan API Key:**
   - Buka [Google Cloud Console](https://console.cloud.google.com/)
   - Create new project atau pilih existing
   - Enable "Places API"
   - Create credentials (API Key)

2. **Update Backend:**

```python
import requests

GOOGLE_API_KEY = os.environ.get('GOOGLE_PLACES_API_KEY')

@app.route('/search/nearby', methods=['GET'])
def search_nearby():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    radius = request.args.get('radius', 5000)  # meters
    
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f"{lat},{lng}",
        'radius': radius,
        'type': 'health',
        'key': GOOGLE_API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Transform data sesuai format aplikasi
    # ...
```

3. **Set Environment Variable:**

```bash
# Heroku
heroku config:set GOOGLE_PLACES_API_KEY=your_api_key

# Railway/Render - set via dashboard
```

## 📱 Cara Penggunaan

### Untuk User

1. **Pencarian dengan Keyword:**
   - Ketik nama klinik atau lokasi di search bar
   - Klik "Cari"
   - Hasil akan muncul dalam bentuk cards

2. **Pencarian Terdekat:**
   - Klik "Temukan Klinik Terdekat"
   - Izinkan browser mengakses lokasi
   - Klinik terdekat akan ditampilkan dengan jarak

3. **Menghubungi Klinik:**
   - **📞 Telepon**: Langsung call
   - **💬 WhatsApp**: Buka chat WA
   - **✉️ Email**: Kirim email
   - **🗺️ Maps**: Lihat di Google Maps

### Untuk Developer

**Tambah Data Klinik:**

Edit `backend/app.py`, tambahkan ke array `MOCK_CLINICS`:

```python
{
    "id": 11,
    "nama_klinik": "Klinik Baru",
    "alamat": "Jl. Contoh No. 123",
    "telepon": "021-12345678",
    "whatsapp": "6281234567890",
    "email": "info@klinikbaru.com",
    "lat": -6.2088,
    "lng": 106.8456,
    "kategori": "Klinik Umum"
}
```

**Customize UI:**

Edit `src/index.css` untuk mengubah:
- Colors
- Layout
- Animations
- Responsive breakpoints

## 📱 Mobile Responsive

Aplikasi ini telah dioptimalkan untuk berbagai ukuran layar:

- 📱 **Mobile (< 480px)**: Layout single column, font size optimal, touch-friendly buttons
- 📱 **Tablet (481px - 768px)**: Layout 1-2 columns, balanced spacing
- 💻 **Desktop (> 768px)**: Multi-column grid layout, full features

Fitur responsive:
- Flexible grid system
- Scalable typography
- Touch-optimized buttons (minimum 44x44px)
- Adaptive spacing and padding
- Mobile-first approach

## 🐛 Troubleshooting

### CORS Error

**Problem:** Frontend tidak bisa akses backend

**Solution:**
```python
# backend/app.py
from flask_cors import CORS
CORS(app, resources={r"/*": {"origins": "*"}})
```

### Geolocation Not Working

**Problem:** Browser tidak bisa akses GPS

**Solution:**
- Pastikan menggunakan HTTPS (Netlify otomatis HTTPS)
- Check browser permissions
- Test di browser lain

### API Connection Failed

**Problem:** Frontend tidak bisa connect ke backend

**Solution:**
1. Check backend sudah running
2. Verify `VITE_API_URL` di `.env`
3. Test API endpoint di browser/Postman
4. Check CORS settings

## 📝 Technology Stack

**Backend:**
- Python 3.x
- Flask (Web framework)
- Flask-CORS (CORS handling)
- Gunicorn (Production server)

**Frontend:**
- React 18
- Vite (Build tool)
- Axios (HTTP client)
- CSS3 (Styling)

**Deployment:**
- Backend: Heroku/Railway/Render
- Frontend: Netlify
- Domain: Custom domain support

## 📄 License

MIT License - Feel free to use this project for personal or commercial purposes.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📧 Support

Jika ada pertanyaan atau issue:
1. Open an issue di GitHub
2. Contact via email: muhammadsobrimaulana31@gmail.com
3. Join WhatsApp Group untuk diskusi

## 🎯 Roadmap

- [x] Responsive design untuk semua device
- [ ] Integrasi dengan Google Places API
- [ ] Filter berdasarkan kategori klinik
- [ ] Rating dan review klinik
- [ ] Booking appointment online
- [ ] Multiple language support
- [ ] Dark mode
- [ ] Progressive Web App (PWA)

---

**Dibuat dengan ❤️ oleh dr. Muhammad Sobri Maulana untuk memudahkan pencarian klinik terdekat**

**Support the project:** [Donate Here](https://lynk.id/muhsobrimaulana) ☕
