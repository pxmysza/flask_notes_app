from datetime import datetime
from app import db


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    _time_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)



