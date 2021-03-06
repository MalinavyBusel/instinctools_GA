import datetime

from pydantic import BaseSettings
from decouple import config


user = config('MONGO_INITDB_ROOT_USERNAME', cast=str)
password = config('MONGO_INITDB_ROOT_PASSWORD', cast=str)
db = config('DATABASE', cast=str)


class Config(BaseSettings):
    DB_URI = f'mongodb://{user}:{password}@{db}:27017'
    DB_NAME = config('MONGO_INITDB_DATABASE', cast=str)
    DB_TABLE = config('DATABASE_TABLE', cast=str)
    HTTP_HOST = config('HTTP_HOST', cast=str)
    HTTP_PORT = config('HTTP_PORT', cast=int)
    DEBUG = config('DEBUG', cast=bool)
    CACHING_SIZE = config('MIN_CACHE_SIZE', cast=int)


settings = Config()
