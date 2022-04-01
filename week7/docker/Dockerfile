FROM python:3

COPY . /calc

ARG start_file="flask_server.py"

RUN pip install -r /calc/requirements.txt

CMD ["python", "./calc/calc2/${start_file}"]
