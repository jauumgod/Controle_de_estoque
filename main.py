from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import DataBaser
import cadastro_cliente




tela = Tk()
tela.geometry("1280x720")
tela.configure(background='#c3d1d9')
tela.resizable(width=False, height=True)
tela.title('Programa teste')

imagem = PhotoImage(file="icons/imagemhehe.png")

#cadastro_produtos_01 = tela1
#cadastro_cliente_01 = cadastro_cliente(tela1)

def SairMain():
    tela.destroy()

#---------------------------------   
def lembrarSENHA():
    senha = 0
#----------------------------------
#layout
TituloLabel = Label(tela, text="ENTRAR", font='Helvetica 18 bold', bg='#c3d1d9', fg="white")
TituloLabel.place(x=1050, y=50)
#-----------------------------------

#-----------------------------------
UserLabel = Label(tela, text="Usuario:", bg='#c3d1d9', fg="white")
UserLabel.place(x=1000, y=140)
UserEntry = Entry(tela, width=30)
UserEntry.place(x=1000, y=160)
#------------------------------------
PasswordLabel = Label(tela,text='Senha:', bg='#c3d1d9', fg="white")
PasswordLabel.place(x=1000, y=180)
PasswordEntry = Entry(tela, show="*",width=30)
PasswordEntry.place(x=1000, y=200)
#--------------------------------------
def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    
    if (usuario == "" and password == "" ):
        messagebox.showwarning(title="Erro no Registro", message="Algum campo vazio!")
        
    Databaser.cursor.execute("""
    """

    )
    


#--------------------------------------
BtnEntrar = ttk.Button(tela, text= 'LOGIN', width=10, command="verifica_senha")
BtnEntrar.place(x=1060, y=230)
#--------------------------------------
x = Checkbutton(tela, text='Lembrar Senha',bg='#c3d1d9', fg="white" )
x.place(x=1000,y=260)
#--------------------------------------



#funções



tela.mainloop()
