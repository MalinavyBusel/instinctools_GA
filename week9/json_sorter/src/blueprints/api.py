import orjson
import pymongo

from flask import Flask, request, Blueprint
from fnvhash import fnv1a_64

from server_parts.sorter import pool_sorter
from server_parts.config import settings


mongodb_client = pymongo.MongoClient(settings.DB_URI)
mongodb = mongodb_client[settings.DB_NAME][settings.DB_TABLE]

api = Blueprint('api', __name__, url_prefix='/api')


@api.post("/posted-sequence")
def main_post():
    json_input = orjson.loads(request.data)
    sorting_type = json_input.get('sorting_selected', 'shaking_sort')
    sequence = json_input['sequence']

    if len(sequence) > 350:
        hashed_sequence = hex(fnv1a_64(orjson.dumps(sequence)))
        sorting_result = mongodb.find_one({'hashed_sequence': hashed_sequence})
        if not sorting_result:
            sorting_result = pool_sorter(sorting_type, sequence,
                                         (hashed_sequence, mongodb))
            # DB adding was moved to pool_sorter as a callback
    else:
        sorting_result = pool_sorter(sorting_type, sequence)

    response = app.response_class(
        response=orjson.dumps(sorting_result),
        status=200,
        mimetype='application/json'
    )
    return response

