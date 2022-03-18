from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base

from instinctools_GA.week5.calculations import opers_list


DeclarativeBase = declarative_base()


class Post(DeclarativeBase):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    operator = Column('operator', Enum(*opers_list, name="operation", create_engine=False))
    number1 = Column('number1', Integer)
    number2 = Column('number2', Integer)
    result = Column('result', Integer)



DATABASE = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'mypassword)',
    'database': 'calculations'
}

if __name__ == '__main__':
    engine = create_engine(URL.create(**DATABASE))
    DeclarativeBase.metadata.create_all(engine)


