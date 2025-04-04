# Imports
import pygame, sys
import random, time

# Initialzing
pygame.init()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #иницилизируем спрайт
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) #обохначает центр

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1 #прошедшие машины
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

    def move(self):
        global COINS
        global SPEED
        #adding different amount of coins depending on location of coin
        
        COINS += random.randint(1,3)
        
        if COINS>=10:
            SPEED+=1
        
        if  COINS>=20:
            SPEED+=1
         
        if COINS>=30:
            SPEED+=1
        
        if COINS>=40:
            SPEED+=1
           
        if COINS>=50:
            SPEED+=1
    
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) #стартовая позиция игрока

    def move(self):
        pressed_keys = pygame.key.get_pressed()#при нажатии
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, 5)

def game_over_screen():
    screen.fill(RED)
    screen.blit(game_over, (30, 250))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Продолжить игру при нажатии на пробел
                    return True
                elif event.key == pygame.K_ESCAPE:  # Закончить игру при нажатии на ESC
                    return False
# FPS
FPS =60
FramePerSec = pygame.time.Clock()

# Creating colors
RED = (255,0,0)
BLACK = (0, 0, 0)


# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COINS = 0


# Setting up Fonts
font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")

# Create screen
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")

# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coinss = pygame.sprite.Group()
coinss.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


background_y = 0  # Initialize background y-coordinate

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # If there is a collision between a player and an enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        continue_game = game_over_screen()
        if continue_game:
            # Перезапуск игры
            SCORE = 0
            COINS = 0
            SPEED = 3
            P1.rect.center = (160, 520)  # Возвращаем игрока на стартовую позицию
            E1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Враг тоже сбрасывается
            C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))
        else:
            pygame.quit()
            sys.exit()

    # Scroll the background
    background_y = (background_y + SPEED) % background.get_height() # двигаем вниз картинку после чего продолжение 171

    # Draw the background at the calculated position
    screen.blit(background, (0, background_y)) # рисуем часть здесь а вторую часть
    screen.blit(background, (0, background_y - background.get_height()))

    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))

    coins = font_small.render(str(COINS), True, BLACK)
    screen.blit(coins, (370, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

       
        if entity == C1:
            if pygame.sprite.spritecollideany(P1, coinss):
                entity.move()
        else:
            entity.move()

    # Move the second random car
    for enemy in enemies:
        enemy.move()

    # Move the coins
    for coin in coinss:
        coin.rect.y += SPEED #чтобы монеты спускались вниз с той же скоростью

        # Respawn coins if they go off-screen
        if coin.rect.top > SCREEN_HEIGHT: #если монета ушла вниз экрана
            coin.rect.y = -coin.rect.height #находится полностью сверху горизонта
            coin.rect.x = random.randint(40, SCREEN_WIDTH - 40) #

    pygame.display.update()
    FramePerSec.tick(FPS)