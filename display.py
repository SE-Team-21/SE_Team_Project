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

    def __init__(self, width = 800, height = 600, colorblind_mode = False):
        self.Button_list = []
        self.Text_list = []
        self.screen = pg.display.set_mode((width, height))
        self.colorblind_mode = colorblind_mode

    def draw_card(self, card, x, y):
        card_image = pg.image.load(os.path.join('assets', f'{card}.png'))
        self.screen.blit(card_image, (x, y))

    def get_color(self, color_name):
        if self.colorblind_mode:
            return COLORBLIND_COLORS.get(color_name, (255, 255, 255))
        else:
            return REGULAR_COLORS.get(color_name, (255, 255, 255))


    @abstractmethod
    def update_screen(self):
        pass

    @abstractmethod
    def next_screen(self):
        pass

    @abstractmethod
    def main_loop(self):
        pass

class Start(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((400, 200), (100, 50), 'SINGLE PLAYER', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((400, 300), (100, 50), 'OPTIONS', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((400, 400), (100, 50), 'QUIT', lambda x,y: self.next_screen(x,y)))
        self.Text_list.append(Text((320, 60), 40, 'UNO Game'))

    def next_screen(self, idx, running):
        if idx == 0:                            
            self.mode[C.NEXT_SCREEN] = C.PLAYING
        elif idx == 1:
            self.mode[C.NEXT_SCREEN] = C.SETTING
            self.mode[C.PREV_SCREEN] = C.START
        elif idx == 2:
            running[0] = False

    def update_screen(self, mouse_pos):
        self.screen.fill((255, 255, 255))
        for item in self.Button_list:
            item.update(mouse_pos)
            item.change_size(self.display_idx)
            item.draw(self.screen)
        for item in self.Text_list:
            item.change_size(self.display_idx)
            item.draw(self.screen)
        pg.display.update()

    def main_loop(self, running):
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                for idx, item in enumerate(self.Button_list):
                    if item.above:
                        item.click((idx, running))

class Setting(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((200, 160), (100, 60), '800x600', lambda idx, running: self.screen_size_change(idx, running)))
        self.Button_list.append(Button((400, 160), (100, 60), '880x660', lambda idx, running: self.screen_size_change(idx, running)))
        self.Button_list.append(Button((600, 160), (100, 60), '960x720', lambda idx, running: self.screen_size_change(idx, running)))
        self.Button_list.append(Button((400, 550), (200, 60), 'Back', lambda idx, running: self.next_screen(idx, running)))
        self.Button_list.append(Button((80, 320), (100, 60), 'UP', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((230, 320), (100, 60), 'DOWN', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((380, 320), (100, 60), 'RIGHT', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((530, 320), (100, 60), 'LEFT', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((680, 320), (100, 60), 'ENTER', lambda idx, running: self.button_setting(idx, running)))
        self.Text_list.append(Text((320, 60), 40, 'Display'))
        self.Text_list.append(Text((320, 200), 40, 'Key Setting'))
        self.Text_list.append(Text((320, 500), 40, 'color mode'))
        self.Text_list.append(Text((320, 550), 40, 'Default Options'))
        self.Text_list.append(Text((50, 260), 40, 'UP'))
        self.Text_list.append(Text((200, 260), 40, 'LEFT'))
        self.Text_list.append(Text((350, 260), 40, 'DOWN'))
        self.Text_list.append(Text((500, 260), 40, 'RIGHT'))
        self.Text_list.append(Text((650, 260), 40, 'Enter'))
        self.key_set = False
        self.index = 0
    
    def update_screen(self, mouse_pos):
        self.screen.fill((255, 255, 255))
        for item in self.Button_list:
            item.update(mouse_pos)
            item.draw(self.screen)
        for item in self.Text_list:
            item.draw(self.screen)
        pg.display.update()

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
        self.screen = pg.display.set_mode(C.DISPLAY_SIZE[self.display_idx])
        for item in self.Button_list:
            item.change_size(self.display_idx)
        for item in self.Text_list:
            item.change_size(self.display_idx)
        self.key_set = False

    def main_loop(self, running):
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                for idx, item in enumerate(self.Button_list):
                    if item.above:
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

    def update_screen(self, mouse_pos):
        self.screen.fill((255, 255, 255))
        for item in self.Button_list:
            item.change_size(self.display_idx)
            item.update(mouse_pos)
            item.draw(self.screen)
        for item in self.Text_list:
            item.change_size(self.display_idx)
            item.draw(self.screen)
        pg.display.update()

    def next_screen(self):
        pass

    def main_loop(self, running):
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
        pass

    def update_screen(self, mouse_pos):
        self.screen.fill((255, 255, 255))
        for item in self.Button_list:
            item.change_size(self.display_idx)
            item.update(mouse_pos)
            item.draw(self.screen)
        for item in self.Text_list:
            item.change_size(self.display_idx)
            item.draw(self.screen)
        pg.display.update()

    def next_screen(self, idx, running):
        if idx==0:
            self.mode[C.NEXT_SCREEN] = C.PLAYING
        elif idx==1:
            self.mode[C.NEXT_SCREEN] = C.SETTING
            self.mode[C.PREV_SCREEN] = C.STOP
        elif idx==2:
            self.mode[C.NEXT_SCREEN] = C.START

    def main_loop(self, running):
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                for idx, item in enumerate(self.Button_list):
                    if item.above:
                        item.click((idx, running))