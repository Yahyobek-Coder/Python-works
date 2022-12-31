import  turtle

won = turtle.Screen()
won.bgcolor("black")
won.setup(width=800,height=600)
won.title("Telegram logo by Yahyobek")
r = turtle.Turtle()
r.pensize(4)

# for the blue circle

r.pu()
r.goto(0,-170)
r.pd()
r.pensize(4)
r.pencolor("royal blue")
r.begin_fill()
r.color("royal blue")
r.circle(180,385)
r.end_fill()


r.speed(1)
r.begin_fill()
r.color("white")
r.pencolor("white")
r.lt(108)
r.pu()
r.fd(75)
r.pd()
r.fd(90)
r.rt(90)
r.fd(110)
r.lt(173)
r.fd(112)
r.rt(79)
r.fd(70)
r.rt(120)
r.fd(190)
r.rt(125)
r.fd(188)
r.end_fill()

r.penup()
r.goto(-170,-270)
r.pendown()
r.color("royal blue")
r.write("Telegram", font=("Vardana", 50, "bold"))

r.hideturtle()
turtle.done()
