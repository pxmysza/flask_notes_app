from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hashlib import md5
from datetime import timedelta
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_moment import Moment

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    encryptor = md5()
    csrf = CSRFProtect(app)
    moment = Moment()
    moment.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=30)
    app.secret_key = encryptor.digest()

    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes_app.db"

    db.init_app(app)

    migrate = Migrate(app, db)

    from .main import display_notes_blueprint, register_blueprint, login_blueprint, logout_blueprint, page_not_found, \
        dissalowed_resource, add_note_blueprint, delete_note_blueprint, edit_note_blueprint

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, dissalowed_resource)
    app.register_blueprint(display_notes_blueprint)
    app.register_blueprint(register_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(logout_blueprint)
    app.register_blueprint(add_note_blueprint)
    app.register_blueprint(delete_note_blueprint)
    app.register_blueprint(edit_note_blueprint)

    return app
