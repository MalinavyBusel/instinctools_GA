from flask import Flask

from server_parts.config import settings
from blueprints.api import api

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 16 + 1

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host=settings.HTTP_HOST,
            port=settings.HTTP_PORT,
            debug=settings.DEBUG)

