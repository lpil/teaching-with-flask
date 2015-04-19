from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/hello/<name>")
def hello(name):
    return "Hello, " + name + "!"

@app.route("/about")
def about():
    return render_template("about.html")

app.debug = True
app.run()
