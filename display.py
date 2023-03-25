import pygame as pg
from abc import *
from pygame.locals import *
import uno.Constants as C
import uno.KeySettings as K
from uno.Button_Class import Button
from uno.Text_Class import Text
import os

COLORBLIND_MODE = False
COLORBLIND_COLORS = {
    'red': (255, 100, 100),
    'green': (100, 255, 100),
    'blue': (100, 100, 255),
    'yellow': (255, 255, 100),
}

REGULAR_COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
}

class Display(metaclass=ABCMeta):
    # Static Variable
    mode = [C.START, C.START]
    display_idx = 0
    key_idx = -1

    def __init__(self, colorblind_mode = False):
        self.Button_list = []
        self.Text_list = []
        self.screen = pg.display.set_mode(C.DISPLAY_SIZE[Display.display_idx])
        self.colorblind_mode = colorblind_mode

    def draw_card(self, card, x, y):
        card_image = pg.image.load(os.path.join('assets', f'{card}.png'))
        self.screen.blit(card_image, (x, y))

    def get_color(self, color_name):
        if self.colorblind_mode:
            return COLORBLIND_COLORS.get(color_name, (255, 255, 255))
        else:
            return REGULAR_COLORS.get(color_name, (255, 255, 255))

    def update_screen(self, mouse_pos): # 현재 화면 업데이트
        for item in self.Button_list:
            item.change_size(Display.display_idx)
            item.update(mouse_pos)
            item.draw(self.screen)
        for item in self.Text_list:
            item.change_size(Display.display_idx)
            item.draw(self.screen)
        pg.display.update()

    @abstractmethod
    def next_screen(self): # 버튼 클릭시 다음 화면으로 전환
        pass

    @abstractmethod
    def main_loop(self):
        pass

class Start(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((100, 150), (120, 60), 'Play', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((100, 300), (120, 60), 'Options', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((100, 450), (120, 60), 'Quit', lambda x,y: self.next_screen(x,y)))
        self.backgroundimg = pg.transform.scale(pg.image.load("./assets/images/Main.png"), C.DISPLAY_SIZE[Display.display_idx])

    def next_screen(self, idx, running):
        if idx == 0:                            
            self.mode[C.NEXT_SCREEN] = C.PLAYING
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
                for idx, item in enumerate(K.KEY_Settings):
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

class Setting(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((200, 120), (100, 60), '800x600', lambda idx, running: self.screen_size_change(idx, running)))
        self.Button_list.append(Button((400, 120), (100, 60), '880x660', lambda idx, running: self.screen_size_change(idx, running)))
        self.Button_list.append(Button((600, 120), (100, 60), '960x720', lambda idx, running: self.screen_size_change(idx, running)))
        self.Button_list.append(Button((400, 550), (200, 60), 'Back', lambda idx, running: self.next_screen(idx, running)))
        self.Button_list.append(Button((95, 290), (110, 60), 'UP', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((217, 290), (110, 60), 'DOWN', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((339, 290), (110, 60), 'RIGHT', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((461, 290), (110, 60), 'LEFT', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((583, 290), (110, 60), 'RETURN', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((705, 290), (110, 60), 'ESCAPE', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((400, 400), (80, 40), 'OFF'))
        self.Button_list.append(Button((400, 470), (140, 60), 'Default Options'))
        self.Text_list.append(Text((353, 40), 40, 'Resolution'))
        self.Text_list.append(Text((349, 180), 40, 'Key Setting'))
        self.Text_list.append(Text((331, 350), 40, 'Colorblind Mode'))
        self.Text_list.append(Text((83, 230), 40, 'UP'))
        self.Text_list.append(Text((194, 230), 40, 'LEFT'))
        self.Text_list.append(Text((307, 230), 40, 'DOWN'))
        self.Text_list.append(Text((430, 230), 40, 'RIGHT'))
        self.Text_list.append(Text((541, 230), 40, 'RETURN'))
        self.Text_list.append(Text((667, 230), 40, 'ESCAPE'))
        self.key_set = False
        self.index = 0

    def next_screen(self, not_use, running):
        if self.mode[C.PREV_SCREEN] == C.START:
            self.mode[C.NEXT_SCREEN] = C.START
        elif self.mode[C.PREV_SCREEN] == C.STOP:
            self.mode[C.NEXT_SCREEN] = C.STOP
        self.key_set = False

    def button_setting(self, idx, not_use):
        self.key_set = True
        self.index = idx

    def screen_size_change(self, idx, not_use):
        Display.display_idx = idx
        self.screen = pg.display.set_mode(C.DISPLAY_SIZE[Display.display_idx])
        self.key_set = False

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
                        if idx == 10:
                            if item.button_text == 'OFF': # 색약 모드 컨트롤
                                item.change_text('ON')
                            else:
                                item.change_text('OFF')
                        elif idx == 11: # 기본 설정으로 세팅
                            print('Default Options Clicked')
                        else:
                            item.click((idx, running))
                        break
                    else:
                        if(self.key_set):
                            self.key_set = False
            if(self.key_set):
                if event.type == pg.KEYUP:
                    self.Button_list[self.index].change_text(pg.key.name(event.key))
                    K.save_settings(self.index-4, event.key)
                    self.key_set = False

class Playing(Display):
    def __init__(self):
        super().__init__()
        self.Text_list.append(Text((220, 60), 40, 'Playing Display'))
        self.Text_list.append(Text((220, 120), 40, 'Press ESC to PAUSE Menu'))

    def next_screen(self):
        pass

    def main_loop(self, running):
        self.screen.fill((255, 255, 255))
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.mode[C.NEXT_SCREEN] = C.STOP

class Pause(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((400, 200), (100, 50), 'RESUME', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((400, 300), (100, 50), 'OPTIONS', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((400, 400), (100, 50), 'GAME QUIT', lambda x,y: self.next_screen(x,y)))

    def next_screen(self, idx, running):
        if idx==0:
            self.mode[C.NEXT_SCREEN] = C.PLAYING
        elif idx==1:
            self.mode[C.NEXT_SCREEN] = C.SETTING
            self.mode[C.PREV_SCREEN] = C.STOP
        elif idx==2:
            self.mode[C.NEXT_SCREEN] = C.START

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
