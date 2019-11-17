# flask-login-boilerplate

Flask login boilerplate using bootstrap (**4.1.3**). Simple user authorization and authentication.

## Getting started

Clone:

```sh
HTTPS: https://github.com/endormi/flask-login-boilerplate.git SSH: git@github.com:endormi/flask-login-boilerplate.git
```

Install requirements:

```sh
pip install -r requirements.txt
```

My `config.py` file is ignored, so you'll have to add it manually.

Example of what to add:

```python
SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
SECRET_KEY = 'Your_Secret_Key'
```

You might need to set `FLASK_APP`.

> I advise you to rename this folder to project or app for example, in these examples I am using project.

Change directory:

```sh
cd..
```

For Windows `Command prompt`:

```sh
set FLASK_APP=project
set FLASK_ENV=development
```

For Windows `Powershell`:

```sh
$env:FLASK_APP = "project"
$env:FLASK_ENV = "development"
```

For Linux and Mac:

```sh
export FLASK_APP=project
export FLASK_ENV=development
```

You need the database, so in order to get it you need to open up `python shell` and add:

```python
from project import db, create_app
db.create_all(app=create_app())
```

Run:

```sh
flask run
```
