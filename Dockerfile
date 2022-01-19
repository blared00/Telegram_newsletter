FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN chmod +x entrypoint.sh


COPY . .


ENTRYPOINT ["/usr/src/app/entrypoint.sh"]