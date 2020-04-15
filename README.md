# Oxowlbot

An ontology chatbot which answers questions and learns from its interlocutor.

## What does it do?

It can answer the three following questions:

- Who is friend with Twilight Sparkle?
- Who is a kirin?
- Who is Fluttershy?

## What does it do? (advanced features)

### Relationship query

#### are-indiv-rel variant

- Who are Twilight Sparkle's friends?
- Who are Flurry Heart's parents?
- Who are Flurry Heart's ascendents?
- Who are Twilight Velvet's descendents?
- Who are Twilight Velvet's children?

#### is-rel-with-indiv variant

- Who is friend with Twilight Sparkle?
- Who is parent of Flurry Heart?
- Who is ascendent of Flurry Heart?
- Who is descendent of Twilight Velvet?
- Who is child of Twilight Velvet?
- Who is married with Twilight Velvet?

### Relationship multi-level queries

#### is-(rel-of)+- variant

- Who is friend of a friend of Twilight Sparkle?
- Who is child of a child of a child of Twilight Velvet?

Additionally, queries for siblings, for sisters and for brothers are detected. The following equivalences apply:

- Who is sibling of Twilight Sparkle? -> Who is child of a parent of Twilight Sparkle?
- Who is brother with Twilight Sparkel? -> Who is male child of a parent of Twilight Sparkle?
- Who is sister with Twilight Sparkel? -> Who is female child of a parent of Twilight Sparkle?
- Who is son of Twilight Velvet? -> Who is male child of Twilight Velvet?
- Who is daugther of Twilight Velvet? -> Who is female child of Twilight Velvet?
- Who is grand-child of Twilight Velvet? -> Who is child of a child of Twilight Velvet?

####

### All available relationships

- ascendant_of <> descendant_of
- parent_of <> child_of
- friend_with <> ~
- lover_of <> ~
- married_with <> ~
- in_love_with <> loved_by

### Class query

#### who-is variant

- Who is a kirin?

#### are-there variant

- Are there kirins?

### Individual

#### what-do-you-know-about-x variant

- What do you know about Fluttershy?

#### who-is-x variant

- Who is Fluttershy?

## [Try it now](http://oxowlbot.oxie.cc/)

## Contributing

Oxowlbot uses Python 3.8.2. It can be installed using brew (`brew install python@3.8`) or using pyenv ([(1) install the dependencies](https://github.com/pyenv/pyenv/wiki#suggested-build-environment), [(2) install pyenv](https://github.com/pyenv/pyenv#the-automatic-installer), (3) run `pyenv install 3.8.2` and then `pyenv global 3.8.2`).

### Oxowlbot uses Poetry

1) Install the python package manager [Poetry](https://github.com/python-poetry/poetry) (also see [the full instructions in the doc](https://python-poetry.org/docs/#installation)). On Linux and OSX, use:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

2) Install the dependencies. Make sure you're at the root of this repository and run the following command:

```bash
poetry install
```

This will install all the dependencies listed in `pyproject.toml`, respecting the version specified in `poetry.lock`.

### Getting started with Poetry

Poetry is quite similar to yarn and npm:

- To add a package to the project use `poetry add ...`
- Use `poetry add --dev ...` for a developer dependency (example: `selenium`)
- To run any CLI installed in the project use `poetry run ...`
    - To run `django-admin` use `poetry run django-admin`
    - To run python with the project dependencies available, use `poetry run python ...`. This applies both to running python files, and starting a python shell.
    - To run `manage.py`, use `poetry run python manage.py`