from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CategoryForm(FlaskForm):
    name = StringField("Name of the new category: ", [validators.Length(min=1, max=150)])

    class Meta:
        csrf = False

class CategoryEditName(FlaskForm):
    name = StringField("New name: ", [validators.Length(min=1, max=150)])
    
    class Meta:
        csrf = False