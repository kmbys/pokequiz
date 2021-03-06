# -*- coding: utf-8 -*-
from flask import Flask, render_template
from lib import Quiz, get_from_zukan, get_distinct_random_nums

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.j2',
        message="第1問",
        quiz=Quiz([get_from_zukan(num) for num in get_distinct_random_nums(151, 4)])
    )

if __name__ == '__main__':
    app.run()
