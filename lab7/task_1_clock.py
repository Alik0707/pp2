import pygame  
import time  


# Инициализация Pygame  
pygame.init()  

# Установка размеров окна  
WIDTH, HEIGHT = 800, 600  
im = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Мики")  

# Загрузка фонового изображения
background = pygame.image.load("lab7/clock.png")  
sec_line = pygame.image.load("lab7/leftarm.png")
min_line = pygame.image.load("lab7/leftarm.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  

# размеры стрелки
min_line  = pygame.transform.scale(min_line, (60,600)) # Минутная стрелка
sec_line = pygame.transform.scale(sec_line, (60,700)) 

#центр  

CENTER = (WIDTH / 2, HEIGHT / 2)  


def rotate(imag,angle):
    rotated_image = pygame.transform.rotate(imag, angle) #rotate уже принимает угол и с обратном направлени
    rect = rotated_image.get_rect(center=CENTER) # после поворота центр смещается чтобы норм было надо центр обозначить
    im.blit(rotated_image, rect.topleft) # topleft левый верхий угол
    


# Основной цикл часов  
running = True  
while running:  
    im.blit(background,(0,0))  # Отображаем фон  
    time_now = time.localtime()
    minut =  time_now.tm_min
    seconds = time_now.tm_sec
    
    sec_angle = -(seconds * 6 )
    min_angle = -(minut * 6 + seconds * 0.1) 

    rotate(sec_line,sec_angle)
    rotate(min_line,min_angle)


    # Обновляем экран  
    pygame.display.update()  
    
    #проверка если закрыта то стоп 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
    
    # Задержка на 1 секунду  
    pygame.time.delay(1000)  

pygame.quit()
