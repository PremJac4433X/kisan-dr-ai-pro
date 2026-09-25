@echo off
echo ========================================================
echo   Starting KisanDr AI - Smart Agricultural Diagnostics
echo ========================================================
echo.
echo Checking Python environment...
python --version
echo.
echo Installing dependencies if needed...
python -m pip install -r requirements.txt
echo.
echo Initializing leaf sample assets...
python -m app.create_samples
echo.
echo Launching Web Server on http://localhost:8000 ...
echo Press Ctrl+C to terminate.
echo ========================================================
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
pause
