import pygame
pygame.init()
window = pygame.display.set_mode([900,300])
font = pygame.font.Font(None, 18)

lowerLimit = 2
upperLimit = 20
iters = {}
maxSoFar = 0
maxVal = 0
scale = 10
for i in range(lowerLimit, upperLimit + 1):
  window.fill("black")
  n = i
  count = 0
  while n != 1:
    if n % 2 == 0:
       n = n//2
    else:
      n = 3*n + 1
    count += 1
  if count > maxSoFar:
    maxSoFar = count
    maxVal = i
  iters[i] = count
  coords = [(x* scale, y * scale) for x, y in iters.items()]
  if len(coords) >= 2:
    pygame.draw.lines(window, 'yellow', False, coords)
    new_display = pygame.transform.flip(window, False, True)
    window.blit( new_display , (0, 0) )
    antialias= True
    msg1= f"The max number of iterations for '{maxVal}' is '{maxSoFar}' "
    msg = font.render(msg1, antialias, 'yellow')
    messageLocation = (10,10)
    window.blit(msg, messageLocation)
    pygame.display.flip()
    pygame.time.wait(2000)
print(iters)