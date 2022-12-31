import turtle
turtle.title("Heart by Yahyobek")

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.hideturtle()
t.goto(0,-10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-75,130)
t.pendown()
t.color('white')
t.write("I Love You",font=("Verdana",20,"bold"))

t.penup()
t.goto(-70,-100)
t.pendown()
t.color('white')
t.write("Ziyodaxon",font=("Verdana",30,"bold"))

turtle.done()
