FROM python

RUN pip install flask
RUN pip install sqlalchemy
RUN pip install pydantic
RUN pip install python-dotenv

COPY . /calc

CMD python /calc/http/flask-server.py
