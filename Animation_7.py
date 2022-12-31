import turtle
turtle.title("Spiral by Yahyobek")
window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor('black')
t.color('aqua')

t.penup()
for i in range(10, 100, 10): 
    t.right(90)  
    t.forward(i)
    t.right(270)
    t.pendown()  
    t.circle(i)  
    t.penup()   
    t.home()   
window.mainloop()
