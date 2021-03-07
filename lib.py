# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from enum import Enum
import random
import json

class Stage:
    def __init__(self, value):
        if value is None:
            self.current = 1
            self.next = 2
            return

        if type(value) is not int:
            raise ValueError

        if value < 1:
            raise ValueError

        self.current = value
        self.next = value + 1

class Level(Enum):
    VERY_EASY = (0, "ベリーイージー", 151)
    EASY = (1, "イージー", 251)
    NORMAL = (2, "ノーマル", 386)
    HARD = (3, "ハード", 493)
    VERY_HARD = (4, "ベリーハード", 649)
    ULTRA_HARD = (5, "ウルトラハード", 807)

    def __init__(self, key, label, max_no):
        self.key = key
        self.label = label
        self.max_no = max_no

    @classmethod
    def from_key(self, key):
        if key == 0:
            return Level.VERY_EASY
        if key == 1:
            return Level.EASY
        if key == 2:
            return Level.NORMAL
        if key == 3:
            return Level.HARD
        if key == 4:
            return Level.VERY_HARD
        if key == 5:
            return Level.ULTRA_HARD
        raise ValueError

    def next(self):
        return Level.from_key(self.key + 1)

class Config:
    def __init__(self, level, stage):
        self.level = level
        self.stage = stage

    def can_levelup(self):
        if self.stage.current > 10 and self.level != Level.ULTRA_HARD:
            return True
        else:
            return False

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
