import pygame
import math
from datetime import datetime

pygame.init()
screen_size = (200, 200)
screen = pygame.display.set_mode(screen_size)
font = pygame.font.SysFont(None, 36)

color_change_enabled = True
while True:
    s = datetime.now().second
    screen.fill((100, 200, 100))
    if color_change_enabled and s > 30:
        screen.fill((200, 100, 100))

    text = font.render(f'Second: {s}', True, (255, 255, 255))
    screen.blit(text, (20, 20))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            

