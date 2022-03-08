FROM python:3.8
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
RUN python3 -m venv venv
RUN source venv/bin/activate
EXPOSE 5000

ENTRYPOINT ["/usr/bin/python3","app.py"]
