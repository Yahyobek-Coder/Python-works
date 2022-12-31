from turtle import *
title("Animation by Yahyobek")
t = Turtle()
#t.screen.setup(450, 450)
t.screen.bgcolor('black')
t.pensize(2)
t.speed(50)
t.color('red')
for x in range(36):
    t.circle(100)
    t.lt(10)

t.screen.exitonclick()

