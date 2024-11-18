from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="White", font=("Ariel", 14, "italic"))
        self.score.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.c_text = self.canvas.create_text(150, 125, text="Hey, I want to do something but i can't because there is no way to know about the future events beforehand.",width=250, font=("Ariel", 14, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image= self.true_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image= self.false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.next()

        self.window.mainloop()

    def next(self):
        if self.quiz.still_has_questions():
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.c_text, text=text)
        else:
            self.canvas.itemconfig(self.c_text, text="You have reached the end of this quiz...")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        answer = "True"
        self.feedback(self.quiz.check_answer(user_answer=answer))
        
    def answer_false(self):
        answer = "False"
        self.feedback(self.quiz.check_answer(user_answer=answer))
            
    def feedback(self, correct):
        if correct:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")

        self.window.after(2000, self.reset_color)
        self.score.config(text=f"Score: {self.quiz.score}")
        self.next()

    def reset_color(self):
        self.canvas.config(bg="white")