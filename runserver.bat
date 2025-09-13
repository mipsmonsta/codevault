:: Window bat file to allow running the Django Runserver
@echo off
cd /d %~dp0
call venv\Scripts\activate

:: Start Django server in a minimized window with a title for easy closing
start "DjangoServer" /min cmd /k "python manage.py runserver"

:: Open the site in the default browser
start http://127.0.0.1:8000

pause