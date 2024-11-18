from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color('black')
        self.board()

    def board(self):
        self.goto(-290, 250)
        self.write(f"LEVEL: {self.level}", font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
