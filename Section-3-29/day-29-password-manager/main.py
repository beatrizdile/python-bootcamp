from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(5, 7)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 3)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list = password_list + [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_list + [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = input_website.get()
    mail = input_mail.get()
    password = input_password.get()

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {mail} "
                                                  f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as doc:
                doc.write(f" {web} | {mail} | {password}\n")

            input_website.delete(0, END)
            input_password.delete(0, END)
            input_website.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)


# Labels
label_web = Label(text="Website:")
label_web.grid(column=0, row=1)

label_mail = Label(text="Email/Username:")
label_mail.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)


# Inputs
input_website = Entry(width=52)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_mail = Entry(width=52)
input_mail.grid(column=1, row=2, columnspan=2)
input_mail.insert(0, "beatriz@gmail.com")

input_password = Entry(width=33)
input_password.grid(column=1, row=3)


# Buttons
generate_butt = Button(text="Generate Password", width=14, command=generate_password)
generate_butt.grid(column=2, row=3)

add_butt = Button(text="Add", width=44, command=save)
add_butt.grid(column=1, row=4, columnspan=2)


window.mainloop()
