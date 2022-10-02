from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)


def convert():
    miles = int(input_miles.get())
    kms = round(miles * 1.6)
    label_3.config(text=kms)


input_miles = Entry(width=10, justify="center")
input_miles.grid(column=1, row=0)

label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text="0")
label_3.grid(column=1, row=1)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)

but = Button(text="Calculate", command=convert)
but.grid(column=1, row=2)

window.mainloop()
