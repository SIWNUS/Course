from tkinter import *

def convert(num):
    val = round(float(num) * 1.609344, 6)
    value.config(text= val)

window = Tk()
window.title("Mile to km convertor")
window.config(padx=20, pady=20)

entry = Entry(window, width= 15)
entry.grid(column= 1, row= 0)

miles = Label(window, text="Miles")
miles.grid(column= 2, row=0)

equal = Label(window, text="is equal to")
equal.grid(column=0, row=1)

value = Label(window, text="0")
value.grid(column=1, row= 1)

km =Label(window, text="km")
km.grid(column=2, row=1)

calculate = Button(window, text="Calculate", command= lambda: convert(entry.get()))
calculate.grid(column=1, row=2)


window.mainloop()