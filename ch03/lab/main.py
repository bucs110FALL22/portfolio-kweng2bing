#1. import modules
import turtle 
import random
import pygame
import math
#Part A
 # 2.  Create a screen
window = turtle.Screen()
window.screensize()
window.bgcolor('lightblue')
 # 3.  Create two turtles
michelangelo = turtle.Turtle()
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
# 4. Pick up the pen so we don’t get lines
michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
random1 = random.randrange(0,101)
random2 = random.randrange(0,101)
michelangelo.forward(random1)
leonardo.forward(random2)
print("Turtle 1 moved" ,str(random1))
print("Turtle 2 moved" ,str(random2))

for i in range(10):
  random1 = random.randrange(0,10)
  michelangelo.forward(random1)
  print("Turtle 1 moved" , str(random1))
  random2 = random.randrange(0,10)
  leonardo.forward(random2)
  print("Turtle 2 moved" , str(random2))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()
coords = []
num_sides = [3,4,6,9,360]
side_length = 80
offset = 100
color = ""'cyan'""
for i in num_sides:
  for shape in range(int(i)):
    theta = (2.0 * math.pi * (shape)) / i
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append([x , y])
  # display shape
  pygame.draw.polygon(window, color, coords)
  pygame.display.flip()
  pygame.time.wait(1000)
  coords = []
  #reset screen
  window.fill('black')
  pygame.display.flip()
  pygame.time.wait(1000)