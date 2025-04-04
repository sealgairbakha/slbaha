import pygame
import random
import sys
import time

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

# рисуем еду
def draw_food(position, weight):
    if weight == 1:
        color = (255, 0, 0)
        size = 30
    elif weight == 2:
        color = (255, 165, 0)
        size = 20
    else:
        color = (255, 255, 0)
        size = 15

    # Центрируем квадрат по клетке
    px = position[0] * CELL_SIZE + CELL_SIZE // 2 - size // 2
    py = position[1] * CELL_SIZE + CELL_SIZE // 2 - size // 2

    pygame.draw.rect(screen, color, pygame.Rect(px, py, size, size))


# создаём еду не на змее
def generate_food(snake):
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake:
            weight = random.choice([1, 2, 3])  # вес: 1, 2 или 3
            timer = time.time()               # время появления
            return pos, weight, timer

# выводим счёт и уровень
def display_info(score, level):
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

# сама игра
def game():
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = (1, 0)
    food_pos, food_weight, food_timer = generate_food(snake)
    score = 0
    level = 1
    speed = 10

    while True:
        screen.fill((10, 30, 10))  # фон
        display_info(score, level)

        # управление
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
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

        # если врезался
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or
            new_head in snake):
            pygame.quit()
            sys.exit()

        snake.insert(0, new_head)

        # если съел еду
        if new_head == food_pos:
            score += food_weight
            food_pos, food_weight, food_timer = generate_food(snake)
            if score % 4 == 0:
                level += 1
                speed += 2
        else:
            snake.pop()

        # проверка таймера — если прошло >5 секунд, еда исчезает
        if time.time() - food_timer > 5:
            food_pos, food_weight, food_timer = generate_food(snake)

        draw_snake(snake)
        draw_food(food_pos, food_weight)

        pygame.display.flip()
        clock.tick(speed)

game()