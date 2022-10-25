from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.debug = True

    from .main import display_notes_blueprint

    app.register_blueprint(display_notes_blueprint)

    return app