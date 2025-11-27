# 🧪 Testing Guide

Panduan lengkap untuk testing aplikasi Clinic Grabber.

## 📋 Prerequisites

- Python 3.11+
- Node.js 18+
- npm atau yarn
- Browser modern (Chrome, Firefox, Safari)

---

## 🔧 Backend Testing

### 1. Setup Backend

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
```

Server akan berjalan di: `http://localhost:5000`

### 2. Test API Endpoints

#### Test Health Check

```bash
curl http://localhost:5000/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-11-27T10:00:00.123456"
}
```

#### Test Root Endpoint

```bash
curl http://localhost:5000/
```

**Expected Response:**
```json
{
  "status": "success",
  "message": "API Pencari Klinik Terdekat",
  "endpoints": {
    "/search/clinic": "Cari klinik berdasarkan keyword",
    "/search/nearby": "Cari klinik terdekat berdasarkan lokasi"
  }
}
```

#### Test Search by Keyword

```bash
curl "http://localhost:5000/search/clinic?keyword=sehat"
```

**Expected Response:**
```json
{
  "status": "success",
  "total": 3,
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
    },
    ...
  ]
}
```

#### Test Search Nearby

```bash
curl "http://localhost:5000/search/nearby?lat=-6.2088&lng=106.8456&radius=10"
```

**Expected Response:**
```json
{
  "status": "success",
  "total": 10,
  "user_location": {
    "lat": -6.2088,
    "lng": 106.8456
  },
  "radius_km": 10,
  "data": [
    {
      "id": 1,
      "nama_klinik": "Klinik Sehat Sentosa",
      "jarak_km": 0.0,
      ...
    },
    ...
  ]
}
```

#### Test Error Handling

**Missing keyword:**
```bash
curl "http://localhost:5000/search/clinic"
```

**Expected Response:**
```json
{
  "status": "error",
  "message": "Parameter 'keyword' diperlukan"
}
```

**Missing location:**
```bash
curl "http://localhost:5000/search/nearby"
```

**Expected Response:**
```json
{
  "status": "error",
  "message": "Parameter 'lat' dan 'lng' diperlukan"
}
```

---

## 🌐 Frontend Testing

### 1. Setup Frontend

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend akan berjalan di: `http://localhost:5173`

### 2. Manual UI Testing

#### Test 1: Search by Keyword

1. Open `http://localhost:5173` di browser
2. Pastikan backend sudah running
3. Ketik "sehat" di search box
4. Click "Cari" button
5. **Expected:** Muncul cards klinik yang mengandung kata "sehat"
6. **Verify:**
   - Loading spinner muncul saat request
   - Cards muncul dengan data lengkap
   - Contact info ditampilkan
   - Action buttons berfungsi

#### Test 2: Search Nearby with GPS

1. Click "Temukan Klinik Terdekat" button
2. Allow browser location access
3. **Expected:** 
   - Loading spinner muncul
   - Cards muncul dengan jarak (km)
   - Sorted by distance (terdekat dulu)
4. **Verify:**
   - Distance badge muncul
   - All clinic info displayed
   - Maps URL correct

#### Test 3: Action Buttons

**Test Call Button:**
1. Click "📞 Telepon" button
2. **Expected:** Opens phone dialer with correct number

**Test WhatsApp Button:**
1. Click "💬 WhatsApp" button
2. **Expected:** Opens WhatsApp with correct number
3. **Verify:** URL format: `https://wa.me/6281234567890`

**Test Email Button:**
1. Click "✉️ Email" button
2. **Expected:** Opens email client
3. **Verify:** Correct email address pre-filled

**Test Maps Button:**
1. Click "🗺️ Maps" button
2. **Expected:** Opens Google Maps in new tab
3. **Verify:** Correct location shown

#### Test 4: Error Handling

**Backend Not Running:**
1. Stop backend server
2. Try searching
3. **Expected:** Error message displayed
4. **Message:** "Gagal menghubungi server..."

**No Results:**
1. Search with keyword "xyz123notfound"
2. **Expected:** Empty state displayed
3. **Message:** "Tidak ada klinik ditemukan"

**Geolocation Denied:**
1. Deny location permission
2. Click "Temukan Klinik Terdekat"
3. **Expected:** Error message
4. **Message:** "Gagal mendapatkan lokasi..."

#### Test 5: API Configuration

1. Click "⚙️ Konfigurasi API Backend" 
2. Expand section
3. Change backend URL to different port
4. **Expected:** Can override API URL
5. Try search with new URL

#### Test 6: Responsive Design

**Desktop:**
- Cards in grid (multiple columns)
- Full-width search bar

**Tablet:**
- Cards in 2 columns
- Responsive buttons

**Mobile:**
- Cards stack vertically
- Search bar full width
- Buttons stack vertically

### 3. Browser Compatibility

