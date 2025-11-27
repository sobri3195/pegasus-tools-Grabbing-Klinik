# 🚀 Panduan Deploy ke Netlify

Project ini sudah dikonfigurasi untuk deployment Netlify yang mudah.

## 📁 Struktur Project

Frontend React sudah ada di root directory untuk memudahkan deployment ke Netlify:

```
clinic-grabber/
├── src/                # React source files
├── public/             # Static assets
├── index.html          # HTML template
├── package.json        # Dependencies
├── vite.config.js      # Vite config
├── netlify.toml        # Netlify config (auto-detect)
├── dist/               # Build output (generated)
└── backend/            # Python API (deploy separately)
```

## ⚡ Quick Deploy

### Option 1: Git-based Deploy (Recommended)

1. **Push ke GitHub/GitLab**
   ```bash
   git add .
   git commit -m "Ready for Netlify"
   git push
   ```

2. **Connect ke Netlify**
   - Login ke [Netlify](https://app.netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Select your Git provider
   - Choose repository

3. **Auto Configuration**
   Netlify akan otomatis detect dari `netlify.toml`:
   - ✅ Build command: `npm run build`
   - ✅ Publish directory: `dist`
   - ✅ Redirects untuk SPA

4. **Set Environment Variable**
   - Site Settings → Environment Variables
   - Add: `VITE_API_URL` = `https://your-backend-url.com`

5. **Deploy!**
   - Click "Deploy site"
   - Setiap push ke main akan auto-deploy

### Option 2: Manual Upload

1. **Build locally**
   ```bash
   npm install
   npm run build
   ```

2. **Upload to Netlify**
   - Drag & drop folder `dist/` ke Netlify dashboard
   - Set environment variable `VITE_API_URL`

### Option 3: Netlify CLI

```bash
# Install CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
npm run build
netlify deploy --prod
```

## 🔧 Konfigurasi

### netlify.toml (Sudah dikonfigurasi)

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Environment Variables

Set di Netlify Dashboard:
- `VITE_API_URL`: URL backend API Anda

Atau edit `.env.production`:
```env
VITE_API_URL=https://your-backend-api.railway.app
```

## 📦 Deploy Backend Terpisah

Backend Python harus di-deploy ke platform yang support Python:

### Railway.app (Recommended)
1. Login ke [Railway.app](https://railway.app)
2. New Project → Deploy from GitHub
3. Select repository
4. Set root directory: `backend`
5. Deploy!

### Render.com
1. Login ke [Render.com](https://render.com)
2. New Web Service
3. Connect repository
4. Root directory: `backend`
5. Build: `pip install -r requirements.txt`
6. Start: `gunicorn app:app`

## ✅ Checklist Deployment

### Sebelum Deploy
- [ ] Backend sudah deployed dan accessible
- [ ] Backend URL sudah dicatat
- [ ] Project sudah di push ke Git

### Deploy Frontend
- [ ] Repository connected ke Netlify
- [ ] Build settings correct (auto dari netlify.toml)
- [ ] Environment variable `VITE_API_URL` set
- [ ] Deploy successful

### Testing
- [ ] Site accessible via Netlify URL
- [ ] Search by keyword works
- [ ] Search nearby works (allow location)
- [ ] All contact buttons work
- [ ] No console errors

## 🔄 Update & Redeploy

Frontend akan auto-deploy setiap kali push ke main branch:

```bash
# Make changes to src/
git add .
git commit -m "Update feature"
git push

# Netlify otomatis rebuild & deploy
```

## 🐛 Troubleshooting

### Build Failed
- Check package.json dependencies
- Verify node version (18+ required)
- Check build logs di Netlify dashboard

### API Connection Failed
- Verify `VITE_API_URL` environment variable
- Check backend is running
- Test backend URL di browser
- Check CORS settings di backend

### Blank Page
- Check browser console for errors
- Verify dist/ folder has files
- Check redirects configuration

## 📚 Resources

- [Netlify Docs](https://docs.netlify.com)
- [Vite Deployment Guide](https://vitejs.dev/guide/static-deploy.html)
- [Project Documentation](./README.md)

---

**Happy Deploying! 🚀**
