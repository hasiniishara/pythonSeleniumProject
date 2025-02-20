@echo off
cd /d "%~dp0"
call .venv\Scripts\activate
python -m pytest -s -v -m "sanity" --html=Reports/report.html testCases/ --browser chrome
rem python -m pytest -s -v -m "regression" --html=Reports/report.html testCases/ --browser chrome
rem python -m pytest -s -v -m "sanity or regression" --html=Reports/report.html testCases/ --browser chrome
rem python -m pytest -s -v -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome
pause