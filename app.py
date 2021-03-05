# -*- coding: utf-8 -*-
from flask import Flask, render_template
import random

app = Flask(__name__)

class Pokemon:
    def __init__(self, name, description, image_uri):
        self.name = name
        self.description = description
        self.image_uri = image_uri

class Option:
    def __init__(self, pokemon, is_correct):
        self.name = pokemon.name
        self.class_name = "correct_option" if is_correct else "wrong_option"

class Quiz:
    def __init__(self, pokemons):        
        self.question = pokemons[0].description
        options = [Option(pokemons[0], True)]
        for i in range(1, len(pokemons)):
            options.append(Option(pokemons[i], False))
        random.shuffle(options)
        self.options = options
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
