import turtle
from tkinter import *
t = turtle.Turtle()
turtle.title('YouTube logo by Yahyobek')

turtle.bgcolor("black")
t.color("red")
t.begin_fill()
t.speed(1)
t.pensize(3)


def rectangle():
    t.circle(50,90)
    t.forward(100)
    t.circle(50,90)
    t.forward(200)
rectangle()
rectangle()
t.end_fill()

# white triangle
t.penup()
t.goto(-125,55)
t.pendown()
t.color("white")
t.begin_fill()
t.left(30)
t.forward(90)
t.left(120)
t.forward(90)
t.left(120)
t.forward(90)
t.end_fill()

t.penup()
t.goto(75,60)
t.pendown()
t.color("grey")
t.write("YouTube", font=("Vardana", 50, "bold"))
t.hideturtle()

turtle.done()