import sqlite3


banco = sqlite3.connect("Banco_Alunos.db")
cursor = banco.cursor()
    
cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos(
            nome TEXT NOT NULL,
            turma TEXT NOT NULL,
            matricula INT PRIMARY KEY NOT NULL,
            senha TEXT NOT NULL 
        )
        ''')
banco.commit()
banco.close()