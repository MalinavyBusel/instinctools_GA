FROM python:3 as http

ADD requirements/requirements.prod.txt /http/
ADD /src/ /http/

RUN pip install -r /http/requirements.prod.txt

WORKDIR /http

CMD [ "gunicorn", "--workers=${WORKERS}", "--threads=${THREADS}",
      "--bind", "${GUNICORN_HOST_AND_PORT}", "http_server:app"]

FROM python:3 as units

ADD requirements/requirements.dev.txt /testing/

ADD src/sortings /testing/
ADD src/server_parts/.env /testing/configuration/
ADD src/server_parts/config.py /testing/configuration/

ADD tests/test_db_methods.py /testing/
ADD tests/test_sortings.py /testing/

RUN pip install -r /testing/requirements.dev.txt
RUN pip install pydantic

WORKDIR /testing

CMD ["pytest"]

FROM python:3 as integration

ADD requirements/requirements.dev.txt /testing/
ADD tests/test_http.py /testing/

RUN pip install -r /testing/requirements.dev.txt
RUN pip install requests

WORKDIR /testing

CMD ["pytest"]
