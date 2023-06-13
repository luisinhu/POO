import customtkinter as ctk
from tkinter import messagebox
from classes import Aluno

#config da janela
janela = ctk.CTk()
janela.resizable(False,False)
janela.title("Faça seu cadastro")

#funções
def cadastrar_sis():
    nome = entrynome.get()
    turma = entryturma.get()
    matricula = entrymatri.get()
    senha = entrysenha.get()
    aluno_cadastrado = Aluno(nome, turma, matricula, senha, 'Futebol')
    if aluno_cadastrado.cadastrar():
        messagebox.showinfo('Parabens!!', 'Seja bem vindo, se cadastre na modalidade Futebol')

    else:
        messagebox.showinfo('Erro!', 'Algo de errado não está certo')

def fazer_login():
    matriculalogin = entrymatrilo.get()
    senha_login = entrysenhalo.get()
    aluno_login = Aluno(None, None, matriculalogin, senha_login,None)
    if aluno_login.login():
        cadastrar_atletas()

def ir_login():
    frame_cadastro.pack_forget()
    frame_login.pack()

def voltar_cadastro():
    frame_login.pack_forget()
    frame_cadastro.pack()

def cadastro_atleta():
    frame_login.pack_forget()
    frame_cadastro.pack()
    atleta = cadastrar_atleta.get()
    atleta_objeto = Aluno(None, None, atleta, None, 'Futebol')
    if atleta_objeto.modalidadep():
        messagebox.showinfo('Parabens!!', 'Você se cadastrou na modalidade futebol')
        janela.destroy()
    else:
        messagebox.showinfo('Erro!', 'Algo de errado não está certo')



#config do frame cadastro
frame_cadastro = ctk.CTkFrame(janela, width= 300, height= 300)

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

botao_cadastro = ctk.CTkButton(frame_cadastro, text="Fazer cadastro", command=cadastrar_sis)
botao_cadastro.pack()

label_cadastro = ctk.CTkLabel(frame_cadastro, text="Caso tenha uma conta, faça uma conta")
label_cadastro.pack(padx = 10, pady= 10)

botao_cadastro = ctk.CTkButton(frame_cadastro, text="Fazer Login", command=ir_login)
botao_cadastro.pack()

frame_cadastro.pack(padx = 10, pady= 10)


#config do frame login
janela.title("Faça login")    
frame_login = ctk.CTkFrame(janela, width= 300, height=300)

labellogin = ctk.CTkLabel(frame_login, text="Faça login")
labellogin.pack(padx = 10, pady = 10)

entrymatrilo = ctk.CTkEntry(frame_login, placeholder_text="Matricula", width= 200, height= 30)
entrymatrilo.pack(padx = 10, pady= 10)

entrysenhalo = ctk.CTkEntry(frame_login, placeholder_text="Senha", width= 200, height= 30)
entrysenhalo.pack(padx = 10, pady= 10)

botao_fazerlo = ctk.CTkButton(frame_login, text="Login")
botao_fazerlo.pack(padx = 10, pady = 10)

botao_voltar = ctk.CTkButton(frame_login, text="Voltar para cadastro", command=voltar_cadastro)
botao_voltar.pack(padx = 10, pady = 10)


#config da janela dos atletas

frame_cadastrar_atletas = ctk.CTkFrame(janela)

cadastrar_atleta = ctk.CTkEntry(frame_cadastrar_atletas, placeholder_text="Matricula", width= 200, height= 30)
cadastrar_atleta.pack(padx = 10, pady= 10)

botao_cadas_atleta = ctk.CTkButton(frame_cadastrar_atletas, text="Cadastre o Atleta")
botao_cadas_atleta.pack(padx = 10, pady = 10)



janela.mainloop()
