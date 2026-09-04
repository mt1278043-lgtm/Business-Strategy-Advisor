@echo off
REM Business Strategy Advisor Agent - Setup Script for Windows

echo Launching Business Strategy Advisor Agent Setup...
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher from https://www.python.org
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo Python version: %PYTHON_VERSION%
echo.

REM Create virtual environment
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo Dependencies installed successfully.
echo.

REM Setup .env file
if not exist ".env" (
    echo Setting up .env file...
    copy .env.example .env
    echo.
    echo WARNING: Please edit .env and add your OpenAI API key:
    echo OPENAI_API_KEY=sk-your-api-key-here
    echo.
) else (
    echo .env file already exists.
)

echo Setup complete!
echo.
echo Next steps:
echo 1. Edit .env and add your OpenAI API key if you haven't already
echo 2. Run the application:
echo    venv\Scripts\activate.bat
echo    streamlit run app.py
echo.
pause
