from flask import Flask, render_template
app = Flask(__name__)

from application import views

class Item:
    def __init__(self, name):
        self.name = name

nimi = "Essi Esimerkki"

lista = [1, 1, 2, 3, 5, 8, 11]

esineet = []
esineet.append(Item("Eka"))
esineet.append(Item("Toka"))
esineet.append(Item("Kolmas"))
esineet.append(Item("Neljäs"))
