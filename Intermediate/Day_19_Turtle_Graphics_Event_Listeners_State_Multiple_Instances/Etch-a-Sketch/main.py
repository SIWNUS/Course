from turtle import Turtle, Screen

tim = Turtle()
start_pos = tim.pos()

def move_forwards():
    tim.fd(20)

def move_backwards():
    tim.backward(20)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clear():
    tim.penup()
    tim.home()
    tim.clear()


screen = Screen()

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.mainloop()