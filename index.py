import turtle
t = turtle.Pen()
t.width(2)
turtle.title('Script Animation by Yahyobek')
colors=[ 'red', 'blue', 'green', 'aqua', 'yellow', 'pink', 'royal blue', 'white', 'purple', 'orange', ]
turtle.bgcolor('black')
number_of_circle= int(turtle.numinput('Ajoyib shakl',
'nechta doira chizilsin',0))
for x in range(number_of_circle):
    turtle.bgcolor('black')
    t.pencolor(colors[x%10])
    t.circle(100)
    t.left(360/number_of_circle)
