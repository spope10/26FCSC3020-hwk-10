'''
CSC3020 - Software Engineering Fundamentals
Instructor: Thyago Mota
Student: 
Description: Homework 10 - Blackbox Testing
'''

from flask import Flask

app = Flask("Blackbox Testing Web App")
#app.secret_key = os.environ['SECRET_KEY']
app.secret_key = 'you will never guess'

from app import routes