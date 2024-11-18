from turtle import Turtle
import time

class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.xcor = xcor
        self.ycor = ycor
        self.configure()


    def configure(self):
        self.penup()
        self.shape('square')
        self.setheading(90)
        self.color('white')
        self.shapesize(stretch_wid = 1.0, stretch_len = 5.0)
        self.setheading(90)
        self.goto(x= self.xcor, y= self.ycor)

    def up(self):
        self.fd(50)

    def down(self):
        self.backward(50)