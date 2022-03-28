from math import *
from operator import *

from pydantic import BaseSettings
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base


class DatabaseSettings(BaseSettings):
    DATABASE = {
        'drivername': 'postgresql',
        'host': 'postgres_container',
        'port': '5432',
        'username': 'postgres',
        'password': 'mypassword)',
        'database': 'calculations'
    }


class CalcSettings(BaseSettings):
    oper_dict = {"add": add, "truediv": truediv, "sub": sub,
                 "mul": mul, "pow": pow, "floordiv": floordiv,
                 "and": and_, "xor": xor, "or": or_,
                 "is": is_, "is_not": is_not, "lshift": lshift,
                 "mod": mod, "rshift": rshift, "lt": lt, "le": le,
                 "eq": eq, "ne": ne, "gt": gt, "ge": ge, "hypot": hypot,
                 "atan2": atan2, "ldexp": ldexp}


class Settings(DatabaseSettings, CalcSettings):
    pass


settings = Settings()

DeclarativeBase = declarative_base()

opers_list = list(settings.oper_dict.keys())


class Post(DeclarativeBase):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    operator = Column('operator', Enum(*opers_list, name="operation", create_engine=False))
    number1 = Column('number1', Integer)
    number2 = Column('number2', Integer)
    result = Column('result', Integer)
