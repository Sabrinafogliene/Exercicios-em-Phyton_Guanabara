# primeira etapa # importar as bibliotecas relevantes

import random
import mysql.connector
from faker import Faker
from datetime import datetime

#criar uma conexão direta com nosso banco de dados mysql
conn = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '', 
    database = 'diobank'
)
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS testeprincipal (
            nome VARCHAR(100),
            Endereco VARCHAR(200),
            Id INT PRIMARY KEY)       


''')

conn.commit()

# endereços
# movimentações
# clientes
# pagamentos

cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            cliente_id INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100),
            cpf VARCHAR(14) UNIQUE,
            email VARCHAR(100)                        
        )        

""")

cursor.execute("""
        CREATE TABLE IF NOT EXISTS enderecos (
            endereco_id INT PRIMARY KEY AUTO_INCREMENT,
            cliente_id INT,
            rua VARCHAR(100),
            cidade VARCHAR(50),
            estado VARCHAR(50),
            cep VARCHAR(10),
            FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
        )
""")

cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentacoes (
            movimentacao_id INT PRIMARY KEY AUTO_INCREMENT,
            cliente_id INT,
            tipo_movimentacao VARCHAR(50),
            valor DECIMAL(10, 2),
            data_movimentacao DATE,
            FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
        )  
""")

cursor.execute("""
        CREATE TABLE IF NOT EXISTS pagamentos (
            pagamento_id INT PRIMARY KEY AUTO_INCREMENT,
            cliente_id INT,
            valor DECIMAL(10, 2),
            data_pagamento DATE,
            FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
        )  
""") 

conn.commit()

fake = Faker()

for i in range(1000):
    nome = fake.name()
    cpf = str(random.randint(10000000000, 99999999999))
    email = fake.email()

    rua = fake.street_address()
    cidade = fake.city()
    estado = fake.state()
    cep = fake.zipcode()

    tipo_movimentacao = random.choice(['deposito', 'saque', 'pix', 'transferencia', 'credito', 'emprestimo', 'titulo'])
    valor = round(random.uniform(50.0, 50000.0), 2)
    data_movimentacao = fake.date_this_year()

    valor_pagamento = round(random.uniform(50.0, 50000.0), 2)
    data_pagamento = fake.date_this_year()

    cursor.execute("""
        INSERT INTO clientes (nome, cpf, email) VALUES (%s, %s, %s)
    """, (nome, cpf, email))
    cliente_id = cursor.lastrowid
    cursor.execute("""
        INSERT INTO enderecos (cliente_id, rua, cidade, estado, cep) VALUES (%s, %s, %s, %s, %s)
    """, (cliente_id, rua, cidade, estado, cep))
    cursor.execute("""
        INSERT INTO movimentacoes (cliente_id, tipo_movimentacao, valor, data_movimentacao) VALUES (%s, %s, %s, %s)
    """, (cliente_id, tipo_movimentacao, valor, data_movimentacao))
    cursor.execute("""
        INSERT INTO pagamentos (cliente_id, valor, data_pagamento) VALUES (%s, %s, %s)
    """, (cliente_id, valor_pagamento, data_pagamento))
    conn.commit()
