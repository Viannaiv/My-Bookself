from flask import render_template
from application import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)