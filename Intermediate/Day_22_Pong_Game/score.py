from turtle import Turtle

STEP = 20
ALIGN = 'center'
FONT = ('Arial', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.display()

    def display(self):
        self.goto(0, 250)
        self.write("SCORE", align=ALIGN, font=FONT)
        self.goto(-100, 200)
        self.write(self.score_1, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.score_2, align=ALIGN, font=FONT)

    def update_1(self):
        self.score_1 += 1
        self.clear()  
        self.display()

    def update_2(self):
        self.score_2 += 1
        self.clear()  
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align=ALIGN, font=FONT)
