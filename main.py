from classes import *
import os


login_ou_cadastro = int(input("Você deseja fazer \n[1] - Cadastro\n[2] - Login\n"))
while login_ou_cadastro != 1 and login_ou_cadastro != 2:
    login_ou_cadastro = int(input("Você deseja fazer \n[1] - Cadastro\n [2] - Login\n"))
if login_ou_cadastro == 1:
    while True:
        os.system('cls')
        nomec = input("Digite seu nome completo\n:")
        turmac = input("Digite sua turma\nex: 2 INFO \n:")
        matriculac = int(input("Digite sua matricula\n:"))
        senhac = input("Digite sua senha\n:")
        modalidadec = input("Digite futebol\n:")
        aluno_cadastrado = Aluno(nomec, turmac, matriculac, senhac, modalidadec)
        if aluno_cadastrado.cadastrar():
            break
        else:
            print("Aperte Enter")

elif login_ou_cadastro == 2:
    calculo = 0 
    while True:
        os.system('cls')
        print("Faça o login:)")
        matriculal = int(input("Digite sua matricula\n: "))
        senhal = input("Digite sua senha\n:")
        aluno_login = Aluno(None, None, matriculal, senhal,None)
        if aluno_login.login():
            os.system('cls')
            print("Bem vindo:) Agora você pode se inscrever na modalidade futebol")
            matricula_inscriçao = int(input("Digite sua matricula\n:"))
            aluno_ins = Aluno(None, None, matricula_inscriçao, None, None)
            aluno_ins.modalidadep()
        else:
            input("Aperte enter")





    





        