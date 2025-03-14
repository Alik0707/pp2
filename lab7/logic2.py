import pygame

pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounding Box Вращение (Две стрелки)")

# Центры вращения
CENTER_1 = (WIDTH // 3, HEIGHT // 2)
CENTER_2 = (2 * WIDTH // 3, HEIGHT // 2)

# Создаём стрелку
arrow = pygame.Surface((20, 100), pygame.SRCALPHA)  # Прозрачный фон
pygame.draw.polygon(arrow, (255, 255, 255), [(10, 0), (20, 20), (15, 20), (15, 100), (5, 100), (5, 20), (0, 20)])

# Основной цикл
angle_1 = 0  # Для первой стрелки
angle_2 = 0  # Для второй стрелки
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((30, 30, 30))  # Чёрный фон

    # ====================== Первая стрелка (вращается по часовой) ====================== #
    rotated_arrow_1 = pygame.transform.rotate(arrow, angle_1)
    rect_1 = rotated_arrow_1.get_rect(center=CENTER_1)

    pygame.draw.rect(screen, (0, 255, 255), rect_1, 3)  # Bounding Box (Голубой)
    screen.blit(rotated_arrow_1, rect_1.topleft)

    pygame.draw.circle(screen, (255, 0, 0), rect_1.topleft, 5)      # 🔴 Верхний левый
    pygame.draw.circle(screen, (0, 255, 0), rect_1.topright, 5)     # 🟢 Верхний правый
    pygame.draw.circle(screen, (0, 0, 255), rect_1.bottomleft, 5)   # 🔵 Нижний левый
    pygame.draw.circle(screen, (255, 255, 0), rect_1.bottomright, 5)  # 🟡 Нижний правый
    pygame.draw.circle(screen, (255, 0, 255), CENTER_1, 5)  # Фиолетовый центр

    # ====================== Вторая стрелка (вращается против часовой) ====================== #
    rotated_arrow_2 = pygame.transform.rotate(arrow, -angle_2)
    rect_2 = rotated_arrow_2.get_rect(center=CENTER_2)

    pygame.draw.rect(screen, (255, 165, 0), rect_2, 3)  # Bounding Box (Оранжевый)
    screen.blit(rotated_arrow_2, rect_2.topleft)

    pygame.draw.circle(screen, (255, 0, 0), rect_2.topleft, 5)      # 🔴 Верхний левый
    pygame.draw.circle(screen, (0, 255, 0), rect_2.topright, 5)     # 🟢 Верхний правый
    pygame.draw.circle(screen, (0, 0, 255), rect_2.bottomleft, 5)   # 🔵 Нижний левый
    pygame.draw.circle(screen, (255, 255, 0), rect_2.bottomright, 5)  # 🟡 Нижний правый
    pygame.draw.circle(screen, (255, 0, 255), CENTER_2, 5)  # Фиолетовый центр

    # Обновляем экран
    pygame.display.flip()
    clock.tick(30)  # Медленный FPS

    # Увеличиваем углы поворота
    angle_1 += 1  # Первая стрелка вращается по часовой
    angle_2 += 1  # Вторая стрелка вращается против часовой

    # Проверяем выход
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
