import mysql.connector


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

    def cadastrar(self):
        conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'Luis',
            password = 'LUISHSB2007',
            database = 'Projeto_integrador'
        )

        cursor = conexao.cursor()

        #CREATE
        comando = f'INSERT INTO alunos (matricula, senha, nome, sexo, turma,modalidade) VALUES ({self.matricula}, "{self.senha}", "{self.nome}", "{self.sexo}", "{self.turma}", "{self.modalidade}")'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()