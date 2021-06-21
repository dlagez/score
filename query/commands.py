# Author : roczhang
# date :   2021/6/21
import click

from query import app, db
from query.models import Score

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
def forge():
    db.create_all()

    scores = [
        {'number': '123', 'name': 'zp', 'score': '100'}
    ]

    for s in scores:
        score = Score(number=s['number'], name=s['name'], score=s['score'])
        db.session.add(score)
    db.session.commit()
    click.echo('Done.')
