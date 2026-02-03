#!/bin/bash
# Setup script for Multi-Agent Travel Planner (macOS/Linux)
# This script automates the creation of virtual environment and installation of dependencies

echo "=================================================="
echo "🚀 Multi-Agent Travel Planner - Setup Script"
echo "=================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher from https://www.python.org/downloads/"
    exit 1
fi

# Display Python version
PYTHON_VERSION=$(python3 --version)
echo "✅ Found: $PYTHON_VERSION"
echo ""

# Step 1: Create virtual environment
echo "📦 Step 1/4: Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment 'venv' already exists"
    read -p "Do you want to recreate it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🗑️  Removing existing virtual environment..."
        rm -rf venv
        python3 -m venv venv
        echo "✅ Virtual environment recreated"
    else
        echo "ℹ️  Using existing virtual environment"
    fi
else
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi
echo ""

# Step 2: Activate virtual environment
echo "📦 Step 2/4: Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Step 3: Upgrade pip
echo "📦 Step 3/4: Upgrading pip..."
pip install --upgrade pip --quiet
echo "✅ Pip upgraded"
echo ""

# Step 4: Install requirements
echo "📦 Step 4/4: Installing dependencies from requirements.txt..."
echo "ℹ️  This may take 2-5 minutes..."
if pip install -r requirements.txt; then
    echo "✅ All dependencies installed successfully!"
else
    echo "❌ Error installing dependencies"
    echo "Please check your internet connection and try again"
    exit 1
fi
echo ""

# Step 5: Check for .env file
echo "🔑 Checking for .env file..."
if [ -f ".env" ]; then
    echo "✅ .env file exists"
else
    echo "⚠️  .env file not found"
    echo ""
    echo "Next steps:"
    echo "  1. Copy .env.example to .env:"
    echo "     cp .env.example .env"
    echo "  2. Edit .env and add your API keys"
    echo "  3. Get API keys from:"
    echo "     - OpenAI: https://platform.openai.com/api-keys"
    echo "     - Tavily: https://app.tavily.com/home"
    echo "     - SERP API: https://serpapi.com/dashboard"
fi
echo ""

# Step 6: Test setup
echo "🧪 Running setup validation..."
if python test_setup.py; then
    echo ""
    echo "=================================================="
    echo "🎉 Setup Complete!"
    echo "=================================================="
    echo ""
    echo "Your environment is ready to use!"
    echo ""
    echo "To start using the application:"
    echo "  1. Make sure virtual environment is active:"
    echo "     source venv/bin/activate"
    echo "  2. Run the application:"
    echo "     python main.py"
    echo ""
    echo "For more information, see README.md"
    echo "=================================================="
else
    echo ""
    echo "⚠️  Setup validation found some issues"
    echo "Please review the errors above and:"
    echo "  - Ensure .env file has all API keys"
    echo "  - Check that all dependencies installed correctly"
    echo ""
    echo "For help, see SETUP_GUIDE.md"
fi
