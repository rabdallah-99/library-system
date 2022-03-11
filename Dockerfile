FROM python:3.8
#WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install flask
EXPOSE 5000

ENTRYPOINT ["python3","app.py"]
