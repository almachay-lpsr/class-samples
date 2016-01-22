# the start of everything to draw a cube
import turtle

# the start to do the first part of the rhombus
def shape(myTurtle):

# the clolor of the shape is light blue
          myTurtle.color('light blue')
# to fill in the shape instead of the color
          myTurtle.begin_fill()
# the start where we draw one rhombus
          myTurtle.right(25)
          myTurtle.forward(30)
          myTurtle.right(120)
          myTurtle.forward(30)
          myTurtle.right(60)
          myTurtle.forward(30)
          myTurtle.right(120)
          myTurtle.forward(30)
# the color is finished
          myTurtle.end_fill()
# the penup is so it doesn't draw anything
          myTurtle.penup()
          myTurtle.right(60)
          myTurtle.forward(30)
          myTurtle.pendown()
# the pendown is to be able to draw again

# the second part of the rhombus
def base(myTurtle):
# it's color is blue
          myTurtle.color('blue')
# to fill in the shape instead of the color
          myTurtle.begin_fill()
          myTurtle.right(60)
          myTurtle.forward(30)
          myTurtle.right(60)
          myTurtle.forward(30)
          myTurtle.right(120)
          myTurtle.forward(30)
          myTurtle.right(60)
          myTurtle.forward(30)
          myTurtle.end_fill()

# the final part of the shape and it's finished making a cube
def otherSide(myTurtle):
          myTurtle.backward(30)
# to fill in the shape instead of the color
          myTurtle.color('blue')
          myTurtle.begin_fill()
          myTurtle.left(120)
          myTurtle.forward(30)
          myTurtle.left(120)
          myTurtle.forward(30)
          myTurtle.left(60)
          myTurtle.forward(30)
          myTurtle.end_fill()

# this is to make one row filled with cubes          
def row(myTurtle):
# penup to not draw anything
          myTurtle.penup()
          myTurtle.right(60)
          myTurtle.backward(30)
          myTurtle.left(120)
          myTurtle.forward(30)
          myTurtle.right(65)
          myTurtle.backward(30)
          myTurtle.left(30)
          myTurtle.forward(55)
# pendown to draw again
          myTurtle.pendown()
          
# this code is to have the shape finished and be in a row
def together(myTurtle):
# time is assign to 0
      time = 0
# while statement to repeat again and again
      while time < 4:
# the three variables that have different stuff to do
          shape(myTurtle)
          base(myTurtle)
          otherSide(myTurtle)
# penup to not draw anything
          myTurtle.penup()
          myTurtle.right(60)
          myTurtle.backward(30)
          myTurtle.left(120)
          myTurtle.forward(30)
          myTurtle.right(65)
          myTurtle.backward(30)
          myTurtle.left(30)
          myTurtle.forward(55)
# pendown to draw again
          myTurtle.pendown()
          time = time + 1

# to draw the second row of cubes
def draw2ndRow(myTurtle):
# penup to not draw anything
  myTurtle.penup()
  myTurtle.backward(260) 
  myTurtle.left(90)
  myTurtle.forward(35)
  myTurtle.right(90)
# pendown to draw again
  myTurtle.pendown()  
# to have everything together  
  together(myTurtle)

# draw the final section of rows of cubes  
def draw3rdRow(myTurtle):
# penup to not draw anything
  myTurtle.penup()
  myTurtle.backward(260)
  myTurtle.left(90)
  myTurtle.forward(35)
  myTurtle.right(90)
# pendown to draw again
  myTurtle.pendown()
# to have everything together  
  together(myTurtle)

# the name of the turtle          
cube = turtle.Turtle()

# the speed to draw everything in the speed of 50
cube.speed(50)

# the names of the different codes there is and each does something different
shape(cube)
base(cube)
otherSide(cube)

# to code to draw one row
row(cube)

# to combine the rest three codes together
together(cube)

# the drawing of the two other rows
draw2ndRow(cube)
draw3rdRow(cube)

# when everything finished we press x to exi out of python
turtle.exitonclick()
