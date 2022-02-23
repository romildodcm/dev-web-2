# mapear objeto para o banco de dados:
class Cliente:
    def __init__(self, nome, cpf, email):
        """ init eh o construtor """
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir(self):
        print(self.nome, self.cpf, self.email)


class Produto:
    def __init__(self, nome, descricao, preco, quantidade) -> None:
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def exibir(self):
        print(self.nome, self.descricao, self.preco, self.quantidade)


if __name__ == '__main__':
    maria = Cliente("Maria", 939393, "test@org.com")
    julia = Cliente("Julia", 111111, "aaa@org.com")
    print(maria.cpf)
    maria.exibir()
    julia.exibir()

    smartphone = Produto("Samsung S22", "Smartphone topo de linha.", 1060, 20)
    notebook = Produto("Notebook Acer", "i17 G12 16GB 500TB.", 998, 300)
    print(notebook.nome)
    smartphone.exibir()
    notebook.exibir()
