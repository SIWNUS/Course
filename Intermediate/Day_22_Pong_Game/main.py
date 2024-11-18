from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

paddle1 = Paddle(370, 0)
paddle2 = Paddle(-370, 0)

ball = Ball()
score = Score()


screen = Screen()
screen.title('Pong')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

screen.listen()

screen.onkey(key='Up', fun=paddle1.up)
screen.onkey(key='Down', fun=paddle1.down)
screen.onkey(key='w', fun=paddle2.up)
screen.onkey(key='s', fun=paddle2.down)

game_on = True
while game_on:
    time.sleep(0.075)
    screen.update()
    ball.move_start()

    if ball.xcor() > 370:
        score.update_1()
        ball.next_round()

    if ball.xcor() < -370:
        score.update_2()
        ball.next_round()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if paddle1.distance(ball) < 50 and ball.xcor() > 350 or  paddle2.distance(ball) < 50 and ball.xcor() < -350:
        ball.speedup()
        ball.bounce_x()

screen.mainloop()