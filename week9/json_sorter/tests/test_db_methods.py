import pymongo
import pytest

from pymongo.errors import ConnectionFailure

from configuration.config import settings


def test_connection_failing():
    with pytest.raises(ConnectionFailure):
        mongodb_client = pymongo.MongoClient('wrong_url')


mongodb_client = pymongo.MongoClient(settings.DB_URI)
mongodb = mongodb_client[settings.DB_NAME][settings.DB_TABLE]


def test_db_adding(mongodb_=mongodb):
    insert_data = {'sorted_sequence': 'test_sequence',
                   'hashed_sequence': hex(12345),
                   'time_taken': 'some_time',
                   'sorting_type': 'any_sorting'}
    mongodb_.insert_one(insert_data)
    data_from_db = mongodb_.find_one({'hashed_sequence': hex(12345)})
    assert data_from_db


def test_db_deleting(mongodb_=mongodb):
    mongodb_.delete_one({'hashed_sequence': hex(12345)})
    data_from_db = mongodb_.find_one({'hashed_sequence': hex(12345)})
    assert not data_from_db
