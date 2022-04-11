from flask import Flask, Blueprint

from server_parts.config import settings
from blueprints.api import api

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 16 + 1

app.register_blueprint(api)
v1 = Blueprint('v1', __name__, url_prefix='/v0.1')
api.register_blueprint(v1)

if __name__ == "__main__":
    app.run(host=settings.HTTP_HOST,
            port=settings.HTTP_PORT,
            debug=settings.DEBUG)

