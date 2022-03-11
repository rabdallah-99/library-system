FROM python:3.5
#WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python3","app.py"]
