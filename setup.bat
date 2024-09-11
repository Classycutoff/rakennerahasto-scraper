@echo off

:: Step 1: Check if Python is installed
python --version
IF ERRORLEVEL 1 (
    echo Python is not installed or not added to the system PATH.
    exit /b 1
)

:: Step 2: Create a virtual environment (venv)
echo Creating virtual environment...
python -m venv venv

:: Step 3: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Step 4: Check if requirements.txt exists
IF NOT EXIST requirements.txt (
    echo requirements.txt file not found.
    exit /b 1
)

:: Step 5: Install dependencies from requirements.txt
echo Installing dependencies...
pip install -r requirements.txt

:: Step 6: Confirm success
echo Setup complete. The virtual environment is activated.
:: pause