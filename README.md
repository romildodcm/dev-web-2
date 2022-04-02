<!-- Justifica o texto (em sistemas que suportam) -->
<!-- <style>body {text-align: justify}</style> -->
# DESENVOLVIMENTO WEB II
**2021.2 - IFPR Foz**

---
## Preparação do Ambiente
*Atividade assíncrona referente as aulas de 21 e 28/12/2021*

**Observação: os passos a seguir foram no sistema operacional Ubuntu**

Instalar, configurar e estudar as ferramentas a seguir:

### Python e Pip

Python é uma linguagem de programação de alto nível, usaremos ela nessa disciplina, para isso é necessário **instalar o interpretador** na máquina, no caso do **Ubuntu**, basta executar o comando a seguir:

`$ sudo apt-get install python3`

Para programar os sistemas dessa disciplina será necessária a instalação de pacotes ou bibliotecas de códigos, para isso usaremos o gerenciador de pacotes **Pip**, use o comando a seguir para instalar:

`$ sudo apt-get install python3-pip`

Foi instalado o *Python 3.9* e o *Pip 21.2*.

### Pycharm

Podemos escrever programas em Python até com o bloco de Notas, mas essa tarefa se torna complexa de gerenciar conforme o sistema vai crescendo, portanto usaremos **Pycharm**, uma IDE (ambiente integrado de desenvolvimento), que trás várias ferramentas para agilizar a programação. Comando para instalar:

`$ sudo apt-get install pycharm`

Foi instalada a versão *2021.3.1*.

### Git

A ferramente **Git** serve para controle e gerenciamento de versão de códigos dos sistemas que serão desenvolvidos, permitindo fazer um versionamento sem precisar ficar renomeando e copiando arquivos. Comando para instalar:

`$ sudo apt-get install git`

Foi instalada a versão *2.35.0*.

### SQLite

Nos projetos precisaremos de um banco de dados, o mais simples e prático para começar a praticar SQL é o SQLite, que consiste de uma biblioteca em C que implementa um banco de dados SQL em arquivo, os programas em Python poderão acessar o banco de dados sem a necessidade de executar um SGBD (sistema gerenciador de banco de dados). Comando para instalar:

`$ sudo apt-get install sqlite3`

Foi instalada a versão *3.31.1*.

### SQLite Browser

Essa ferramenta serve facilitar o acesso ao banco de dados, oferecendo interface gráfica onde o usuário pode criar, projetar e editar arquivos de banco de dados SQLite. Comando para instalar:

`$ sudo apt-get install sqlitebrowser`

Foi instalada a versão *3.12.2*.
