import turtle
from turtle import *

turtle.bgcolor("black")
turtle.speed(0)
turtle.right(0)

for i in range(10):
    for k in range(10):
        for l in ['DeepSkyBlue', 'purple', 'VioletRed']:
            turtle.width(2)
            turtle.right(0)
            turtle.up()
            turtle.forward(3)
            turtle.down()
            turtle.color(1)
            turtle.left(100)
            turtle.circle(150-1*6,110)
            turtle.left(70)
            turtle.color(1)
            turtle.circle(150-1*6,110)

turtle.done()