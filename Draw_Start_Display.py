from Button_Class import Button
from Text_Class import Text
import pygame as pg

Button_list = []
Button_list.append(Button((400, 200), (100, 50), 'SINGLE PLAYER'))
Button_list.append(Button((400, 300), (100, 50), 'OPTIONS'))
Button_list.append(Button((400, 400), (100, 50), 'QUIT'))

Text_list = []
Text_list.append(Text((320, 60), 40, 'UNO Game'))

def draw(screen, mode, running):
    for event in pg.event.get():
        mouse_pos = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            running[0] = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Check if the mouse click was inside a button
            for idx, item in enumerate(Button_list):
                if item.rect.collidepoint(mouse_pos):
                    item.active()
                    if idx==0:
                        mode[0]=3
                    elif idx==1:
                        mode[0]=2
                        mode[1]=1
                    elif idx==2:
                        running[0] = False
        elif Button_list[0].rect.collidepoint(mouse_pos): # for문으로 수정해야할듯
            Button_list[0].above()
        elif Button_list[1].rect.collidepoint(mouse_pos):
            Button_list[1].above()
        elif Button_list[2].rect.collidepoint(mouse_pos):
            Button_list[2].above()
        else:
            for item in Button_list:
                item.inactive()
    
    # Fill the background color
    screen.fill((255, 255, 255))
    
    # Draw the buttons and text
    for item in Button_list:
        item.draw(screen)
    for item in Text_list:
        item.draw(screen)
