import os

from operator import *
from math import *

from pydantic import BaseSettings
from decouple import config


class ConnectionSettings(BaseSettings):
    HOST = '0.0.0.0'
    FLASK_PORT = '5000'
    SOCKET_PORT = '65432'


class DatabaseSettings(BaseSettings):
    DB = config('POSTGRES_DB', cast=str)
    DB_USERNAME = config('POSTGRES_USER', cast=str)
    DB_PASSWORD = config('POSTGRES_PASSWORD', cast=str)
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
