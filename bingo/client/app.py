import os
from flask import Blueprint
from flask.ext.restful import Api
from flask.ext.stormpath import logout_user, user, login_required

def create_app():
    app = Blueprint('client', __name__)
    app.debug=True

    from bingo.client import resources

    app.add_url_rule('/', view_func=resources.Game.as_view('game'), methods=['GET'])
    app.add_url_rule('/admin', view_func=resources.GameAdmin.as_view('gameadmin'), methods=['GET'])

    @app.route('/logout')
    @login_required
    def logout():
        """
        Log out a logged in user.  Then redirect them back to the main page of the
        site.
        """
        logout_user()
        return redirect(url_for('index'))
    return app
