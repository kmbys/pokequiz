pokequiz
====

A web application for quiz game.

## Demo

https://pokequiz-307002.an.r.appspot.com

## Requirements

- Python 3.7+ installed
- Pip and Pipenv installed

## Development

Clone this repository and setup the virtual environment.

```
git clone https://github.com/nsbt/pokequiz
cd pokequiz
pipenv install
pipenv run python main.py
```

Then access to http://localhost:8080 in your browser.

## Test

```
pipenv run python test.py
```

## Deployment

### Google App Engine

```
pipenv run pip freeze > requirements.txt
gcloud app deploy
```

### Heroku

Clone this repository to Heroku.
