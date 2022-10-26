from flask import Blueprint, request, render_template, url_for, redirect
from . import db
from .data_forms import UserForm
from .models import User, Note

display_notes_blueprint = Blueprint("notes", __name__)
login_blueprint = Blueprint("login", __name__)
register_blueprint = Blueprint("register", __name__)


@display_notes_blueprint.route("/")
def notes():
    return render_template("notes.html")


@register_blueprint.route("/register", methods=["POST", "GET"])
def register():
    form = UserForm()
    if form.validate_on_submit(): #Automatically checks if method is POST and form is valid
        user = User()
        user.username = form.username.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("notes.notes"))
    return render_template("register.html", form=form)



