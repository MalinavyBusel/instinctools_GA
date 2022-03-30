import os

from operator import *
from math import *

from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class ConnectionSettings(BaseSettings):
    HOST = '0.0.0.0'
    F_PORT = '5000'
    S_PORT = '65432'


class DatabaseSettings(BaseSettings):
    DB = os.environ.get('POSTGRES_DB')
    DB_USERNAME = os.environ.get('POSTGRES_USER')
    DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    DATABASE = {
        'drivername': 'postgresql',
        'host': 'postgres_container',
        'port': '5432',
        'username': DB_USERNAME,
        'password': DB_PASSWORD,
        'database': DB
    }


class CalcSettings(BaseSettings):
    oper_dict = {"add": add, "truediv": truediv, "sub": sub,
                 "mul": mul, "pow": pow, "floordiv": floordiv,
                 "and": and_, "xor": xor, "or": or_,
                 "is": is_, "is_not": is_not, "lshift": lshift,
                 "mod": mod, "rshift": rshift, "lt": lt, "le": le,
                 "eq": eq, "ne": ne, "gt": gt, "ge": ge, "hypot": hypot,
                 "atan2": atan2, "ldexp": ldexp}


class Settings(DatabaseSettings, CalcSettings, ConnectionSettings):
    pass


settings = Settings()
