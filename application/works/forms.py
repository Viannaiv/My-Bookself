from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, validators

class WorkForm(FlaskForm):
    name = StringField("Name: ", [validators.Length(min=1, max=150)])
    published = IntegerField("Year of publication: ", [validators.NumberRange(min=0, max=2018)])
    description = TextAreaField("Description: ", [validators.Length(max=600, min=1)])
 
    class Meta:
        csrf = False

# BC and AD might be a good idea to add