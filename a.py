import sqlite3


banco = sqlite3.connect("Banco_Alunos.db")
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Modalidade(
    matricula INT,
    modalidade TEXT,
''')
banco.commit()
banco.close()
