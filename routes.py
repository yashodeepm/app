from flask import render_template
from app import app
import subprocess
subprocess.call(['python','test.py'])
@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Yasho","title":"dius"}
    posts = [
        {
            "author":{"username":'Jawandhiya'},
            "body":"yoooooo"
        },
        {
            "author":{"username":'Ruchika'},
            "body":"hgdafsda"
        }

    ]
    return render_template('index.html', user = user, posts = posts)
