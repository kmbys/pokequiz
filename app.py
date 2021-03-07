# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, escape
from lib import Stage, Quiz

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('get_quiz', stage="1"))

@app.route('/<stage>')
def get_quiz(stage):
    stage_obj = None
    try:
        stage_obj = Stage(stage)
    except ValueError:
        return "予期しないリクエストを受けました", 400

    return render_template(
        'index.j2',
        stage=stage_obj,
        quiz=Quiz(151, 4)
    )

if __name__ == '__main__':
    app.run()
