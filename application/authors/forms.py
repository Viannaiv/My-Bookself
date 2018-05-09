from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators

class AuthorForm(FlaskForm):
    name = StringField("Name: ", [validators.Length(min=1, max=150)])

    class Meta:
        csrf = False

class AuthorAddWork(FlaskForm):
    work = SelectField("Select work: ", [validators.data_required()], choices=[], coerce=int)

    class Meta:
        csrf = False

class AuthorEditName(FlaskForm):
    name = StringField("New name: ", [validators.Length(min=1, max=150)])
    
    class Meta:
        csrf = False