Test di:
- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers

---

## 🏗️ Build Testing

### Test Production Build

```bash
cd frontend

# Build for production
npm run build

# Preview build
npm run preview
```

**Verify:**
- ✅ Build completes without errors
- ✅ `dist/` folder created
- ✅ All assets included
- ✅ App works in preview mode

---

## 🔍 API Test Script

Create `test_api.sh`:

```bash
#!/bin/bash

API_URL="http://localhost:5000"

echo "Testing Backend API..."
echo ""

echo "1. Health Check"
curl -s "$API_URL/health" | python3 -m json.tool
echo ""

echo "2. Root Endpoint"
curl -s "$API_URL/" | python3 -m json.tool
echo ""

echo "3. Search by Keyword"
curl -s "$API_URL/search/clinic?keyword=sehat" | python3 -m json.tool | head -30
echo ""

echo "4. Search Nearby"
curl -s "$API_URL/search/nearby?lat=-6.2088&lng=106.8456&radius=5" | python3 -m json.tool | head -30
echo ""

echo "5. Error Test - Missing Keyword"
curl -s "$API_URL/search/clinic" | python3 -m json.tool
echo ""

echo "6. Error Test - Missing Location"
curl -s "$API_URL/search/nearby" | python3 -m json.tool
echo ""

echo "All tests completed!"
```

Run:
```bash
chmod +x test_api.sh
./test_api.sh
```

---

## 📊 Performance Testing

### Backend Load Test

Using Apache Bench:

```bash
# Install ab (Apache Bench)
sudo apt-get install apache2-utils

# Test 1000 requests, 10 concurrent
ab -n 1000 -c 10 "http://localhost:5000/search/clinic?keyword=sehat"
```

**Expected:**
- Requests per second: > 100 rps
- No failed requests
- Mean response time: < 100ms

### Frontend Performance

1. Open Chrome DevTools
2. Run Lighthouse audit
3. **Target Scores:**
   - Performance: > 90
   - Accessibility: > 95
   - Best Practices: > 90
   - SEO: > 80

---

## 🐛 Common Issues & Solutions

### Issue 1: CORS Error

**Symptom:**
```
Access to XMLHttpRequest blocked by CORS policy
```

**Solution:**
Check backend CORS settings in `app.py`:
```python
from flask_cors import CORS
CORS(app)  # Should allow all origins in dev
```

### Issue 2: Port Already in Use

**Symptom:**
```
Port 5000 is in use by another program
```

**Solution:**
```bash
# Find process
lsof -i :5000

# Kill process
kill -9 <PID>
```

### Issue 3: Module Not Found

**Symptom:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
# Activate venv
source venv/bin/activate

# Reinstall
pip install -r requirements.txt
```

### Issue 4: npm Install Fails

**Symptom:**
```
npm ERR! code ENOENT
```

**Solution:**
```bash
# Clear cache
npm cache clean --force

# Remove node_modules
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

---

## ✅ Testing Checklist

### Backend
- [ ] Health endpoint responds
- [ ] Root endpoint shows API info
- [ ] Search by keyword works
- [ ] Search nearby calculates distance
- [ ] CORS enabled
- [ ] Error handling works
- [ ] JSON responses valid
- [ ] No database required

### Frontend
- [ ] App loads without errors
- [ ] Search by keyword works
- [ ] Nearby search works
- [ ] GPS permission handled
- [ ] Cards display correctly
- [ ] All buttons functional
- [ ] Loading states work
- [ ] Error states work
- [ ] Empty states work
- [ ] Responsive on mobile
- [ ] API URL configurable
- [ ] Build succeeds

### Integration
- [ ] Frontend connects to backend
- [ ] Data displays correctly
- [ ] Actions work (call, WhatsApp, email, maps)
- [ ] Distance calculated correctly
- [ ] No console errors

### Deployment
- [ ] Backend deployable
- [ ] Frontend builds
- [ ] Environment variables work
- [ ] HTTPS works (Netlify)
- [ ] Cross-origin requests work

---

## 📝 Test Report Template

```markdown
# Test Report

**Date:** 2024-11-27
**Tester:** Your Name
**Environment:** Development/Production

## Backend Tests
- [ ] Health Check: PASS/FAIL
- [ ] Search Clinic: PASS/FAIL
- [ ] Search Nearby: PASS/FAIL
- [ ] Error Handling: PASS/FAIL

## Frontend Tests
- [ ] UI Loads: PASS/FAIL
- [ ] Search Works: PASS/FAIL
- [ ] GPS Works: PASS/FAIL
- [ ] Actions Work: PASS/FAIL
- [ ] Responsive: PASS/FAIL

## Issues Found
1. Issue description
2. Steps to reproduce
3. Expected vs Actual

## Recommendations
- List of improvements
```

---

**Happy Testing! 🎉**
