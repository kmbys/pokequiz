# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, escape
from lib import Quiz

app = Flask(__name__)

@app.route('/')
def index():
    stage = escape(request.args.get("stage"))
    return render_template(
        'index.j2',
        stage=1 if stage is None else stage,
        quiz=Quiz(151, 4)
    )

if __name__ == '__main__':
    app.run()
