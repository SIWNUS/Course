from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = int(0)
CHECKMARK = "✔"

# ---------------------------- TIMER VARIABLES ------------------------------- # 
work_sec = WORK_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60
timer_running = True

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_running, REPS
    canvas.itemconfig(timer, text="00:00")
    REPS = int(0)
    timer_running = False

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global work_sec, short_break_sec, long_break_sec, REPS, timer_running, CHECKMARK
    REPS += 1

    count = REPS // 2
    if count > 4:
        count -= 4
    check.config(text=((count) * CHECKMARK))

    if REPS % 8 == 0:
        window.deiconify()
        count_down(long_break_sec)
        title.config(text="Long Break")
    elif REPS % 2 == 0:
        window.deiconify()
        count_down(short_break_sec)
        title.config(text="Short Break")
    else:
        window.withdraw()
        count_down(work_sec)
        title.config(text="Work Time")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(tot_sec):
    global timer_running
    mins = tot_sec // 60
    sec = tot_sec % 60
    canvas.itemconfig(timer, text=f"{mins:02}:{sec:02}")
    if tot_sec > 0 and timer_running:
        window.after(1000, count_down, tot_sec - 1)
    elif timer_running:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=90, pady=50, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), highlightthickness=0, bg=YELLOW)
title.grid(column=1, row=0)

canvas = Canvas(width=200 , height=224, bg=YELLOW, highlightthickness=0)
pomodoro_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_image)
timer = canvas.create_text(100, 140, text="00:00", justify="center", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1 , row=1)

start = Button(text="Start", fg="blue", highlightthickness=0, command= start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", fg="blue", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check.grid(column=1, row=3)

window.mainloop()