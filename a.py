import sqlite3


banco = sqlite3.connect("banco_de_dados.db")
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos(nome TEXT,turma TEXT,sexo TEXT,matricula INT PRIMARY KEY,senha INT,modalidade TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Modalidade(matricula INT,modalidade TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Professor(nome TEXT,sexo TEXT,matricula INT,senha TEXT)''')
banco.commit()
banco.close()
