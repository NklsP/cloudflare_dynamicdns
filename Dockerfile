FROM python:3

WORKDIR /usr/src/app

RUN pip install requests

COPY main.py ./
COPY config.cfg ./

CMD [ "python", "./main.py" ]
