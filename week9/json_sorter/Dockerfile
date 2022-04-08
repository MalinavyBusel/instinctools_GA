FROM python:3 as http

ADD requirements/requirements.prod.txt /req
ADD /src /http

RUN pip install -r /req/requirements.prod.txt

WORKDIR /http

CMD [ "gunicorn", "-w", "5", "--bind", "0.0.0.0:5000", "http_server:app"]

FROM python:3 as units

ADD requirements/requirements.dev.txt /req

ADD src/sortings /testing/sortings
ADD src/server_parts/.env /testing/configuration
ADD src/server_parts/config.py /testing/configuration

ADD tests/test_db_methods.py /testing
ADD tests/test_sortings.py /testing

RUN pip install -r req/requirements.dev.txt

WORKDIR /testing

CMD ["pytest"]

FROM python:3 as integration

ADD requirements/requirements.dev.txt /req
ADD tests/test_http.py /testing

RUN pip install -r /req/requirements.dev.txt
RUN pip install requests

WORKDIR /testing

CMD ["pytest"]
