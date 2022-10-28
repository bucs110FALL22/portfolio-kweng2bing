import turtle

def display():
  display = turtle.Screen()
  width=400
  height= 400
  display.screensize(canvwidth=width, canvheight=height)
  displaySize = display.screensize()
  return width
  


def tictactoeboard():
  draw = turtle.Turtle()
  draw.color('black')
  draw.penup()
  fromedge = displaySize[0]/8
  print(f"distancefromline{fromedge}")
  a = (displaySize[0] - (fromedge * 2)) /3
  print(a)
  coordsleft=[(-(fromedge + a), fromedge), (-(fromedge + a), -fromedge)]
  print(coordsleft)
  for i in range(len(coordsleft)): 
    print(i)
    draw.goto(coordsleft[i])
    draw.pendown()
    draw.forward(300)
    draw.penup()
  coordstop = [(-fromedge,(fromedge + a)), (fromedge, (fromedge+ a))]
  for i in range(len(coordstop)): 
    draw.goto(coordstop[i])
    draw.pendown()
    draw.right(90)
    draw.forward(300)
    draw.left(90)
    draw.penup()

def main():
  a = display()
  print(display)
  tictactoeboard()



display.exitonclick()