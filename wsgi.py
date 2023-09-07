from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return 'Deploy Test which is modified by Joe.\n This is in development environment.'

