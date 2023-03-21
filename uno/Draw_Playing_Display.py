from uno.Button_Class import Button
from uno.Text_Class import Text
import pygame as pg
import uno.constants as C

Text_list = []
Text_list.append(Text((220, 60), 40, 'Playing Display'))
Text_list.append(Text((220, 120), 40, 'Press ESC to PAUSE Menu'))

def draw(screen, mode, running):
    screen.fill((255, 255, 255))
    for item in Text_list:
        item.draw(screen)
    for event in pg.event.get():
        mouse_pos = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            running[0] = False
            return
        elif event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                mode[C.NEXT_SCREEN] = C.STOP