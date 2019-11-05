from . import db
from flask_login import UserMixin


class __user__(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225))
    email = db.Column(db.String(75), unique=True)
    password = db.Column(db.String(50))
