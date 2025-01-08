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
