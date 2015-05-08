from flask import request, jsonify
from flask.ext.restful import Resource, abort
from flask.ext.restful.reqparse import RequestParser

class Game(Resource):
    def get(self):
        return jsonify({'games': []})
