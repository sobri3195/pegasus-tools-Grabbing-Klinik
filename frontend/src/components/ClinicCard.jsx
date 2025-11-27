const ClinicCard = ({ clinic }) => {
  const formatPhoneNumber = (phone) => {
    return phone.replace(/^0/, '+62').replace(/[^0-9+]/g, '')
  }

  const formatWhatsAppNumber = (wa) => {
    if (wa.startsWith('62')) return wa
    if (wa.startsWith('0')) return '62' + wa.substring(1)
    return wa
  }

  return (
    <div className="clinic-card">
      <div className="clinic-header">
        <h3 className="clinic-name">{clinic.nama_klinik}</h3>
        <span className="clinic-category">{clinic.kategori}</span>
        <p className="clinic-address">📍 {clinic.alamat}</p>
        {clinic.jarak_km && (
          <div className="clinic-distance">
            🚗 {clinic.jarak_km} km dari lokasi Anda
          </div>
        )}
      </div>

      <div className="clinic-contacts">
        <div className="contact-item">
          <span className="contact-icon">📞</span>
          <span className="contact-label">Telepon:</span>
          <span className="contact-value">{clinic.telepon}</span>
        </div>

        <div className="contact-item">
          <span className="contact-icon">💬</span>
          <span className="contact-label">WhatsApp:</span>
          <span className="contact-value">{clinic.whatsapp}</span>
        </div>

        <div className="contact-item">
          <span className="contact-icon">✉️</span>
          <span className="contact-label">Email:</span>
          <span className="contact-value">{clinic.email}</span>
        </div>
      </div>

      <div className="clinic-actions">
        <a
          href={`tel:${formatPhoneNumber(clinic.telepon)}`}
          className="action-btn action-call"
        >
          📞 Telepon
        </a>

        <a
          href={`https://wa.me/${formatWhatsAppNumber(clinic.whatsapp)}`}
          target="_blank"
          rel="noopener noreferrer"
          className="action-btn action-whatsapp"
        >
          💬 WhatsApp
        </a>

        <a
          href={`mailto:${clinic.email}`}
          className="action-btn action-email"
        >
          ✉️ Email
        </a>

        <a
          href={clinic.maps_url}
          target="_blank"
          rel="noopener noreferrer"
          className="action-btn action-maps"
        >
          🗺️ Maps
        </a>
      </div>
    </div>
  )
}

export default ClinicCard
