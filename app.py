from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World, Testing with some changes!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
