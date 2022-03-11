#!/bin/bash
#always activate virtual environment
#run pytest
cd /app
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report term-missing --cov-report xml:coverage.xml --junitxml=junit_report.xml
