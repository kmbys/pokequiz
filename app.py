# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

class Pokemon:
    def __init__(self, name, description, image_uri):
        self._name = name
        self._description = description
        self._image_uri = image_uri

class Quiz:
    def __init__(self):
        self.question = "うまれたときから　せなかに　しょくぶつの　タネが　あって　すこしずつ　おおきく　そだつ。　（『ポケモン ソード』より）"
        self.options = [
            {"name": "フシギダネ", "class_name": "correct_option"},
            {"name": "ゼニガメ", "class_name": "wrong_option"},
            {"name": "ヒトカゲ", "class_name": "wrong_option"},
            {"name": "ピカチュウ", "class_name": "wrong_option"}
        ]
        self.answer_name = "フシギダネ"
        self.answer_image = "https://zukan.pokemon.co.jp/zukan-api/up/images/index/7b705082db2e24dd4ba25166dac84e0a.png"

@app.route('/')
def index():
    return render_template(
        'index.j2',
        message="第1問",
        quiz=Quiz()
    )

if __name__ == '__main__':
    app.run()
