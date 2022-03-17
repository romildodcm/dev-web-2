from flask import Flask, render_template, request
from manter.dao import DaoCliente, DaoProduto
from manter.entities import Cliente, Produto
# importando a variavel app do __init__.py
from . import app


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/save")
def save():
    # recebe os campos do formulario
    # criar o objeto cliente
    # chamar a classe que persiste no banco de dados
    # campos do formulario: nome, cpf, email
    # <form name='manter' ><input name='nome'>
    form = request.form.get('manter')
    form = form.to_dict()
    nome = form['nome']
    cpf = form['cpf']
    email = form['email']
    cliente = Cliente(nome, cpf, email)
    # salva no banco (sqlite)
    # Database.create(cliente)
    return "manter.html"


@app.route("/delete/<id>")
def delete(id):
    # # select from cliente where id = id
    # # consulta o banco, e recupera o cliente
    # cliente = Database.getCliente(id)
    # Database.delete(cliente.id)
    
    conn.execute("DELETE from STUDENT where ID = 2;")
    conn.commit()

    return "manter.html"


@app.route("/update")
def update():

    # # alem dos atributos eh necessario o ID
    # cliente = Database.find(id)
    # # atualiza os campos...
    # Database.update(cliente)
    return "manter.html"


@app.route("/cliente/findall")
def findallCliente():
    dao = DaoCliente()
    clientes = dao.findall()
    return render_template("manter.html", clientes=clientes)


@app.route("/produto/findall")
def findallProduto():
    dao = DaoProduto()
    produtos = dao.findall()
    return render_template("manter.html", clientes=produtos)
