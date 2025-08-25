import os
from dotenv import load_dotenv
import openai
import mysql.connector

load_dotenv()
host = os.getenv('host')
port = os.getenv('port')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

conn = mysql.connector.connect(
    host = host,
    port = port,
    user = user,
    password = password,
    database = database
)
cursor = conn.cursor()

cursor.execute('SHOW TABLES')

tabelas = cursor.fetchall()
colunas = {}
for tabela in tabelas:
    cursor.execute(f"DESCRIBE {tabela[0]};")
    colunas_tabelas = cursor.fetchall()
    colunas[tabela[0]] = (coluna[0] for coluna in colunas_tabelas)

cursor.close()
conn.close()

# construir a nossa inteligência artificial

prompt = f"""
Voce e um assistente de SQL que opera para um banco de dados ficticio chamado Dio Bank.
Voce deve gerar queries SQL com base na estrutura do banco de dados fornecida.
A estrutura do banco de dados e a seguinte:
{colunas}
pergunta: {input("Faça a sua pergunta: ")}
resposta em SQL: 

"""

openai.api_key = OPENAI_API_KEY
response = openai.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{"role": "system", "content": "Voce e um assistente de SQL que opera para um banco de dados ficticio chamado Dio Bank."},
                {"role": "user", "content": prompt}],
    max_tokens = 150,
    temperature = 0, #quanto mais próximo do 0 maior será a sua determinação e quanto mais perto do 1 ela vai ser completamente alucinada.
)


query_gerada = response.choices[0].message.content
query_gerada = query_gerada.replace("```sql", "").replace("```", "")
print(query_gerada)

conn = mysql.connector.connect(
    host = host,
    port = port,
    user = user,
    password = password,
    database = database
)
cursor = conn.cursor()

cursor.execute(query_gerada)
resultados = cursor.fetchall()
print(resultados)

