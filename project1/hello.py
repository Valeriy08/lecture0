from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    headline = "Hello world!"
    names = ["Val", "Bob", "Dave"]
    return render_template("index.html", headline=headline, names=names)

@app.route("/<string:name>")
def hello(name):
    name=name.capitalize()
    return f"Hello, {name}"
