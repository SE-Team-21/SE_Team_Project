from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.KeySettings import Data
from uno.Button_Class import Button
import uno.Music as Music

class Start(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((100, 150), (120, 60), 'Play', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((100, 300), (120, 60), 'Options', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((100, 450), (120, 60), 'Quit', lambda x,y: self.next_screen(x,y)))
        self.backgroundimg = pg.transform.scale(pg.image.load("./assets/images/Main.png"), C.DISPLAY_SIZE[Display.display_idx])
        Music.Background_Music(0).play()

    def next_screen(self, idx, running):
        if idx == 0:                            
            self.mode[C.NEXT_SCREEN] = C.MODE
        elif idx == 1:
            self.mode[C.NEXT_SCREEN] = C.SETTING
            self.mode[C.PREV_SCREEN] = C.START
        elif idx == 2:
            running[0] = False
    
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
                if event.key not in Data.data.KEY_Settings:
                    print("error")
