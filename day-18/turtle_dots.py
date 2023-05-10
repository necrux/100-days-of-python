#!/usr/bin/env python3

import turtle
#import colorgram
from random import choice
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.width(20)
tim.speed(0)
tim.hideturtle()
turtle.colormode(255)

colors = [(198, 32, 12), (231, 242, 250), (250, 16, 237), (39, 190, 76), (38, 69, 217), (237, 5, 226), (229, 46, 159),
          (27, 157, 39)]
#def get_colors():
#    """Get a color palette from an image using colorgram.py"""
#    color_palette = []
#    colors = colorgram.extract('image.jpg', 10)
#    for rgb in colors:
#        r = rgb.rgb[0]
#        b = rgb.rgb[1]
#        g = rgb.rgb[2]
#        new_color = (r, g, b)
#        color_palette.append(new_color)
#    return color_palette


def new_line(vertical):
    tim.setx(0)
    tim.sety(vertical)


def draw_row(spacing):
    color = choice(colors)
    tim.color(color)
    tim.pendown()
    tim.forward(0)
    tim.penup()
    tim.forward(spacing)


y_axis = 0
for _ in range(10):
    for _ in range(10):
        draw_row(50)
    y_axis += 50
    new_line(y_axis)

screen = Screen()
screen.exitonclick()
