from flask_app.exts.extensions import db

from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True,
                         nullable=False, index=True)
    email = db.Column(db.String(50), unique=True,
                      nullable=False, index=True, server_default='')
    password = db.Column(db.String(80), nullable=False, server_default='')
