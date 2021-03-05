# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

class Pokemon:
    def __init__(self, name, description, image_uri):
        self.name = name
        self.description = description
        self.image_uri = image_uri

class Quiz:
    def __init__(self, pokemons):        
        self.question = pokemons[0].description
        self.options = [
            {"name": pokemons[0].name, "class_name": "correct_option"},
            {"name": pokemons[1].name, "class_name": "wrong_option"},
            {"name": pokemons[2].name, "class_name": "wrong_option"},
            {"name": pokemons[3].name, "class_name": "wrong_option"}
        ]
        self.answer_name = pokemons[0].name
        self.answer_image = pokemons[0].image_uri

@app.route('/')
def index():
    quiz = Quiz([
        Pokemon(
            "フシギダネ",
            "うまれたときから　せなかに　しょくぶつの　タネが　あって　すこしずつ　おおきく　そだつ。　（『ポケモン ソード』より）",
            "https://zukan.pokemon.co.jp/zukan-api/up/images/index/7b705082db2e24dd4ba25166dac84e0a.png"
        ),
        Pokemon("ゼニガメ", "図鑑1", "https://example.com/image1.png"),
        Pokemon("ヒトカゲ", "図鑑2", "https://example.com/image2.png"),
        Pokemon("ピカチュウ", "図鑑3", "https://example.com/image3.png")
    ])
    return render_template(
        'index.j2',
        message="第1問",
        quiz=quiz
    )

if __name__ == '__main__':
    app.run()
