# Database Setup

A database is where we keep our data. It's made up of tables, each of which has
columns and rows. It's like a spreadsheet, only our programs can read from it.

We probably want one of these.

## Method

First, create a schema in the project directory (See schema.sql). A schema is a
description of the shape of our data in the database.

Then add the DATABASE value to your application config.

```python
app.config.update(dict(
    DATABASE='database.sqlite3',
    DEBUG=True,
))
```

Create a function to connect to the DB.

```python
def connect_db():
    return database.connect(app.config['DATABASE'])
```

Another that initializes the DB with the schema.

```python
def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
        db.commit()
    print('Initialized the database.')
```

In order to run this, make a new file called "setup_database.py", write the
following in it.

```python
from app import init_db
init_db()
```

...And then run that file with `python setup_database.py`.

Boom! We've got a database

Don't forget to add `*.sqlite3` to your .gitignore. We don't want the database
in the repo!
