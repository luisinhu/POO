import sqlite3



banco = sqlite3.connect("banco_de_dados.db")
cursor = banco.cursor()
cursor.execute("SELECT * FROM Alunos")
mostrar_alunos = cursor.fetchall()
for i in mostrar_alunos:
    for a in i:
        print(a)
