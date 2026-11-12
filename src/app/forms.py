'''
CSC3020 - Software Engineering Fundamentals
Instructor: Thyago Mota
Student: 
Description: Homework 10 - Blackbox Testing
'''

from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import InputRequired

class InputForm(FlaskForm):
    a = IntegerField('a', validators=[InputRequired()])
    b = IntegerField('b', validators=[InputRequired()])
    submit = SubmitField('=')