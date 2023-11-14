# import os
# from app import app
# from datetime import datetime
# from dotenv import load_dotenv
# from flask_sqlalchemy import SQLAlchemy
#
# load_dotenv()
#
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///diana.db"
# app.config['SQLALCHEMY_BINDS'] = {
#     'db': "sqlite:///diana.db",
# }
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)
#     articles = db.relationship('Article', backref='author', lazy=True)
#
#     def __repr__(self):
#         return f'<User {self.id}>'