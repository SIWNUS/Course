from turtle import Turtle, Screen
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

class CarManager():
    
    def __init__(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.list = []
        # self.generate()

    def generate(self):
        if random.randint(1, 6) == 1:
            car = Turtle('square')
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2.0, stretch_wid=1.0)
            car.goto(290, random.randint(-250, 250))
            car.setheading(180)
            self.list.append(car)

    def move(self):
        for car in self.list:
            car.fd(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
