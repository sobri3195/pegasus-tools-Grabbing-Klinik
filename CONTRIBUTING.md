# 🤝 Contributing to Clinic Grabber

Terima kasih sudah tertarik untuk berkontribusi! Berikut panduan untuk membantu Anda memulai.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Adding Features](#adding-features)
- [Reporting Bugs](#reporting-bugs)

---

## Code of Conduct

Kami mengharapkan semua kontributor untuk:
- Bersikap sopan dan profesional
- Menghormati pendapat berbeda
- Memberikan feedback yang konstruktif
- Fokus pada apa yang terbaik untuk komunitas

---

## Getting Started

### 1. Fork Repository

```bash
# Clone your fork
git clone https://github.com/your-username/clinic-grabber.git
cd clinic-grabber
```

### 2. Setup Development Environment

**Backend:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Frontend:**
```bash
cd frontend
npm install
```

### 3. Create Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

---

## Development Workflow

### Running Development Servers

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Making Changes

1. Make your changes
2. Test locally
3. Commit with descriptive message
4. Push to your fork
5. Create Pull Request

---

## Coding Standards

### Python (Backend)

**Style Guide:** PEP 8

```python
# Good
def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two points using Haversine formula"""
    R = 6371  # Earth radius in km
    # ... implementation

# Bad
def calcDist(l1,lo1,l2,lo2):
    r=6371
    # ... implementation
```

**Key Points:**
- Use snake_case for functions and variables
- 4 spaces for indentation
- Docstrings for all functions
- Type hints where applicable
- Maximum line length: 100 characters

### JavaScript/React (Frontend)

**Style Guide:** Airbnb JavaScript Style Guide (modified)

```javascript
// Good
const ClinicCard = ({ clinic }) => {
  const formatPhone = (phone) => {
    return phone.replace(/^0/, '+62')
  }
  
  return (
    <div className="clinic-card">
      {/* ... */}
    </div>
  )
}

// Bad
const clinicCard = props => {
  return <div className="clinic-card">{/* ... */}</div>
}
```

**Key Points:**
- Use camelCase for variables and functions
- Use PascalCase for components
- 2 spaces for indentation
- Functional components with hooks
- PropTypes or TypeScript (if migrating)
- Destructure props

### CSS

```css
/* Good - BEM-like naming */
.clinic-card {
  padding: 20px;
}

.clinic-card__header {
  font-size: 1.5rem;
}

.clinic-card--featured {
  border: 2px solid gold;
}

/* Bad */
.c1 {
  padding: 20px;
}
```

---

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples

```bash
# Feature
git commit -m "feat(frontend): add filter by clinic category"

# Bug fix
git commit -m "fix(backend): correct distance calculation for nearby search"

# Documentation
git commit -m "docs(readme): update deployment instructions"

# Multiple changes
git commit -m "feat(backend): add pagination to search results

- Add limit and offset parameters
- Update API documentation
- Add tests for pagination

Closes #123"
```

---

## Pull Request Process

### Before Submitting

1. **Test your changes**
   ```bash
   # Backend
   python -m pytest
   
   # Frontend
   npm run build
   ```

2. **Update documentation** if needed
   - README.md
   - API documentation
   - Code comments

3. **Check code style**
   ```bash
   # Python
   flake8 backend/
   
   # JavaScript
   npm run lint
   ```

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tested locally
- [ ] Added tests
- [ ] All tests pass

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

### Review Process

1. Maintainer akan review dalam 2-3 hari
2. Address feedback jika ada
3. Setelah approved, PR akan di-merge
4. Delete your branch setelah merge

---

## Adding Features

### Adding New Backend Endpoint

1. **Define route in `app.py`:**
```python
@app.route('/api/new-endpoint', methods=['GET'])
def new_endpoint():
    # Implementation
    return jsonify({
        "status": "success",
        "data": result
    })
```

2. **Add tests:**
```python
def test_new_endpoint():
    response = client.get('/api/new-endpoint')
    assert response.status_code == 200
```

3. **Update API documentation in README**

### Adding New Frontend Component

1. **Create component file:**
```javascript
// src/components/NewComponent.jsx
const NewComponent = ({ prop1, prop2 }) => {
  return (
    <div className="new-component">
      {/* Implementation */}
    </div>
  )
}

export default NewComponent
```

2. **Add styles in `index.css`:**
```css
.new-component {
  /* Styles */
}
```

3. **Import and use:**
```javascript
import NewComponent from './components/NewComponent'
```

### Adding Mock Data

Edit `backend/app.py`:
```python
MOCK_CLINICS = [
    {
        "id": 11,
        "nama_klinik": "New Clinic",
        "alamat": "Address",
        "telepon": "021-12345678",
        "whatsapp": "6281234567890",
        "email": "info@clinic.com",
        "lat": -6.2088,
        "lng": 106.8456,
        "kategori": "Klinik Umum"
    }
]
```

---

## Reporting Bugs

### Before Reporting

1. Search existing issues
2. Try latest version
3. Check if it's already fixed

### Bug Report Template

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., Windows 10, macOS, Ubuntu]
- Browser: [e.g., Chrome 120, Firefox 121]
- Version: [e.g., v1.0.0]

## Screenshots
Add screenshots if applicable

## Additional Context
Any other relevant information
```

---

## Feature Requests

### Feature Request Template

```markdown
## Feature Description
Clear description of the feature

## Problem It Solves
Why is this needed?

## Proposed Solution
How should it work?

## Alternatives Considered
Other approaches you've thought about

## Additional Context
Mockups, examples, etc.
```

---

## Development Tips

### Backend Tips

**Use virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Install in development mode:**
```bash
pip install -e .
```

**Debug mode:**
```python
app.run(debug=True)  # Auto-reload on changes
```

### Frontend Tips

**Hot reload:**
```bash
npm run dev  # Auto-reload on file changes
```

**Debug in browser:**
- Open DevTools (F12)
- Check Console for errors
- Use React DevTools extension

**Build and test:**
```bash
npm run build
npm run preview
```

---

## Project Structure

```
clinic-grabber/
├── backend/
│   ├── app.py                    # Main Flask app
│   ├── app_with_google_places.py # Google Places example
│   ├── requirements.txt          # Python dependencies
│   └── README.md                 # Backend docs
│
├── frontend/
│   ├── src/
│   │   ├── components/           # React components
│   │   │   ├── ClinicCard.jsx
│   │   │   └── SearchSection.jsx
│   │   ├── App.jsx              # Main app component
│   │   ├── main.jsx             # Entry point
│   │   └── index.css            # Global styles
│   ├── public/                  # Static assets
│   ├── package.json             # Node dependencies
│   ├── netlify.toml             # Netlify config
│   └── README.md                # Frontend docs
│
├── README.md                    # Main documentation
├── DEPLOYMENT.md                # Deployment guide
├── TEST_GUIDE.md                # Testing guide
├── CONTRIBUTING.md              # This file
└── LICENSE                      # MIT License
```

---

## Code Review Checklist

### For Contributors

- [ ] Code works as expected
- [ ] No console errors
- [ ] Follows style guidelines
- [ ] Added tests (if applicable)
- [ ] Documentation updated
- [ ] No hardcoded credentials
- [ ] Error handling implemented
- [ ] Responsive (for UI changes)

### For Reviewers

- [ ] Code quality acceptable
- [ ] No security issues
- [ ] Performance acceptable
- [ ] Backward compatible
- [ ] Documentation clear
- [ ] Tests pass
- [ ] Follows project architecture

---

## Questions?

- Open an issue with label "question"
- Check existing documentation
- Review closed issues

---

## Recognition

Contributors akan dicantumkan di:
- README.md (Contributors section)
- Release notes
- Project website (jika ada)

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Happy Contributing! 🎉**

Terima kasih telah membantu membuat Clinic Grabber lebih baik!
