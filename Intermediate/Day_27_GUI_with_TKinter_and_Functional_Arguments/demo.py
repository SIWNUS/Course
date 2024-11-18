from tkinter import *

def click(new_text):
    my_label.config(text= new_text)

def click_new():
    button1.config(text= "Clicked", state="disabled")

# def get_spin():
#     print(spin.get())

# def get_scale(num):
#     print(num)

# def checkbutton_used():
#     print(check_status.get())

# def radio_used():
#     print(radio_status.get())

# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 600, height= 300)

my_label = Label(window, text="I am a label", font=("Ariel",24, "italic"))
my_label.grid(column=0, row=0)

button1 = Button(window, text="New Button", command= click_new)
button1.grid(column=2, row=0)

button = Button(window, text="Click me", command= lambda: click(input.get()))
button.grid(column=1, row=1)


input = Entry(width=30)
input.insert(END, string="Enter something")
input.grid(column=3, row=2)


# textbox = Text(height=6, width=30)
# textbox.insert(END, chars="This is for text")
# print(textbox.get("1.0", END))


# spin = Spinbox(from_= 0, to = 10, width = 10, command = get_spin)


# scale = Scale(from_= 0, to = 100, command = get_scale)


# check_status = IntVar()
# checkbutton = Checkbutton(text= "Is on?", variable = check_status, command = checkbutton_used)


# radio_status = IntVar()
# radio1 = Radiobutton(text="Option 1", value=1, variable=radio_status, command=radio_used)
# radio2 = Radiobutton(text="Option 2", value=2, variable=radio_status, command=radio_used)


# listbox = Listbox(height=4, justify="center")
# cars = ["Bugatti", "Lamborghini", "Koneinseigg", "Pagani"]
# for car in cars:
#     listbox.insert(cars.index(car), car)
# listbox.bind("<<ListboxSelect>>", listbox_used)


window.mainloop()