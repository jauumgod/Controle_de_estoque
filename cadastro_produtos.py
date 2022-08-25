from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import DataBaser
import tkinter  as tk 
from tkcalendar import DateEntry



tela1 = Tk()
tela1.geometry("1280x720")
tela1.configure(background='#c3d1d9')
tela1.resizable(width=False, height=True)
tela1.title('Cadastrar Produtos')

#layout

TituloLabel = Label(tela1, text="Cadastrar Produtos", font='Helvetica 18 bold', bg='#c3d1d9', fg="white")
TituloLabel.place(x=550, y=50)



#-----------------------------------
Pdlabel = Label(tela1, text="Produto:", bg='#c3d1d9', fg="white")
Pdlabel.place(x=500, y=140)
PdEntry = Entry(tela1, width=40)
PdEntry.place(x=500, y=160)
#------------------------------------
val_label = Label(tela1, text='Valor:', bg='#c3d1d9', fg="white")
val_label.place(x=500, y=180)
valEntry = Entry(tela1,width=40)
valEntry.place(x=500, y=200)
#--------------------------------------
qntLabel = Label(tela1, text='Quantidade:', bg='#c3d1d9', fg="white")
qntLabel.place(x=500, y=220)
qnt_entry = Entry(tela1,width=40)
qnt_entry.place(x=500, y=240)

class calendario:
    def __init__(self):
        self.calendario = Tk()
        self.calendario.geometry("290x210")
        self.calendario.resizable(width=False, height=True)  
        calendar1 = DateEntry(self.calendario, selectmode='day')
        calendar1.grid(row=1,column=1,padx=15)

        self.calendario.mainloop()


dataLabel = Label(tela1, text='Selecionar Data: ', bg='#c3d1d9', fg="white")
dataLabel.place(x=500, y=260)

Btncalendar = ttk.Button(tela1, text= 'CALENDARIO', width=10, command=calendario)
Btncalendar.place(x=590, y=265)

NFLabel = Label(tela1, text='Numero da nota: ', bg='#c3d1d9', fg="white")
NFLabel.place(x=500, y=300)

NFentry = Entry(tela1,width=40)
NFentry.place(x=500, y=320)


#funções:

def Sair():
    tela1.destroy()

def cadastrarbtn():
    if PdEntry == "":
        messagebox.showerror(title="Erro", message="Preencha todos os campos")
    else:
        messagebox.showinfo(title="Mensagem", message=" Item cadastrado Cadastrado!")

#---------------------------------------
BtnCad = ttk.Button(tela1, text= 'CADASTRAR', width=10, command=cadastrarbtn)
BtnCad.place(x=620, y=450)


#--------------------------------------
sairbtn = ttk.Button(tela1, text='Sair', command=Sair)
sairbtn.place(x=1160,y=680)


#---------------------------------
def register_item_data_base():
        
    produto = PdEntry.get()
    valor = val_label.get()
    quantidade = qnt_entry.get()

    if (produto == "" and valor == "" and quantidade == ""):
        messagebox.showwarning(title="Erro no Registro", message="Algum campo vazio!")
    else:
        DataBaser.cursor.execute("""
        INSERT INTO Users(name, usuario, password )VALUES(?, ?, ?)
        """,(produto, valor, quantidade))

        DataBaser.conn.commit()
        messagebox.showinfo(title="Informações", message="Criado com sucesso!")
#--------------------------------

tela1.mainloop()
            