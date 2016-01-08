import turtle
 
def drawTriPattern(myTurtle):
	myTurtle.forward(20)
	myTurtle.left(120)
	myTurtle.forward(10)
	myTurtle.left(120)
        myTurtle.forward(10)
        myTurtle.left(120)
        myTurtle.forward(10)
        myTurtle.left(120) 
	myTurtle.forward(10)
       	myTurtle.left(120)
       	myTurtle.forward(10)
def drawTriangle(myTurtle):
	time = 0
	while time < 10:
		drawTriPattern(myTurtle)
		King.left(120)
		King.forward(10)
		time = time + 1
def side(myTurtle):
	myTurtle.penup()
	myTurtle.goto(65,45)
	myTurtle.pendown()
	myTurtle.forward(20)
        myTurtle.left(120)
        myTurtle.forward(10)
        myTurtle.left(120)
        myTurtle.forward(10)
        myTurtle.left(120)
        myTurtle.forward(10		
King = turtle.Turtle()

drawTriangle(King)
side(King)
turtle.exitonclick()
