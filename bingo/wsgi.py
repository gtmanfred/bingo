import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

app = Flask(__name__)
app.config.from_object('config.{0}'.format(os.getenv('APP_SETTINGS', 'Config')))
app.debug=True
db = SQLAlchemy(app)
CORS(app)

import bingo.api.app
import bingo.client.app
app.register_blueprint(bingo.api.app.create_app())
app.register_blueprint(bingo.client.app.create_app())
