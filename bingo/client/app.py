import os
from flask import Blueprint
from flask.ext.stormpath import logout_user, user, login_required

def create_app():
    app = Blueprint('client', __name__)
    app.debug=True

    from bingo.client.resources import (
        Game,
        GameAdmin,
    )

    resources = {
        Game: '/',
        GameAdmin: '/admin',
    }

    for resource, route in resources.items():
        app.add_url_rule(route, view_func=resource.as_view(resource.__name__))

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
