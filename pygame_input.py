import pygame
import math
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((640, 480))

box_position = (100, 100)
box_size = (25, 25)

run_flag = True
while run_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                box_position = (box_position[0] - 5, box_position[1])
            if event.key == pygame.K_RIGHT:
                box_position = (box_position[0] + 5, box_position[1])
            if event.key == pygame.K_UP:
                box_position = (box_position[0], box_position[1] - 5)
            if event.key == pygame.K_DOWN:
                box_position = (box_position[0], box_position[1] + 5)

    
    screen.fill((255, 255, 255))
    rect = box_position + box_size
    pygame.draw.rect(screen, (0,0,0), rect)
    pygame.display.flip()



            

