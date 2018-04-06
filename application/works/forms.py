from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField

class WorkForm(FlaskForm):
    name = StringField("Name: ")
    published = IntegerField("Year of publication: ")
    description = TextAreaField("Description: ")
 
    class Meta:
        csrf = False