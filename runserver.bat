:: Window bat file to allow running the Django Runserver
@echo off
cd /d %~dp0
call venv\Scripts\activate
python manage.py runserver
pause