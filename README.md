# Overview

This project is a Selenium-based automation framework built using Python. It automates web browser interactions for testing web applications efficiently.

## Technologies Used

Python - Core programming language

Selenium : Web automation framework

PyTest : Testing framework (if applicable)

PyTest-html : Pytest HTMl Reports

PyTest-xdist : Run tests parallel

Openpyxl: MS Excel support

ChromeDriver / GeckoDriver - Browser drivers

Virtual Environment (.venv) - Isolated dependencies

## Run the test
CMD : python -m pytest -s -v -m "sanity" --html=Reports/report.html testCases/ --browser chrome
Or Double click on the run.bat file.
