import customtkinter as ctk
from tkinter import messagebox
from classes import Aluno



janela = ctk.CTk()


frame_cadastro = ctk.CTkFrame(janela, width= 300, height= 300)
frame_cadastro.pack(padx = 10, pady= 10)

janela.title("Faça seu cadastro")

label_cadastro = ctk.CTkLabel(frame_cadastro, text="Faça seu cadastro")
label_cadastro.pack(padx = 10, pady= 10)


entrynome = ctk.CTkEntry(frame_cadastro, placeholder_text="Nome Completo", width= 200, height= 30)
entrynome.pack(padx = 10, pady= 10)


entryturma = ctk.CTkEntry(frame_cadastro, placeholder_text="Turma", width= 200, height= 30)
entryturma.pack(padx = 10, pady= 10)

entrymatri = ctk.CTkEntry(frame_cadastro, placeholder_text="Matricula", width= 200, height= 30)
entrymatri.pack(padx = 10, pady= 10)

entrysenha = ctk.CTkEntry(frame_cadastro, placeholder_text="Senha", width= 200, height= 30)
entrysenha.pack(padx = 10, pady= 10)

def cadastrar():
    nome = entrynome.get()
    turma = entryturma.get()
    matricula = entrymatri.get()
    senha = entrysenha.get()
    aluno_cadastrado = Aluno(nome, turma, matricula, senha, 'Futebol')
    if aluno_cadastrado.cadastrar():
        messagebox.showinfo('Parabens!!', 'Seja bem vindo, se cadastre na modalidade Futebol')
        fra
        
    else:
        messagebox.showinfo('Erro!', 'Algo de errado não está certo')

botao_cadastro = ctk.CTkButton(frame_cadastro, text="Fazer cadastro", command= cadastrar)
botao_cadastro.pack()

label_cadastro = ctk.CTkLabel(frame_cadastro, text="Caso tenha uma conta, faça uma conta")
label_cadastro.pack(padx = 10, pady= 10)

def fazer_login():
    frame_cadastro.pack_forget()
    
    janela.title("Faça login")
    frame_login = ctk.CTkFrame(janela, width= 300, height=300)
    frame_login.pack()

    labellogin = ctk.CTkLabel(frame_login, text="Faça login")
    labellogin.pack(padx = 10, pady = 10)

    entrymatrilo = ctk.CTkEntry(frame_login, placeholder_text="Matricula", width= 200, height= 30)
    entrymatrilo.pack(padx = 10, pady= 10)

    entrysenhalo = ctk.CTkEntry(frame_login, placeholder_text="Senha", width= 200, height= 30)
    entrysenhalo.pack(padx = 10, pady= 10)


    def cadastrar_atletas():
        frame_login.pack_forget()
        frame_cadastrar_atletas = ctk.CTkFrame(janela)
        frame_cadastrar_atletas.pack()
        cadastrar_atleta = ctk.CTkEntry(frame_cadastrar_atletas, placeholder_text="Matricula", width= 200, height= 30)
        cadastrar_atleta.pack(padx = 10, pady= 10)
        def meu_deus():
            atleta = cadastrar_atleta.get()
            atleta_objeto = Aluno(None, None, atleta, None, 'Futebol')
            atleta_objeto.modalidadep()
        botao_cadas_atleta = ctk.CTkButton(frame_cadastrar_atletas, text="Cadastre o Atleta",command=meu_deus)
        botao_cadas_atleta.pack(padx = 10, pady = 10)



    def fazer_login():
        matriculalogin = entrymatrilo.get()
        senha_login = entrysenhalo.get()
        aluno_login = Aluno(None, None, matriculalogin, senha_login,None)
        if aluno_login.login():
            cadastrar_atletas()
    

    botao_fazerlo = ctk.CTkButton(frame_login, text="Login", command=fazer_login)
    botao_fazerlo.pack(padx = 10, pady = 10)


    def voltar():
        frame_login.pack_forget()
        frame_cadastro.pack()

    botao_voltar = ctk.CTkButton(frame_login, text="Voltar para cadastro", command=voltar)
    botao_voltar.pack(padx = 10, pady = 10)




botao_cadastro = ctk.CTkButton(frame_cadastro, text="Fazer Login", command=fazer_login)
botao_cadastro.pack()



janela.mainloop()