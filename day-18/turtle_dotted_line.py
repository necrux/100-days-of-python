#!/usr/bin/env python3

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.speed(10)

directions = [0, 90, 180, 270]

for _ in range(4):
    for n in range(100):
        if n % 2 == 0:
            tim.penup()
        else:
            tim.pendown()
        tim.forward(5)
    tim.right(90)

screen = Screen()
screen.exitonclick()
