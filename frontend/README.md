# Frontend - Clinic Grabber React App

Aplikasi React untuk mencari klinik terdekat dengan informasi kontak lengkap.

## 🚀 Fitur

- ✅ Pencarian klinik berdasarkan kata kunci
- ✅ Pencarian klinik terdekat menggunakan GPS
- ✅ Tampilan informasi kontak lengkap (telepon, WhatsApp, email)
- ✅ Tombol aksi langsung (call, WhatsApp, email, maps)
- ✅ Responsive design
- ✅ Loading dan error states
- ✅ Dapat di-deploy ke Netlify

## 📦 Instalasi

```bash
npm install
```

## 🛠️ Development

```bash
npm run dev
```

Aplikasi akan berjalan di `http://localhost:5173`

## 🏗️ Build

```bash
npm run build
```

File hasil build akan ada di folder `dist/`

## 🌐 Deploy ke Netlify

### Cara 1: Deploy Manual

1. Build aplikasi:
   ```bash
   npm run build
   ```

2. Upload folder `dist/` ke Netlify melalui dashboard

### Cara 2: Deploy via Netlify CLI

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login ke Netlify
netlify login

# Deploy
netlify deploy --prod
```

### Cara 3: Deploy via Git (Otomatis)

1. Push repository ke GitHub/GitLab
2. Connect repository di Netlify Dashboard
3. Set build settings:
   - Build command: `npm run build`
   - Publish directory: `dist`
4. Set environment variables:
   - `VITE_API_URL`: URL backend API Anda

## ⚙️ Konfigurasi

### Environment Variables

Buat file `.env` di root folder frontend:

```env
VITE_API_URL=http://localhost:5000
```

Untuk production, update di Netlify Dashboard atau `.env.production`:

```env
VITE_API_URL=https://your-backend-api.herokuapp.com
```

### Netlify Configuration

File `netlify.toml` sudah tersedia dengan konfigurasi:
- Build command dan publish directory
- SPA redirect rules
- Dev server settings

## 🔗 Menghubungkan dengan Backend

1. Pastikan backend Python sudah berjalan
2. Update `VITE_API_URL` di file `.env` atau melalui UI settings
3. Backend harus mengaktifkan CORS untuk domain Netlify Anda

## 📱 Cara Penggunaan

### Pencarian dengan Kata Kunci

1. Masukkan nama klinik atau lokasi di search bar
2. Klik tombol "Cari"
3. Hasil akan ditampilkan dalam bentuk cards

### Pencarian Klinik Terdekat

1. Klik tombol "Temukan Klinik Terdekat"
2. Izinkan browser mengakses lokasi Anda
3. Klinik terdekat akan ditampilkan dengan jarak

### Menghubungi Klinik

Setiap card klinik memiliki tombol:
- **📞 Telepon**: Langsung membuka aplikasi telepon
- **💬 WhatsApp**: Membuka chat WhatsApp
- **✉️ Email**: Membuka email client
- **🗺️ Maps**: Membuka Google Maps

## 🎨 Customization

### Styling

Edit file `src/index.css` untuk mengubah tampilan:
- Colors: Ubah variabel warna di bagian atas
- Layout: Sesuaikan grid dan spacing
- Animations: Tambahkan atau ubah animasi

### Components

Struktur komponen:
```
src/
├── App.jsx              # Main component
├── components/
│   ├── ClinicCard.jsx   # Card untuk menampilkan klinik
│   └── SearchSection.jsx # Section pencarian
├── index.css            # Global styles
└── main.jsx            # Entry point
```

## 🐛 Troubleshooting

### CORS Error

Jika terjadi CORS error:
1. Pastikan backend sudah mengaktifkan CORS
2. Tambahkan domain Netlify Anda ke CORS allowed origins

### Geolocation Not Working

1. Pastikan menggunakan HTTPS (Netlify otomatis menggunakan HTTPS)
2. Pastikan browser mengizinkan akses lokasi
3. Cek browser console untuk error messages

### Build Error

Jika build gagal:
```bash
# Clear cache
rm -rf node_modules dist
npm install
npm run build
```

## 📄 License

MIT
