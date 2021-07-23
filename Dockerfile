FROM python:latest

RUN mkdir -p /usr/src/app/telegram_bot
WORKDIR /usr/src/app/telegram_bot

COPY . /usr/src/app/telegram_bot

RUN pip install -r requirements.txt

CMD ["python", "app.py"]