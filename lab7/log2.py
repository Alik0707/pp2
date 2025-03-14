import pygame

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounding Box Вращение (4 точки)")

# Создаём стрелку
arrow = pygame.Surface((20, 100), pygame.SRCALPHA)  # Прозрачный фон
pygame.draw.polygon(arrow, (255, 255, 255), [(10, 0), (20, 20), (15, 20), (15, 100), (5, 100), (5, 20), (0, 20)])

# Позиции центров вращения
pos_topleft = (WIDTH // 4, HEIGHT // 4)  # Верхний левый угол
pos_topright = (3 * WIDTH // 4, HEIGHT // 4)  # Верхний правый угол
pos_bottomleft = (WIDTH // 4, 3 * HEIGHT // 4)  # Нижний левый угол
pos_bottomright = (3 * WIDTH // 4, 3 * HEIGHT // 4)  # Нижний правый угол

# Основной цикл
angle = 0  # Один общий угол (медленный поворот)
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((30, 30, 30))  # Чёрный фон

    # ======================== 🔴 Вращение вокруг `topleft` ======================== #
    rotated_arrow_1 = pygame.transform.rotate(arrow, angle)
    rect_1 = rotated_arrow_1.get_rect(topleft=pos_topleft)

    pygame.draw.rect(screen, (0, 255, 255), rect_1, 3)  # Bounding Box (Голубой)
    screen.blit(rotated_arrow_1, rect_1.topleft)

    pygame.draw.circle(screen, (255, 0, 0), rect_1.topleft, 5)  # 🔴 Вершина

    # ======================== 🟢 Вращение вокруг `topright` ======================== #
    rotated_arrow_2 = pygame.transform.rotate(arrow, angle)
    rect_2 = rotated_arrow_2.get_rect(topright=pos_topright)

    pygame.draw.rect(screen, (255, 165, 0), rect_2, 3)  # Bounding Box (Оранжевый)
    screen.blit(rotated_arrow_2, rect_2.topleft)

    pygame.draw.circle(screen, (0, 255, 0), rect_2.topright, 5)  # 🟢 Вершина

    # ======================== 🔵 Вращение вокруг `bottomleft` ======================== #
    rotated_arrow_3 = pygame.transform.rotate(arrow, angle)
    rect_3 = rotated_arrow_3.get_rect(bottomleft=pos_bottomleft)

    pygame.draw.rect(screen, (255, 255, 0), rect_3, 3)  # Bounding Box (Жёлтый)
    screen.blit(rotated_arrow_3, rect_3.topleft)

    pygame.draw.circle(screen, (0, 0, 255), rect_3.bottomleft, 5)  # 🔵 Вершина

    # ======================== 🟣 Вращение вокруг `bottomright` ======================== #
    rotated_arrow_4 = pygame.transform.rotate(arrow, angle)
    rect_4 = rotated_arrow_4.get_rect(bottomright=pos_bottomright)

    pygame.draw.rect(screen, (128, 0, 128), rect_4, 3)  # Bounding Box (Фиолетовый)
    screen.blit(rotated_arrow_4, rect_4.topleft)

    pygame.draw.circle(screen, (255, 0, 255), rect_4.bottomright, 5)  # 🟣 Вершина

    # Обновляем экран
    pygame.display.flip()
    clock.tick(10)  # 🔥 Медленное вращение (10 FPS)

    # Увеличиваем угол
    angle += 2  # Очень плавно

    # Проверяем выход
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
