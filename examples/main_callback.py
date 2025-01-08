import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

# ---

from config import Config
from subscriber import Subscriber
import json

def callback_processing(ch, method, properties, body):
    # Process the incoming callback messages
    callback_data = json.loads(body)
    print(f"Received callback: {callback_data}")

def main():
    callback_subscriber = Subscriber(Config.CALLBACK_QUEUE)

    try:
        callback_subscriber.channel.basic_consume(
            queue='webhook:callback',
            on_message_callback=callback_processing,
            auto_ack=True
        )

        print('Waiting for callback messages. To exit press CTRL+C')
        callback_subscriber.channel.start_consuming()
    except KeyboardInterrupt:
        print('\nGraceful stopping the server ...')
        callback_subscriber.close()
        quit()
    except Exception as e:
        print(f'Something went wrong {e.message}')
    finally:
        # @todo: restart the server process
        print('@todo: restart the server process')

if __name__ == '__main__':
    main()
