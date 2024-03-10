from flask import Flask

app = Flask(__name__)


@app.route("/health")
def health():
    """ Cehck health"""
    return "OK"


@app.route("/hello")
def hello_world():
    return "Hello, World!"