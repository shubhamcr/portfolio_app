from flask import render_template
from .portfolio import app
from portfolio import profile


@app.route('/')
def index():
    return render_template('index.html', skills = profile.get_skills())