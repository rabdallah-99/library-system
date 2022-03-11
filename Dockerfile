FROM python:3.8
COPY . .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python3","app.py"]
