from flask import request, jsonify, render_template, session
from flask.views import MethodView
from flask.ext.stormpath import login_required, user

class Game(MethodView):
    @login_required
    def get(self):
        return render_template('index.html', title='The Game!')
