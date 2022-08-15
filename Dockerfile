FROM python:slim-bullseye

ADD . /app
WORKDIR /app

CMD ["python", "-u", "/app/main.py"]
