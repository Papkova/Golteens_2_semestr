import os
from flask import Flask, render_template
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


@app.route("/base")
def base():
    return render_template("base.html", title="Python course")


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
