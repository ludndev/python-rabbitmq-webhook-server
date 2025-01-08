# python-rabbitmq-webhook-server


## todos

- [ ] make `app.py` support multithreading for processing or many workers


## 
```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management
```

## helpers cmd

````bash

python3 -m venv .venv
.venv/bin/activate

pip3 install -r requirements.txt 

cp .env.example .env

python3 app.py

`````
