from turtle import Turtle, Screen

tim = Turtle()

def move_forwards():
    tim.fd(10)

print(tim.pos()[0])

screen = Screen()

screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()