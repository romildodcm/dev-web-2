from http import client
from flask import Flask, render_template, request
from manter.entities import Cliente

from . import app


@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/new")
def new():
    # recebe os campos do formulario
    # cria o objeto cliente
    # chamar a classe que persiste no banco de dados
    # nome, cpf e email
    form = request.form.get('manter')  # <form nome><input name='nome'>
    form = form.to_dict()
    nome = form['nome']
    cpd = form['cpd']
    email = form['email']

    cliente = Cliente(nome, cpf, email)

    # salva no banco (sqlite)
    Database.create(cliente)
    return "manter.html"


@app.route("/delete")
def delete():
    # select from cliente where id == id
    # consulta o banco e recupera o cliente
    cliente = Database.getCliente(id)
    Database.delete(cliente.id)
    return "manter.html"


@app.route("/update")
def update():
    # dao = Data Acess Object ou persistence
    # alem dos atributos é necessário o ID
    cliente = Database.find(id)
    # atualiza os campos

    # salva
    Database.update(cliente)
    return "manter.html"


@app.route("/listall")
def listall():
    clientList = Database.findall()
    return "manter.html"
