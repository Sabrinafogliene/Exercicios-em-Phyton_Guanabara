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
openai.api_key = os.getenv('OPENAI_API_KEY')

conn = mysql.connector.connect(
    host = host,
    port = port,
    user = user,
    password = password,
    database = database
)
cursor = conn.cursor()
