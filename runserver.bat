:: Window bat file to allow running the Django Runserver
@echo off
cd /d %~dp0
call venv\Scripts\activate

:: Start Django server in a minimized window with a title for easy closing
start "DjangoServer" /min cmd /k "python manage.py runserver"

:: Open the site in the default browser
start http://127.0.0.1:8000

echo.
echo Django server is running. Press any key to stop the server and close the browser...
pause >nul

:: Kill the Django server window by title
taskkill /FI "WINDOWTITLE eq DjangoServer*" /T /F

:: Close common browsers if opened
taskkill /IM msedge.exe /F >nul 2>&1
taskkill /IM chrome.exe /F >nul 2>&1
taskkill /IM firefox.exe /F >nul 2>&1

echo All processes stopped.
pause