import pygame
import random
import os
from sys import exit 

pygame.init()

def snake_animation():
    global snake_img, snake_img2, snake_index, snake_move, snake_surf
    snake_index += 0.1

    if snake_index > len(snake_move):
        snake_index = 0

    snake_surf = pygame.transform.rotozoom(snake_move[int(snake_index)], 0, 3)

screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_height, screen_width))

clock = pygame.time.Clock()

snake = pygame.Rect(100, 100, 50, 50)

snake_x = screen_width - 100
snake_y = 300

snake_img = pygame.image.load("star1.png") 
snake_img2 = pygame.image.load("star2.png")
snake_move = [snake_img, snake_img2] 

snake_index = 0
snake_surf = snake_move[snake_index]

snake_rect = snake_surf.get_rect(midbottom=(snake_x, snake_y))
snake_speed = 5

font = pygame.font.Font("PixelifySans-Regular.ttf", 25)

running = True

while running:
    screen.fill("green")
    #kontrola hry (start, end)
    for event in pygame.event.get:
        if event.type == pygame.QUIT:
            running = False 
            exit()

    key = pygame.key.get_pressed()

    if key[pygame.k_w]:
        snake_rect.top -= snake_speed
    if key[pygame.k_a]:
        snake_rect.left -= snake_speed
    if key[pygame.k_s]:
        snake_rect.bottom += snake_speed
    if key[pygame.k_d]:
        snake_rect.right += snake_speed


screen.blit(snake_surf, snake_rect)  
pygame.display.update()
clock.tick(60)


