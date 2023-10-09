import pygame
import math

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window")

def draw_smiley(screen, position = (100, 100), color = (255, 255, 0)):
    radius = 100
    pygame.draw.circle(screen, color, position, radius)
    pygame.draw.circle(screen, (0, 0, 0),
                       (position[0] - 40, position[1] - 30), 10)
    pygame.draw.circle(screen, (0, 0, 0),
                       (position[0] + 40, position[1] - 30), 10)
    pygame.draw.arc(screen, (0, 0, 0),
                    (position[0] - 40, position[1] - 20, 80, 80),
                    math.pi, 0, 10)
    return radius

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white
    
    draw_smiley(screen, color = (0, 255, 0))
    draw_smiley(screen, (400, 350))
    
    pygame.display.flip()



