from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.KeySettings import Data
from uno.play import Playing
from uno.Button_Class import Button

class Mode(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((100, 150), (120, 60), 'Story Mode', lambda x,y: self.next_screen(x,y)))  #스토리모드 선택
        self.Button_list.append(Button((100, 250), (120, 60), 'Single Play', lambda x,y: self.next_screen(x,y)))  #싱글모드 선택
        self.Button_list.append(Button((100, 350), (120, 60), 'Multi Play', lambda x,y: self.next_screen(x,y)))  #싱글모드 선택
        self.Button_list.append(Button((100, 450), (120, 60), 'Back', lambda x,y: self.next_screen(x,y)))  #시작 화면 되돌아가기
        self.backgroundimg = pg.transform.scale(pg.image.load("./assets/images/Main.png"), C.DISPLAY_SIZE[Display.display_idx])

    def next_screen(self, idx, running):
        if idx == 0:
            self.mode[C.NEXT_SCREEN] = C.STORY
            C.game_mode = 1
        elif idx == 1:
            self.mode[C.NEXT_SCREEN] = C.PLAYING
            C.game_mode = 0
        elif idx == 2:
            self.mode[C.NEXT_SCREEN] = C.MULTI
        elif idx == 3:
            self.mode[C.NEXT_SCREEN] = C.START
    
    def main_loop(self, running):
        self.screen.fill((255, 255, 255))
        self.backgroundimg = pg.transform.scale(self.backgroundimg, C.DISPLAY_SIZE[Display.display_idx])
        self.screen.blit(self.backgroundimg, (0, 0))
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.Button_list[Display.key_idx].on_key = False
                Display.key_idx = -1
                for idx, item in enumerate(self.Button_list):
                    if item.above:
                        item.click((idx, running))
            elif event.type == pg.KEYUP:
                for idx, item in enumerate(Data.data.KEY_Settings):
                    if event.key == item:
                        if idx == 0 or idx == 1: # Up and Left Key
                            if Display.key_idx == 0:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx = len(self.Button_list)-1
                            elif Display.key_idx == -1:
                                Display.key_idx = 0
                            else:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx -= 1
                            self.Button_list[Display.key_idx].on_key = True
                        elif idx == 2 or idx == 3: # Right and Down Key
                            if Display.key_idx == len(self.Button_list)-1:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx = 0
                            elif Display.key_idx == -1:
                                Display.key_idx = 0
                            else:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx += 1
                            self.Button_list[Display.key_idx].on_key = True
                        elif idx == 4: # Return Key
                            if Display.key_idx != -1:
                                self.Button_list[Display.key_idx].on_key = False
                                self.next_screen(Display.key_idx, running)
                                Display.key_idx = -1