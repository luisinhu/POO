import sqlite3

class Pessoa:
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo

class Aluno(Pessoa):
    def __init__(self,nome,turma, sexo, matricula, senha, modalidade):
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
class Professor(Pessoa):
    def __init__(self, nome,sexo,matricula, senha):
        super().__init__(nome, sexo)
        self.matricula = matricula
        self.senha = senha
    def cadastro_professor(self):
        banco = sqlite3.connect("banco_de_dados.db")
        cursor = banco.cursor()
        cursor.execute("INSERT INTO Professor VALUES(:nome,:sexo,:matricula,:senha)",{
            'nome': self.nome,
            'sexo': self.sexo,
            'matricula': self.matricula,
            'senha': self.senha
            
        })
        if self.nome == None or self.matricula == None or self.senha == None:
            print("Cadê seus dados?")
            return False
        else:
            banco.commit()
            banco.close()
            return True
    def login_professor (self): 
        banco = sqlite3.connect("banco_de_dados.db")
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM Professor WHERE(matricula = ? AND senha = ?)",(self.matricula, self.senha))
        verifica_login_prof = cursor.fetchall()
        if len(verifica_login_prof) > 0:
            print('Login feito com sucesso')
            banco.close()
            return True
        else:
            print("teste...")
            return False

    def excluir_aluno(self):
      banco = sqlite3.connect('banco_de_dados.db')
      cursor = banco.cursor()
      cursor.execute("SELECT * FROM Professor WHERE(matricula = ? AND senha = ?)",(self.matricula, self.senha))
      verificador = cursor.fetchall()
      if len(verificador) > 0:
        cursor.execute("DELETE FROM Modalidade WHERE (matricula = ? AND modalidade = ?)",(self.matricula, self.modalidade))
        banco.commit()
        banco.close()
      else:
        print("A")