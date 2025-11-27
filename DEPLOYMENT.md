# 📦 Panduan Deployment Lengkap

Guide lengkap untuk deploy backend dan frontend ke production.

## 🎯 Overview

- **Backend**: Deploy ke Heroku, Railway, atau Render
- **Frontend**: Deploy ke Netlify
- **Database**: Tidak ada (stateless API)

---

## 🔧 Backend Deployment

### Option 1: Deploy ke Heroku

#### Persiapan

1. Install Heroku CLI:
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. Login ke Heroku:
   ```bash
   heroku login
   ```

#### Deploy

```bash
# Navigate ke root project
cd clinic-grabber

# Create Heroku app
heroku create clinic-grabber-api

# Deploy backend
git subtree push --prefix backend heroku main

# Atau jika sudah ada Heroku remote:
git push heroku `git subtree split --prefix backend main`:main --force

# Check logs
heroku logs --tail

# Open app
heroku open
```

#### Set Environment Variables (Opsional)

```bash
heroku config:set GOOGLE_PLACES_API_KEY=your_api_key
```

#### URL Backend

Backend akan tersedia di: `https://clinic-grabber-api.herokuapp.com`

---

### Option 2: Deploy ke Railway.app

#### Steps

1. **Sign up di Railway.app**
   - Visit: https://railway.app
   - Login dengan GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Pilih repository Anda

3. **Configure Service**
   - Set root directory: `backend`
   - Railway akan auto-detect Python
   - Environment variables (jika perlu):
     - `PORT`: 5000
     - `GOOGLE_PLACES_API_KEY`: your_key

4. **Deploy**
   - Railway akan auto-deploy
   - URL: `https://your-app.railway.app`

**Kelebihan Railway:**
- ✅ Auto-deploy on git push
- ✅ Free tier generous
- ✅ Easy setup
- ✅ Custom domains

---

### Option 3: Deploy ke Render.com

#### Steps

1. **Sign up di Render.com**
   - Visit: https://render.com
   - Login dengan GitHub

2. **Create New Web Service**
   - Click "New +"
   - Select "Web Service"
   - Connect repository

3. **Configure**
   - Name: `clinic-grabber-api`
   - Root Directory: `backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

4. **Environment Variables**
   - Add `PYTHON_VERSION`: `3.11.0`
   - Add `GOOGLE_PLACES_API_KEY`: your_key (optional)

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment
   - URL: `https://clinic-grabber-api.onrender.com`

---

## 🌐 Frontend Deployment (Netlify)

### Option 1: Deploy via Netlify Dashboard (Termudah)

#### Steps

1. **Build Frontend Locally**
   ```bash
   npm install
   npm run build
   ```

2. **Upload ke Netlify**
   - Visit: https://app.netlify.com
   - Drag & drop folder `dist/` ke dashboard
   - Done! ✅

#### Set Environment Variable

1. Site Settings → Environment Variables
2. Add variable:
   - Key: `VITE_API_URL`
   - Value: `https://your-backend-api.herokuapp.com`
3. Redeploy site

---

### Option 2: Deploy via Netlify CLI

#### Install CLI

```bash
npm install -g netlify-cli
```

#### Deploy

```bash
# Login
netlify login

# Initialize site
netlify init

# Build
npm run build

# Deploy
netlify deploy --prod
```

#### Set Environment Variable

```bash
netlify env:set VITE_API_URL https://your-backend-api.herokuapp.com
```

---

### Option 3: Auto-Deploy via Git (Recommended)

#### Steps

1. **Push ke GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connect di Netlify**
   - Visit: https://app.netlify.com
   - Click "Add new site"
   - Click "Import an existing project"
   - Select GitHub repository

3. **Configure Build Settings**
   - Build command: `npm run build`
   - Publish directory: `dist`
   - (Netlify akan otomatis detect dari netlify.toml)

4. **Set Environment Variables**
   - Click "Add environment variables"
   - Add `VITE_API_URL` with your backend URL

5. **Deploy**
   - Click "Deploy site"
   - Wait for build to complete
   - Site akan live di: `https://random-name.netlify.app`

#### Auto-Deploy Setup

Setelah setup, setiap push ke branch main akan auto-deploy! 🚀

#### Custom Domain

1. Site settings → Domain settings
2. Click "Add custom domain"
3. Follow DNS configuration

---

## 🔗 Menghubungkan Backend & Frontend

### Update Frontend Environment

**Netlify Dashboard:**
```
VITE_API_URL=https://clinic-grabber-api.herokuapp.com
```

**Atau edit `.env.production`:**
```env
VITE_API_URL=https://clinic-grabber-api.herokuapp.com
```

### Update Backend CORS

Edit `backend/app.py`:

