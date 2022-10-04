import pygame

pygame.init()
window = pygame.display.set_mode(size=(300,300))
screenSize = pygame.display.get_window_size() #522,326
print(screenSize[0], screenSize[1])
radius = int(screenSize[0]/2)
centerofscreen = (int(screenSize[0])/2,int(screenSize[1])/2)
print(centerofscreen[0])
window.fill('yellow')
pygame.display.flip()
pygame.time.wait(1000)
pygame.draw.circle(window, 'blue',centerofscreen, radius)
pygame.draw.line(window, 'red', (centerofscreen[0]-radius,centerofscreen[1]), (centerofscreen[0]+radius, centerofscreen[1]))
pygame.draw.line(window, 'red', (centerofscreen[0],centerofscreen[1]-radius), (centerofscreen[0], centerofscreen[1]+radius))
pygame.display.flip()