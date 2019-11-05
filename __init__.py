from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    db.init_app(app)

    __signin__ = LoginManager()
    __signin__.login_view = 'authenticate.signin'
    __signin__.init_app(app)

    from .users import __user__

    @__signin__.user_loader
    def user_load(user_id):
        return __user__.query.get(int(user_id))

    from .base import base
    app.register_blueprint(base)

    from .authenticate import authenticate
    app.register_blueprint(authenticate)

    return app
