import sqlite3
from tkinter import messagebox

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    def __init__(self,nome, turma, matricula, senha, modalidade):
        super().__init__(nome)
        self.turma = turma
        self.matricula = matricula
        self.senha = senha
        self.modalidade = modalidade


    def cadastrar(self):
        banco = sqlite3.connect("Banco_Alunos.db")
        cursor = banco.cursor()
        cursor.execute(" INSERT INTO Alunos VALUES(:nome,:turma,:matricula,:senha,:modalidade)",{
            'nome': self.nome,
            'turma': self.turma,
            'matricula': self.matricula,
            'senha': self.senha,
            'modalidade': self.modalidade
        })
        if self.nome == '' or self.turma == '' or self.matricula == None or self.senha == '':
            return False
        elif len(self.senha ) < 5:
            print("Senha pequena demais")
            return False
        else:
            banco.commit()
            banco.close()
            return True
    
    def login(self):
        banco = sqlite3.connect("Banco_Alunos.db")
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM Alunos WHERE(matricula = ? AND senha = ?)",(self.matricula, self.senha))
        
        verificador = cursor.fetchall()
        if len(verificador) > 0:
            messagebox.showinfo('Parabens', 'Login Feito com sucesso')
            banco.close()
            return True

        else:
            messagebox.showwarning('Erro!', 'Você digitou algo incorretamente')
            return False

    def modalidadep(self):
        banco = sqlite3.connect("Banco_Alunos.db")
        cursor = banco.cursor()


        cursor.execute("SELECT * FROM Modalidade WHERE matricula = ?", (self.matricula,))
        if cursor.fetchone():
            messagebox.showwarning('Erro!', 'Matrícula já existente na tabela Modalidade')
            return False

        cursor.execute("INSERT INTO Modalidade VALUES (:matricula, :modalidade)", {
            'matricula': self.matricula,
            'modalidade': self.modalidade
        })

        banco.commit()
        banco.close()
        return True
