DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS produto;
CREATE TABLE cliente(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    cpf text NOT NULL,
    email text NOT NULL,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO cliente(nome, cpf, email)
VALUES ('admin', '1002000', 'admin@test.org'),
    (
        "Maria Silver",
        "949.282.111-82",
        "mariam@test.org"
    ),
    (
        "Jairo Carlile",
        "144.217.577-11",
        "carlile@test.org"
    ),
    (
        "Marcos Oliva",
        "433.144.644-52",
        "marcos@test.org"
    );
CREATE TABLE produto(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    descricao text NOT NULL,
    preco real NOT NULL,
    quantidade integer DEFAULT 0,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO produto (nome, descricao, preco, quantidade)
VALUES (
        'RTL-SDR v3 dongle',
        'Receptor via software de 500 KHz a 1.7 GHz.',
        150.50,
        20
    ),
    (
        'Lime SDR Mini',
        'Transceptor via software.',
        1500.20,
        5
    ),
    (
        'Hackrf one sdr',
        'Transceptor via software 1 MHz a 6 GHz',
        620.50,
        12
    );