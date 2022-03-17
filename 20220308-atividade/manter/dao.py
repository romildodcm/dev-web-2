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
            (cliente.nome, cliente.cpf, cliente.email)
        )
        conn.commit()

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

    def find_by_id(self, id):  # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM cliente where id = ?",
            (id)
        )
        return res.fetchone()

    def find_by_nome(self, nome):  # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        # find = f"%{nome}%"
        res = conn.execute(
            "SELECT * FROM cliente WHERE nome =?",
            (nome,)
        )
        return res.fetchone()

    def findall(self):  # R
        # pegar da Database a conexao com o BD
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

    def save(self, produto):    # C
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO produto (nome, descricao, preco, quantidade)
            VALUES (?, ?, ?, ?)
            """,
            (produto.nome, produto.descricao, produto.preco, produto.quantidade)
        )
        conn.commit()

    def update(self, produto):  # U
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE produto SET nome = ?, descricao = ? , preco = ?, quantidade = ?
            WHERE id = ?
            """,
            (produto.nome, produto.descricao,
             produto.preco, produto.quantidade, produto.id)
        )
        conn.commit()

    def delete(self, id):  # D
        conn = Database.get_connection()
        conn.execute(
            f"""
            DELETE from produto
            WHERE id = ?    
            """, (id)
        )
        conn.commit()

    def find_by_id(self, id):  # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM produto where id = ?",
            (id)
        )
        return res.fetchone()

    def find_by_nome(self, nome):  # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        # find = f"%{nome}%"
        res = conn.execute(
            "SELECT * FROM produto WHERE nome =?",
            (nome,)
        )
        return res.fetchone()

    def findall(self):  # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM produto"
        )
        return res.fetchall()
