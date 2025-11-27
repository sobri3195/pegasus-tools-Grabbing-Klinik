import { useState } from 'react'
import axios from 'axios'
import ClinicCard from './components/ClinicCard'
import SearchSection from './components/SearchSection'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

function App() {
  const [clinics, setClinics] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [searchPerformed, setSearchPerformed] = useState(false)
  const [apiUrl, setApiUrl] = useState(API_URL)

  const searchByKeyword = async (keyword) => {
    if (!keyword.trim()) {
      setError('Masukkan kata kunci pencarian')
      return
    }

    setLoading(true)
    setError(null)
    setSearchPerformed(true)

    try {
      const response = await axios.get(`${apiUrl}/search/clinic`, {
        params: { keyword }
      })

      if (response.data.status === 'success') {
        setClinics(response.data.data)
      } else {
        setError(response.data.message || 'Terjadi kesalahan')
      }
    } catch (err) {
      setError(
        err.response?.data?.message || 
        'Gagal menghubungi server. Pastikan backend sudah berjalan.'
      )
      console.error('Search error:', err)
    } finally {
      setLoading(false)
    }
  }

  const searchNearby = async () => {
    if (!navigator.geolocation) {
      setError('Browser Anda tidak mendukung geolocation')
      return
    }

    setLoading(true)
    setError(null)
    setSearchPerformed(true)

    navigator.geolocation.getCurrentPosition(
      async (position) => {
        const { latitude, longitude } = position.coords

        try {
          const response = await axios.get(`${apiUrl}/search/nearby`, {
            params: {
              lat: latitude,
              lng: longitude,
              radius: 10
            }
          })

          if (response.data.status === 'success') {
            setClinics(response.data.data)
          } else {
            setError(response.data.message || 'Terjadi kesalahan')
          }
        } catch (err) {
          setError(
            err.response?.data?.message || 
            'Gagal menghubungi server. Pastikan backend sudah berjalan.'
          )
          console.error('Nearby search error:', err)
        } finally {
          setLoading(false)
        }
      },
      (err) => {
        setLoading(false)
        setError('Gagal mendapatkan lokasi. Pastikan Anda mengizinkan akses lokasi.')
        console.error('Geolocation error:', err)
      }
    )
  }

  return (
    <div className="app">
      <header className="header">
        <h1>🏥 Pencari Klinik Terdekat</h1>
        <p>Temukan klinik terdekat dengan informasi kontak lengkap</p>
      </header>

      <SearchSection
        apiUrl={apiUrl}
        setApiUrl={setApiUrl}
        onSearchKeyword={searchByKeyword}
        onSearchNearby={searchNearby}
        loading={loading}
      />

      {error && (
        <div className="error">
          <strong>❌ Error:</strong> {error}
        </div>
      )}

      {loading && (
        <div className="loading">
          <div className="loading-spinner"></div>
          <p>Mencari klinik...</p>
        </div>
      )}

      {!loading && searchPerformed && clinics.length > 0 && (
        <div>
          <div className="results-header">
            <h2>📍 Hasil Pencarian</h2>
            <p>{clinics.length} klinik ditemukan</p>
          </div>
          <div className="clinic-grid">
            {clinics.map((clinic) => (
              <ClinicCard key={clinic.id} clinic={clinic} />
            ))}
          </div>
        </div>
      )}

      {!loading && searchPerformed && clinics.length === 0 && !error && (
        <div className="empty-state">
          <div className="empty-state-icon">🔍</div>
          <h3>Tidak ada klinik ditemukan</h3>
          <p>Coba ubah kata kunci pencarian atau perluas area pencarian</p>
        </div>
      )}

      {!loading && !searchPerformed && (
        <div className="empty-state">
          <div className="empty-state-icon">👋</div>
          <h3>Selamat Datang!</h3>
          <p>Gunakan pencarian di atas untuk menemukan klinik terdekat</p>
        </div>
      )}
    </div>
  )
}

export default App
