import turtle #1. import modules
import random
import pygame
import math


#Part A
# window = turtle.Screen() # 2.  Create a screen
# window.screensize(2000,2000)
# window.bgcolor('lightblue')

# michelangelo = turtle.Turtle() # 3.  Create two turtles
# leonardo = turtle.Turtle()
# michelangelo.color('orange')
# leonardo.color('blue')
# michelangelo.shape('turtle')
# leonardo.shape('turtle')

# michelangelo.up() # 4. Pick up the pen so we don’t get lines
# leonardo.up()
# michelangelo.goto(-100,20)
# leonardo.goto(-100,-20)

# ## 5. Your PART A code goes here
# random1 = random.randrange(0,101)
# random2 = random.randrange(0,101)
# leonardo.forward(random1)
# leonardo.forward(random2)

# for i in range(10):
#   random1 = random.randrange(0,10)
#   print("Turtle 1 moved" , str(random1))
#   leonardo.forward(random1)
#   random2 = random.randrange(0,10)
#   print("Turtle 2 moved" , str(random2))
#   leonardo.forward(random2)
# michelangelo.goto(-100,20)
# leonardo.goto(-100,-20)
# window.exitonclick()
# PART B - complete part B here
pygame.init()
screen =  pygame.display.set_mode()
screen.fill([255, 0, 0])
pygame.display.flip()

pygame.time.wait(500)

screen.fill([0, 255, 0])
pygame.display.flip()

# pygame.time.wait(500)

# screen.fill([0, 0, 255])
# pygame.display.flip()



