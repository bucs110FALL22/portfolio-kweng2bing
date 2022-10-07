import pygame
import random
import math

pygame.init()
window = pygame.display.set_mode(size=(300,300))
screenSize = pygame.display.get_window_size()
# print(screenSize[0], screenSize[1])
radius = int(screenSize[0]/2)
centerofscreen = (screenSize[0]/2, screenSize[1]/2)

print(centerofscreen[0])
# display box for choosing
redbox = pygame.Rect(0, 0 , screenSize[0]/2, screenSize[1])
bluebox = pygame.Rect(0, 0 , screenSize[0]/2, screenSize[1])
bluebox.topleft = redbox.topright
player1 = pygame.draw.rect(window,'red', redbox)
player2 = pygame.draw.rect(window,'blue', bluebox)
pygame.display.flip()
print("Choose who do you think will win. Player 1 is red and player 2 is blue")
# pygame.time.wait(1000)
winner = 0
while winner == 0:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_click_pos = event.pos
      print(mouse_click_pos)
      if redbox.collidepoint(mouse_click_pos):
        print("red")
        winner = 1
      if bluebox.collidepoint(mouse_click_pos):
        winner = 2
        print("blue") 

# # board
window.fill('darkgray')
pygame.display.flip()
pygame.draw.circle(window, 'yellow',centerofscreen, radius)
pygame.draw.line(window, 'red', (centerofscreen[0]-radius,centerofscreen[1]), (centerofscreen[0]+radius, centerofscreen[1]))
pygame.draw.line(window, 'red', (centerofscreen[0],centerofscreen[1]-radius), (centerofscreen[0], centerofscreen[1]+radius))
pygame.display.flip()

player1points = 0 
player2points = 0
# dart game
for i in range(10):
  print("#Round", i+1)
  for j in range(2):
    xcoord = random.randrange(0, screenSize[0])
    ycoord = random.randrange(0, screenSize[1])
    distance_from_center = math.hypot(xcoord - screenSize[0] / 2, ycoord - screenSize[1] / 2) 
    is_in_circle = distance_from_center <= screenSize[0]/2
    if is_in_circle:
      if j == 0:
        pygame.draw.circle(window, 'red', (xcoord, ycoord),3)
        player1points += 1
        print("Player 1 has earned 1 point. Total points:", str(player1points))
      elif j == 1:
        pygame.draw.circle(window, 'blue', (xcoord, ycoord),3)
        player2points += 1
        print("Player 2 earned 1 point. Total point(s):", str(player2points),)
    else:
      pygame.draw.circle(window, 'black', (xcoord, ycoord), 3)
      print("Player ", j+1, "missed. No points earned")
      
    pygame.display.flip()
    pygame.time.wait(1000)
pygame.time.wait(3000)

print(f"Player 1 has {player1points} points.")
print(f"Player 1 has {player2points} points.")

actualwinner = 0
if player1points > player2points:
  actualwinner = 1
  print("Player 1 won")
elif player1points < player2points:
  actualwinner = 2
  print("Player 2 won")
else:
  print("No players won")

if actualwinner == winner:
  print("Your guess is correct.")
else:
  print("Your guess is wrong.")