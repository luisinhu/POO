import sqlite3

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
        cursor.execute(" INSERT INTO Alunos VALUES(:nome,:turma,:matricula,:senha)",{
            'nome': self.nome,
            'turma': self.turma,
            'matricula': self.matricula,
            'senha': self.senha,
        })
        if self.nome == '' or self.turma == '' or self.matricula == None or self.senha == '':
            print("Você digitou algo incorretamente ")
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
            print(f'Login feito com sucesso{self.nome}')
            banco.close()
            return True

        else:
            print("Algo de errado não está certo")
            return False
    def modalidadep (self):
        banco = sqlite3.connect("Banco_Alunos.db")
        cursor = banco.cursor()
        cursor.execute("INSERT INTO Modalidade VALUES(:matricula)",{
            'matricula': self.matricula,
            'modalidade': self.modalidade,

        })
        if self.matricula == None:
            print("Digite seus dados corretamente")
            return False
        else:
            banco.commit()
            banco.close()
            return True
