from turtle import Turtle, Screen
import time
from game_logic import Snake, Food, ScoreBoard

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
scoreboard.display()
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on =True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.body:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.mainloop()

