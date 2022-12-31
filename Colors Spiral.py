import turtle #import turtle
turtle.title("Best Colors Spiral by Yahyobek")

colors = ['red','yellow','green','purple','blue','orange'] #defining the colors

t = turtle.Pen() #setup the turtle pen

turtle.bgcolor('black') #background

#movements

for x in range(500): # no, of iteration more iteration more big

	t.pencolor(colors[x%6]) #set the color

	t.width(x/50+1.3) #set the width

	t.forward(x) # pointer of that triangle if backward it will make from edge of removed no draw

	t.left(59) #rotate the turtle with angle, less angle more circle like structure
