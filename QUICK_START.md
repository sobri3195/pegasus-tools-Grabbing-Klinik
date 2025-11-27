# ⚡ Quick Start Guide

Get up and running in 5 minutes!

## 🎯 Prerequisites

- Python 3.11+ 
- Node.js 18+
- Git

## 🚀 Option 1: One-Command Start (Linux/Mac)

```bash
./start.sh
```

That's it! The script will:
1. ✅ Setup backend virtual environment
2. ✅ Install Python dependencies
3. ✅ Start backend server (port 5000)
4. ✅ Install npm dependencies
5. ✅ Start frontend dev server (port 5173)

Open browser: **http://localhost:5173**

---

## 🔧 Option 2: Manual Setup

### Step 1: Backend

```bash
# Navigate to backend
cd backend

# Create virtual environment
python3 -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
```

✅ Backend running on: **http://localhost:5000**

### Step 2: Frontend

Open new terminal:

```bash
# Install dependencies (in project root)
npm install

# Run dev server
npm run dev
```

✅ Frontend running on: **http://localhost:5173**

---

## 🧪 Test It!

1. Open **http://localhost:5173** in browser
2. Type "sehat" in search box
3. Click "Cari" button
4. See results! 🎉

Or click "Temukan Klinik Terdekat" to use GPS.

---

## 📱 Using the App

### Search by Keyword
1. Type clinic name or location
2. Click "Cari"
3. Browse results

### Find Nearby Clinics
1. Click "Temukan Klinik Terdekat"
2. Allow location access
3. See clinics sorted by distance

### Contact Clinic
- **📞 Telepon**: Click to call
- **💬 WhatsApp**: Click to chat
- **✉️ Email**: Click to email
- **🗺️ Maps**: Click to see location

---

## 🌐 Deploy to Production

### Deploy Backend

**Railway (Recommended - Free Tier):**
1. Visit: https://railway.app
2. Login with GitHub
3. New Project → Deploy from GitHub
4. Select repository
5. Set root directory: `backend`
6. Deploy! ✅

**Your API URL:** `https://your-app.railway.app`

### Deploy Frontend

**Netlify (Recommended - Free):**
1. Visit: https://app.netlify.com
2. Login with GitHub
3. New site from Git
4. Select repository
5. Netlify akan otomatis detect settings dari `netlify.toml`:
   - Build command: `npm run build`
   - Publish directory: `dist`
6. Environment variable:
   - Key: `VITE_API_URL`
   - Value: Your backend URL
7. Deploy! ✅

**Your app URL:** `https://your-app.netlify.app`

---

## 🔄 Update Backend URL

After deploying backend, update frontend:

**Option 1: Via UI**
1. Click "⚙️ Konfigurasi API Backend"
2. Enter your backend URL
3. Try searching

**Option 2: Via Code**
1. Edit `.env.production` in project root
2. Set `VITE_API_URL=https://your-backend.railway.app`
3. Rebuild: `npm run build`
4. Redeploy to Netlify

---

## 🐛 Troubleshooting

### Backend won't start

**Error: Port 5000 in use**
```bash
# Find process
lsof -i :5000

# Kill it
kill -9 <PID>
```

**Error: Module not found**
```bash
# Make sure venv is activated
source venv/bin/activate

# Reinstall
pip install -r requirements.txt
```

### Frontend won't start

**Error: ENOENT**
```bash
# Clear and reinstall
rm -rf node_modules package-lock.json
npm install
```

### CORS Error

**In browser console:**
```
Access blocked by CORS policy
```

**Fix:**
1. Make sure backend is running
2. Check backend CORS settings in `backend/app.py`
3. Restart backend

### Can't find clinics

**Check:**
1. ✅ Backend is running (http://localhost:5000/health)
2. ✅ Frontend can connect (check browser console)
3. ✅ Try different keywords: "sehat", "pratama", "medika"

### GPS not working

**Common causes:**
- Browser doesn't support geolocation
- Location permission denied
- Not using HTTPS (required for geolocation)

**Fix:**
- Allow location when prompted
- Use HTTPS (automatic on Netlify)
- Try different browser

---

## 📚 Next Steps

### Customize Data
Edit `backend/app.py` → `MOCK_CLINICS` array

### Integrate Google Places API
1. Get API key: https://console.cloud.google.com/
2. Replace `backend/app.py` with `backend/app_with_google_places.py`
3. Set environment variable: `GOOGLE_PLACES_API_KEY`

### Customize UI
Edit `src/index.css` for styling

### Add Features
See `FEATURES.md` for roadmap

---

## 📖 Full Documentation

- **README.md** - Main documentation
- **DEPLOYMENT.md** - Detailed deployment guide
- **TEST_GUIDE.md** - Testing guide
- **CONTRIBUTING.md** - How to contribute
- **FEATURES.md** - Feature list and roadmap

---

## 💬 Get Help

- Check existing documentation
- Search [GitHub issues](https://github.com/your-repo/issues)
- Open new issue with details
- Include error messages and logs

---

## ✅ Checklist

### Development
- [ ] Backend running on 5000
- [ ] Frontend running on 5173
- [ ] Can search by keyword
- [ ] Can search nearby
- [ ] All buttons work

### Production
- [ ] Backend deployed
- [ ] Frontend deployed
- [ ] Frontend connected to backend
- [ ] HTTPS enabled
- [ ] No console errors

---

## 🎉 You're Ready!

Start building and deploying awesome clinic finder apps!

**Questions?** Check the documentation or open an issue.

**Happy Coding! 🚀**
