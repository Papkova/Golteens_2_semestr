from flask import Flask


app = Flask(__name__)


@app.route("/birthday")
def main():
    return "My birthday 29 June"


if __name__ == "__main__":
    app.run("/birthday")
