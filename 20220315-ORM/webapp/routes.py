from flask import (
    Flask, render_template, request, redirect
)
from manter.database import Database
from manter.entities import Fornecedor
from manter.entities import Cliente
from manter.dao import DaoCliente
# importando a variavel app do __init__.py
from . import app
from . import db  # SQLAlchemy vem do __initi__.py


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/cliente/add")
def cliente_add():
    return render_template('cadastro_cliente.html', cliente=None)


@app.route("/cliente/edit/<id>")
def cliente_edit(id):
    # buscar na dao o cliente
    # find_by_id(id) - recupera 1 cliente
    dao = DaoCliente()
    cliente = dao.find_by_id(id)
    return render_template(
        'cadastro_cliente.html',
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


@app.route('/createdb')
def createdb():
    db.drop_all # apagar todos os dados (cuidado!)
    db.create_all()
    # Cria um objeto
    f1 = Fornecedor(nome="Empresa test SA", cnpj=195929, site="www", pedidos=28)

    db.session.add(f1)  # INSERT
    db.session.commit()  # Realiza a operação

    return "ok database criada!"


@app.route('/fornecedor/list')
def fornecedor_list():
    query = Fornecedor.query.all()
    return f"{query}"

@app.route("/fornecedor/delete/<id>")
def fornecedor_delete(id):
    # Equivalente a select from fornecedor whre id = id
    fn = Fornecedor.query.get(id)
    # delete
    db.session.delete(fn)
    # persiste
    db.session.commit()
    return f"Ok, fornecedor id = {id} foi removido com sucesso!"

# TODO: redirecionar para fornecedor/findall

# Select para achar um por nome
# select from Fornecedor whre nome == "Empresa SA" limit 1
# fn = Fornecedor.query.filter_by(nome = "Empresa SA").first() # Esse apresenta apenas o primeiro resultado
# fn = Fornecedor.query.filter_by(cnpj=1999)

# Pesquisa com mais condições
# Lista de fornecedores temrinados em "SA" sem ordenação
# lista = Fornecedor.query.filter(
#     Fornecedor.nome.endswith("SA")
# ).all()

# Lista de fornecedores ordenados por numeros de pedidos
# lista = Fornecedor.query.filter_by(
#     Fornecedor.nome.endswith("SA")
# )..order_by(Fornecedor.pedidos.desc())

# TODO: fornecedor_save() (basicamente o create db + receber de um form, igual no cliente)
# TODO: get_fornecedor(id) passa um id e recebe o fornecedor, a linha fn = Fornecedor.query.get(id) do delete

# Descobrir os fornecedores com pedidos maior que 100
# list = Fornecedor.query.filter_by(pedidos=100)

@app.route("/update")
def update():
    # alem dos atributos eh necessario o ID
    # cliente = Database.find(id)
    # atualiza os campos...
    # Database.update(cliente)
    return "manter.html"


@app.route("/cliente/findall/")
def findall():
    dao = DaoCliente()
    clientes = dao.findall()
    return render_template("manter.html", clientes=clientes)
