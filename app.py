import os
from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
@app.route("/")
def main():
    return render_template(".index.html")


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
