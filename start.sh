#!/bin/bash

echo "🏥 Clinic Grabber - Quick Start Script"
echo "======================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.11+"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 18+"
    exit 1
fi

echo "✅ Prerequisites check passed"
echo ""

# Start Backend
echo "🔧 Setting up Backend..."
cd backend

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

if [ ! -f "venv/lib/python*/site-packages/flask/__init__.py" ]; then
    echo "Installing Python dependencies..."
    pip install -r requirements.txt
fi

echo "Starting backend server..."
python app.py &
BACKEND_PID=$!
echo "Backend running on PID: $BACKEND_PID"

# Setup Frontend
echo ""
echo "🌐 Setting up Frontend..."
cd ..

if [ ! -d "node_modules" ]; then
    echo "Installing npm dependencies..."
    npm install
fi

echo ""
echo "================================"
echo "✅ Setup Complete!"
echo "================================"
echo ""
echo "Backend: http://localhost:5000"
echo "Frontend: Will start on http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop all servers"
echo ""

# Start Frontend (this will block)
npm run dev

# Cleanup when Ctrl+C is pressed
echo ""
echo "Stopping servers..."
kill $BACKEND_PID 2>/dev/null
echo "Goodbye! 👋"
