FROM python:3.7.7-slim

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

RUN pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt

ARG GROUPO_NUMERO

ENV env_GROUPO_NUMERO $GROUPO_NUMERO

COPY titulo.py .

EXPOSE 9080

CMD ["sh", "-c", "python3 titulo.py $GROUPO_NUMERO && python3 /practica_creativa2/bookinfo/src/productpage/productpage.py 9080"]









