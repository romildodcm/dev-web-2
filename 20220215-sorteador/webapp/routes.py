from flask import Flask, render_template, request

from datetime import datetime
from random import randrange

from . import app

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/gerar")
def gerar():
    # onde vamos gerar os numeros
    # mudar de list para set
    num = [11, 25, 34, 42, 51, 60]
    for c in range(0, 6):
        num[c] = randrange(1,60)


    # retorna os numeros para a view, usaremos a prórpia index
    return render_template("index.html", numeros = num)

# http://127.0.0.1:5000/imc?peso=77&altura=1.65
@app.route("/imc")
def imc():
    peso = float(request.args.get("peso"))
    altura = float(request.args.get("altura"))

    print(f"Peso: {peso} / Altura: {altura}")

    imc_calc = peso/(altura*altura)

    if imc_calc >=


    return f"Seu imc é: {imc_calc}"
    # return render_template("imc.html", imc = imc_calc)


