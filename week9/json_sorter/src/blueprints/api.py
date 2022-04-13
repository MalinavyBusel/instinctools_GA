import orjson
import pymongo

from flask import Flask, request, Blueprint
from fnvhash import fnv1a_64

from server_parts.sorter import pool_sorter
from server_parts.config import settings, InputData, OutputData


mongodb_client = pymongo.MongoClient(settings.DB_URI)
mongodb = mongodb_client[settings.DB_NAME][settings.DB_TABLE]

api = Blueprint('api', __name__, url_prefix='/api')
v1 = Blueprint('v1', __name__, url_prefix='/v0.1')
api.register_blueprint(v1)

CACHE_MIN_SIZE = settings.CACHING_SIZE


@api.post("/posted-sequence")
def main_post():
    json_input = InputData(**orjson.loads(request.data))
    sorting_type = json_input.sorting_selected  # default moved to pydantic model
    sequence = json_input.sequence

    if len(sequence) > CACHE_MIN_SIZE:
        hashed_sequence = hex(fnv1a_64(orjson.dumps(sequence)))
        sorting_result = mongodb.find_one({'hashed_sequence': hashed_sequence})
        if not sorting_result:
            sorting_result = pool_sorter(sorting_type, sequence,
                                         (hashed_sequence, mongodb))
            # DB adding was moved to pool_sorter as a callback
    else:
        sorting_result = pool_sorter(sorting_type, sequence)
    response_data = OutputData(**sorting_result)

    response = app.response_class(
        response=response_data.json(),
        status=200,
        mimetype='application/json'
    )
    return response

