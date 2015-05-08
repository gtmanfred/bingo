import os
from flask import Blueprint
from flask.ext.restful import Api

def create_app():
    app = Blueprint('client', __name__)
    app.debug=True

    from bingo.client import resources

    app.add_url_rule('/', view_func=resources.Game.as_view('game'), methods=['GET'])
    app.add_url_rule('/admin', view_func=resources.GameAdmin.as_view('gameadmin'), methods=['GET'])
    return app
