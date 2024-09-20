from turtle import *
import turtle

size=300

screen = Screen()
screen.screensize(400,400,"white")

def draw_petal(turtle, radius):
    heading = turtle.heading()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.setheading(heading)

def petal(my_radius,my_petals,c):
    for _ in range(my_petals):
        bob.color(c)
        bob.fillcolor(c)
        bob.begin_fill()
        draw_petal(bob, my_radius)
        bob.left(360 / my_petals)
        bob.end_fill()
        bob.hideturtle()

bob = Turtle()
pen = Pen()
bob.speed(1000)
pen.speed(1000)

flag=0

def fillshape(steps,radius,c1,c2):
    if(flag==0):
        c2=c1
    pen.color(c1)
    pen.fillcolor(c2)
    pen.begin_fill()
    pen.down()
    if(steps!=0):
        pen.circle(radius,steps=steps)
    else:
        pen.circle(radius)
    pen.end_fill()
    pen.up()
    pen.hideturtle()

pen.goto(0,-size)
c1="orange"
c2="orange"

fillshape(0,size,c1,c2)

pen.goto(0,0)
x=0
turtle.delay(0)
colormode(255)
no=12

for i in range (no*6):
    pen.goto(0,0)
    pen.right(30)
    if(i<no):
        c1="darkred"
        fillshape(4,size/2,c1,c2)

        my_radius = 270
        my_petals = 36

        if(i%no==11):
            for _ in range(my_petals):
                bob.color('black')
                bob.fillcolor('yellow')
                bob.begin_fill()
                draw_petal(bob, my_radius)
                bob.left(360 / my_petals)
                bob.end_fill()

    elif(i<no*2):
        c1="orangered"
        fillshape(4,size/2-10,c1,c2)

    elif(i<no*3):
        c1="orange"
        fillshape(4,size/2-20,c1,c2)

        my_radius = 240
        my_petals = 36

        if(i%no==11):
            for _ in range(my_petals):
                bob.color('black')
                bob.fillcolor('tomato')
                bob.begin_fill()
                draw_petal(bob, my_radius)
                bob.left(360 / my_petals)
                bob.end_fill()

    elif(i<no*4):
        c1="white"
        fillshape(4,size/2-30,c1,c2)

    elif(i<no*5):
        c1="lightblue"
        fillshape(4,size/2-40,c1,c2)

    elif(i<no*6):
        c1="red"
        fillshape(4,size/2-50,c1,c2)

x=30
pen.right(15)
pen.pensize(10)
for i in range(12):

    pen.goto(0,0)
    c1="white"
    fillshape(2,130,c1,c2)
    pen.right(30)

for i in range(12):

    pen.goto(0,0)
    c1="orange"
    fillshape(2,120,c1,c2)
    pen.right(30)

for i in range(12):

    pen.goto(0,0)
    c1="orangered"
    fillshape(2,110,c1,c2)
    pen.right(30)

for i in range(12):

    pen.goto(0,0)
    c1="darkred"
    fillshape(2,100,c1,c2)
    pen.right(30)

pen.left(15)
pen.width(1)
for i in range(no*3):

    if(i<no):
        pen.goto(0,0)
        c1="pink"
        fillshape(4,90,c1,c2)
        pen.right(30)

    elif(i<no*2):
        pen.goto(0,0)
        c1="darkgreen"
        fillshape(4,90,c1,c2)
        pen.right(30)

    elif(i<no*3):
        pen.goto(0,0)
        c1="purple"
        fillshape(4,90,c1,c2)
        pen.right(30)

    if(i%no==11):
        pen.right(12)

size2 = 150
pen.goto(0,-size2)
pen.left(35)
c1="brown"
fillshape(0,size2,c1,c2)

bob.speed(1000)


petal(150,12,'crimson')
petal(110,12,'lightblue')
petal(70,12,'purple')

pen.width(4)
pen.speed(2000)

flag=1

bob.hideturtle()
pen.hideturtle()
pen.hideturtle()

# Add this line to keep the window open
turtle.done()