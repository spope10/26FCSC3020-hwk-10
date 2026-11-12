'''
CSC3020 - Software Engineering Fundamentals
Instructor: Thyago Mota
Student: 
Description: Homework 10 - Blackbox Testing
'''

from app import app
from app.forms import InputForm
from flask import render_template, redirect, url_for
import math

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index(): 
    form = InputForm()
    if form.validate_on_submit(): 
        try: 
            a = form.a.data
            b = form.b.data
            try: 
                result = a / b 
                return redirect(url_for('display_result', result=result))
            except: 
                return f'<p>Denominator cannot be zero</p>'
        except Exception as ex: 
            print(ex)
    return render_template('index.html', form=form)

@app.route('/result/<result>', methods=['GET'])
def display_result(result: int):
    result = float(result)
    return f'<p>Result: {round(result, 2)}</p>'
    