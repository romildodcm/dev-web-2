from manter.database import Database

class DaoCliente:
    """
    dao == Data Access Object ou persistence
    Implementa operacoes "CRUD"
        - Create
        - Read
        - Update
        - Delete
    """
    def save(self, cliente):    # C
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO cliente (nome, cpf, email )
            VALUES (?, ?, ?)
            """,
            ( cliente.nome, cliente.cpf, cliente.email )
        )
        conn.commit()

    def find(self):    # R
        pass
    def update(self, cliente):  # U
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE cliente SET nome = ?, cpf = ? , email = ?
            WHERE id = ?
            """,
            (cliente.nome, cliente.cpf, cliente.email, cliente.id)
        )
        conn.commit()

    def delete(self, id):  # D
        conn = Database.get_connection()
        conn.execute(
            f"""
            DELETE from cliente
            WHERE id = ?    
            """, (id)
        )
        conn.commit()

    def find_by_id(self, id): # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM cliente where id = ?",
            (id)
        )
        return res.fetchone()

    def findall(self): # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM cliente"
        )
        return res.fetchall()
