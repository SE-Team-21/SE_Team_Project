from uno.Button_Class import Button
from uno.Text_Class import Text
import pygame as pg
import uno.constants as C

Button_list = []
Button_list.append(Button((400, 200), (100, 50), 'SINGLE PLAYER'))
Button_list.append(Button((400, 300), (100, 50), 'OPTIONS'))
Button_list.append(Button((400, 400), (100, 50), 'QUIT'))

Text_list = []
Text_list.append(Text((320, 60), 40, 'UNO Game'))

def draw(screen, mode, running):
    for event in pg.event.get():
        mouse_pos = pg.mouse.get_pos()
        flag = True
        for item in Button_list:
            if item.rect.collidepoint(mouse_pos):
                item.above()
                flag = False
        if event.type == pg.QUIT:
            running[0] = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            for idx, item in enumerate(Button_list):
                if item.rect.collidepoint(mouse_pos):
                    item.active()
                    if idx == 0:                            
                        mode[0] = C.PLAYING
                    elif idx == 1:
                        mode[0] = C.SETTING
                        mode[1] = C.START
                    elif idx==2:
                        running[0] = False
        else:
            if flag:
                for item in Button_list:
                    item.inactive()
    screen.fill((255, 255, 255))
    for item in Button_list:
        item.draw(screen)
    for item in Text_list:
        item.draw(screen)