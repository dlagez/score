from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, '../data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# scores = [
#     {'name': 'zp', 'id': '123', 'score': '100'}
# ]


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20))
    name = db.Column(db.String(20))
    score = db.Column(db.String(20))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
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


@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html'), 404  # 返回模板和状态码


@app.errorhandler(500)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('500.html'), 500  # 返回模板和状态码


if __name__ == '__main__':
    app.run(debug=True)