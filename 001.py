from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/hello/<name>")
def hello(name):
    return "Hello, " + name + "!"

app.debug = True
app.run()
