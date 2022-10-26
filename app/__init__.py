from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hashlib import md5
from datetime import timedelta

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    encryptor = md5()

    app.permanent_session_lifetime = timedelta(minutes=30)
    app.secret_key = encryptor.digest()

    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes_app.db"

    db.init_app(app)

    from .main import display_notes_blueprint, register_blueprint, login_blueprint

    app.register_blueprint(display_notes_blueprint)
    app.register_blueprint(register_blueprint)
    app.register_blueprint(login_blueprint)

    return app