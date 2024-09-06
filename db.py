import sqlite3 as sql

try:
    
    conexao = sql.Connection("Banco.db")
    cursor = conexao.cursor()
    
except Exception:
    print("Erro a conectar no banco")

def createTable():
    
    with conexao:
        
        query = ("CREATE TABLE IF NOT EXISTS BARBEARIA (id INTEGER PRIMARY KEY AUTOINCREMENT, cadastro TEXT)");
        
        
        query = ("CREATE TABLE IF NOT EXISTS TABELA_DE_VALORES (id INTEGER PRIMARY KEY AUTOINCREMENT, cabelo INTEGER, pezinho INTEGER, barba INTEGER, luzes INTEGER)");
        
        cursor.execute(query)
        
        print("Tabela criada com sucesso")
        

def  insertDado():
    
    with conexao:
        
        query = ("INSERT INTO BARBEARIA (id, cadastro) VALUES (8, 'Jonathan')");
        
        cursor.execute(query)
        
        print("Dados cadastrado com sucesso")
    
        
