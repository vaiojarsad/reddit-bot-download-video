FROM python:3.8-alpine
WORKDIR /bot
COPY ./config.py .
COPY ./main.py .
COPY ./processor.py .
COPY ./util.py .
COPY ./praw.ini .
COPY ./requirements/release.txt ./requirements/release.txt
COPY ./requirements.txt .

ENV PYTHONUNBUFFERED 1

RUN apk update && pip install -r requirements.txt

ENTRYPOINT ["python", "./main.py"]
