from uno.Button_Class import Button
from uno.Text_Class import Text
import pygame as pg
import uno.Constants as C
import test as t
Text_list = []
#Text_list.append(Text((220, 60), 40, 'Playing Display'))
#Text_list.append(Text((220, 120), 40, 'Press ESC to PAUSE Menu'))
Button_list = []

def draw(screen, mode, running):
    t.game_start()
    x = 60
    y = 60
    Text_list.clear()
    for idx, player in enumerate(t.game.players):
        Text_list.append(Text((x, y), 20, 'Player : '+str(idx)))
        x+=220
        for card in player.hand:
            temp = Button((x, y), (60, 120), str(card.card_type))
            if str(card.color)=='red':
                temp.color = C.RED
            elif str(card.color)=='blue':
                temp.color = C.BLUE
            elif str(card.color)=='yellow':
                temp.color = C.YELLOW
            elif str(card.color)=='green':
                temp.color = C.GREEN
            else:
                temp.color = C.INACTIVE_COLOR
            Button_list.append(temp)
            x+=220
        y+=180
        x=60
    run = True
    while run:
        screen.fill((255, 255, 255))
        for item in Text_list:
            item.draw(screen)
        for item in Button_list:
            item.draw(screen)
        for event in pg.event.get():
            mouse_pos = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    mode[C.NEXT_SCREEN] = C.STOP
                    run = False
        pg.display.update()
