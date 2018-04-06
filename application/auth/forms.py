from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username: ", [validators.Length(min=6, max=50)])
    password = PasswordField("Password: ", [validators.Length(min=8, max=20)])
  
    class Meta:
        csrf = False