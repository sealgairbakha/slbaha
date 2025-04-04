import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    color = (0, 0, 255)  # начальный цвет — синий
    bg_color = (0, 0, 0)
    points = []

    tool = 'draw'  # текущий инструмент
    drawing_shape = False
    shape_start = (0, 0)
    shape_end = (0, 0)

    canvas = pygame.Surface((640, 480))  # холст
    canvas.fill(bg_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            # горячие клавиши для инструментов и цвета
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: tool = 'draw'
                elif event.key == pygame.K_2: tool = 'circle'
                elif event.key == pygame.K_3: tool = 'rect'
                elif event.key == pygame.K_4: tool = 'square'
                elif event.key == pygame.K_5: tool = 'triangle_right'
                elif event.key == pygame.K_6: tool = 'triangle_eq'
                elif event.key == pygame.K_7: tool = 'rhombus'
                elif event.key == pygame.K_e: tool = 'eraser'
                elif event.key == pygame.K_r: color = (255, 0, 0)
                elif event.key == pygame.K_g: color = (0, 255, 0)
                elif event.key == pygame.K_b: color = (0, 0, 255)

            # нажали мышкой
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    shape_start = event.pos
                    drawing_shape = True
                elif event.button == 4: radius = min(200, radius + 1)
                elif event.button == 5: radius = max(1, radius - 1)

            # отпустили мышь
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing_shape:
                    shape_end = event.pos
                    draw_shape(canvas, tool, shape_start, shape_end, color if tool != 'eraser' else bg_color)
                    drawing_shape = False

        # кисть или ластик
        if pygame.mouse.get_pressed()[0] and tool in ['draw', 'eraser']:
            pos = pygame.mouse.get_pos()
            points.append((pos, tool, color if tool != 'eraser' else bg_color, radius))
            points = points[-256:]  # ограничим список, чтобы не тормозило

        screen.blit(canvas, (0, 0))  # рисуем холст

        # отрисовка точек (кисть/ластик)
        for pt, t, col, r in points:
            pygame.draw.circle(screen, col, pt, r)

        # предпросмотр фигуры
        if drawing_shape and tool not in ['draw', 'eraser']:
            shape_end = pygame.mouse.get_pos()
            draw_shape(screen, tool, shape_start, shape_end, color if tool != 'eraser' else bg_color, preview=True)

        pygame.display.flip()
        clock.tick(60)

# тут рисуются фигуры
def draw_shape(surface, tool, start, end, color, preview=False):
    temp_surface = surface if not preview else surface.copy()

    x1, y1 = start
    x2, y2 = end

    if tool == 'circle':
        center = ((x1 + x2) // 2, (y1 + y2) // 2)
        r = max(abs(x1 - x2), abs(y1 - y2)) // 2
        pygame.draw.circle(temp_surface, color, center, r, 0 if not preview else 2)

    elif tool == 'rect':
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(temp_surface, color, rect, 0 if not preview else 2)

    elif tool == 'square':
        size = min(abs(x2 - x1), abs(y2 - y1))
        rect = pygame.Rect(x1, y1, size if x2 >= x1 else -size, size if y2 >= y1 else -size)
        pygame.draw.rect(temp_surface, color, rect, 0 if not preview else 2)

    elif tool == 'triangle_right':
        points = [start, (x1, y2), (x2, y2)]
        pygame.draw.polygon(temp_surface, color, points, 0 if not preview else 2)

    elif tool == 'triangle_eq':
        # равносторонний треугольник, основание снизу
        height = abs(y2 - y1)
        midpoint = ((x1 + x2) // 2, y1)
        points = [midpoint, (x1, y2), (x2, y2)]
        pygame.draw.polygon(temp_surface, color, points, 0 if not preview else 2)

    elif tool == 'rhombus':
        # ромб через середины сторон
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        dx = abs(x2 - x1) // 2
        dy = abs(y2 - y1) // 2
        points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
        pygame.draw.polygon(temp_surface, color, points, 0 if not preview else 2)

    if preview:
        surface.blit(temp_surface, (0, 0))

main()