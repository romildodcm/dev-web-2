from manter.database import Database

# class Database:
#     # obtem uma conexao com o SQLite
#     pass

class DaoCliente:
    """
    dao == Data Access Object ou persistence
    Implementa operacoes "CRUD"
        - Create
        - Read
        - Update
        - Delete
    """
    def save(self):    # C
        pass
    def find(self):    # R
        pass
    def update(self):  # U
        pass
    def delete(self):  # D
        pass
    def findall(self): # R
        # Buscar todos os clientes cadastrados no banco de dados
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM cliente"
        )
        return res.fetchall()

class DaoProduto:
    """
    dao == Data Access Object ou persistence
    Implementa operacoes "CRUD"
        - Create
        - Read
        - Update
        - Delete
    """
    def save(self):    # C
        pass
    def find(self):    # R
        pass
    def update(self):  # U
        pass
    def delete(self):  # D
        pass
    def findall(self): # R
        # Buscar todos os clientes cadastrados no banco de dados
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM produto"
        )
        return res.fetchall()

