#third party imports
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


#local imports
from config import app_configuration

db = SQLAlchemy()    #database object
login_manager = LoginManager()  #login manager object


def create_app(configuration_name):
    app = Flask(__name__, instance_relative_config = True)

    app.config.from_object(app_configuration[configuration_name])

    app.config.from_pyfile('config.py')
    Bootstrap(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)

    from app import models
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .game import game as game_blueprint
    app.register_blueprint(game_blueprint)

    return app





