from flask import Flask


app = Flask(__name__)


@app.route("/hobby")
def main():
    return "My hobby is programming and target"


if __name__ == "__main__":
    app.run()
