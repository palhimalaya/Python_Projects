# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('spot-painting.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

color_list = [(233, 233, 236), (233, 232, 230), (233, 230, 233), (223, 233, 228), (40, 94, 151), (183, 42, 74),
              (228, 207, 97), (211, 154, 85), (181, 169, 29), (140, 88, 58)]
turtle.colormode(255)
timmy = Turtle()
screen = Screen()
timmy.speed("fastest")
timmy.penup()


def random_color():
    random_colors = random.choice(color_list)
    return random_colors


def print_dot():
    timmy.setheading(180)
    timmy.forward(200)
    timmy.setheading(270)
    timmy.forward(200)
    timmy.setheading(0)
    for _ in range(10):
        timmy.dot(40, random_color())
        for _ in range(9):
            timmy.forward(50)
            timmy.dot(40, random_color())
        go_back()


def go_back():
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    for _ in range(9):
        timmy.forward(50)
    timmy.setheading(0)


print_dot()
timmy.hideturtle()
screen.exitonclick()
