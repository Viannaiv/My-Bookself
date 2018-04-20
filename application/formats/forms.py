from flask_wtf import FlaskForm
from wtforms import StringField, validators

class FormatForm(FlaskForm):
    name = StringField("Name: ", [validators.Length(min=2, max=50)])

    class Meta:
        csrf = False