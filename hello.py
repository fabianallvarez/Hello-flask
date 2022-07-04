from flask import Flask


app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/hola')
def hola():
    return "Hola, soy Flask, y tu, ¿Como te llamas?"

@app.route('/adios')
def otra():
    return "Hasta Luego"