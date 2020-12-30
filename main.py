from colorgram import extract
from turtle import Turtle, Screen
import random

jojo = Turtle()
screen = Screen()
screen.colormode(255)
jojo.hideturtle()
Screen().screensize(300, 300)

# Extract the colors
# color_objects = extract('hisrt.jpg', 30)
colors = [(231, 85, 205), (228, 89, 148), (120, 186, 167), (216, 227, 222), (162, 19, 11), (31, 160, 111),
          (234, 45, 81), (175, 14, 19), (124, 145, 177), (5, 36, 99), (189, 23, 186), (207, 23, 65), (26, 43, 131),
          (10, 76, 40), (243, 5, 202), (14, 40, 63), (86, 22, 14), (135, 99, 84), (48, 74, 167), (4, 140, 65),
          (173, 149, 134), (39, 19, 22), (49, 195, 150), (228, 161, 171), (219, 69, 63), (73, 188, 134),
          (173, 175, 204)]


#
# for color in color_objects:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     rbg = r, b, g
#     colors.append(rbg)
# print(colors)

# Random color
def random_color():
    r_color = random.choice(colors)
    return r_color


jojo.speed(0)


def paint(dots):
    jojo.penup()
    # set initial position
    x = 250
    y = 250
    jojo.setx(-x)
    jojo.sety(-y)
    distance = 50
    for _ in range(dots):
        jojo.dot(15, random_color())
        jojo.forward(50)
        if jojo.pos()[0] == x:
            jojo.setpos(-x, -y + distance)
            distance += 50


paint(100)

# Screen
screen.exitonclick()
print(jojo.pos())
