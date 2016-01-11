import turtle

def drawSquare(myTurtle):
# first square
        myTurtle.color('blue')
        myTurtle.backward(20)
        myTurtle.left(90)
        myTurtle.backward(20)
        myTurtle.penup()
        myTurtle.left(90)
        myTurtle.backward(20)
        myTurtle.pendown()
        myTurtle.left(90)
        myTurtle.backward(20)
# second square 
        myTurtle.color('red')
        myTurtle.left(90)
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(20)
        myTurtle.right(90)
# third half
        myTurtle.color('green')
        myTurtle.forward(20)
# fourth square
        myTurtle.color('yellow')
        myTurtle.forward(20)
        myTurtle.left(90)
        myTurtle.forward(20)
        myTurtle.left(90)
        myTurtle.forward(20)
        myTurtle.left(90)
        myTurtle.forward(20)
# back to square three  
        myTurtle.color('green')
        myTurtle.right(90)
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(20)
        
        
def drawFiveSqaure(myTurtle):
        time = 0
        while time < 4:
          drawSquare(shawn)
          drawSquareFive(shawn)
          shawn.right(50)
          shawn.penup()
          shawn.forward(30)
          shawn.pendown()
          shawn.left(50)
          time = time + 1
        
  
def drawSquareFive(myTurtle):
            myTurtle.color('blue')
            myTurtle.forward(20)
            myTurtle.right(90)
            myTurtle.forward(20)
            myTurtle.right(90)
            myTurtle.forward(20)
            myTurtle.right(90)
            myTurtle.forward(20)
# second square 
            myTurtle.color('red')
            myTurtle.right(90)
            myTurtle.backward(20)
            myTurtle.left(90)
            myTurtle.backward(20)
            myTurtle.left(90)
# third half
            myTurtle.color('green')
            myTurtle.backward(20)
# fourth square
            myTurtle.color('yellow')
            myTurtle.backward(20)
            myTurtle.right(90)
            myTurtle.backward(20)
            myTurtle.right(90)
            myTurtle.backward(20)
            myTurtle.right(90)
            myTurtle.backward(20)
# back to square three  
            myTurtle.color('green')
            myTurtle.left(90)
            myTurtle.backward(20)
            myTurtle.left(90)
            myTurtle.backward(20)
            myTurtle.left(90)
            myTurtle.backward(20)

shawn = turtle.Turtle()
shawn.speed(50)

drawSquare(shawn)
drawFiveSqaure(shawn)
drawSquareFive(shawn)



