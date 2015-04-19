from flask      import Flask, render_template
from sqlite3    import dbapi2 as database
from contextlib import closing

app = Flask(__name__)

############
#  Routes  #
############


@app.route("/")
def index():
    return "Hello, world!"

@app.route("/hello/<name>")
def hello(name):
    return "Hello, " + name + "!"

@app.route("/about")
def about():
    return render_template("about.html")


##############
#  Database  #
##############

def connect_db():
    return database.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    print('Initialized the database.')

################
#  App config  #
################

app.config.update(dict(
    DATABASE='database.sqlite3',
    DEBUG=True,
))
if __name__ == '__main__':
    app.run()
