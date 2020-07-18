FROM python:alpine3.7

COPY . /app

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5001

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
