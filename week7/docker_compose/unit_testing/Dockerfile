FROM python:3

COPY . /testing

RUN pip install -r /testing/requirements.txt

WORKDIR /testing/bsnss_logic_tests

CMD ["pytest"]
