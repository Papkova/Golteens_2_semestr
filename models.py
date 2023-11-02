import os

from app import app
from datetime import datetime
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
#app.config['SQLALCHEMY_BINDS'] = {
#    'db': "sqlite:///diana.db",
#}
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_kay=True)
    title = db.Column(db.Srting(100), nullable=False)
    intro = db.Column(db.Srting(100), nullable=False)
    text = db.Column(db.Text, nullablr=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Article {self.id}>'