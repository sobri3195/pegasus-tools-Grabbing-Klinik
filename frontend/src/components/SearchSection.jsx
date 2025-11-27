import { useState } from 'react'

const SearchSection = ({ apiUrl, setApiUrl, onSearchKeyword, onSearchNearby, loading }) => {
  const [keyword, setKeyword] = useState('')
  const [showApiConfig, setShowApiConfig] = useState(false)

  const handleSearch = (e) => {
    e.preventDefault()
    onSearchKeyword(keyword)
  }

  return (
    <div className="search-section">
      <div className="api-config">
        <div 
          className="api-config-title"
          onClick={() => setShowApiConfig(!showApiConfig)}
          style={{ cursor: 'pointer' }}
        >
          ⚙️ Konfigurasi API Backend
          <span style={{ marginLeft: 'auto', fontSize: '0.9rem' }}>
            {showApiConfig ? '▼' : '▶'}
          </span>
        </div>
        {showApiConfig && (
          <div>
            <input
              type="text"
              value={apiUrl}
              onChange={(e) => setApiUrl(e.target.value)}
              placeholder="URL Backend API"
            />
            <div className="api-config-hint">
              Default: http://localhost:5000 (untuk development)
            </div>
          </div>
        )}
      </div>

      <form onSubmit={handleSearch}>
        <div className="search-box">
          <input
            type="text"
            className="search-input"
            placeholder="Cari klinik berdasarkan nama atau lokasi..."
            value={keyword}
            onChange={(e) => setKeyword(e.target.value)}
            disabled={loading}
          />
          <button
            type="submit"
            className="btn btn-primary"
            disabled={loading || !keyword.trim()}
          >
            🔍 Cari
          </button>
        </div>
      </form>

      <div className="divider">ATAU</div>

      <button
        className="btn btn-secondary"
        onClick={onSearchNearby}
        disabled={loading}
        style={{ width: '100%' }}
      >
        📍 Temukan Klinik Terdekat
      </button>
    </div>
  )
}

export default SearchSection
