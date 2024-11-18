from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.configure()
        self.x_move = 10
        self.y_move = 10

    def configure(self):
        self.penup()
        self.speed('slowest')
        self.shape('circle')
        self.color('white')
        self.setheading(random.choice([45, 135, 225, 315]))

    def move_start(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def speedup(self):
        self.x_move *= 1.1
        self.y_move *= 1.1


    def next_round(self):
        self.goto(0, 0)  # Reset to center
        self.setheading(random.choice([random.randint(45, 135), random.randint(225, 315)]))  # Random direction
        self.x_move = 10
        self.y_move = 10