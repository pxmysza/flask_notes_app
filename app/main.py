from flask import Blueprint, request, render_template, url_for

display_notes_blueprint = Blueprint("notes", __name__)


@display_notes_blueprint.route("/")
def notes():
    return render_template("notes.html")