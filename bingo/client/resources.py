from flask import request, jsonify, render_template, session
from flask.views import MethodView
from flask.ext.stormpath import user, groups_required

class Game(MethodView):
    def get(self):
        return render_template('index.html', title='The Game!')

class GameAdmin(MethodView):
    decorators = [
        groups_required(['admin'])
    ]
    def get(self):
        return render_template('admin.html', title='The Game!')
