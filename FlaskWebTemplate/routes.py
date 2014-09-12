from datetime import datetime
from flask import render_template
from FlaskWebTemplate import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title = 'Home Page',
        page = '/internal/home',
        height = '800px',
        year = datetime.now().year
    )


@app.route('/project/01')
def project01():
    return render_template(
        'index.html',
        title = 'Project 01',
        page = '/internal/project/01',
        height = '1600px',
        year = datetime.now().year
        )

@app.route('/project/02')
def project02():
    return render_template(
        'index.html',
        title = 'Project 02',
        page = '/internal/project/02',
        height = '1600px',
        year = datetime.now().year
        )

@app.route('/internal/home')
def in_home():
    return render_template('home.html')

@app.route('/internal/project/01')
def in_project01():
    return render_template('project/1.html')

@app.route('/internal/project/02')
def in_project02():
    return render_template('project/2.html')


