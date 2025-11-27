# 🚀 Deploy ke Netlify - Quick Guide

## ⚡ Super Cepat (5 Menit)

### Method 1: Drag & Drop (Paling Mudah!)

1. **Build:**
   ```bash
   npm install
   npm run build
   ```

2. **Deploy:**
   - Buka: https://app.netlify.com/drop
   - Drag folder `dist/` ke browser
   - Done! 🎉

3. **Set Environment Variable:**
   - Site Settings → Environment Variables
   - Tambah: `VITE_API_URL` = URL backend Anda

---

### Method 2: Git Auto-Deploy (Recommended untuk Production)

1. **Push ke GitHub:**
   ```bash
   git add .
   git commit -m "Deploy to Netlify"
   git push origin main
   ```

2. **Connect Netlify:**
   - Login ke https://app.netlify.com
   - Click "Add new site" → "Import an existing project"
   - Pilih GitHub → Pilih repository
   - Netlify otomatis detect dari `netlify.toml`
   - Click "Deploy site"

3. **Set Environment Variable:**
   - Site Settings → Environment Variables
   - Tambah: `VITE_API_URL` = URL backend Anda

4. **Auto-Deploy:**
   - Setiap push ke main → Otomatis deploy! 🚀

---

### Method 3: Netlify CLI

```bash
# Install CLI (sekali saja)
npm install -g netlify-cli

# Login
netlify login

# Deploy
npm run build
netlify deploy --prod
```

---

## 🔧 Konfigurasi Otomatis

File `netlify.toml` di root sudah dikonfigurasi:

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

✅ Netlify akan otomatis:
- Detect build command
- Detect publish directory
- Setup SPA redirects

---

## ⚙️ Environment Variables

### Option 1: Netlify Dashboard
1. Site Settings → Environment Variables
2. Add variable:
   - Key: `VITE_API_URL`
   - Value: `https://your-backend-url.com`
3. Redeploy

### Option 2: .env.production
Edit file `.env.production`:
```env
VITE_API_URL=https://your-backend-url.com
```

Commit & push:
```bash
git add .env.production
git commit -m "Update API URL"
git push
```

---

## 🎯 Checklist Deploy

### Pre-Deploy
- [ ] Backend sudah deployed (Railway/Render)
- [ ] Backend URL sudah dicatat
- [ ] Frontend build sukses: `npm run build`

### Deploy
- [ ] Repository connected ke Netlify
- [ ] Build settings correct (otomatis dari netlify.toml)
- [ ] Environment variable `VITE_API_URL` sudah set
- [ ] Deploy sukses

### Post-Deploy Testing
- [ ] Site accessible via Netlify URL
- [ ] Search by keyword berfungsi
- [ ] Search nearby berfungsi (allow location)
- [ ] Tombol call/WA/email/maps berfungsi
- [ ] No errors di console browser
- [ ] Mobile responsive

---

## 🐛 Troubleshooting

### Build Failed
```bash
# Clear dan rebuild
rm -rf node_modules dist
npm install
npm run build
```

### API Connection Failed
1. Check `VITE_API_URL` environment variable
2. Verify backend is running
3. Test backend URL di browser
4. Check CORS settings di backend

### Blank Page
1. Check browser console for errors
2. Verify `dist/` folder has files
3. Check netlify.toml redirects configuration

### GPS Not Working
- Netlify otomatis HTTPS (required untuk GPS)
- Allow location permission di browser
- Test di different browser

---

## 📱 Custom Domain

1. **Add Domain:**
   - Site settings → Domain management
   - Add custom domain
   - Follow DNS instructions

2. **HTTPS:**
   - Netlify otomatis provision SSL certificate
   - Auto-renew setiap 3 bulan

---

## 🔄 Update & Redeploy

```bash
# Make changes to src/
git add .
git commit -m "Update feature"
git push

# Netlify otomatis rebuild & deploy! 🚀
```

---

## 📊 Monitor Deploy

### Netlify Dashboard
- View deploy logs
- Check build time
- Monitor bandwidth usage
- View analytics

### Deploy Notifications
- Email notifications (default)
- Slack integration (optional)
- Discord webhook (optional)

---

## 💡 Tips

1. **Preview Deploys:**
   - Setiap PR buat preview deploy
   - Test sebelum merge ke main

2. **Branch Deploys:**
   - Deploy multiple branches
   - Test features in isolation

3. **Rollback:**
   - Instant rollback ke deploy sebelumnya
   - No downtime

4. **Forms:**
   - Netlify Forms built-in (gratis)
   - Add contact forms easy

5. **Functions:**
   - Serverless functions available
   - Deploy API endpoints dengan Netlify

---

## 📚 Resources

- [Netlify Docs](https://docs.netlify.com)
- [Vite Deployment](https://vitejs.dev/guide/static-deploy.html)
- [Full Documentation](./README.md)
- [Netlify Deploy Guide](./NETLIFY_DEPLOY.md)

---

## ✅ Success Indicators

Your deploy is successful when:
- ✅ Green deploy status in Netlify
- ✅ Site loads without errors
- ✅ All features working (search, GPS, buttons)
- ✅ No console errors
- ✅ Mobile responsive

---

## 🎉 Deploy Backend Juga?

### Railway.app (Recommended)
1. https://railway.app
2. New Project → Deploy from GitHub
3. Root directory: `backend`
4. Auto-deploy! ✅

### Render.com
1. https://render.com
2. New Web Service
3. Root directory: `backend`
4. Start command: `gunicorn app:app`

**Copy URL backend → Set di Netlify environment variables!**

---

**Happy Deploying! 🚀**

**Butuh bantuan?** Lihat [NETLIFY_DEPLOY.md](./NETLIFY_DEPLOY.md) untuk guide lengkap.
