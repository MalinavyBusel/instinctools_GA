FROM python:3

COPY . /calc

RUN pip install -r /calc/requirements.txt

WORKDIR /calc

CMD ["python", "./calc2/flask_server.py"]

