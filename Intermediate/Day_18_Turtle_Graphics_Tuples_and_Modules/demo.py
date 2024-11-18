from turtle import Turtle,Screen,colormode
from random import choice, randint

colormode(255)

timmy = Turtle()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)


# for i in range(3, 11):
#     timmy.pensize(10)
#     timmy.speed(0)
#     timmy.pencolor(choice(colors))
#     draw_shape(i)

angle = [90, 180, 270, 0]

def random_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

# def random_walk(size, distance, speed, degree):
#     timmy.pensize(size)
#     timmy.speed(speed)    
#     timmy.forward(distance)
#     timmy.setheading(degree)

# for _ in range(200):
#     color = random_colors()
#     timmy.pencolor(color)
#     random_walk(10, 25, 0, choice(angle))

def spirograph(increase):
    for _ in range(int(360/increase)):
        timmy.pensize(2)
        timmy.pencolor(random_colors())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + increase)

timmy.speed(0)
spirograph(5)


screen = Screen()

screen.exitonclick()
