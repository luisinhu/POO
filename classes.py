import sqlite3
#Danielly
class Pessoa:
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo
#Danielly
class Aluno(Pessoa):
    def __init__(self,nome,turma, sexo, matricula, senha, modalidade):
        super().__init__(nome, sexo)
        self.turma = turma
        self.matricula = matricula
        self.senha = senha
        self.modalidade = modalidade

    #Luis
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
    #Luis
    def login(self):
        banco = sqlite3.connect("banco_de_dados.db")
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM Alunos WHERE(matricula = ? AND senha = ?)",(self.matricula, self.senha))
        verificador = cursor.fetchall()
        if len(verificador) > 0:
            print('Login feito com sucesso')
            banco.close()
            return True

        else:
            print("Algo de errado não está certo")
            return False
#Danielly
class Professor(Pessoa):
    def __init__(self, nome, sexo, matricula, senha):
        super().__init__(nome, sexo)
        self.matricula = matricula
        self.senha = senha
    #Marcos
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
    #Marcos
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
            print("Erro, algo está errado")
            return False
    #Daniel
    def exibir_alunos(self):
        banco = sqlite3.connect("banco_de_dados.db")
        cursor = banco.cursor()
        cursor.execute("SELECT nome,turma,sexo,matricula,modalidade FROM Alunos ")
        mostrar_alunos = cursor.fetchall()
        for mostrar_alunos in mostrar_alunos:
            nome = mostrar_alunos[0]
            turma = mostrar_alunos[1]
            sexo = mostrar_alunos[2]
            matricula = mostrar_alunos[3]
            modalidade = mostrar_alunos[4]
            print("Nome:", nome)
            print("Turma:",turma)
            print("Sexo:",sexo)
            print("Matricula:",matricula)
            print("Modalidade:",modalidade)
            print()

        banco.close()
    