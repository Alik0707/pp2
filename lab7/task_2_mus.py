import pygame  
import os
import time  

def play_music(index):
    pygame.mixer.music.load(list_of_mus[index])  #Загружаем музыку
    pygame.mixer.music.play() #сразу воспроизводим
def name_mus(index):
    font = pygame.font.Font(None,22) #создание шрифта
    text = font.render(for_txt[index],True,(0,0,0))#высвечивается трек
    return text



pygame.init()
pygame.mixer.init()



#ссылки на музыку
mus_fl_path = "/home/zhanybekov-alikhan/Рабочий стол/pp2/lab7/mus"
for_txt = os.listdir(mus_fl_path)
list_of_mus = os.listdir(mus_fl_path)
for i in range(len(list_of_mus)):
    list_of_mus[i] = mus_fl_path+"/"+list_of_mus[i]

#приводим музуку в переменную
mus = pygame.mixer.music.load(list_of_mus[0]) 
play_music(0)
index = 0




#загрузка фона
WIDTH, HEIGHT = 600,800  
im = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("pl")
background = pygame.image.load("/home/zhanybekov-alikhan/Рабочий стол/pp2/lab7/" + "background.jpg")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))


#зона где будет кнопки
fon = pygame.Surface((300, 200))  
fon.fill((255, 255, 255)) 

#buttoms
next = pygame.image.load("/home/zhanybekov-alikhan/Рабочий стол/pp2/lab7/" + "next.png")
next = pygame.transform.scale(next,(100,100))
back = pygame.image.load("/home/zhanybekov-alikhan/Рабочий стол/pp2/lab7/" + "back.png")
back = pygame.transform.scale(back,(100,100))
plae = pygame.image.load("/home/zhanybekov-alikhan/Рабочий стол/pp2/lab7/" + "play.png")
plae = pygame.transform.scale(plae,(100,100))
pause = pygame.image.load("/home/zhanybekov-alikhan/Рабочий стол/pp2/lab7/" + "pause.png")
pause = pygame.transform.scale(pause,(115,113))


#сам принцип работы
running = True    
while running:
    im.blit(background, (0,0))
    im.blit(fon, (155, 500))
    im.blit(next,(350,580))
    im.blit(back,(165,580))
    im.blit(name_mus(index),(200,530))
    
    #---------------------------- чтобы кнопка паузы менялась

    if pygame.mixer.music.get_busy():
        im.blit(pause,(249,575))
        
    else:
        im.blit(plae,(256,580))
        


    for event in pygame.event.get():  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #чтобы кнопка паузы менялась
                if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                        im.blit(pause,(249,575))
                        
                else:
                    pygame.mixer.music.unpause()
                    
                    im.blit(plae,(256,580))
                #--------------------------
            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(list_of_mus)
                play_music(index)

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(list_of_mus)
                play_music(index)
            
            
    

        if event.type == pygame.QUIT:  
            running = False  

    pygame.display.update()





pygame.quit()
