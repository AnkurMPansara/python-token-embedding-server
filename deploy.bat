@echo off

set LISTEN_PORT=8000

IF NOT EXIST "venv" (
    echo Virtual environment not found. Creating venv...
    python -m venv venv
) ELSE (
    echo Virtual environment already exists.
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo Starting server on port %LISTEN_PORT%...
python main.py %LISTEN_PORT%

pause
