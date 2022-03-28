from operator import *
from math import *

from pydantic import BaseSettings


class ConnectionSettings(BaseSettings):
    HOST = '0.0.0.0'
    PORT = '65432'


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


class Settings(DatabaseSettings, CalcSettings, ConnectionSettings):
    pass


settings = Settings()
