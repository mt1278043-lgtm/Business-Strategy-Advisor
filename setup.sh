#!/bin/bash

# Business Strategy Advisor Agent - Setup Script

set -e

echo "🚀 Setting up Business Strategy Advisor Agent..."
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python $PYTHON_VERSION found"
echo ""

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Setup .env file
if [ ! -f ".env" ]; then
    echo "⚙️  Setting up .env file..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your OpenAI API key:"
    echo "   OPENAI_API_KEY=sk-your-api-key-here"
    echo ""
else
    echo "✅ .env file already exists"
fi

echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Edit .env and add your OpenAI API key if you haven't already"
echo "2. Run the application:"
echo "   source venv/bin/activate"
echo "   streamlit run app.py"
echo ""
