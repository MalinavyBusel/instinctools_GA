import orjson
import pymongo

from flask import Flask, request
from fnvhash import fnv1a_64

from server_parts.sorter import pool_sorter
from server_parts.config import settings

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 16 + 1

mongodb_client = pymongo.MongoClient(settings.DB_URI)
mongodb = mongodb_client[settings.DB_NAME][settings.DB_TABLE]


@app.route("/api/v0.1/posted-sequence", methods=['POST'])
def main_post():
    json_input = orjson.loads(request.data)
    sorting_type = json_input.get('sorting_selected', 'shaking_sort')
    sequence = json_input['sequence']

    hashed_sequence = hex(fnv1a_64(orjson.dumps(sequence)))
    sorting_result = mongodb.find_one({'hashed_sequence': hashed_sequence})
    if not sorting_result:
        sorting_result = pool_sorter(sorting_type, sequence)
        db_data = dict()
        db_data['hashed_sequence'] = hashed_sequence
        db_data['sorted_sequence'] = sorting_result['sorted_sequence']
        mongodb.insert_one(db_data)

    response = app.response_class(
        response=orjson.dumps(sorting_result),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(host=settings.HTTP_HOST,
            port=settings.HTTP_PORT,
            debug=settings.DEBUG)

