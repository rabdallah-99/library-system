FROM python:3.8
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["/usr/bin/python3","app.py"]
