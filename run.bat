@echo off
title ELRAMA matkul monitoring

:: cek apakah udah nginstall python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python belum terinstall, install dulu lee.
    pause
    exit
)

:: cek apakah venv udah ada
if not exist venv\ (
    echo Membuat virtual environment...
    python -m venv venv
    echo Virtual environment berhasil dibuat!
)

:: mengaktifkan virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: install/upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: install semua requirements
echo Installing requirements...
pip install -r requirements.txt

:: clear screen
cls

:: gassss
echo Starting SIRAMA Course Monitor...
echo =====================================
python main.py

:: Deactivate virtual environment
call venv\Scripts\deactivate

pause