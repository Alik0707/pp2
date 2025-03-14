import pygame

pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounding Box при разных точках вращения")

# Центры вращения
CENTER_TOPLEFT = (WIDTH // 5, HEIGHT // 3)
CENTER_TOPRIGHT = (4 * WIDTH // 5, HEIGHT // 3)
CENTER_BOTTOMLEFT = (WIDTH // 5, 2 * HEIGHT // 3)
CENTER_BOTTOMRIGHT = (4 * WIDTH // 5, 2 * HEIGHT // 3)

# Создаём стрелку (если нет изображения)
arrow = pygame.Surface((20, 100), pygame.SRCALPHA)  # Прозрачный фон
pygame.draw.polygon(arrow, (255, 255, 255), [(10, 0), (20, 20), (15, 20), (15, 100), (5, 100), (5, 20), (0, 20)])

# Основной цикл
angle = 0
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((30, 30, 30))  # Чёрный фон

    # Поворачиваем стрелки
    rotated_arrow1 = pygame.transform.rotate(arrow, angle)
    rotated_arrow2 = pygame.transform.rotate(arrow, angle)
    rotated_arrow3 = pygame.transform.rotate(arrow, angle)
    rotated_arrow4 = pygame.transform.rotate(arrow, angle)

    # Получаем границы нового изображения
    rect1 = rotated_arrow1.get_rect(center=CENTER_TOPLEFT)
    rect2 = rotated_arrow2.get_rect(center=CENTER_TOPRIGHT)
    rect3 = rotated_arrow3.get_rect(center=CENTER_BOTTOMLEFT)
    rect4 = rotated_arrow4.get_rect(center=CENTER_BOTTOMRIGHT)

    # **Рисуем Bounding Box (границы объекта)**
    pygame.draw.rect(screen, (0, 255, 255), rect1, 2)  # Голубая рамка (topleft)
    pygame.draw.rect(screen, (255, 0, 255), rect2, 2)  # Фиолетовая рамка (topright)
    pygame.draw.rect(screen, (0, 255, 0), rect3, 2)    # Зелёная рамка (bottomleft)
    pygame.draw.rect(screen, (255, 255, 0), rect4, 2)  # Жёлтая рамка (bottomright)

    # **Рисуем стрелки**
    screen.blit(rotated_arrow1, rect1.topleft)
    screen.blit(rotated_arrow2, rect2.topright)
    screen.blit(rotated_arrow3, rect3.bottomleft)
    screen.blit(rotated_arrow4, rect4.bottomright)

    # **Рисуем центр вращения**
    pygame.draw.circle(screen, (255, 0, 0), CENTER_TOPLEFT, 5)   # Красная точка (topleft)
    pygame.draw.circle(screen, (255, 0, 0), CENTER_TOPRIGHT, 5)  # Красная точка (topright)
    pygame.draw.circle(screen, (255, 0, 0), CENTER_BOTTOMLEFT, 5)  # Красная точка (bottomleft)
    pygame.draw.circle(screen, (255, 0, 0), CENTER_BOTTOMRIGHT, 5)  # Красная точка (bottomright)

    # Обновляем экран
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

    # Увеличиваем угол поворота
    angle += 2

    # Обрабатываем выход
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
