import turtle
from turtle import *

turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()

for i in range(120):
    turtle.color("red")
    turtle.circle(i)
    turtle.color("orange")
    turtle.circle(i*0.8)
    turtle.right(3)
    turtle.forward(3)

turtle.done()