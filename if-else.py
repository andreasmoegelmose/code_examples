import pygame
import math
from datetime import datetime

pygame.init()
screen_size = (200, 200)
screen = pygame.display.set_mode(screen_size)
screen_center = (screen_size[0] // 2, screen_size[1] // 2)
font = pygame.font.SysFont(None, 36)

while True:
    screen.fill((100, 200, 100))
    s = datetime.now().second
    if s > 30:
        pygame.draw.rect(screen, (200, 100, 100), (30, 70, 140, 60))
    else:
        pygame.draw.ellipse(screen, (100, 100, 200), (30, 70, 140, 60))

    text = font.render(f'Second: {s}', True, (255, 255, 255))
    text_pos = (screen_center[0] - text.get_width() // 2,
                screen_center[1] - text.get_height() // 2)
    screen.blit(text, text_pos)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            

