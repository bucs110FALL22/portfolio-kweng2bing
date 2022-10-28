import turtle
display = turtle.Screen()
width=400
height= 400
display.screensize(canvwidth=width, canvheight=width)
displaySize = display.screensize()
print(displaySize)
def tictactoeboard():
  draw = turtle.Turtle()
  draw.color('black')
  draw.penup()
  fromedge = width/8
  print(f"distancefromline{fromedge}")
  a = (width - (fromedge * 2)) /3
  print(a)
  coords=[(-(fromedge + a), fromedge), (-(fromedge + a), -fromedge)]
  print(coords)
  for i in range(len(coords)): 
    print(i)
    draw.goto(coords[i])
    draw.pendown()
    draw.forward(300)
    draw.penup()
# 
  # draw.goto(-150,50)
  # draw.pendown()
  # draw.forward(300)
tictactoeboard()



display.exitonclick()