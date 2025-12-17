# sitn-django-plugins

This repository has two goals:

* demo how to use a sitn django plugins within this a basic Django app
* provide a sandbox to develop new custom plugins

## Requirements

* Postgis
* poetry (pip install poetry)
* poetry Shell plugin (poetry self add poetry-plugin-shell)
* Poetry Dotenv Plugin (poetry self add poetry-dotenv-plugin)

## Getting started

1. Create a local postgis database 

```sql
CREATE DATABASE sitn;
CREATE EXTENSION postgis;
CREATE SCHEMA sitn;
```

2. Fill your `.env` accordingly. A `.env.sample` is provided to help you.

3. Install you app and activate venv:

```powershell
poetry install
poetry shell
```

4. Migrate and run your app

```shell
python manage.py migrate
python manage.py runserver
```

## Start developing

The django app is now running the plugins installed from pypi.org. If you want it to run directly from the sub-directory, it is possible. This way you don't have to compile your package and install it to test your dev.

Let's say you want to start developing a new feature on django-extended-ol. Run this in your poetry shell activated:

```shell
poetry remove django-extended-ol
cd django-extended-ol
python -m pip install --editable .
cd ..
python manage.py runserver
```

With `python -m pip install --editable .` we install a live-reloaded version of the plugin that we will need to uninstall later.

At the end of the development, don't forget to revert back:

```shell
cd django-extended-ol
python -m pip uninstall django-extended-ol
cd ..
poetry add django-extended-ol
```

# Build and publish

1. Don't forget to update README.md of your package and increment the version number in the pyproject.toml.

2. Build your package, for example for `django-extended-ol`:

```shell
cd django-extended-ol
python -m build
```

If necessary, delete old built versions in `dist` folder.

3. Publish it to pypi.org 

```shell
python -m twine upload dist/*
```
