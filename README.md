# Oxowlbot

An ontology chatbot which answers questions and learns from its interlocutor.

## [Try it now](http://oxowlbot.herokuapp.com/)

## What does it do?

It can answer the three following questions:

- Who is friend with Twilight Sparkle?
- Who is a kirin?
- Who is Fluttershy?

### Relationship query

#### is-rel-with-indiv variant

- Who is friend with Twilight Sparkle?
- Who is parent of Flurry Heart?
- Who is ascendent of Flurry Heart?
- Who is descendent of Twilight Velvet?
- Who is child of Twilight Velvet?
- Who is married with Twilight Velvet?

### Class query

- Who is a kirin?
- Who is an alicorn?
- Who is a dragon?

### All classes

Gender:

- Female
- Male

Specy:

- Alicorn
- Changeling
- Donkey
- Draconequus
- Dragon
- Earth Pony
- Griffon
- Hippogriff
- Kirin
- Pegasus
- Sea Serpent
- Siren
- Sphix Specy
- Unicorn
- Yak
- Zebra

The following two are parent classes. They are currently not correctly handeled:

- Pony
- Creature

### Individual

- Who is Fluttershy?

## Contributing

Oxowlbot uses Python 3.8.2. It can be installed using brew (`brew install python@3.8`) or using pyenv ([(1) install the dependencies](https://github.com/pyenv/pyenv/wiki#suggested-build-environment), [(2) install pyenv](https://github.com/pyenv/pyenv#the-automatic-installer), (3) run `pyenv install 3.8.2` and then `pyenv global 3.8.2`).

### Oxowlbot uses Poetry

1. Install the python package manager [Poetry](https://github.com/python-poetry/poetry) (also see [the full instructions in the doc](https://python-poetry.org/docs/#installation)). On Linux and OSX, use:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

2. Install the dependencies. Make sure you're at the root of this repository and run the following command:

```bash
poetry install
```

This will install all the dependencies listed in `pyproject.toml`, respecting the version specified in `poetry.lock`.

### Oxowlbot uses types (with pyright)

If you use VSCode, you can install pyright's extension.

### Getting started with Poetry

Poetry is quite similar to yarn and npm:

- To add a package to the project use `poetry add ...`
- Use `poetry add --dev ...` for a developer dependency (example: `selenium`)
- To run any CLI installed in the project use `poetry run ...`
  - To run `django-admin` use `poetry run django-admin`
  - To run python with the project dependencies available, use `poetry run python ...`. This applies both to running python files, and starting a python shell.
  - To run `manage.py`, use `poetry run python manage.py`
  - ALTERNATIVELY, you can use `poetry shell` to activate the virtual environment, and then freely run the CLIs installed in it: `django-admin ...`, `python manage.py ...`, etc.
