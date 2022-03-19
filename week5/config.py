from operator import *
from math import *

from pydantic import BaseSettings
from dataclasses import dataclass


@dataclass
class DatabaseSettings(BaseSettings):
    DATABASE = {
        'drivername': 'postgresql',
        'host': 'localhost',
        'port': '5432',
        'username': 'postgres',
        'password': 'mypassword)',
        'database': 'calculations'
    }


@dataclass
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
