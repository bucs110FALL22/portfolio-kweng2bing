import turtle

wn = turtle.Screen()
drawing = turtle.Turtle()
numberOfSides = int(input("How many sides do you want your shape to have?"))
userColor = input("What color?")
drawing.color(userColor)
print (numberOfSides)
Angle = 360 // numberOfSides
for i in range(numberOfSides):
    drawing.left(Angle)
    drawing.forward(50)
wn.exitonclick()
