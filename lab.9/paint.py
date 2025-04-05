import pygame
import sys
import math
pygame.init()

width, height = 800, 800 #size of screen
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
#квадрат
flag_square = False
square_ready = False
#парвильный треуг
flag_right_triangle = False
right_triangle_ready = False
#равнобедренный треуг
flag_equilateral_triangle = False
equilateral_triangle_ready = False
#ромб
flag_rhombus = False
rhombus_ready = False


#значения при нажатии и отпускании мышки
start_x , start_y = 0,0
end_x , end_y = 0,0

top_left_x, top_left_y = 0, 0

side = 0


drawing = False
brush_color = black
#action и онулировании значении флаа круга и прямоугольника

def reset_flags():
    global flag_circle, flag_rect, flag_square, flag_right_triangle, flag_equilateral_triangle, flag_rhombus
    flag_circle = flag_rect = flag_square = flag_right_triangle = flag_equilateral_triangle = flag_rhombus = False

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
    pygame.draw.rect(screen, white, (0, 100, 800, 800))  # очищаем только область рисования
    reset_flags()
def eraser():
    global brush_color
    brush_color = white
    reset_flags()

def square():
    reset_flags()
    global flag_square
    flag_square = True

def right_triangle():
    reset_flags()
    global flag_right_triangle
    flag_right_triangle = True

def equilateral_triangle():
    reset_flags()
    global flag_equilateral_triangle
    flag_equilateral_triangle = True

def rhombus():
    reset_flags()
    global flag_rhombus
    flag_rhombus = True

def circle():
    reset_flags()
    global flag_circle
    flag_circle = True
    
def rectangle():
    reset_flags()
    global flag_rect 
    flag_rect = True
    


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
    Button(680, 10, 60, 30, 'rect', gray, rectangle),
    Button(10, 50, 120, 30, 'Square', gray, square),
    Button(140, 50, 120, 30, 'Right Tri', gray, right_triangle),
    Button(270, 50, 160, 30, 'Equilateral', gray, equilateral_triangle),
    Button(440, 50, 120, 30, 'Rhombus', gray, rhombus)


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
                    drawing = False
                if flag_rect:
                    rect_ready = True#точно самое готовность рисовать 
                    drawing = False
                if flag_square: #аналогично
                    square_ready = True
                    drawing = False
                if flag_right_triangle:#аналогично
                    drawing = False
                    right_triangle_ready = True
                if flag_equilateral_triangle:#аналогично
                    drawing = False
                    equilateral_triangle_ready = True
                if flag_rhombus:#аналогично
                    drawing = False
                    rhombus_ready = True

        for button in buttons:
            button.check_action(event)

    if rect_ready: # после отпускания дает сигнал надо рисовать 
        width = end_x - start_x
        height = end_y - start_y

        top_left_x = min(start_x, end_x)#из двух выбирает верхнее то есть
        top_left_y = min(start_y, end_y)

        pygame.draw.rect(screen, brush_color, (top_left_x, top_left_y, abs(width), abs(height)))
        rect_ready = False

    if circle_ready: # после отпускания дает сигнал надо рисовать 
        radius = int(math.hypot(end_x - start_x, end_y - start_y) / 2)#radius 
        center_x = (start_x + end_x) /2
        center_y = (start_y + end_y) /2
        pygame.draw.circle(screen, brush_color, (center_x, center_y), radius)
        circle_ready = False
    if square_ready:
        side = min(abs(end_x - start_x), abs(end_y - start_y))
        top_left_x = start_x
        top_left_y = start_y

        if end_x < start_x:
            top_left_x = start_x - side
        if end_y < start_y:
            top_left_y = start_y - side

        pygame.draw.rect(screen, brush_color, (top_left_x, top_left_y, side, side))
        square_ready = False

    if right_triangle_ready:
        points = [(start_x, start_y), (start_x, end_y), (end_x, end_y)]#
        pygame.draw.polygon(screen, brush_color, points)
        right_triangle_ready = False

    if equilateral_triangle_ready:
        side = abs(end_x - start_x)#сторона
        height_triangle = int(math.sqrt(3) / 2 * side)#высота
        x1,y1 = min(start_x,end_x), max(end_y,start_y)#левая точка
        x2,y2= max(start_x,end_x),max(end_y,start_y)#правая точка 
        x3,y3= x1 + side / 2,end_y - height_triangle#ввверх
        pygame.draw.polygon(screen, brush_color, [(x1, y1), (x2, y2), (x3, y3)])
        equilateral_triangle_ready = False

    if rhombus_ready:
        center_x = (start_x + end_x) // 2
        center_y = (start_y + end_y) // 2
        dx = abs(end_x - start_x) // 2#height x
        dy = abs(end_y - start_y) // 2#высота по y 
        points = [
            (center_x, center_y - dy),
            (center_x + dx, center_y),
            (center_x, center_y + dy),
            (center_x - dx, center_y)
        ]
        pygame.draw.polygon(screen, brush_color, points)
        rhombus_ready = False

    if drawing and not (flag_circle or flag_rect or flag_square or flag_right_triangle or flag_equilateral_triangle or flag_rhombus):
        mouse_x , mouse_y = pygame.mouse.get_pos()
        if mouse_y > 50:
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)

    pygame.draw.rect(screen, gray, (0, 0, width, 100))
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()



    






