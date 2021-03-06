# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, escape
from lib import Stage, Quiz

app = Flask(__name__)

@app.route('/')
def index():
    stage = None
    try:
        stage = Stage(escape(request.args.get("stage")))
    except ValueError:
        return "予期しないリクエストを受けました", 400
    return render_template(
        'index.j2',
        stage=stage.value,
        quiz=Quiz(151, 4)
    )

if __name__ == '__main__':
    app.run()
