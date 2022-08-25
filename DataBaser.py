import sqlite3

conn = sqlite3.connect('data_project.db')

cursor = conn.cursor()
#criar a tabela de usuarios

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
       usuario TEXT NOT NULL,
       name TEXT NOT NULL,
       password TEXT NOT NULL);
    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
       produto TEXT NOT NULL,
       valor TEXT NOT NULL,
       quantidade TEXT NOT NULL,
       criado_em DATE NOT NULL
       );
    """)

    
#Inserir dado na tabela

#cursor.execute(""" INSERT INTO Users (Name) VALUES (Dev Gamer)""")


#DELETE BANCO DE DADOS

#conn = sqlite3.connect('data_project.db')
#cursor = conn.cursor()

#id_cliente = 8

# excluindo um registro da tabela
#cursor.execute("""
#DELETE FROM users
#WHERE id = ?
#""", (id_cliente,))

#conn.commit()

#print('Registro excluido com sucesso.')

#conn.close()