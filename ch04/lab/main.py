import pygame

window = pygame.display.set_mode()
screenSize = pygame.display.get_window_size() #522,326
print(screenSize[0], screenSize[1])
window.fill('yellow')
pygame.draw.circle(window, 'blue', 50)