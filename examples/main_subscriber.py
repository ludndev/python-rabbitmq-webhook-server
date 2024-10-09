from config import Config
from subscriber import Subscriber

def main():
    subscriber = Subscriber(Config.WEBHOOK_QUEUE)

    try:
        subscriber.start()
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
