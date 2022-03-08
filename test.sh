#!/bin/bash
#always activate virtual environment
source venv/bin/activate
#run pytest
python3 -m pytest --cov=application --cov-report term-missing --cov-report xml:coverage.xml --junitxml=junit_report.xml
