from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base

from calculations import opers_list
from config import settings


DATABASE = settings.DATABASE

DeclarativeBase = declarative_base()


class Post(DeclarativeBase):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    operator = Column('operator', Enum(*opers_list, name="operation", create_engine=False))
    number1 = Column('number1', Integer)
    number2 = Column('number2', Integer)
    result = Column('result', Integer)


if __name__ == '__main__':
    engine = create_engine(URL.create(**DATABASE))
    DeclarativeBase.metadata.create_all(engine)


