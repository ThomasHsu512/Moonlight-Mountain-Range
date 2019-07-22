#Our class function file
def polygon(t,d,s):
    a = 360/s
    for times in range(s):
        t.forward(d)
        t.right(a)
def polygonFill(t,d,s,c):#parameters
    a = 360 / s
    t.color(c)
    t.begin_fill()
    for times in range(s):
            t.forward(d)
            t.right(a)
    t.end_fill()

def moveTo(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

