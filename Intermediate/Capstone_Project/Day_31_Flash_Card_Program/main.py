from tkinter import *
import pandas as pd # type: ignore
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ---------------------------- READ FILE ------------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/frequent_words.csv")

data_dict = data.to_dict(orient="records")

# ---------------------------- BUTTON SETUP ------------------------------- #
def next_card():
    global timer, current_card
    window.after_cancel(timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(lang, text="Japanese Romaji", fill="black")
    canvas.itemconfig(word, text=f"{current_card['Romaji']}", fill="black")
    canvas.itemconfig(c_image, image = front)
    timer = window.after(3000, answer_card)

# ---------------------------- ANSWER CARD ------------------------------- #
def answer_card():
    global current_card
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(c_image, image = back)    

def is_correct():
    global data_dict, current_card
    for item in data_dict:
        if item == current_card:
            data_dict.remove(item)
    to_learn = pd.DataFrame(data_dict)
    to_learn.to_csv("data/words_to_learn.csv", index=False)

    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
c_image = canvas.create_image(400, 263, image = front)
lang = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="Japanese Romaji")
word = canvas.create_text(400, 263, font=("Ariel", 40, "bold"), text="")
timer = window.after(3000, answer_card)
canvas.grid(column=0, columnspan=2, row=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_correct)
right.grid(column=1, row=1)

next_card()

window.mainloop()
