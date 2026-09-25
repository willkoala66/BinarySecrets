import flask
import os
import sys
sys.path.append(".")

def create_app(test_config=None):
    app = flask.Flask(__name__ , instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'baked.sqlite'),)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    import db
    db.init_app(app)


    return app

