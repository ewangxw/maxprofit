FROM python:3.9.6-alpine

WORKDIR /usr/src/app

COPY maxprofit.py ./

CMD [ "python", "./maxprofit.py"]