FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV USER_AGENT='Webhook Engine'
ENV RABBITMQ_URL=''
ENV WEBHOOK_QUEUE=webhook
ENV CALLBACK_QUEUE=webhook:callback

CMD ["python", "app.py"]
