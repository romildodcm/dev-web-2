DROP TABLE IF EXISTS cliente;

CREATE TABLE cliente(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    cpf text NOT NULL,
    email text NOT NULL,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO cliente (nome, cpf, email)
VALUES
    ('admin', '1002000', 'admin@test.org'),
    ("Maria Silver", "949.282.111-82", "mariam@test.org"),
    ("Jairo Carlile", "144.217.577-11", "carlile@test.org"),
    ("Marcos Oliva", "433.144.644-52", "marcos@test.org");

CREATE TABLE produto(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    descricao text NOT NULL,
    preco float NOT NULL,
    quantidade integer NOT NULL
);

INSERT INTO produto (nome, descricao, preco, quantidade)
VALUES
    ("Relógio XIAOMI", "Brilha no escuro e faz até café.", 380, 480),
    ("Mi band", "Chronometra seu sono.", 120, 540),
    ("Samsung S22", "Smartphone topo de linha.", 1060, 20),
    ("Notebook Acer", "i17 G12 16GB 500TB.", 998, 300);
