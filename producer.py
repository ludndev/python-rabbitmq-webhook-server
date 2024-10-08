import pika
from payload_dto import PayloadDto
from config import Config

class Producer:
    def __init__(self):
        self.connection = self.conn()
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Config.WEBHOOK_QUEUE, durable=True)

    def conn(self):
        config = pika.ConnectionParameters(host=Config.RABBITMQ_HOST, port=Config.RABBITMQ_PORT)
        return pika.BlockingConnection(config)

    def produce_message(self, payload: PayloadDto):
        self.channel.basic_publish(
            exchange='',
            routing_key=Config.WEBHOOK_QUEUE,
            body=payload.to_json()
        )
        print(f"Sent: {payload.to_json()}")

    def close(self):
        self.connection.close()
