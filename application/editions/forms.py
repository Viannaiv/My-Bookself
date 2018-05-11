from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, SelectField, validators

class EditionForm(FlaskForm):
    name = StringField("Name: ", [validators.Length(min=2, max=150)])
    printed = IntegerField("Printed in: (year) ", [validators.NumberRange(min=1377, max=2018)])
    publisher = StringField("Publisher: ", [validators.Length(min=1, max=100)])
    language = StringField("Language: ", [validators.Length(min=3, max=50)])
    read = BooleanField("I have read this book: ")

    class Meta:
        csrf = False

class EditionEditName(FlaskForm):
    name = StringField("New name: ", [validators.Length(min=1, max=150)])
    
    class Meta:
        csrf = False

class EditionEditPrinted(FlaskForm):
    printed = IntegerField("Printed in: (year) ", [validators.NumberRange(min=1377, max=2018)])
    
    class Meta:
        csrf = False

class EditionEditPublisher(FlaskForm):
    publisher = StringField("New name: ", [validators.Length(min=1, max=100)])
    
    class Meta:
        csrf = False

class EditionEditLanguage(FlaskForm):
    language = StringField("Language: ", [validators.Length(min=3, max=50)])

    class Meta:
        csrf = False

class EditionEditRead(FlaskForm):
    read = BooleanField("I have read this book: ")

    class Meta:
        csrf = False

class EditionEditNotes(FlaskForm):
    notes = TextAreaField("Notes: ", [validators.Length(min=2, max=300)])

    class Meta:
        csrf = False

class EditionSelectWork(FlaskForm):
    work = SelectField("Select work: ", [validators.data_required()], choices=[], coerce=int)

    class Meta:
        csrf = False

class EditionSelectFormat(FlaskForm):
    format = SelectField("Select work: ", [validators.data_required()], choices=[], coerce=int)

    class Meta:
        csrf = False