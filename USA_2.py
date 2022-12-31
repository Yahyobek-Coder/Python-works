import turtle
import time
screen = turtle.getscreen()
screen.bgcolor("black")
screen.title("USA Flag ")
oogway = turtle.Turtle()
oogway.speed(10)
oogway.penup()
oogway.shape("turtle")
flag_height = 250
flag_width = 471
start_x = -237
start_y = 125
stripe_height = flag_height/13
stripe_width = flag_width
star_size = 10
def draw_fill_rectangle(x, y, height, width, color):
    oogway.goto(x,y)
    oogway.pendown()
    oogway.color(color)
    oogway.begin_fill()
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.end_fill()
    oogway.penup()
def draw_star(x,y,color,length) :
    oogway.goto(x,y)
    oogway.setheading(0)
    oogway.pendown()
    oogway.begin_fill()
    oogway.color(color)
    for turn in range(0,5) :
        oogway.forward(length)
        oogway.right(144)
        oogway.forward(length)
        oogway.right(144)
    oogway.end_fill()
    oogway.penup()
def draw_stripes():
    x = start_x
    y = start_y    
    for stripe in range(0,6):
        for color in ["red", "white"]:
            draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
            y = y - stripe_height           
    draw_fill_rectangle(x, y, stripe_height, stripe_width, 'red')
    y = y - stripe_height
def draw_square():
    square_height = (7/13) * flag_height
    square_width = (0.76) * flag_height
    draw_fill_rectangle(start_x, start_y, square_height, square_width, 'navy')
def draw_six_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    y = 112
    for row in range(0,5) :
        x = -222
        for star in range (0,6) :
            draw_star(x, y, 'white', star_size)
            x = x + gap_between_stars
        y = y - gap_between_lines
def draw_five_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    y = 100
    for row in range(0,4) :
        x = -206
        for star in range (0,5) :
            draw_star(x, y, 'white', star_size)
            x = x + gap_between_stars
        y = y - gap_between_lines
time.sleep(5)
draw_stripes()
draw_square()
draw_six_stars_rows()
draw_five_stars_rows()
oogway.hideturtle()
screen.mainloop()
