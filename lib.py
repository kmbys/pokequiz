# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import json

class Stage:
    def __init__(self, value):
        if int(value) < 1:
            raise ValueError
        self.value = 1 if value is None else value

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
    def __init__(self, range_, size):
        pokemons = [get_from_zukan(num) for num in get_distinct_random_nums(range_, size)]

        options = [Option(pokemons[0], True)]
        for i in range(1, len(pokemons)):
            options.append(Option(pokemons[i], False))
        random.shuffle(options)

        self.options = options
        self.question = pokemons[0].description
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
