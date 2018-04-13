from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class EditionForm(FlaskForm):
    name = StringField("Name: ", [validators.Length(min=2, max=150)])
    printed = IntegerField("Printed in: (year) ", [validators.NumberRange(min=1377, max=2018)])
    publisher = StringField("Publisher: ", [validators.Length(min=1, max=100)])
    language = StringField("Language: ", [validators.Length(min=3, max=50)])
    read = BooleanField("I have read this book: ")

