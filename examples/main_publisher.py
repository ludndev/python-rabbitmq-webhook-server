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

from producer import Producer
from payload_dto import PayloadDto
import time
import hashlib
import json
import hmac

def generate_hmac_signature(payload: str, secret_key: bytes) -> str:
    return hmac.new(secret_key, payload.encode(), hashlib.sha256).hexdigest()

if __name__ == '__main__':
    # Example producer usage
    producer = Producer()

    event='event.test'
    payload_body = {
        'key': 'value',
        'event': event,
        'at': time.time(),
    }
    signature = generate_hmac_signature(json.dumps(payload_body), 'hmac_verification_token'.encode('utf-8'))
    payload = PayloadDto(
        event=event,
        url='http://localhost:9090/webhook',
        body=payload_body,
        headers={
            'x-webhook-signature': signature
        }
    )

    producer.produce_message(payload)

    print("---$---")

    event = 'event.test.second'
    payload_body = {
        'key': 'value',
        'event': event,
        'at': time.time(),
    }
    signature = generate_hmac_signature(json.dumps(payload_body), 'hmac_verification_token'.encode('utf-8'))
    payload = PayloadDto(
        event=event,
        url='http://localhost:9090/webhook',
        body=payload_body,
        headers={
            'x-webhook-signature': signature
        }
    )

    producer.produce_message(payload)

    print("---$---")

    event = 'event.test.third'
    payload_body = {
        'key': 'value',
        'event': event,
        'at': time.time(),
    }
    signature = generate_hmac_signature(json.dumps(payload_body), 'hmac_verification_token'.encode('utf-8'))
    payload = PayloadDto(
        event=event,
        url='http://localhost:9090/webhook',
        body=payload_body,
        headers={
            'x-webhook-signature': signature
        }
    )
    producer.produce_message(payload)

    producer.close()
