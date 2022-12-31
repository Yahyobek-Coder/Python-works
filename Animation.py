import turtle
turtle.title("Big Spiral by Yahyobek")

t=turtle.Turtle()
s = turtle.Screen()
s.bgcolor("white")
t.pencolor("black")
a = 0
b = 0
t.speed(100000)
move=1
for i in range(360):
	t.pendown()
	t.right(move)
	t.forward(100)
	t.right(30)
	t.forward(60)
	t.left(30)
	t.forward(30)
	t.penup()
	t.home()
	move = move+1
