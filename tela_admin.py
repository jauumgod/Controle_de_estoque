from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import DataBaser




tela_adm = Tk()
tela_adm.geometry("1280x720")
tela_adm.configure(background='#0f232e')
tela_adm.resizable(width=False, height=True)
tela_adm.title('Programa teste')

def Sair():
    tela_adm.destroy()


#----------------------------------
#layout
TituloLabel = Label(tela_adm, text="REGISTRAR", font='Helvetica 18 bold', bg='#0f232e', fg="white")
TituloLabel.place(x=1050, y=50)
#-----------------------------------
NomeUsuariolb = Label(tela_adm, text="Nome:", bg='#0f232e', fg="white")
NomeUsuariolb.place(x=1000, y=100)
NomeUsuario = Entry(tela_adm, width=30)
NomeUsuario.place(x=1000, y=120)
#-----------------------------------
UserLabel = Label(tela_adm, text="Usuario:", bg='#0f232e', fg="white")
UserLabel.place(x=1000, y=140)
UserEntry = Entry(tela_adm, width=30)
UserEntry.place(x=1000, y=160)
#------------------------------------
PasswordLabel = Label(tela_adm,text='Senha:', bg='#0f232e', fg="white")
PasswordLabel.place(x=1000, y=180)
PasswordEntry = Entry(tela_adm, show="*", width=30)
PasswordEntry.place(x=1000, y=200)
#--------------------------------------
def registrar():
    name = NomeUsuario.get()
    usuario = UserEntry.get()
    password = PasswordEntry.get()
    if (name == "" and usuario == "" and password == ""):
        messagebox.showwarning(title="Erro no Registro", message="Algum campo vazio!")
    else:
        DataBaser.cursor.execute("""
        INSERT INTO Users(name, usuario, password )VALUES(?, ?, ?)
        """,(name, usuario, password))

        DataBaser.conn.commit()
        messagebox.showinfo(title="Informações", message="Criado com sucesso!")

BtnEntrar = ttk.Button(tela_adm, text= 'Registrar', width=10, command=registrar)
BtnEntrar.place(x=1060, y=230)
#--------------------------------------

#--------------------------------------



#funções

tela_adm.mainloop()