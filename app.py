from flask import Flask


app = Flask(__name__)


@app.route("/Full_name")
def main():
    return "Papkova Diana Valeriivna"


if __name__ == "__main__":
    app.run("/Full_name")
