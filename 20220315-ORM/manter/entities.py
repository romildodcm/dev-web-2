from tkinter.font import BOLD
from sqlalchemy import (Column, Integer, String, Boolean)
import site
from webapp import db

Base = db.Model

# dizemos ao ORM que essa classe deve ser mapeada par uma tabela


class Fornecedor(Base):
    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    cnpj = Column(Integer, nullable=False, unique=True)
    site = Column(String(120), nullable=True)
    pedidos = Column(Integer, default=0)
    # is_active = Column(Boolean, default=True) para deletar lógicamente

    def __repr__(self):
        return f"{self.id} | {self.nome} | {self.pedidos}"

# mapear objeto para o banco de dados:


class Cliente:
    def __init__(self, nome, cpf, email):
        """ init eh o construtor """
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir(self):
        print(self.nome, self.cpf, self.email)


if __name__ == '__main__':
    maria = Cliente("Maria", 939393, "test@org.com")
    julia = Cliente("Julia", 111111, "aaa@org.com")
    print(maria.cpf)
    maria.exibir()
    julia.exibir()
