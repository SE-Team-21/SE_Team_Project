from uno.Button_Class import Button
from uno.Text_Class import Text
import pygame as pg
from uno.Dataset import change_size
import uno.constants as C
import uno.KeySettings as K

Button_list = []
Button_list.append(Button((200, 160), (100, 60), '800x600'))
Button_list.append(Button((400, 160), (100, 60), '880x660'))
Button_list.append(Button((600, 160), (100, 60), '960x720'))
Button_list.append(Button((400, 550), (200, 60), 'Back'))
Button_list.append(Button((80, 320), (100, 60), 'UP'))
Button_list.append(Button((230, 320), (100, 60), 'DOWN'))
Button_list.append(Button((380, 320), (100, 60), 'RIGHT'))
Button_list.append(Button((530, 320), (100, 60), 'LEFT'))
Button_list.append(Button((680, 320), (100, 60), 'ENTER'))

Text_list = []
Text_list.append(Text((320, 60), 40, 'Display'))
Text_list.append(Text((320, 200), 40, 'Key Setting'))
Text_list.append(Text((320, 500), 40, 'color mode'))
Text_list.append(Text((320, 550), 40, 'Default Options'))
Text_list.append(Text((50, 260), 40, 'UP'))
Text_list.append(Text((200, 260), 40, 'LEFT'))
Text_list.append(Text((350, 260), 40, 'DOWN'))
Text_list.append(Text((500, 260), 40, 'RIGHT'))
Text_list.append(Text((650, 260), 40, 'Enter'))

screen_size = [(800, 600), (880, 660), (960, 720)]
key_set = False
index = 0

def draw(screen, mode, running):
    for event in pg.event.get():
        mouse_pos = pg.mouse.get_pos()
        flag = True
        global key_set, index
        for item in Button_list:
            if item.rect.collidepoint(mouse_pos):
                item.above()
                flag = False
        if event.type == pg.QUIT:
            running[0] = False
            return
        elif event.type == pg.MOUSEBUTTONDOWN:
            for idx, item in enumerate(Button_list):
                if item.rect.collidepoint(mouse_pos):
                    item.active()
                    if idx == 3:
                        if mode[C.PREV_SCREEN] == C.START:
                            mode[C.NEXT_SCREEN] = C.START
                        elif mode[C.PREV_SCREEN] == C.STOP:
                            mode[C.NEXT_SCREEN] = C.STOP
                        if(key_set):
                            print(1)
                            key_set = False
                    elif idx >= 4 and idx <= 8:
                        key_set = True
                        print(key_set)
                        index = idx
                        break
                    else:
                        screen = pg.display.set_mode(screen_size[idx])
                        for item in Button_list:
                            item.change_size(idx)
                        for item in Text_list:
                            item.change_size(idx)
                        change_size(idx)
                        if(key_set):
                            print(2)
                            key_set = False
                else:
                    if(key_set):
                        print(3)
                        key_set = False
        else:
            if flag:
                for item in Button_list:
                    item.inactive()
        if(key_set):
            if event.type == pg.KEYUP:
                Button_list[index].change_text(pg.key.name(event.key))
                K.save_settings(index, event.key)
                key_set = False
                
            
    screen.fill((255, 255, 255))
    for item in Button_list:
        item.draw(screen)
    for item in Text_list:
        item.draw(screen)