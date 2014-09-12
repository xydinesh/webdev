from datetime import datetime
from flask import render_template
from FlaskWebTemplate import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title = 'Home Page',
        year = datetime.now().year,
        page = '/static/index.html'
    )


@app.route('/project/01')
def project01():
    return render_template(
        'index.html',
        title = 'Project 01',
        page = '/static/project_1.html',
        year = datetime.now().year
        )


