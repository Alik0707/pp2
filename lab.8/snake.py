import pygame

import sys
import random
pygame.init()
score = 0
speed = 10
level = 1
width , height = 500,500
cell_size = 10 # size of snake
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("SNAKE")
black = (0,0,0)
green = (0,255,0)
snake_pos = [100,100] #for changing
snake_body=[[100,100],[80,100],[60,100]] # part of body
direction = 'RIGHT'
change_to = direction
clock =pygame.time.Clock()


#changin level 
def lev():
    global level 
    global speed
    level = (score // 6)+1
    if level == 2:
        speed = 12
    elif level == 3:
        speed = 14
    elif level == 4:
        speed = 16
    elif level == 5:
        speed = 18
    elif level == 6:
        speed = 20
    elif level == 7:
        speed = 22
    elif level == 8:
        speed = 24                    



class apple():
    def __init__(self):
         #подгоняю картинку 
        self.image = pygame.image.load("apple.png")
        self.image = pygame.transform.scale(self.image,(30,30)) 
        self.rect = self.image.get_rect()#прямоуголник картинки
        self.rect.center = (random.randint(30, width - 30), random.randint(30, height - 30)) #центр установливаем
    def eat(self):
        global score 
        snake_head = pygame.Rect(snake_body[0][0], snake_body[0][1], cell_size, cell_size)  # Создаем прямоугольник для головы змеи
        if snake_head.colliderect(self.rect):  # Проверяем столкновение с яблоком
            self.rect.center = (random.randint(30, width - 30), random.randint(30, height - 30))
            score += 1
            return True #for checking eat чтобы узнать надо ли удалять хвост или нет
        return False



app = apple()

Running = True

while Running:
    #paint all the elements
    screen.fill(black)
    screen.blit(app.image,app.rect)
    #check colliderect 
    app.eat()

    #word SCORE
    font = pygame.font.SysFont("Verdana", 15)
    word_score = font.render(f"SCORE:{score}",True,(255,255,255))
    screen.blit(word_score,(0,0))

    #word level and unction level
    lev()
    word_level = font.render(f"LEVEL:{level}",True,(255,255,255))
    screen.blit(word_level,(420,0))
    #check keydown 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != "UP":
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = 'LEFT'  
    direction = change_to

    #change position of part of body
    if  direction == 'UP':
        snake_pos[1] = (snake_pos[1]-cell_size)% height
    elif direction == 'DOWN':
        snake_pos[1] = (snake_pos[1] + cell_size)%height
    elif direction == 'RIGHT':
        snake_pos[0]= (snake_pos[0] + cell_size)%width 
    elif direction == 'LEFT':
        snake_pos[0] = (snake_pos[0] - cell_size)%width 
    
    snake_body.insert(0,list(snake_pos))
    if not app.eat():
        snake_body.pop()

    for block in snake_body:
        pygame.draw.rect(screen,green,pygame.Rect(block[0],block[1],cell_size,cell_size))

        # проверяем 
    for block in snake_body[1:]:  # Не проверяем саму голову [0], только тело
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            Running = False # Завершить игру
            break
    pygame.display.flip()
    clock.tick(speed)