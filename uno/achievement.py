from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.Button_Class import Button
from uno.Text_Class import Text

class Achievement(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((400, 500), (120, 60), 'Back', self.next_screen))
        self.Text_list.append(Text((40, 20), 30, 'First Win in Single Mode', C.WHITE))
        self.Text_list.append(Text((40, 70), 30, 'Story Mode Area1 Clear', C.WHITE))
        self.Text_list.append(Text((40, 120), 30, 'Story Mode Area2 Clear', C.WHITE))
        self.Text_list.append(Text((40, 170), 30, 'Story Mode Area3 Clear', C.WHITE))
        self.Text_list.append(Text((40, 220), 30, 'Story Mode Area4 Clear', C.WHITE))
        self.Text_list.append(Text((40, 270), 30, 'Win in 10 Turns', C.WHITE))
        self.Text_list.append(Text((40, 320), 30, 'With No Active Card', C.WHITE))
        self.Text_list.append(Text((40, 370), 30, 'UNO', C.WHITE))


    def next_screen(self):
        self.mode[C.NEXT_SCREEN] = self.mode[C.PREV_SCREEN]

    def main_loop(self, running):
        self.screen.fill(C.BLACK)
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                for idx, item in enumerate(self.Button_list):
                    if item.above:
                        item.click()