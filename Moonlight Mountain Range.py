import turtle
b=turtle.Turtle()
from myFunctions import*
turtle.colormode(255)
b.speed(111)
b.pensize(15)
b.shape("circle")
turtle.bgcolor("black")
x=0
y=0

#1600x900

def moveToDR(t,x,y):
    t.penup()
    t.home()
    t.goto(x,y)
    t.pendown()

#sky
moveToDR(b,x-800,y+450)
for times in range(150):
    b.color(0,0,0+times)
    b.forward(1600)
    b.right(90)
    b.forward(2)
    b.right(90)
    b.forward(1600)
    b.left(90)
    b.forward(2)
    b.left(90)

#mountains
moveToDR(b,x-800,y-400)
b.color(255,255,255)
b.begin_fill()
b.left(90)
b.forward(325)
b.right(45)

t=500

for times in range(3):
    b.forward(times*5+150)
    b.right(85)
    b.forward(times*5+200)
    b.left(87)

b.forward(times*5+250)
b.right(83)
b.forward(times*5+187)
b.left(79)

for times in range(2):
    b.forward(times*5+200)
    b.right(86)
    b.forward(times*5+250)
    b.left(83)

b.right(123)
b.forward(350)

b.goto(x-800,y-400)
b.end_fill()

#mountaingradient

moveToDR(b,x-800,y-235)
for times in range(180):
    b.color(times+75,times+75,times+75)
    b.forward(1600)
    b.left(90)
    b.forward(0.35)
    b.left(90)
    b.forward(1600)
    b.right(90)
    b.forward(0.35)
    b.right(90)

    
#----mountainshade---------------------------------
moveToDR(b,0,0)
b.pensize(1)
b.color(0,0,70)

#1stshade
moveTo(b,x-694,y+41)
b.begin_fill()
b.right(58)
b.forward(500)
b.left(90)
b.forward(50)
b.left(87)
b.forward(315)
b.goto(x-694,y+41)
b.end_fill()

#2ndshade
moveTo(b,x-433,y+24)
b.begin_fill()
b.right(180)
b.forward(500)
b.left(90)
b.forward(53)
b.left(85)
b.forward(320)
b.goto(x-433,y+24)
b.end_fill()

#3rdshade
moveTo(b,x-170,y+20)
b.begin_fill()
b.right(180)
b.forward(500)
b.left(90)
b.forward(55)
b.left(81)
b.forward(327)
b.goto(x-170,y+20)
b.end_fill()

#4thshade
moveTo(b,x+165,y+98)
b.begin_fill()
b.right(180)
b.forward(500)
b.left(90)
b.forward(50)
b.left(77.2)
b.forward(368)
b.goto(x+165,y+98)
b.end_fill()

#5thshade
moveTo(b,x+468,y+141)
b.begin_fill()
b.right(150)
b.forward(500)
b.left(90)
b.forward(50)
b.left(83.5)
b.forward(270)
b.goto(x+468,y+141)
b.end_fill()
#-------------------------------------------

#ground
b.color(0,60,0)

moveToDR(b,x-800,y-400)
b.begin_fill()
b.left(90)
b.forward(150)
b.right(90)
for times in range(16):
    b.left(3+times)
    b.forward(100+times)
    b.right(3+times)
    b.forward(100+times)
    
b.right(90)
b.forward(500)
b.goto(x-800,y-400)
b.end_fill()

moveToDR(b,x-800,y-400)
b.begin_fill()
b.left(90)
b.forward(200)
b.right(90)
for times in range(7):
    b.forward(75+times)
    b.right(5-times)

b.right(90)
b.forward(500)
b.goto(x-800,y-400)
b.end_fill()

#water
b.color(0,0,30)

moveToDR(b,x-800,y-450)
b.begin_fill()
b.left(90)
b.forward(150)
b.right(90)
for times in range(16):
    b.left(11-times)
    b.forward(100+times)
    b.right(13-times)
    b.forward(100+times)

b.goto(x-800,y-450)
b.end_fill()

#stars
    
moveToDR(b,x-400,y+360)
b.penup()
b.right(90)
b.pendown()
for times in range(2):
    b.penup()
    b.forward((times+0)*125)
    b.left(90)
    for times in range(5):
        b.penup()
        b.forward(200)
        b.pendown()
        b.color(255,255,240)
        b.stamp()
    moveTo(b,x-338,y+360)
    b.right(90)
    b.pendown()

#moon
moveToDR(b,x-475,y+80)
b.color(255,255,240)
b.begin_fill()
b.circle(150)
b.end_fill()

b.pensize(2)
for times in range(25):
    moveToDR(b,-475,80-times)
    b.color(255-7*times,255-7*times,240-7*times)
    b.circle(150+times)
    
#name
b.color(0,0,0)
moveTo(b,x-535,y+230)
b.write("Moonlight Mountain Range")



#grid
b.penup()
b.pensize(1)
b.home()
b.pendown()
b.color("red")
b.goto(0,225)
b.write(0,225)
b.goto(0,225)
b.goto(0,450)
b.goto(0,-225)
b.write(0,-225)
b.goto(0,-225)
b.goto(0,-450)
b.goto(0,0)
b.goto(400,0)
b.write(400,0)
b.goto(800,0)
b.goto(-800,0)
b.goto(-400,0)
b.write(-400,0)


b.ht()
turtle.done()




