
import turtle
wn = turtle.Screen()          
# Set up the window and its attributes
wn.bgcolor("pink")
wn.screensize(1000, 800)


tess = turtle.Turtle() 
tess.shape("turtle")
# create tess and draw a square
tess.color("purple")
tess.pensize(5)
for i in range(4):
    tess.left(90)
    tess.forward(50)

tess.up()
tess.goto(50,50)
# create uber to draw another square
turtle.down()
uber = turtle.Turtle()  
uber.up()
uber.goto(50,50)
uber.down()
uber.color("red")
for i in range(4):
    uber.left(90)
    uber.forward(50)

# turtle draw any shape
vertex = turtle.Turtle()
vertex.up()
vertex.goto(150,-50)
vertex.down()
userColor = input("What color?")
vertex.color(userColor)
# if vertex.color(userColor).status_code == 200:
#   print("YES")
# else:
#  print("nooo")
vertex.pensize(3)
vertex.shape("turtle")
numberOfSides = int(input("How many sides do you want your shape to have?"))

print (numberOfSides)
Angle = 360 // numberOfSides

for i in range(numberOfSides):
    vertex.left(Angle)
    vertex.forward(50)


wn.exitonclick()
