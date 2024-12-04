from flask import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    name = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('send')
