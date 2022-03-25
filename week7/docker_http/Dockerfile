FROM python:3

COPY . /calc

RUN pip install -r /calc/requirements.txt

EXPOSE 5000
EXPOSE 5432

CMD ["python", "./calc/calc2/flask_server.py"]
