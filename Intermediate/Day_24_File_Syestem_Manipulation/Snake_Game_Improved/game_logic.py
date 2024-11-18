from turtle import Turtle
import random

STEP = 20
ALIGN = 'center'
FONT = ('Arial', 24, 'normal')

class Snake:
    def __init__(self):
        self.list = []
        self.size = 3
        self.create_snake()
        self.head = self.list[0]
        self.body = self.list[1: ]

    def create_snake(self):
        shift_pos = 0
        for _ in range(self.size):
            snake = Turtle()
            snake.penup()
            snake.shape('square')
            snake.color('white')
            self.list.append(snake)
            current_pos = snake.pos()
            snake.goto(current_pos[0] - shift_pos, current_pos[1])
            shift_pos += 20

    def move(self):
        for index in range(int(len(self.list)) - 1, 0, -1):
            x = self.list[index - 1].xcor()
            y = self.list[index - 1].ycor()
            self.list[index].goto(x, y)
        self.list[0].fd(STEP)

    def grow(self):
        snake = Turtle()
        snake.penup()
        snake.shape('square')
        snake.color('white')
        
        current_pos = self.list[-1].pos()
        if self.list[-1].heading() == 270:
            snake.goto(current_pos[0], current_pos[1] + 20)
        elif self.list[-1].heading() == 90:
            snake.goto(current_pos[0], current_pos[1] - 20)
        elif self.list[-1].heading() == 180:
            snake.goto(current_pos[0] + 20, current_pos[1])
        elif self.list[-1].heading() == 0:
            snake.goto(current_pos[0] + 20, current_pos[1])
        
        self.list.append(snake)
        snake.showturtle()

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

    def reset(self):
        for snake in self.list:
            snake.goto(1000, 1000)
        self.list.clear()
        self.create_snake()
        self.head = self.list[0]
        self.body = self.list[1: ]
        
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.pencolor('blue')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as score:
            self.high_score = int(score.read())
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 260)
        self.display()

    def display(self):
        self.clear() 
        self.write(f"Score = {self.score}, High Score = {self.high_score}", align=ALIGN, font=FONT)

    def update(self):
        self.score += 1 
        self.display()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over!", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("score.txt", "w") as score:
                score.write(str(self.high_score))
        self.score = 0
        self.display()


