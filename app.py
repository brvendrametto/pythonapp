from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "ok"


@app.route("/services/service-2")
def hello():
    return "Python App Service-br2"


@app.route("/services/service-2/status")
def status():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
