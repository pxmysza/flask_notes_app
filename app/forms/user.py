from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from app.models import User


class UserForm(FlaskForm):

    def unique_username_validator(self, field):
        message = "Username already exists!"
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError(message)

    def length_validator(self, field):
        if len(field.data) < 4:
            raise ValidationError("Password must have at least 4 characters!")

    username = StringField('Username', validators=[DataRequired(), unique_username_validator])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("repeat_password", "Passwords must match"),
                                                     length_validator])
    repeat_password = PasswordField("Confirm password", validators=[DataRequired()])