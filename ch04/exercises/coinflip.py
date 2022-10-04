import turtle
import pygame
import random
red = [200, 0, 0]
window = turtle.Screen()
screensize = window.screensize()
edgescreen = (screensize[0]/2, screensize[1]/2)
window.bgcolor('lightblue')
turtle1 = turtle.Turtle()
turtle1.shape('turtle')
turtle1.color('red')
turtle1.forward(50)
coinflip = random.randrange(0,2)
run = False
turtle1.goto(0,0)
turtle1position= turtle1.pos()
while not run is True:
  if abs(int(turtle1position[0])) >= abs(int(edgescreen[0])) or abs(int(turtle1position[1])) >= abs(int(edgescreen[1])):
    run = True
  else:
    coinflip = random.randrange(0,2)
    if coinflip == 0:
      print("Heads. Move left 50")
      turtle1.left(90)
      turtle1.forward(50)
      turtle1position= turtle1.pos()
    elif coinflip == 1:
      print("Tails. Move right 50")
      turtle1.right(90)
      turtle1.forward(50)
      turtle1position= turtle1.pos()
window.exitonclick()