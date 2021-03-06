# -*- coding: utf-8 -*-
from flask import Flask, render_template
from lib import Quiz

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.j2',
        message="第1問",
        quiz=Quiz(151, 4)
    )

if __name__ == '__main__':
    app.run()
