from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class UserForm(FlaskForm):
    username = StringField('Username', validators=DataRequired())
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("repeat_password", "Passwords must match")])
    repeat_password = PasswordField("Confirm password", validators=DataRequired())


class NoteForm(FlaskForm):
    title = StringField("Title", validators=DataRequired())
    content = StringField("Content")
