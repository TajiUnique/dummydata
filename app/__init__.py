from flask import Flask
from flask_bootstrap import Bootstrap


def createapp(home=''):
    app = Flask(__name__, template_folder='Designs')


    app.secret_key = ''

    Bootstrap(app)

# register the blueprints

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint

    app.register_blueprint(home_blueprint)

    return app

