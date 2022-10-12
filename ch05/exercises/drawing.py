import turtle
def turtlefun(num_sides, side_length):
  wn = turtle.Screen()
  turtle1 = turtle.Turtle()
  turtle1.shape('turtle')
  turtle1.color('green')
  turtle1.forward(side_length)
  angle = 360 // num_sides
  for i in range(num_sides):
    turtle1.left(angle)
    turtle1.forward(side_length)
  wn.exitonclick()
         
                 
num_sides = int(input("Number of Sides?"))
side_length = int(input("Side Length?"))

turtlefun(num_sides, side_length)
