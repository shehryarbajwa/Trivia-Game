FROM python:latest

WORKDIR /

COPY requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
COPY ./flaskr /

RUN export FLASK_APP=flaskr/app.py

CMD flask run