```python
from flask_cors import CORS

# Production - specific origins
CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:5173",  # Development
            "https://your-app.netlify.app"  # Production
        ]
    }
})
```

Commit dan push perubahan.

---

## ✅ Verification Checklist

### Backend
- [ ] Backend deployed dan accessible
- [ ] API endpoints berfungsi (`/search/clinic`, `/search/nearby`)
- [ ] CORS configured untuk Netlify domain
- [ ] Environment variables set (jika ada)
- [ ] Health check endpoint works: `/health`

### Frontend
- [ ] Frontend deployed ke Netlify
- [ ] `VITE_API_URL` set ke backend URL
- [ ] Search by keyword berfungsi
- [ ] Search nearby berfungsi
- [ ] GPS permission works (HTTPS)
- [ ] All action buttons work (call, WhatsApp, email, maps)

### Testing URLs

**Test Backend:**
```bash
# Health check
curl https://your-backend.herokuapp.com/health

# Search clinic
curl "https://your-backend.herokuapp.com/search/clinic?keyword=sehat"

# Search nearby
curl "https://your-backend.herokuapp.com/search/nearby?lat=-6.2088&lng=106.8456&radius=10"
```

**Test Frontend:**
- Visit: `https://your-app.netlify.app`
- Try searching
- Check browser console for errors

---

## 🚨 Troubleshooting

### CORS Error

**Symptom:** Frontend tidak bisa akses backend

**Fix:**
```python
# backend/app.py
CORS(app, origins="*")  # Development only

# Production
CORS(app, origins=["https://your-app.netlify.app"])
```

### Netlify Build Failed

**Common Issues:**

1. **Node version:**
   ```toml
   # netlify.toml
   [build.environment]
     NODE_VERSION = "18"
   ```

2. **Build command:**
   ```bash
   # Check package.json
   "scripts": {
     "build": "vite build"
   }
   ```

3. **Environment variable tidak set:**
   - Check Netlify dashboard → Environment variables

### Backend Not Starting

**Heroku:**
```bash
heroku logs --tail
heroku ps:scale web=1
```

**Railway:**
- Check logs di dashboard
- Verify `Procfile` exists

**Render:**
- Check logs di dashboard
- Verify start command: `gunicorn app:app`

### API Connection Failed

1. **Check backend URL:**
   ```bash
   curl https://your-backend.herokuapp.com/health
   ```

2. **Check CORS:**
   - Open browser console
   - Look for CORS errors

3. **Check environment variable:**
   ```bash
   # Netlify
   netlify env:list
   ```

---

## 🎉 Success!

Jika semua checklist ✅, aplikasi Anda sudah production-ready!

**Share your app:**
- Frontend: `https://your-app.netlify.app`
- Backend API: `https://your-backend.herokuapp.com`

---

## 📊 Monitoring

### Heroku

```bash
# Check dyno status
heroku ps

# View logs
heroku logs --tail

# Check metrics
heroku open
# Navigate to Metrics tab
```

### Netlify

- Dashboard → Site overview
- View deploys history
- Check analytics
- Monitor bandwidth

### Railway

- Dashboard shows CPU, Memory, Bandwidth
- View logs
- Check deployment history

---

## 🔄 Updates & Maintenance

### Update Backend

```bash
# Make changes
git add backend/
git commit -m "Update backend"

# Deploy
git push heroku `git subtree split --prefix backend main`:main --force
# or just git push (Railway/Render auto-deploy)
```

### Update Frontend

```bash
# Make changes to src/ files
git add .
git commit -m "Update frontend"
git push

# Netlify akan auto-deploy
```

---

## 💰 Cost Estimation

### Free Tier Limits

**Heroku Free:**
- ❌ No longer free (Need paid plan)
- ✅ Use Railway or Render instead

**Railway Free:**
- ✅ $5 free credit/month
- ✅ Enough for small apps

**Render Free:**
- ✅ Free tier available
- ⚠️ Sleeps after inactivity
- ⚠️ 750 hours/month

**Netlify Free:**
- ✅ 100GB bandwidth/month
- ✅ Unlimited sites
- ✅ 300 build minutes/month
- ✅ More than enough!

### Recommended Setup

**Free:**
- Backend: Railway (free tier)
- Frontend: Netlify (free tier)
- Total: $0/month 🎉

**Production:**
- Backend: Railway ($5-10/month)
- Frontend: Netlify (free or $19/month Pro)
- Total: $5-29/month

---

## 📚 Resources

- [Heroku Python Guide](https://devcenter.heroku.com/articles/getting-started-with-python)
- [Railway Docs](https://docs.railway.app)
- [Render Docs](https://render.com/docs)
- [Netlify Docs](https://docs.netlify.com)
- [Vite Deployment Guide](https://vitejs.dev/guide/static-deploy.html)

---

**Happy Deploying! 🚀**
