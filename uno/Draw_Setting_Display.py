from uno.Button_Class import Button
from uno.Text_Class import Text
import pygame as pg
from uno.Dataset import change_size
import uno.constants as C

Button_list = []
Button_list.append(Button((400, 400), (200, 60), 'Back'))
Button_list.append(Button((200, 160), (100, 60), '800x600'))
Button_list.append(Button((400, 160), (100, 60), '880x660'))
Button_list.append(Button((600, 160), (100, 60), '960x720'))

Text_list = []
Text_list.append(Text((320, 60), 40, 'Display'))
Text_list.append(Text((320, 200), 40, 'Key Setting'))
Text_list.append(Text((320, 260), 40, 'color mode'))
Text_list.append(Text((320, 320), 40, 'Default Options'))

screen_size = [(800, 600), (880, 660), (960, 720)]

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
                    if idx==0:
                        if mode[C.PREV_SCREEN] == C.START:
                            mode[C.NEXT_SCREEN] = C.START
                        elif mode[C.PREV_SCREEN] == C.STOP:
                            mode[C.NEXT_SCREEN] = C.STOP
                    else:
                        screen = pg.display.set_mode(screen_size[idx-1])
                        for item in Button_list:
                            item.change_size(idx)
                        for item in Text_list:
                            item.change_size(idx)
                        change_size(idx)
        else:
            if flag:
                for item in Button_list:
                    item.inactive()
    screen.fill((255, 255, 255))
    for item in Button_list:
        item.draw(screen)
    for item in Text_list:
        item.draw(screen)