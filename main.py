from classes import *
import os


login_ou_cadastro = int(input("Você deseja fazer \n[1] - Cadastro\n[2] - Login\n: "))
while login_ou_cadastro != 1 and login_ou_cadastro != 2:
    login_ou_cadastro = int(input("Você deseja fazer \n[1] - Cadastro\n [2] - Login\n: "))
if login_ou_cadastro == 1:
    while True:
        os.system('cls')
        nomec = input("Digite seu nome completo\n:")
        turmac = input("Digite sua turma\nex: 2 INFO \n:")
        matriculac = int(input("Digite sua matricula\n:"))
        senhac = input("Digite sua senha\n:")
        aluno_cadastrado = Aluno(nomec, turmac, matriculac, senhac, None)
        if aluno_cadastrado.cadastrar():
            break
        else:
            print("Aperte Enter")

elif login_ou_cadastro == 2:
    calculo = 0 
    os.system('cls')
    print("Faça o login:)")
    matriculal = int(input("Digite sua matricula\n: "))
    senhal = input("Digite sua senha\n:")
    aluno_login = Aluno(None, None, matriculal, senhal,None)
    if aluno_login.login():
        os.system('cls')
        escolha = int(input("Bem vindo ao nosso sistema\nSe inscreva na modalidade de futebol\n1-[sim]\n2-[não]\n: "))
        if escolha == 1:
            matricula_modalidade = int(input("Digite sua matricula do login\n: "))
            inscricao_modalidade = input("Digite futebol para registrar no sistema\n: ")
            inscricao_do_aluno = Aluno(None,None,matricula_modalidade,None,inscricao_modalidade)
            inscricao_do_aluno.modalidadep()
        else:
            print("Parou")           
    else:
        input("Aperte enter")  