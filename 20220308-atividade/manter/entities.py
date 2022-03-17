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
    def __init__(self, nome, descricao, preco, quantidade):
        """ init eh o construtor """
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

    kerberos = Produto("Kerberos sdr", "4 canais de recepção simultânea, radar passivo, formação de feixe.", 1300.50, 16)
    sw_receptor = Produto("Receptor SW", "Receptor de rádio de banda si4732", 350.10, 50)
    kerberos.exibir();
    sw_receptor.exibir()

