import turtle
turtle.title("Spiral by Yahyobek")
win=turtle.Screen()
turtle.bgcolor("black")
t=turtle.Turtle()
for i in range (6) :
    for i in range (4) :
        t.pu()
        t.goto(0,0)
        t.pd()
        t.pensize(3)
        t.pencolor("aqua")
        t.circle(100,steps=6)
        t.right(100)
t.speed(0)