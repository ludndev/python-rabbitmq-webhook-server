from config import Config
from subscriber import Subscriber
from flask import Flask, jsonify
import pika

app = Flask(__name__)

def check_rabbitmq():
    try:
        credentials = pika.PlainCredentials(username=Config.RABBITMQ_USER, password=Config.RABBITMQ_PASS)
        config = pika.ConnectionParameters(host=Config.RABBITMQ_HOST, port=Config.RABBITMQ_PORT, credentials=credentials)
        conn = pika.BlockingConnection(config)
        conn.close()
        return True
    except Exception as e:
        print(f"RabbitMQ connection failed: {e}")
        return False

@app.route('/health')
def health():
    # Check RabbitMQ connection
    if check_rabbitmq():
        return jsonify(status="Healthy"), 200
    else:
        return jsonify(status="Unhealthy", error="RabbitMQ not reachable"), 500

def main():
    subscriber = Subscriber(Config.WEBHOOK_QUEUE)

    try:
        subscriber.start()
        app.run(host='0.0.0.0', port=8080, debug=False)
    except KeyboardInterrupt:
        print('\nGraceful stopping the server ...')
        subscriber.close()
        quit()
    except Exception as e:
        print(f'Something went wrong {e.message}')
    finally:
        # @todo: restart the server process
        print('@todo: restart the server process')

if __name__ == '__main__':
    main()
