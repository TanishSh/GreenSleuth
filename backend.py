import flask

green_sleuth_app = flask.Flask(__name__)

@green_sleuth_app.route("/")
def hello_world():
    return "<p>Hi</p>"