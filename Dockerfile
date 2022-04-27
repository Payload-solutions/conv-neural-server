FROM python:3.10.4

RUN pip install --upgrade pip

WORKDIR /neuronnetwork

ENV FLASK_APP wsgi.py

ENV FLASK_DEBUG=1

ENV FLASK_ENV=development

ENV FLASK_RUN_HOST 127.0.0.1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]