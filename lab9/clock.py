import pygame
import sys
import math
from datetime import datetime

pygame.init()

width, height = 800, 800
center = (400, 400)

screen = pygame.display.set_mode((width, height))

clock_background = pygame.image.load('main-clock.png')
left_hand_image = pygame.image.load('left-hand.png')
right_hand_image = pygame.image.load('right-hand.png')
clock_rect = clock_background.get_rect()
right_hand_rect = right_hand_image.get_rect()
left_hand_rect = left_hand_image.get_rect()

clock_pygame = pygame.time.Clock()
FPS = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((255, 255, 255))
    screen.blit(clock_background, clock_rect)
    current_time = datetime.now()
    sec = current_time.second
    minute = current_time.minute
    sec_degree = (sec % 60) * 6 - 90
    min_degree = (minute % 60) * 6 - 90
    hour_rotated = pygame.transform.rotate(left_hand_image, -sec_degree)
    minute_rotated = pygame.transform.rotate(right_hand_image, -min_degree)

    hour_rect = hour_rotated.get_rect(center=center)
    minute_rect = minute_rotated.get_rect(center=center)

    screen.blit(hour_rotated, hour_rect)
    screen.blit(minute_rotated, minute_rect)
    pygame.display.flip()
    clock_pygame.tick(FPS)
