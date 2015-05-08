import os
from flask import Blueprint
from flask.ext.restful import Api

def create_app():
    app = Blueprint('client', __name__)
    app.debug=True
    #api = Api(app)

    from bingo.client import resources
#.resources import (
#        Game,
#    )

    app.add_url_rule('/', view_func=resources.Game.as_view('game'), methods=['GET'])
    #for resource, route in resources.items():
    #    api.add_resource(resource, route)
    return app
