import pygame
import sys
import math
pygame.init()
width, height = 800, 600 #size of screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple paint') # name of view
#colors
white = (255, 255, 255)
black = (0, 0 , 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

class Button:
    def __init__(self, x, y, width, height, text, color, action):#for init button on the screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text= text
        self.color = color
        self.action = action
    def draw(self, screen): #paint button
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 12))
    def check_action(self, event):#check нажали кнопку или нет
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()
#start variables  
# circle              
flag_circle = False#flag на нажатие кнопки круг
circle_ready = False#нажатие на кнопку мышки после нажатия кнопки круг
# rectangle
flag_rect = False#flag на нажатие кнопки rectangle
rect_ready = False#нажатие на кнопку мышки после нажатия кнопки rect

#значения при нажатии и отпускании мышки
start_x , start_y = 0,0
end_x , end_y = 0,0

drawing = False
brush_color = black
#action и онулировании значении флаа круга и прямоугольника
def reset_flags():
    global flag_circle
    flag_circle = False
    global flag_rect 
    flag_rect = False
def set_black():
    global brush_color
    brush_color = black
    reset_flags()
def set_green():
    global brush_color
    brush_color = green
    reset_flags()
def set_red():
    global brush_color
    brush_color = red
    reset_flags()
def set_blue():
    global brush_color
    brush_color = blue
    reset_flags()
def clear_screen():
    pygame.draw.rect(screen, white, (0, 50, 800, 550))  # очищаем только область рисования
    reset_flags()
def eraser():
    global brush_color
    brush_color = white
    reset_flags()
def circle():
    global flag_circle
    flag_circle = True
    global flag_rect 
    flag_rect = False
def rectangle():
    global flag_rect 
    flag_rect = True
    global flag_circle
    flag_circle = False


def exit_app():
    pygame.quit()
    sys.exit()


buttons =[
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(380, 10, 60, 30, 'Exit', gray, exit_app),
    Button(480, 10, 60, 30, 'Eraser', gray, eraser),
    Button(580, 10, 60, 30, 'Circle', gray, circle),
    Button(680, 10, 60, 30, 'Rect', gray, rectangle)


]

clear_screen()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_x , start_y = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_x , end_y = pygame.mouse.get_pos()
                if flag_circle:
                    circle_ready = True#только при отпускании и закрепляется конечная точка end_x and end_y
                if flag_rect:
                    rect_ready = True#точно саиое готовность рисовать 

        for button in buttons:
            button.check_action(event)
    #rectangle
    if rect_ready: # после отпускания дает сигнал надо рисовать 
        width = end_x - start_x
        height = end_y - start_y

        top_left_x = min(start_x, end_x)#из двух выбирает верхнее то есть
        top_left_y = min(start_y, end_y)

        pygame.draw.rect(screen, brush_color, (top_left_x, top_left_y, abs(width), abs(height)))
        rect_ready = False
    #circle
    if circle_ready: # после отпускания дает сигнал надо рисовать 
        radius = int(math.hypot(end_x - start_x, end_y - start_y) / 2)
        center_x = (start_x + end_x) /2
        center_y = (start_y + end_y) /2
        pygame.draw.circle(screen, brush_color, (center_x, center_y), radius)
        circle_ready = False
    #кисть
    elif drawing and not flag_circle and not flag_rect:
        mouse_x , mouse_y = pygame.mouse.get_pos()
        if mouse_y > 50:
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)
    #фон и кнопки
    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()



    






