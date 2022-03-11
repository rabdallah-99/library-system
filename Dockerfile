FROM python:3.8-alpine
#WORKDIR /app
COPY . .
RUN apt-get update pip -y
RUN pip install -r requirements.txt
RUN pip install flask
EXPOSE 5000

ENTRYPOINT ["python","app.py"]
