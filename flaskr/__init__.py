import os

from flask import Flask
from flaskr.model import init_db
from flaskr.config import DevelopmentConfig
from flaskr import auth
from flaskr import recipe


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    init_db(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth.bp)
    app.register_blueprint(recipe.bp)
    app.add_url_rule('/', endpoint='index')

    return app
