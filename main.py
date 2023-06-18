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
os.system("cls")
while True:
    os.system("cls")
    login_ou_cadastro = int(input("Você deseja fazer \n[1] - Cadastro\n[2] - Login\n[3] - Sair\n: "))
    while login_ou_cadastro != 1 and login_ou_cadastro != 2 and login_ou_cadastro != 3:
        login_ou_cadastro = int(input("Você deseja fazer \n[1] - Cadastro\n [2] - Login\n[3] - Sair\n: "))
    if login_ou_cadastro == 1:
            pergunta = int(input("Escolha para fazer seu cadastro\n[1] Para professor\n[2] Para aluno\nR: "))
            while pergunta != 1 and pergunta != 2:
                print("Erro responda novamente")
                pergunta = int(input("Escolha para fazer seu cadastro\n[1] Para professor\n[2] Para aluno\nR: "))
            if pergunta == 1:
                nome_prof = input("Digite seu nome\n: ")
                sexo_prof = input("Digite seu sexo\n: ")
                matricula_prof = int(input("Digite sua matricula\n: "))
                senha_prof = input("Digite sua senha\n: ")
                professor_cadastrado = Professor(nome_prof,sexo_prof,matricula_prof,senha_prof)
                if professor_cadastrado.cadastro_professor():
                    print("Professor cadastrado")
                    time.sleep(1)
                    os.system("cls")
                    exibicao_alunos=int(input("Deseja ver os alunos cadastrados na modalidade futebol?"))
                else:
                    print("Aperta enter")
            else:     
                os.system('cls')
                pergunta_repeticao = int(input("Quantos alunos(as), irá cadastrar?\n: "))
                for i in range(pergunta_repeticao):
                    nomec = input("Digite seu nome completo\n: ")
                    turmac = input("Digite sua turma\nex: 2 INFO \n: ")
                    sexoc = input("Digite seu sexo\n: ")
                    matriculac = int(input("Digite sua matricula\n: "))
                    senhac = input("Digite sua senha\n: ")
                    modalidadec = int(input("Deseja se inscrever em futebol\n[1] - Sim\n[2] - Não\n: "))         
                    if modalidadec == 1:
                        aluno_cadastrado = Aluno (nomec,turmac, sexoc, matriculac,senhac,"Futebol")
                    else:
                        aluno_cadastrado = Aluno(nomec, turmac, sexoc, matriculac, senhac, None)
                    if aluno_cadastrado.cadastrar():
                        print("Aluno cadastrado")
                        time.sleep(1)
                        os.system("cls")
                    else:
                        print("Algo deu errado!")
    elif login_ou_cadastro == 2:
        resposta = int(input("Deseja fazer login como:\n[1] Professor\n[2] Aluno\n: "))
        while resposta != 1 and resposta != 2:
            print("Responda corretamente!")
            resposta = int(input("Deseja fazer login como:\n[1] Professor\n[2] Aluno\n: "))
        if resposta == 1:
            os.system("cls")
            print("Faça o login:)")
            matriculaprof= int(input("Digite sua matricula\n:"))
            senha_login_prof = input("Digite sua senha\n: ")
            professor_login = Professor(None,None,None,matriculaprof,senha_login_prof,None)
            if professor_login.login_professor():
                acao_professor= int(input("Bem vindo ao nosso sistema\n[1] - Ve alunos cadastrados\n[2] - Excluir cadastro de aluno\n: "))
                while acao_professor != 1 and acao_professor != 2:
                    print("Erro, responda corretamente!")
                    acao_professor= int(input("Bem vindo ao nosso sistema\n[1] - Ve alunos cadastrados\n[2] - Excluir cadastro de aluno\n: "))
                if acao_professor == 1:
                    print("Vamos lá")
                    if professor_login.exibir_alunos():
                        print("Esses são os alunos cadastrados")
    
                        
                    
                else:
                    print("Em atualizações futuras...")
                    time.sleep(10)
                

                
        if resposta == 2:
            os.system("cls")
            print("Faça o login")
            matricula_aluno = int(input("Digite sua matricula\n:"))
            senha_login_aluno = input("Digite sua senha\n: ")
            aluno_login = Aluno(None,None,None,matricula_aluno,senha_login_aluno,None)
            if aluno_login.login():
                print("Bem Vindo!")
                time.sleep(10)
            
    else:
        print("Obrigado por executar nosso projeto jics")
        time.sleep(2)
        loading = ("Desligando: {----------}")
        for i in range(11):
            os.system('cls')
            print (loading)
            print ("")
            loading = loading.replace("-","=",1)
            time.sleep(0.2)
        os.system("cls")
        quit()

