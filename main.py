from classes import *
import os


login_ou_cadastro = int(input("Você deseja fazer \n[1] - Cadastro\n[2] - Login\n"))
while login_ou_cadastro != 1 and login_ou_cadastro != 2:
    login_ou_cadastro = int(input("Você deseja fazer \n[1] - Cadastro\n [2] - Login\n"))
if login_ou_cadastro == 1:
    while True:
        os.system('cls')
        nomec = input("Digite seu nome completo:")
        turmac = input("Digite sua turma\nex: 2 INFO \n:")
        nomec = input("Digite sua turma")
        matriculac = int(input("Digite sua matricula"))
        senhac = input("Digite sua senha")
        aluno_cadastrado = Aluno(nomec, turmac, matriculac, senhac)
        if aluno_cadastrado.cadastrar():
            break
        else:
            print("Aperte Enter")

elif login_ou_cadastro == 2:
    while True:
        os.system('cls')
        print("Faça o login:)")
        matriculal = int(input("Digite sua matricula: "))
        senhal = input("Digite sua senha:")
        aluno_login = Aluno(None, None, matriculal, senhal)
        if aluno_login.login():
            print("Bem vindo:) Agora você pode se inscrever na modalidade futebol")
            matriculainscrição = int(input("Digite sua matricula para se inscrever\n\:"))
            
        else:
            input("Aperte enter")





    





        