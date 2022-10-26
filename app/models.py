from datetime import datetime
from . import db
from werkzeug.security import check_password_hash, generate_password_hash



class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    content = db.Column(db.String)
    _time_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, title, content):
        self.title, self.content = title, content


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    notes = db.relationship("Note")

    # def __init__(self, username, password):
    #     self.username, self.password = username, password

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method="pbkdf2:sha256", salt_length=16)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)