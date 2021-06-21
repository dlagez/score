# Author : roczhang
# date :   2021/6/21

from query import db


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20))
    name = db.Column(db.String(20))
    score = db.Column(db.String(20))