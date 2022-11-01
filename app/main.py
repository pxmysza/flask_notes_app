from flask import Blueprint, render_template, url_for, redirect, session, request, flash, abort
from app import db
from app.forms import UserForm, NoteForm, LoginForm
from app.models import User, Note


display_notes_blueprint = Blueprint("notes", __name__)
login_blueprint = Blueprint("login", __name__)
register_blueprint = Blueprint("register", __name__)
logout_blueprint = Blueprint("logout", __name__)
add_note_blueprint = Blueprint("add_note", __name__)


@display_notes_blueprint.route("/")
def notes():
    if "username" not in session:
        return redirect(url_for("login.login"))
    user = User.query.filter_by(username=session["username"]).first()
    notes = Note.query.filter_by(owner_id=user.id).all()
    print(notes)
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
        session.update({"username": form.username.data})
        return redirect(url_for("notes.notes"))
    if "username" in session:
        return redirect(url_for("notes.notes"))
    return render_template("register.html", form=form)


@login_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        # If user does not exist
        if not u:
            flash("Incorrect username/password", "warning")
            return redirect(url_for("login.login"))
        # If user exists, check if password is correct
        if u.check_password(form.password.data):
            session.update({"username": u.username})
            return redirect(url_for("notes.notes"))
        else:
            flash("Incorrect username/password", "warning")
            return redirect(url_for("login.login"))
    # If session exists
    if "username" in session:
        return redirect(url_for("notes.notes"))
    return render_template("login.html", form=form)

@logout_blueprint.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
        flash("You've been logged off successfully", "success")
        return redirect(url_for("login.login"))
    else:
        return abort(403)

@add_note_blueprint.route("/add_note", methods=["GET", "POST"])
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=session["username"]).first()
        note = Note()
        note.title = form.title.data
        note.content = form.content.data
        note.owner_id = user.id
        db.session.add(note)
        db.session.commit()
        return redirect(url_for("notes.notes"))
    return render_template("new_note.html", form=form)



def page_not_found(e):
    return render_template("404.html"), 404

def dissalowed_resource(e):
    return render_template("403.html"), 403