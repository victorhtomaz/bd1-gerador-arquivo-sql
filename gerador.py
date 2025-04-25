from os.path import ismount
import random
from faker import Faker
import pandas as pd
import os

fake = Faker()

q_cliente = int(input('Digite a quantidade de clientes para gerar: '))
q_produtos = int(input('Digite a quantidade de produtos para gerar: '))
q_pedidos = int(input('Digite a quantidade de pedidos para gerar: '))
q_itens_pedidos = int(input('Digite a quantidade de itens de um pedido para gerar: '))

clientes = []
for i in range(q_cliente):
    clientes.append({
        'nome': fake.name(),
        'email': fake.email(),
        'telefone': fake.phone_number(),
        'endereco': fake.address().replace("\n", ", ")
    })

produtos = []
for i in range(q_produtos):
    produtos.append({
        'nome': fake.word().capitalize(),
        'descricao': fake.sentence(),
        'preco': round(random.uniform(10.0, 500.0), 2),
        'estoque': random.randint(0, 100)
    })

pedidos = []
for i in range(q_pedidos):
    pedidos.append({
        'cliente_id': random.randint(1, q_cliente),
        'data_pedido': fake.date_time_this_year(),
        'status': random.choice(['Pendente', 'Enviado', 'Entregue', 'Cancelado'])
    })

itens_pedido = []
for i in range(q_itens_pedidos):
    itens_pedido.append({
        'pedido_id': random.randint(1, q_pedidos),
        'produto_id': random.randint(1, q_produtos),
        'quantidade': random.randint(1, 5),
        'preco_unitario': round(random.uniform(10.0, 500.0), 2)
    })

df_clientes = pd.DataFrame(clientes)
df_produtos = pd.DataFrame(produtos)
df_pedidos = pd.DataFrame(pedidos)
df_itens_pedido = pd.DataFrame(itens_pedido)

file = open("lojaimport.sql", "w")
file.write('CREATE DATABASE IF NOT EXISTS Loja; \n')
file.write('USE Loja; \n')
file.write('\n')
file.write('''CREATE TABLE IF NOT EXISTS Clientes(
    Cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(80) NOT NULL,
    Email VARCHAR(150) NOT NULL,
    Telefone VARCHAR(50) NOT NULL,
    Endereco TEXT NOT NULL
);\n''')

file.write('INSERT INTO Clientes (Nome, Email, Telefone, Endereco) VALUES\n')
for  index, cliente in enumerate(clientes):
    file.write(f"\t('{cliente['nome']}', '{cliente['email']}', '{cliente['telefone']}', '{cliente['endereco']}')")
    if index + 1 < q_cliente :
        file.write(',\n')
    else:
        file.write(';\n')

file.write('\n')
   
file.write('''CREATE TABLE IF NOT EXISTS Produtos(
    Produto_id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao TEXT NOT NULL,
    Preco FLOAT NOT NULL,
    Estoque INT NOT NULL
);\n''')

file.write('INSERT INTO Produtos (Nome, Descricao, Preco, Estoque) VALUES\n')
for  index, produtos in enumerate(produtos):
    file.write(f"\t('{produtos['nome']}', '{produtos['descricao']}', {produtos['preco']}, {produtos['estoque']})")
    if index + 1 < q_produtos :
        file.write(',\n')
    else:
        file.write(';\n')


file.write('\n')

file.write('''CREATE TABLE IF NOT EXISTS Pedidos(
    Pedido_id INT AUTO_INCREMENT PRIMARY KEY,
    Cliente_id INT NOT NULL,
    Data_pedido DATETIME NOT NULL,
    Status VARCHAR(20) NOT NULL,
    FOREIGN KEY (Cliente_id) REFERENCES Clientes(Cliente_id)
);\n''')

file.write('INSERT INTO Pedidos (Cliente_id, Data_pedido, Status) VALUES\n')
for  index, pedidos in enumerate(pedidos):
    file.write(f"\t({pedidos['cliente_id']}, '{pedidos['data_pedido']}', '{pedidos['status']}')")
    if index + 1 < q_pedidos :
        file.write(',\n')
    else:
        file.write(';\n')

file.write('\n')

file.write('''CREATE TABLE IF NOT EXISTS Itens_Pedidos(
    Item_id INT AUTO_INCREMENT PRIMARY KEY,
    Pedido_id INT NOT NULL,
    Produto_id INT NOT NULL,
    Quantidade SMALLINT NOT NULL,
    Preco_unitario FLOAT NOT NULL,
    FOREIGN KEY (Pedido_id) REFERENCES Pedidos(Pedido_id),
    FOREIGN KEY (Produto_id) REFERENCES Produtos(Produto_id)
);\n''')

file.write('INSERT INTO Itens_Pedidos (Pedido_id, Produto_id, Quantidade, Preco_unitario) VALUES\n')
for  index, itens_pedido in enumerate(itens_pedido):
    file.write(f"\t({itens_pedido['pedido_id']}, {itens_pedido['produto_id']}, {itens_pedido['quantidade']}, {itens_pedido['preco_unitario']})")
    if index + 1 < q_itens_pedidos :
        file.write(',\n')
    else:
        file.write(';\n')

file.write('\n')

file.close()