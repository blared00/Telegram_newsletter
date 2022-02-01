FROM python:3.8

WORKDIR /usr/src/app/tg_bot

COPY entrypoint.sh .

RUN pip3 install --upgrade pip
RUN pip3 install aiogram
RUN pip3 install python-decouple
RUN chmod +x entrypoint.sh


COPY . .

ENTRYPOINT ["/usr/src/app/tg_bot/entrypoint.sh"]
