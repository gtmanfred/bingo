import os
from flask import Blueprint
from flask.ext.cors import CORS
#from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

def create_app():
    app = Blueprint('backend', __name__)
    app.debug=True
    #global db
    #db = SQLAlchemy(app)
    api = Api(app)

    from bingo.api.resources import (
        Rules,
        Rule
    )
    resources={
        Rules: '/rules',
        Rule: '/rules/<name>',
    }

    for resource, route in resources.items():
        api.add_resource(resource, route)
    return app
