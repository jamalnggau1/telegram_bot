FROM python:latest

RUN mkdir -p /usr/src/app/telegram_bot
WORKDIR /usr/src/app/telegram_bot

COPY . /usr/src/app/telegram_bot

RUN requirements install

CMD ["python", "app.py"]