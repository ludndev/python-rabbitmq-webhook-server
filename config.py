import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    USER_AGENT = os.getenv('USER_AGENT', 'Webhook Engine')

    RABBITMQ_VIRTUAL_HOST = os.getenv('RABBITMQ_VIRTUAL_HOST', '/')
    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
    RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', 5672))
    RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'admin')
    RABBITMQ_PASS = os.getenv('RABBITMQ_PASS', 'admin')

    WEBHOOK_QUEUE = os.getenv('WEBHOOK_QUEUE', 'webhook')
    CALLBACK_QUEUE = os.getenv('CALLBACK_QUEUE', 'webhook:callback')
