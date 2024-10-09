from producer import Producer
from payload_dto import PayloadDto
import time

if __name__ == '__main__':
    # Example producer usage
    producer = Producer()

    event='event.test'
    payload = PayloadDto(
        event=event,
        url='https://webhook.site/28ac8163-9fd8-43d2-b8b0-71ebe1436e6d',
        body={
            'key': 'value',
            'event': event,
            'at': time.time(),
        },
        headers={
            'x-webhook-signature': 'hmac_verification_token'
        }
    )

    producer.produce_message(payload)

    event = 'event.test.second'
    payload = PayloadDto(
        event=event,
        url='https://webhook.site/28ac8163-9fd8-43d2-b8b0-71ebe1436e6d',
        body={
            'key': 'value',
            'event': event,
            'at': time.time(),
        },
        headers={
            'x-webhook-signature': 'hmac_verification_token'
        }
    )
    producer.produce_message(payload)

    event = 'event.test.third'
    payload = PayloadDto(
        event=event,
        url='https://webhook.site/28ac8163-9fd8-43d2-b8b0-71ebe1436e6d',
        body={
            'key': 'value',
            'event': event,
            'at': time.time(),
        },
        headers={
            'x-webhook-signature': 'hmac_verification_token'
        }
    )
    producer.produce_message(payload)

    producer.close()
