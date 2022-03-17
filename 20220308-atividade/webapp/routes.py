from flask import (
    Flask, render_template, request, redirect
)
from manter.database import Database
from manter.entities import Cliente, Produto
from manter.dao import DaoCliente, DaoProduto
from . import app


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/cliente/add")
def cliente_add():
    return render_template('cadastro-cliente.html', cliente=None)


@app.route("/cliente/edit/<id>")
def cliente_edit(id):
    # buscar na dao o cliente
    # find_by_id(id) - recupera 1 cliente
    dao = DaoCliente()
    cliente = dao.find_by_id(id)
    return render_template(
        'cadastro-cliente.html',
        cliente=cliente
    )


@app.route("/save", methods=["POST"])
def save():
    # recebe os campos do formulario
    # criar o objeto cliente
    # chamar a dao que salva no banco de dados
    id = request.form.get("id")
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    email = request.form.get("email")
    cliente = Cliente(nome, cpf, email)
    dao = DaoCliente()
    if id:
        cliente.id = id
        dao.update(cliente)
    else:
        dao.save(cliente)
    return findall()


@app.route("/delete/<id>")
def delete(id):
    dao = DaoCliente()
    dao.delete(id)
    # return findall()
    return redirect("/cliente/findall/")


@app.route('/restore')
def restore():
    Database.create_db()
    return redirect("/cliente/findall")


@app.route("/cliente/findall/")
def findall():
    dao = DaoCliente()
    clientes = dao.findall()
    return render_template("manter-cliente.html", clientes=clientes)


@app.route("/cliente/findbyname/", methods=["POST"])
def cliente_findbyname():
    nome = request.form.get("nome")
    print(nome)

    dao = DaoCliente()
    cliente = dao.find_by_nome(nome)

    print(str(cliente))

    return render_template("findbyname-cliente.html", cliente=cliente)


@app.route("/produto/add")
def produto_add():
    return render_template('cadastro-produto.html', produto=None)


@app.route("/produto/edit/<id>")
def produto_edit(id):
    # buscar na dao o produto
    # find_by_id(id) - recupera 1 produto
    dao = DaoProduto()
    produto = dao.find_by_id(id)
    return render_template(
        'cadastro-produto.html',
        produto=produto
    )


@app.route("/produto/save", methods=["POST"])
def produto_save():
    # recebe os campos do formulario
    # criar o objeto cliente
    # chamar a dao que salva no banco de dados
    id = request.form.get("id")
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    preco = float(request.form.get("preco"))
    quantidade = int(request.form.get("quantidade"))
    produto = Produto(nome, descricao, preco, quantidade)
    dao = DaoProduto()
    if id:
        produto.id = id
        dao.update(produto)
    else:
        dao.save(produto)
    return produto_findall()


@app.route("/produto/delete/<id>")
def produto_delete(id):
    dao = DaoProduto()
    dao.delete(id)
    # return findall()
    return redirect("/produto/findall/")


@app.route("/produto/findall/")
def produto_findall():
    dao = DaoProduto()
    produtos = dao.findall()
    return render_template("manter-produto.html", produtos=produtos)


@app.route("/produto/findbyname/", methods=["POST"])
def produto_findbyname():
    nome = request.form.get("nome")
    print(nome)
    dao = DaoProduto()
    produto = dao.find_by_nome(nome)
    print(str(produto))
    return render_template("findbyname-produto.html", produto=produto)
