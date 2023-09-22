import pygame
import math
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((640, 480))

start_point = (100, 100)
box_size = (25, 25)

while True:
    screen.fill((255, 255, 255))
    box_position = (start_point[0] + datetime.now().second*5,
                    start_point[1])
    rect = box_position + box_size
    pygame.draw.rect(screen, (0,0,0), rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            

