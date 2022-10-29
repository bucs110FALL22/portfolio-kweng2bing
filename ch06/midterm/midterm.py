import turtle

def tictactoeboard(displaysize):
# A function that sets up the board. The function takes in the dimension of the screen. No returns.
  draw = turtle.Turtle()
  draw.color('black')
  draw.penup()
  fromedge = displaysize/8
  distance = (displaysize- (fromedge * 2)) /3
  coordsleft=[(-(fromedge + distance), fromedge), (-(fromedge + distance), -fromedge)]
  print(coordsleft)
  for i in range(len(coordsleft)): 
    draw.goto(coordsleft[i])
    draw.pendown()
    draw.forward(300)
    draw.penup()
  coordstop = [(-fromedge,(fromedge + distance)), (fromedge, (fromedge + distance))]
  for i in range(len(coordstop)): 
    draw.goto(coordstop[i])
    draw.pendown()
    draw.right(90)
    draw.forward(300)
    draw.left(90)
    draw.penup()
  draw.ht()

def shape1(pos):
# A function for drawing Player 1's shape == circle. The function takes in the position to know where to start. No returns
  shape1 = turtle.Turtle()
  shape1.shape('turtle')
  shape1.penup()
  shape1.goto(pos)
  shape1.pendown()
  shape1.fillcolor('purple')
  shape1.begin_fill()
  shape1.circle(40)
  shape1.end_fill()
  shape1.ht()

# Player 2 shape drawing
def shape2(pos):
  # A function that draws Player 2's shape == star. The function takes in the position to know where to start. No returns
  shape2 = turtle.Turtle()
  shape2.penup()
  shape2.goto(pos)
  shape2.fillcolor('lightblue')
  shape2.begin_fill()
  shape2.pendown()
  shape2.right(90)
  for i in range(5):
    shape2.right(144)
    shape2.forward(80)
  shape2.end_fill()
  shape2.ht()
def topos(input): 
  # A function used to translate a1...c3 to coordinates. The function takes in the user input and returns the coordinates for that particular input.
  dict = [
  ["a1", (-100,60)],
  ["a2", (0, 60)],
  ["a3", (100, 60)],
  ["b1", (-100, -40)],
  ["b2", (0,-40)],
  ["b3", (100, -40)],
  ["c1", (-100, -140)],
  ["c2", (0, -140)],
  ["c3", (100, -140)]
]
  for posarg in dict:
    if posarg[0] == input:
      return posarg[1]
def game():
# A function for the overall game. No parameters and does not return anything
  gameOver = False
  count = 0
  player1choice =[]
  player2choice =[]
  while gameOver == False:
    print("Type a1,a2,a3,b1,b2,b3,c1,c2, or c3")
    for i in range(2):
      if count == 8 and i ==0:
        print("Player 1 Turn.")
        choice = input("Which box?")
        pos = topos(choice)
        shape1(pos)
        player1choice.append(choice)
        gameOver = True 
        break
      if i == 0:
        print("Player 1 Turn.")
        choice = input("Which box?")
        pos = topos(choice)
        shape1(pos)
        player1choice.append(choice)
        result = win(player1choice)
        if result == True:
          gameOver = True
          print("Player 1 wins")
          break
        count += 1
      if i == 1:
        print("Player 2 Turn.")
        choice = input("Which box?")
        pos = topos(choice)
        shape2(pos)
        player2choice.append(choice)
        result= win(player2choice)
        if result == True:
          gameOver = True
          print("Player 2 wins")
          break
        count += 1
def win(playerset):
  # A function to determine if a player has a winning set. The function takes the boxes the player types and returns a boolean depending on if there is a winning set.
  winSet = [
    ['a1','a2','a3'],
    ['b1','b2','b3'],
    ['c1','c2','c3'],
    ['a1','b1','c1'],
    ['a2','b2','c2'],
    ['a3','b3','c3'],
    ['a1','b2','c3'],
    ['a3','b2','c1']
  ]
  for i in winSet:
    if all(value in playerset for value in i):
      return True
def main():
  # The function that starts everything.
  display = turtle.Screen()
  displaysize=400
  display.screensize(canvwidth=displaysize, canvheight=displaysize)
  tictactoeboard(displaysize)
  game()
  display.exitonclick()
  
main()
