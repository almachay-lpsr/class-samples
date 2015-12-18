import turtle
import random
from Tkinter import *

# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

def rsquare(myTurtle):
        myTurtle.right(90)
        myTurtle.forward(100)
	time = 0
	while time > 4:
		 myTurtle.right(90)
       		 myTurtle.forward(100)
		 time = time + 1
colorlist = ['red','yellow','pink','green','black','purple']
# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
bwd = Button(frame,text='bwd', command=lambda: shawn.backward(50))
left = Button(frame, text='left',command=lambda: shawn.left(90))
right = Button(frame,text='right',command=lambda: shawn.right(90))
penup = Button(frame,text='penup', command=lambda: shawn.penup())
pendown = Button(frame,text='pendown', command=lambda: shawn.pendown())
color = Button(frame, text="random color", command=lambda: shawn.color(random.choice(colorlist)))
square = Button(frame,text="square", command=lambda: rsquare(shawn))


# put it all together
fwd.pack(side=LEFT)
bwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
color.pack(side=LEFT)
square.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
