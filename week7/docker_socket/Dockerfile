FROM python:3

COPY . /calc

RUN pip install -r /calc/requirements.txt

EXPOSE 5432
EXPOSE 65432

CMD ["python", "/calc/calc3/server.py"]


