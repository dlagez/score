# Author : roczhang
# date :   2021/6/21
from flask import render_template, request, redirect

from query import app,db
from query.models import Score

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query', methods=['GET', 'POST'])
def query():
    name = str(request.form.get('name'))
    number = str(request.form.get('number'))
    print(name, number)
    score = Score.query.filter_by(name=name, number=number).first()
    # score = db.execute(
    #     'select * from score where name = ? and number = ?', (name, number)
    # ).fetchone()
    #
    # print(score.name)
    return render_template('result.html', score=score)