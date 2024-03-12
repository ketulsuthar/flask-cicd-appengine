from flask import Flask

app = Flask(__name__)


@app.route("/health")
def health():
    """ Cehck health"""
    return "OK"


@app.route("/hello/<name>")
def hello_world(name):
    return f"Hello, {name}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
