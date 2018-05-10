from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, validators

class WorkForm(FlaskForm):
    name = StringField("Name: ", [validators.Length(min=1, max=150)])
    published = IntegerField("Year of publication: ", [validators.NumberRange(min=0, max=2018)])
    description = TextAreaField("Description: ", [validators.Length(max=600, min=1)])
 
    class Meta:
        csrf = False

class WorkEditName(FlaskForm):
    name = StringField("New name: ", [validators.Length(min=1, max=150)])
    
    class Meta:
        csrf = False

class WorkEditPublished(FlaskForm):
    published = IntegerField("Year of publication: ", [validators.NumberRange(min=0, max=2018)])
    
    class Meta:
        csrf = False

class WorkEditDescription(FlaskForm):
    description = TextAreaField("Description: ", [validators.Length(max=600, min=1)])

    class Meta:
        csrf = False

class WorkAddCategory(FlaskForm):
    category = SelectField("Select category: ", [validators.data_required()], choices=[], coerce=int)

    class Meta:
        csrf = False