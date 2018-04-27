from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username: ", [validators.Length(min=6, max=50)])
    password = PasswordField("Password: ", [validators.Length(min=8, max=20)])
  
    class Meta:
        csrf = False

class SigninForm(FlaskForm):
    name = StringField("Name: ", [validators.Length(min=3, max=150)])
    username = StringField("Username: ", [validators.Length(min=6, max=50)])
    password = PasswordField("Password: ", [validators.Length(min=8, max=20), validators.EqualTo('confirm', message="Passwords must match")])
    confirm  = PasswordField("Repeat Password: ")

    class Meta:
        csrf = False

class ChangePasswordForm(FlaskForm):
    password = PasswordField("New password: ", [validators.Length(min=8, max=20), validators.EqualTo('confirm', message="Passwords must match")])
    confirm  = PasswordField("Repeat password: ")

    class Meta:
        csrf = False

class ChangeUsernameForm(FlaskForm):
    username = StringField("New username: ", [validators.Length(min=6, max=50)])

    class Meta:
        csrf = False

class ChangeNameForm(FlaskForm):
    name = StringField("New name: ", [validators.Length(min=3, max=150)])

    class Meta:
        csrf = False