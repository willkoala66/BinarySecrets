import flask


from app.db import db

bp = flask.Blueprint('index', __name__)

bp.route("/", methods=("GET", "POST"))
def index():
    return flask.render_template("index.html")
