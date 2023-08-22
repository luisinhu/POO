from my_sql import *



matriC = int(input("Digite sua matricula"))
senhaC = input("Digite sua senha")
nomeC = input("Digite seu nome")
turmaC = input("Digite sua turma")
sexoC = input("Digite seu sexo")
modaC = input("Digite sua modalidade")

teste = Aluno(nomeC, turmaC, sexoC, matriC, senhaC, modaC)
teste.cadastrar()