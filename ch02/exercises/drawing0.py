import pygame

print (pygame.ver)
# import turtle
# wn = turtle.Screen()

screen = pygame.display.set_mode()


screen.fill([255,0,0])
pygame.display.flip()
pygame.time.wait(500)
screen.fill([0,255,0])
pygame.display.flip()
screen.fill([0,0,255])
pygame.display.flip()






# for c in "apple":
#   print(c)

# for i in [1,2,3,4]:
#    print(i)
#    i = i + 10
#    print(i)

# result = range(10) 
# #up to the limit - non-inclusive
# print( list(result) )

# result = range(5, 10) 
# # start (inclusive), stop (non-inclusive)
# print( list(result) )

# result = range(50, 100, 2) 
# # start (inclusive), stop (non-inclusive), step - by some num
# print( list(result) )








# Random Classwork stuff
# draw = turtle.Turtle()
# sides = 4
# length = 50
# Angle = 90
# colors = ["red", "purple", "green"]
# for c in colors:
#   draw.color(c)
#   for i in range(4):
#     draw.left(Angle)
#     draw.forward(50)
  

# wn.exitonclick()