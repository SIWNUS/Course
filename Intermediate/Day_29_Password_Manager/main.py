#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_details.delete(0, END)
    password_details.clipboard_clear()

    s_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    c_letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    password_list = [choice(s_letters) for char in range(randint(2, 8))]
    password_list += [choice(c_letters) for char in range(randint(1, 8))]
    password_list += [choice(numbers) for num in range(randint(2, 8))]
    password_list += [choice(symbols) for sym in range(randint(3, 8))]
    shuffle(password_list)

    random_password = "".join(password_list)

    password_details.insert(0, random_password)
    password_details.clipboard_append(random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if website_name.get() == "" or password_details.get() == "" or email_name.get() == "":
        messagebox.showwarning(title="Incomplete submission!!", message="Please fill all the blocks. Empty blocks are not accepted!")
    else:
        proceed = messagebox.askyesnocancel(title="Do you want ot save your password?", message=f"The details are:\nWebsite: {website_name.get()}\nEmail/Username: {email_name.get()}\nPassword: {password_details.get()}")
        if proceed == True:
            with open("password_manager.txt", "a") as data:
                data.write(f"{website_name.get()} | {email_name.get()} | {password_details.get()}\n")
                website_name.delete(0, END)
                password_details.delete(0, END)
                website_name.focus()
                messagebox.showinfo(title="Confirmation", message="Password has been successfully added!")
        elif proceed == None:
            window.destroy()
        else:
            website_name.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

# LOGO
canvas = Canvas(window, width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = img)
canvas.grid(column=1, row=0, sticky= NE)

# WEBSITE
website = Label(text= "Website: ")
website.grid(column=0, row=1, sticky= E)

website_name = Entry(width=45)
website_name.grid(column=1, row=1, columnspan=2, sticky= W)
website_name.focus()

# EMAIL
email = Label(text= "Email/Username: ")
email.grid(column=0, row=2, sticky= E)

email_name = Entry(width=45)
email_name.grid(column=1, row=2, columnspan=2, sticky= W)
email_name.insert(0, "arcadiafelis@gmail.com")

# PASSWORD
password = Label(text= "Password: ")
password.grid(column=0, row=3, sticky= E)

password_details = Entry(width=25)
password_details.grid(column=1, row=3, sticky= W)

# GENERATE PASSWORD
generate = Button(text="Generate Password", width=16, command=generate_password)
generate.grid(column=2, row=3, sticky= W)

# SAVE PASSWORD
add = Button(text="Add", width=42, command=save_password)
add.grid(column=1, row=4, columnspan=2, sticky= W)


window.mainloop()