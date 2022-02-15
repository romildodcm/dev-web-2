from datetime import datetime
from flask import render_template, request
from flask import Flask
from random import randrange

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello/<name>")
def hello(name):
    today = datetime.now()
    data_local = today.strftime("%d/%m/%y - %H:%M:%S")
    return render_template("hello.html", name=name, today=data_local)

@app.route("/about")
def about():
    return render_template("about.html")

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


if __name__ == "__main__":
    app.run(debug=True)