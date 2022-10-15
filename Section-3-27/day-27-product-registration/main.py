from tkinter import *

base = Tk()
base.geometry("550x500")
base.title('Registration form')

lbl_0 = Label(base, text="Cadastro e listagem de produtos", font=("bold", 20))
lbl_0.place(x=90, y=60)

lbl_1 = Label(base, text="Nome do produto", width=20, font=("bold", 10))
lbl_1.place(x=80, y=130)

enter_3 = Entry(base, width=20)
enter_3.place(x=240, y=130)

lbl_2 = Label(base, text="Descrição do produto", width=20, font=("bold", 10))
lbl_2.place(x=68, y=180)

enter_2 = Text(base, height=5, width=20)
enter_2.place(x=240, y=180)

lbl_3 = Label(base, text="Valor do produto", width=20, font=("bold", 10))
lbl_3.place(x=80, y=290)

enter_3 = Entry(base, width=10)
enter_3.place(x=240, y=290)

lbl_4 = Label(base, text="Disponível para venda", width=20, font=("bold", 10))
lbl_4.place(x=65, y=330)

vars = IntVar()

Radiobutton(base, text="Sim", padx=5, variable=vars, value=1).place(x=235, y=330)
Radiobutton(base, text="Não", padx=20, variable=vars, value=2).place(x=290, y=330)

Button(base, text='Cadastrar', width=20, bg="black", fg='white').place(x=220, y=400)

base.mainloop()