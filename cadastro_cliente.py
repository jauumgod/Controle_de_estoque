from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class cadastro_cliente:
    def __init__(self):
        self.cad = Tk()
        self.cad.geometry("1280x720")
        self.cad.config(bg="#5549f5")
        self.cad.title("Cadastro Cliente")

        def sair(self):
                self.cad.destroy()
#labels
        labeltitle = Label(self.cad, text="CADASTRO CLIENTE", font="sans-serif 28 bold", bg="#5549f5", fg="White")
        labeltitle.place(x=480, y=50)

        label1 = Label(self.cad,text="Nome do cliente:", bg="#5549f5", fg="white")
        label1.place(x=100, y=200)
        entrada1 = Entry(self.cad, width=30)
        entrada1.place(x=200, y=200)

        label2 = Label(self.cad, text="                CPF:", bg="#5549f5", fg="white")
        label2.place(x=100, y=220)
        entrada2 = Entry(self.cad, width=30)
        entrada2.place(x=200, y=220)

        label3 = Label(self.cad, text="               Telefone:", bg="#5549f5", fg="white")
        label3.place(x=100, y=240)
        entrada3 = Entry(self.cad, width=30)
        entrada3.place(x=200, y=240)

        label4 = Label(self.cad, text="             Endereço:", bg="#5549f5", fg="white")
        label4.place(x=100, y=260)
        entrada4 = Entry(self.cad, width=30)
        entrada4.place(x=200, y=260)
        
        def CadastroCliente(self):
            self.nome = entrada1
            self.cpf = entrada2
            self.telefone = entrada3
            self.endereco = entrada4
            if entrada1, entrada2, entrada3, entrada4 ==0:
                print("dados inseridos com sucesso!")
            else:
                print("dados invalidos")
              
                
            
        
        btn_submit = Button(self.cad, text="Cadastrar", command = CadastroCliente)
        btn_submit.place(x=1100, y=600)



        btnsair = Button(self.cad, text="Sair", command=sair)
        btnsair.place(x=1100, y=700)




#rodar app
        self.cad.mainloop()




cadastro_cliente()


