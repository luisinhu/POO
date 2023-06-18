import sqlite3

class Pessoa:
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo

class Aluno(Pessoa):
    def __init__(self,nome, turma, matricula, senha, modalidade):
        super().__init__(nome, sexo)
        self.turma = turma
        self.matricula = matricula
        self.senha = senha
        self.modalidade = modalidade


    def cadastrar(self):
        banco = sqlite3.connect("banco_de_dados.db")
        cursor = banco.cursor()
        cursor.execute("INSERT INTO Alunos VALUES(:nome,:turma,:sexo,:matricula,:senha,:modalidade)",{
            'nome': self.nome,
            'turma': self.turma,
            'sexo': self.sexo,
            'matricula': self.matricula,
            'senha': self.senha,
            'modalidade': self.modalidade
        })
        if self.nome == '' or self.turma == '' or self.sexo == '' or self.matricula == None or self.senha == '':
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
        banco = sqlite3.connect("banco_de_dados.db")
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
        banco = sqlite3.connect("banco_de_dados.db")
        cursor = banco.cursor()
        cursor.execute("INSERT INTO Modalidade VALUES(:matricula, :modalidade)",{
            'matricula': self.matricula,
            'modalidade': self.modalidade

        })
        if self.matricula == None or self.modalidade == '':
            print("Digite seus dados corretamente")
            return False
        else:
            banco.commit()
            banco.close()
            return True
class Professor(Pessoa):
    def __init__(self, nome,matricula):
        super().__init__(nome, sexo)
        self.matricula = matricula
    def cadastro_professor(self):
        banco = sqlite3.connect("banco_de_dados.db")
        cursor = banco.cursor()
        cursor.execute("INSERT INTO Professor VALUES(:nome,:sexo,:matricula)",{
            'nome': self.nome,
            'sexo': self.sexo,
            'matricula': self.matricula
            
        })
        if self.nome == None or self.matricula == None:
            print("Cadê seus dados?")
            return False
        else:
            banco.commit()
            banco.close()
            return True