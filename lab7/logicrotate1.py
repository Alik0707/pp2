import pygame

pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounding Box Вращение")

# Центр экрана (центр вращения)
CENTER = (WIDTH // 2, HEIGHT // 2)

# Создаём стрелку
arrow = pygame.Surface((20, 100), pygame.SRCALPHA)  # Прозрачный фон
pygame.draw.polygon(arrow, (255, 255, 255), [(10, 0), (20, 20), (15, 20), (15, 100), (5, 100), (5, 20), (0, 20)])

# Основной цикл
angle = 0
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((30, 30, 30))  # Чёрный фон

    # Поворачиваем стрелку
    rotated_arrow = pygame.transform.rotate(arrow, angle)

    # Получаем новые границы изображения
    rect = rotated_arrow.get_rect(center=CENTER)

    # **Bounding Box**
    pygame.draw.rect(screen, (0, 255, 255), rect, 3)  # Прямоугольник голубого цвета

    # **Рисуем стрелку**
    screen.blit(rotated_arrow, rect.topleft)

    # **Рисуем точки углов**
    pygame.draw.circle(screen, (255, 0, 0), rect.topleft, 5)      # 🔴 Верхний левый угол
    pygame.draw.circle(screen, (0, 255, 0), rect.topright, 5)     # 🟢 Верхний правый угол
    pygame.draw.circle(screen, (0, 0, 255), rect.bottomleft, 5)   # 🔵 Нижний левый угол
    pygame.draw.circle(screen, (255, 255, 0), rect.bottomright, 5)  # 🟡 Нижний правый угол

    # **Рисуем центр вращения**
    pygame.draw.circle(screen, (255, 0, 255), CENTER, 5)  # Фиолетовый центр

    # Обновляем экран
    pygame.display.flip()
    clock.tick(30)  # Медленный FPS

    # Увеличиваем угол поворота
    angle += 1

    # Проверяем выход
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
