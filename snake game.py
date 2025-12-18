import pygame
import sys
import random

pygame.init()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game 🐍")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

snake_size = 20
speed = 20

snake = [[100, 100]]
snake_length = 1

food_x = random.randrange(0, width, snake_size)
food_y = random.randrange(0, height, snake_size)

dx = 0
dy = 0

clock = pygame.time.Clock()

def game_over():
    font = pygame.font.SysFont(None, 50)
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (200, 180))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -speed
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = speed
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -speed
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = speed

    new_head = [snake[0][0] + dx, snake[0][1] + dy]
    snake.insert(0, new_head)

    if len(snake) > snake_length:
        snake.pop()

    # Border collision
    if (snake[0][0] < 0 or snake[0][0] >= width or
        snake[0][1] < 0 or snake[0][1] >= height):
        game_over()

    # Eat food
    if snake[0][0] == food_x and snake[0][1] == food_y:
        snake_length += 1
        food_x = random.randrange(0, width, snake_size)
        food_y = random.randrange(0, height, snake_size)

    screen.fill(BLACK)

    pygame.draw.circle(
        screen,
        RED,
        (food_x + snake_size // 2, food_y + snake_size // 2),
        snake_size // 2
    )

    # 🐍 Draw real snake
    for index, block in enumerate(snake):
        x, y = block

        if index == 0:
            pygame.draw.circle(
                screen,
                (0, 200, 0),
                (x + snake_size // 2, y + snake_size // 2),
                snake_size // 2 + 2
            )
            pygame.draw.circle(screen, BLACK, (x + 7, y + 7), 3)
            pygame.draw.circle(screen, BLACK, (x + 13, y + 7), 3)
        else:
            pygame.draw.circle(
                screen,
                GREEN,
                (x + snake_size // 2, y + snake_size // 2),
                snake_size // 2
            )

    pygame.display.update()
    clock.tick(10)
