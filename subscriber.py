import time
import time
import pika
import requests
import json
from payload_dto import PayloadDto
from producer import Producer
from config import Config

class Subscriber:
    ACCEPTED_HEADERS = [200, 201]

    def __init__(self, queue_name):
        self.connection = self.conn()
        self.channel = self.connection.channel()
        self.queue_name = queue_name
        self.channel.queue_declare(queue=self.queue_name, durable=True)
        self.producer = Producer()

    def conn(self):
        url_parameter = pika.URLParameters(Config.RABBITMQ_URL)
        return pika.BlockingConnection(url_parameter)

    def process(self, ch, method, properties, body):
        headers = {
            'user-agent': Config.USER_AGENT,
        }

        payload = json.loads(body)
        dto = PayloadDto(**payload)

        print(f"Subscriber: Data received", dto)

        if 'headers' in payload and len(payload['headers']) > 0:
            headers.update(payload['headers'])

        try:
            response = requests.post(dto.url, json=dto.body, headers=dto.headers)

            if response.status_code in self.ACCEPTED_HEADERS:
                self.emit_callback(dto.event, response.status_code)
        except Exception as e:
            print(f"Error processing message: {e}")

    def emit_callback(self, event: str, status: int):
        self.producer.channel.queue_declare(queue=Config.CALLBACK_QUEUE)

        callback_message = {
            'webhook_id': 'X1234567890',  # oid/uuid/nanoid
            'event': event,
            'status': status,
            'at': time.time(),
        }

        self.producer.channel.basic_publish(
            exchange='',
            routing_key=Config.CALLBACK_QUEUE,
            body=json.dumps(callback_message)
        )

        print(f"Callback Sent: {callback_message}")

    def start(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.process, auto_ack=True)
        print(f'Waiting for messages on {self.queue_name}. To exit press CTRL+C')
        self.channel.start_consuming()

    def close(self):
        self.connection.close()
