FROM python:3 as base

ADD src/__init__.py /basedir
ADD src/calc_processing /basedir/calc_processing
ADD requirements/requirements.prod.txt /req

RUN pip install -r /req/requirements.prod.txt

FROM base as socket

COPY --from=base /basedir /socket
ADD src/socket_server.py /socket

CMD ["python", "./socket/socket_server.py"]

FROM base as flask

COPY --from=base /basedir /flask
ADD src/flask_server.py /flask
ADD src/templates /flask/templates

RUN pip install flask

WORKDIR /flask

CMD ["python", "flask_server.py"]

FROM base as alembic

COPY --from=base /basedir/calc_processing/.env /alembic
ADD alembic.ini /alembic
ADD alembic /alembic
ADD requirements/requirements.dev.txt /alembic
ADD tests/test_migrations.py /alembic

RUN pip install -r /alembic/requirements.dev.txt
RUN pip install alembic

WORKDIR /alembic

CMD ["pytest"]

FROM base as units

COPY --from=base /basedir /testing
ADD tests/test_db_methods.py /testing
ADD tests/test_calculator.py /testing
ADD requirements/requirements.dev.txt /testing

RUN pip install -r /testing/requirements.dev.txt
RUN pip install sqlalchemy_utils

WORKDIR /testing

CMD ["pytest"]

FROM python:3 as integration

ADD tests/test_flask.py /testing
ADD tests/test_socket.py /testing
ADD requirements/requirements.dev.txt /testing

RUN pip install -r /testing/requirements.dev.txt
RUN pip install requests

WORKDIR /testing

CMD ["pytest"]
