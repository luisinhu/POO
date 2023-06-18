from classes import *
import os
import time
#7 digitos matricula de professor
#13 digitos matricula do aluno
primeira_acao = int(input("Escolha uma opção.\n[1]Iniciar\n[2]Programadores\nR: "))
while primeira_acao != 1 and primeira_acao != 2 :
    print("Tente novamente")
    primeira_acao = int(input("Escolha uma opção.\n[1]Iniciar\n[2]Programadores\nR: "))
if primeira_acao == 1:
    loading = ("Carregando: {----------}")
    for i in range(11):
        os.system('cls')
        print (loading)
        print ("")
        loading = loading.replace("-","=",1)
        time.sleep(0.2)

if primeira_acao == 2:
    print('\033[1m'"="*15)
    print("Nossos programadores são:\nDaniel\nDanielly\nLuis\nMarcos")
    print("="*15,'\033[0;0m')
    time.sleep(4)
    os.system('cls')
    print("Vamos lá")
login_ou_cadastro = int(input("Você deseja fazer \n[1] - Cadastro\n[2] - Login\n: "))
while login_ou_cadastro != 1 and login_ou_cadastro != 2:
    login_ou_cadastro = int(input("Você deseja fazer \n[1] - Cadastro\n [2] - Login\n: "))
if login_ou_cadastro == 1:
        pergunta = int(input("Escolha para fazer seu cadastro\n[1] Para professor\n[2] Para aluno\nR: "))
        while pergunta != 1 and pergunta != 2:
            print("Erro responda novamente")
            pergunta = int(input("Escolha para fazer seu cadastro\n[1] Para professor\n[2] Para aluno\nR: "))
        if pergunta == 1:
            nome_prof = input("Digite seu nome\n: ")
            sexo_prof = input("Digite seu sexo\n: ")
            matricula_prof = int(input("Digite sua matricula\n: "))
            professor_cadastrado = Professor(nome_prof,sexo_prof, matricula_prof)
            if professor_cadastrado.cadastro_professor():
                print("Professor cadastrado")
            else:
                print("Aperta enter")
        else:     
            os.system('cls')
            nomec = input("Digite seu nome completo\n: ")
            turmac = input("Digite sua turma\nex: 2 INFO \n: ")
            sexoc = input("Digite seu sexo\n: ")
            matriculac = int(input("Digite sua matricula\n: "))
            senhac = input("Digite sua senha\n: ")
            aluno_cadastrado = Aluno(nomec, turmac,sexoc, matriculac, senhac, None)
            if aluno_cadastrado.cadastrar():
                print("Aluno cadastrado")
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
            while inscricao_modalidade != "futebol" or inscricao_modalidade != "Futebol":
                print("Digito incorreto!")
                matricula_modalidade = int(input("Digite sua matricula do login\n: "))
            
            inscricao_do_aluno = Aluno(None,None,matricula_modalidade,None,inscricao_modalidade)
            inscricao_do_aluno.modalidadep()
        else:
            print("Parou")           
    else:
        input("Aperte enter")  