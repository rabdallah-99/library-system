FROM python:3.6
#WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN apt install python3-venv
RUN python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python","app.py"]
