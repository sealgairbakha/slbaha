import pygame
import random
import sys

pygame.init()

# настройки экрана и клеток
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")

font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

# рисуем змею
def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

# еда
def draw_food(position):
    pygame.draw.rect(screen, RED, pygame.Rect(position[0]*CELL_SIZE, position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

# ставим еду не на змею
def generate_food(snake):
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake:
            return pos

# выводим счёт и уровень
def display_info(score, level):
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

# сама игра
def game():
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = (1, 0)
    food = generate_food(snake)
    score = 0
    level = 1
    speed = 10

    while True:
        screen.fill((10, 30, 10))  # тёмный фон
        display_info(score, level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # управление
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        # проверка на врезался
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or
            new_head in snake):
            pygame.quit()
            sys.exit()

        snake.insert(0, new_head)

        # съел еду
        if new_head == food:
            score += 1
            food = generate_food(snake)
            if score % 4 == 0:
                level += 1
                speed += 2
        else:
            snake.pop()

        draw_snake(snake)
        draw_food(food)

        pygame.display.flip()
        clock.tick(speed)

game()