import colorgram # type: ignore
import turtle as t
from random import choice

def palette(colors):
    color_band_list = []
    for color in colors:
        rgb = color.rgb
        red = rgb.r
        green = rgb.g
        blue = rgb.b
        color_band = (red, green, blue)
        color_band_list.append(color_band)
    return color_band_list

palette_size = 39
colors = colorgram.extract('hirst.jpg', palette_size)
color_palette = palette(colors)
del color_palette[0: 3]

tim = t.Turtle()
t.colormode(255)

def my_hirst_paintaing():
    tim.teleport(-250, -225)
    for i in range(20):
        current_pos = tim.pos()
        for _ in range(20):
            c_pos = tim.pos()
            tim.dot(10, choice(color_palette))
            tim.teleport(c_pos[0] + 25, c_pos[1])
        tim.teleport(current_pos[0], current_pos[1] + 25)

my_hirst_paintaing()

screen = t.Screen()
screen.exitonclick()
