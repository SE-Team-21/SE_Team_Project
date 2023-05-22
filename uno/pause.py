from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.Button_Class import Button

class Pause(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((400, 150), (120, 60), 'RESUME', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((400, 250), (120, 60), 'OPTIONS', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((400, 350), (120, 60), 'Achievement', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((400, 450), (120, 60), 'GAME QUIT', lambda x,y: self.next_screen(x,y)))

    def next_screen(self, idx, running):
        if idx == 0:
            self.mode[C.NEXT_SCREEN] = C.PLAYING
        elif idx == 1:
            self.mode[C.NEXT_SCREEN] = C.SETTING
            self.mode[C.PREV_SCREEN] = C.STOP
        elif idx == 2 :
            self.mode[C.NEXT_SCREEN] = C.ACHIEVEMENT
            self.mode[C.PREV_SCREEN] = C.STOP
        elif idx == 3:
            self.mode[C.NEXT_SCREEN] = C.START
            C.IS_GAME_END = True

    def main_loop(self, running):
        self.screen.fill((255, 255, 255))
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                for idx, item in enumerate(self.Button_list):
                    if item.above:
                        item.click((idx, running))