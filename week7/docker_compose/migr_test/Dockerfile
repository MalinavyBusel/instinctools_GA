FROM python:3

COPY . /test_dir

RUN pip install -r /test_dir/requirements.txt

WORKDIR /test_dir

CMD ["pytest"]
