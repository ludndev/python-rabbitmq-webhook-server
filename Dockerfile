FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV USER_AGENT='Webhook Engine'
ENV RABBITMQ_HOST=127.0.0.1
ENV RABBITMQ_PORT=5672
ENV RABBITMQ_USER=guest
ENV RABBITMQ_PASS=guest
ENV WEBHOOK_QUEUE=webhook
ENV CALLBACK_QUEUE=webhook:callback

CMD ["python", "app.py"]
