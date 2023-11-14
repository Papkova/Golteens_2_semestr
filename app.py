import os
#from datetime import datetime
from flask import Flask, render_template , request, redirect
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///diana.db"
app.config['SQLALCHEMY_BINDS'] = {
    'db': "sqlite:///diana.db",
}
db = SQLAlchemy(app)

# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     intro = db.Column(db.String(100), nullable=False)
#     text = db.Column(db.Text, nullable=False)
#     data = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return f'<Article {self.id}>'
#
# @app.route("/create-article", methods=["POST", "GET"])
# def create_article():
#     if request.method == "POST":
#         title = request.form["title"]
#         intro = request.form["intro"]
#         text = request.form["text"]
#
#         article = Article(
#             title=title,
#             intro=intro,
#             text=text
#         )
#         try:
#             db.session.add(article)
#             db.session.commit()
#             return redirect("/")
#         except Exception as exc:
#             return f"При збереженні запису у базу даних виникла помилка: {exc}"
#     else:
#         return render_template("create_article.html")
#
#
# @app.route("/articles")
# def list_articles():
#     articles = Article.query.order_by(Article.data.desc()).all()
#     return render_template("articles.html", articles=articles)
#
#
# @app.route("/articles/<int:id>/")
# def article_detail(id):
#     article = Article.query.get(id)
#     return render_template("article_detail.html", article=article)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)
#     articles = db.relationship('Article', backref='author', lazy=True)
#
#     def __repr__(self):
#         return f'<User {self.username}>'

@app.route("/user", methods=["POST", "GET"])
def name():
    if request.method == "POST":
        username = request.form["username"]
        password_hash = request.form["password_hash"]
        articles = request.form["articles"]


        user = User(
             title=username,
             intro=password_hash,
             text=articles
                  )
        try:
            db.session.add(user)
            db.session.commit()
            return redirect("/")
        except Exception as exc:
            return f"При збереженні запису у базу даних виникла помилка: {exc}"
    else:
        return render_template("name.html")


@app.route("/user")
def list_user():
    user = User.query.order_by(User.data.desc()).all()
    return render_template("user.html", articles=user)

@app.route("/user/<int:id>/")
def article_detail(id):
    user = User.query.get(id)
    return render_template("user.html", article=user)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    articles = db.relationship('Article', backref='author', lazy=True)

    def __repr__(self):
        return f'<User {self.id}>'


@app.route("/")
def base():
    return render_template("base.html", title="Python course")


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))

