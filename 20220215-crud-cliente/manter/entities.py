# Mapear objeto para banco de dados
class CarrinhoCompras:
    pass

class Cliente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir(self):
        print(self.nome, self.cpf, self.email)

if __name__ == '__main__':
    maria = Cliente("Maria", "52445298785", "teste@test.com")
    luiz = Cliente("Luiz", "52445298785", "luiz@test.com")
    maria.exibir()
    luiz.exibir()
    print(maria.cpf)