from turtle import Turtle

STEP = 20

class Snake():
    def __init__(self):
        self.list = []
        self.size = 3
        self.create_snake()
        self.head = self.list[0]

    def create_snake(self):
        shift_pos = 0
        for _ in range(self.size):
            snake = Turtle()
            snake.penup()
            snake.shape('square')
            snake.color('white')
            self.list.append(snake)
            current_pos = snake.pos()
            snake.teleport(current_pos[0] - shift_pos, current_pos[1])
            shift_pos += 20

    def move(self):
        for index in range(len(self.list) - 1, 0, -1):
            x = self.list[index - 1].xcor()
            y = self.list[index - 1].ycor()
            self.list[index].goto(x, y)
        self.list[0].fd(STEP)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        

