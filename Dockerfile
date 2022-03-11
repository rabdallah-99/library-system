FROM python:3.8
RUN python3 -m pip install --upgrade pip
COPY . .

RUN pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python3","app.py"]
