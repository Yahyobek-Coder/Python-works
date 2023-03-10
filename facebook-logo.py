import turtle as tur
tur.speed(1)
tur.title("Facebook logo by Yahyobek")

tur.penup()
tur.goto(0,150)
tur.bgcolor("black")
tur.pendown()

tur.begin_fill()
tur.color("#0270d3")
tur.pensize(2)
tur.forward(150)
tur.circle(-50,90)
tur.forward(300)
tur.circle(-50,90)
tur.forward(300)
tur.circle(-50,90)
tur.forward(300)
tur.circle(-50,90)
tur.forward(150)
tur.end_fill()

tur.color("white")
tur.penup()
tur.goto(140,80)
tur.pendown()


tur.begin_fill()
tur.right(180)
tur.forward(50)
tur.circle(80,90)
tur.forward(50)
tur.right(90)
tur.forward(80)
tur.left(90)
tur.forward(40)
tur.left(90)
tur.forward(80)
tur.right(90)
tur.forward(160)
tur.left(90)
tur.forward(55)
tur.left(90)
tur.forward(160)
tur.right(90)
tur.forward(70)
tur.left(80)
tur.forward(45)
tur.left(100)
tur.forward(80)
tur.right(90)
tur.forward(40)
tur.circle(-40,90)
tur.forward(40)
tur.left(90)
tur.forward(45)
tur.end_fill()

tur.penup()
tur.color("white")
tur.goto(-80,200)
tur.pendown()
tur.write("""Facebook logo
    by  " YAHYOBEK " """,
font=('Arial', 15, 'bold'))
tur.right(90)
tur.begin_fill()
tur.forward(210)
tur.right(90)
tur.backward(55)
tur.left(90)
tur.backward(215)
tur.left(90)
tur.backward(55)
tur.right(90)
tur.forward(60)
tur.left(90)
tur.forward(25)
tur.right(90)
tur.forward(145)
tur.left(90)
tur.backward(25)
tur.left(90)
tur.forward(80)
tur.left(90)
tur.forward(40)
tur.done()
