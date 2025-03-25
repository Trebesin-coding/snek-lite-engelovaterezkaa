import pygame
import random
from sys import exit

pygame.init()

screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))  # první šířka
pygame.display.set_caption("Hadík :P")

clock = pygame.time.Clock()

# snake = pygame.Rect(100, 100, 50, 50)
snake_size = 50
snake_x = screen_width // 2
snake_y = screen_height // 2  # vydeli vysku 2 => polovina obrazovky
snake_speed = 5
score = 0

# snake_img = pygame.image.load("star1.png")
# snake_img2 = pygame.image.load("star2.png")
# snake_move = [snake_img, snake_img2]

# snake_index = 0
# snake_surf = snake_move[snake_index]

# snake_rect = snake_surf.get_rect(midbottom=(snake_x, snake_y))


def coin():
    return random.randint(0, screen_width - snake_size), random.randint(
        0, screen_height - snake_size
    )


coin_x, coin_y = coin()


def green_coin():
    return random.randint(0, screen_width - snake_size), random.randint(
        0, screen_height - snake_size
    )


green_coin_x, green_coin_y = green_coin()
green_coin_visible = False  # není na začátku vidět
green_coin_timer = pygame.time.get_ticks()  # uklada aktualni cas


# font = pygame.font.Font("PixelifySans-Regular.ttf", 25)
font = pygame.font.Font(None, 36)

running = True

direction = "right"  # nesmi byt ve smycce

while running:
    screen.fill("grey")
    # kontrola hry (start, end)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        # key = pygame.key.get_pressed() --lepsi keydown, kdyz je key get pressed spatne se aktivuje
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != "down":
                direction = "up"
            elif event.key == pygame.K_s and direction != "up":
                direction = "down"
            elif event.key == pygame.K_a and direction != "right":
                direction = "left"
            elif event.key == pygame.K_d and direction != "left":
                direction = "right"

    # Pohyb hada
    if direction == "up":
        snake_y -= 5
    elif direction == "down":
        snake_y += 5
    elif direction == "left":
        snake_x -= 5
    elif direction == "right":
        snake_x += 5

    # if key[pygame.K_w]:
    #     snake_y -= snake_speed
    # if key[pygame.K_a]:
    #     snake_x -= snake_speed
    # if key[pygame.K_s]:
    #     snake_y += snake_speed
    # if key[pygame.K_d]:
    #     snake_x += snake_speed

    # def snake_animation():
    #     global snake_img, snake_img2, snake_index, snake_move, snake_surf
    #     snake_index += 0.1

    #     if snake_index > len(snake_move):
    #         snake_index = 0

    #     snake_surf = pygame.transform.rotozoom(snake_move[int(snake_index)], 0, 3)

    # screen.blit(snake_surf, snake_rect)

    # (povrch, barva, (x, y, šířka, výška)) = had
    pygame.draw.rect(screen, "orange", (snake_x, snake_y, snake_size, snake_size))

    pygame.draw.rect(screen, "red", (coin_x, coin_y, snake_size, snake_size))

    if pygame.Rect(snake_x, snake_y, snake_size, snake_size).colliderect(
        pygame.Rect(coin_x, coin_y, snake_size, snake_size)
    ):
        score += 1
        coin_x, coin_y = coin()

    if green_coin_visible:
        pygame.draw.rect(
            screen, "green", (green_coin_x, green_coin_y, snake_size, snake_size)
        )

    if (
        not green_coin_visible and pygame.time.get_ticks() - green_coin_timer > 3000
    ):  # kdyz neni visible coin a cas je pod 3 s tak se spawne coin a je videt, funkce se opakuje az po sebrani (v collide se nastavi visible false)
        green_coin_x, green_coin_y = green_coin()
        green_coin_visible = True

    if green_coin_visible and pygame.Rect(
        snake_x, snake_y, snake_size, snake_size
    ).colliderect(pygame.Rect(green_coin_x, green_coin_y, snake_size, snake_size)):
        score += 100
        green_coin_visible = False
        green_coin_timer = pygame.time.get_ticks()  # restart casu

    # elif green_coin_visible and pygame.Rect(snake_x, snake_y, snake_size, snake_size).colliderect(pygame.Rect(green_coin_x, green_coin_y, snake_size, snake_size)) == False and pygame.time.get_ticks() - green_coin_timer < 2000:
    #     green_coin_visible = False
    #     green_coin_timer = pygame.time.get_ticks()

    # if green_coin_visible and pygame.Rect(snake_x, snake_y, snake_size, snake_size).colliderect(pygame.Rect(green_coin_x, green_coin_y, snake_size, snake_size)) == False and pygame.time.get_ticks() - green_coin_timer < 2000:
    #     green_coin_visible = False
    #     green_coin_timer = pygame.time.get_ticks()

    score_text = font.render(f"Skóre: {score}", True, "white")
    screen.blit(score_text, (screen_width - 120, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
