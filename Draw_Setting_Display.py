from Button_Class import Button
from Text_Class import Text
import pygame as pg

Button_list = []
Button_list.append(Button((400, 350), (200, 60), 'Return to Main Menu'))
Text_list = []
Text_list.append(Text((320, 60), 40, 'Display'))
Text_list.append(Text((320, 120), 40, 'Key Setting'))
Text_list.append(Text((320, 180), 40, 'color mode'))
Text_list.append(Text((320, 240), 40, 'Default Options'))

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
                        mode[0]=1
        elif Button_list[0].rect.collidepoint(mouse_pos):
            Button_list[0].above()
        else:
            for item in Button_list:
                item.inactive()
    
    screen.fill((255, 255, 255))
    for item in Button_list:
        item.draw(screen)
    for item in Text_list:
        item.draw(screen)