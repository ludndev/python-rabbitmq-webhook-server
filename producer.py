import pika
from payload_dto import PayloadDto
from config import Config

class Producer:
    def __init__(self):
        self.connection = self.conn()
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Config.WEBHOOK_QUEUE, durable=True)

    def conn(self):
        url_parameter = pika.URLParameters(Config.RABBITMQ_URL)
        return pika.BlockingConnection(url_parameter)

    def produce_message(self, payload: PayloadDto):
        self.channel.basic_publish(
            exchange='',
            routing_key=Config.WEBHOOK_QUEUE,
            body=payload.to_json(),
            properties=pika.BasicProperties(
              delivery_mode=2,
            )
        )
        print(f"Sent: {payload.to_json()}")

    def close(self):
        self.connection.close()
