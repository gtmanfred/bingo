import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

app = Flask(__name__)
app.config.from_object('config.{0}'.format(os.getenv('APP_SETTINGS', 'Config')))
db = SQLAlchemy(app)
CORS(app)

from bingo.api.app import create_app
app.register_blueprint(create_app())

app.run()
