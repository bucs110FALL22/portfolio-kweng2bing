import turtle

def tictactoeboard(ab):
  draw = turtle.Turtle()
  draw.color('black')
  draw.penup()
  fromedge = ab/8
  print(f"distancefromline{fromedge}")
  a = (ab- (fromedge * 2)) /3
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
  draw.ht()
def shape1(pos):
  shape1 = turtle.Turtle()
  shape1.penup()
  shape1.goto(pos)
  shape1.pendown()
  shape1.circle(40)

def shape2(pos):
  shape2 = turtle.Turtle()
  shape2.penup()
  shape2.goto(pos)
  shape2.pendown()
  shape2.right(90)
  for i in range(5):
    shape2.right(144)
    shape2.forward(80)

def topos(input): 
  dict = {
  "a1": (-100,60),
  "a2": (0, 60),
  # a3: (-100, 60),
  # b1: (-100, -40),
  # b2: (0,-40),
  # b3: (100, -40),
  # c1: (-100, -140),
  # c2: (0, -140),
  # c3: (100, -140)
}
  for posarg in dict:
    if posarg[0] == input:
      return posarg[1]
      print(posarg[1])
      print(type(posarg[1]))
      print(input)
  

  
def main():
  display = turtle.Screen()
  displaysize=400
  display.screensize(canvwidth=displaysize, canvheight=displaysize)
  tictactoeboard(displaysize)
  shape1((0,-40))
  shape2((100,-40))
  input1 = input("Test?")
  pos = topos(input1)
  print(pos)
  print(type(pos))
  shape1(pos)
  display.exitonclick()
  
main()
