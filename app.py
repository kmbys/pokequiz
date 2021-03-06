# -*- coding: utf-8 -*-
from flask import Flask, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import json

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

def get_from_zukan(no):
    p = json.loads(
        BeautifulSoup(
            urlopen("https://zukan.pokemon.co.jp/detail/{}".format(no)).read(),
            'html.parser'
        ).select_one("#json-data").contents[0]
    )["pokemon"]
    return Pokemon(p["name"], p["text_1"], p["image_s"])

def get_distinct_random_nums(range_, size):
    return random.sample(range(1, range_ + 1), size)

@app.route('/')
def index():
    return render_template(
        'index.j2',
        message="第1問",
        quiz=Quiz([
            get_from_zukan("010"),
            get_from_zukan("004"),
            get_from_zukan("007"),
            get_from_zukan("001")
        ])
    )

if __name__ == '__main__':
    app.run()
