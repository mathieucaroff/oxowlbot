# Oxowlbot

An ontology chatbot which answers questions and learns from its interlocutor.

## [Try it now](http://oxowlbot.oxie.cc/)

## Contributing

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