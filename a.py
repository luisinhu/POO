import sqlite3


banco = sqlite3.connect("Banco_Alunos.db")
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Modalidade(
    matricula INT PRIMARY KEY NOT NULL
    modalidade TEXT NOT NULL
)
''')
banco.commit()
banco.close()
