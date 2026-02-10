@echo off
REM Setup script for Multi-Agent Travel Planner (Windows)
REM This script automates the creation of virtual environment and installation of dependencies

echo ==================================================
echo 🚀 Multi-Agent Travel Planner - Setup Script
echo ==================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed
    echo Please install Python 3.8 or higher from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Display Python version
echo ✅ Found Python:
python --version
echo.

REM Step 1: Create virtual environment
echo 📦 Step 1/4: Creating virtual environment...
if exist venv (
    echo ⚠️  Virtual environment 'venv' already exists
    set /p RECREATE="Do you want to recreate it? (y/N): "
    if /i "%RECREATE%"=="y" (
        echo 🗑️  Removing existing virtual environment...
        rmdir /s /q venv
        python -m venv venv
        echo ✅ Virtual environment recreated
    ) else (
        echo ℹ️  Using existing virtual environment
    )
) else (
    python -m venv venv
    echo ✅ Virtual environment created
)
echo.

REM Step 2: Activate virtual environment
echo 📦 Step 2/4: Activating virtual environment...
call venv\Scripts\activate.bat
echo ✅ Virtual environment activated
echo.

REM Step 3: Upgrade pip
echo 📦 Step 3/4: Upgrading pip...
python -m pip install --upgrade pip --quiet
echo ✅ Pip upgraded
echo.

REM Step 4: Install requirements
echo 📦 Step 4/4: Installing dependencies from requirements.txt...
echo ℹ️  This may take 2-5 minutes...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Error installing dependencies
    echo Please check your internet connection and try again
    pause
    exit /b 1
)
echo ✅ All dependencies installed successfully!
echo.

REM Step 5: Check for .env file
echo 🔑 Checking for .env file...
if exist .env (
    echo ✅ .env file exists
) else (
    echo ⚠️  .env file not found
    echo.
    echo Next steps:
    echo   1. Copy .env.example to .env:
    echo      copy .env.example .env
    echo   2. Edit .env and add your API keys
    echo   3. Get API keys from:
    echo      - OpenAI: https://platform.openai.com/api-keys
    echo      - Tavily: https://app.tavily.com/home
    echo      - SERP API: https://serpapi.com/dashboard
)
echo.

REM Step 6: Test setup
echo 🧪 Running setup validation...
python test_setup.py
if errorlevel 1 (
    echo.
    echo ⚠️  Setup validation found some issues
    echo Please review the errors above and:
    echo   - Ensure .env file has all API keys
    echo   - Check that all dependencies installed correctly
    echo.
    echo For help, see SETUP_GUIDE.md
) else (
    echo.
    echo ==================================================
    echo 🎉 Setup Complete!
    echo ==================================================
    echo.
    echo Your environment is ready to use!
    echo.
    echo To start using the application:
    echo   1. Make sure virtual environment is active:
    echo      venv\Scripts\activate
    echo   2. Run the application:
    echo      python main.py
    echo.
    echo For more information, see README.md
    echo ==================================================
)

pause
