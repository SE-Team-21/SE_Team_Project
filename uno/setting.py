from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.KeySettings import Data
from uno.Button_Class import Button
from uno.Text_Class import Text
from uno.Slider_Class import Slider
import uno.Music as Music

class Setting(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((540, 80), (20, 20), '<', lambda idx, running: self.screen_size_change(idx, running)))
        self.Button_list.append(Button((740, 80), (20, 20), '>', lambda idx, running: self.screen_size_change(idx, running)))
        self.Button_list.append(Button((540, 120), (20, 20), '<', lambda idx, running: self.colorblind_control(idx, running)))
        self.Button_list.append(Button((740, 120), (20, 20), '>', lambda idx, running: self.colorblind_control(idx, running)))
        self.Button_list.append(Button((320, 210), (120, 30), 'UP', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((320, 250), (120, 30), 'DOWN', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((320, 290), (120, 30), 'RIGHT', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((320, 330), (120, 30), 'LEFT', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((320, 370), (120, 30), 'RETURN', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((320, 410), (120, 30), 'ESCAPE', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((680, 210), (120, 30), '1', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((680, 250), (120, 30), '2', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((680, 290), (120, 30), '3', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((680, 330), (120, 30), '4', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((680, 370), (120, 30), '5', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((700, 510), (140, 40), 'Default Options', lambda idx, running: self.default_setting(idx, running)))
        self.Button_list.append(Button((700, 570), (140, 40), 'Back', lambda idx, running: self.next_screen(idx, running)))
        self.Text_list.append(Text((20, 20), 30, 'DISPLAY', C.WHITE))
        self.Text_list.append(Text((40, 70), 20, 'Resolution', C.WHITE))
        self.Text_list.append(Text((605, 70), 20, '800x600', C.WHITE))
        self.Text_list.append(Text((40, 110), 20, 'Colorblind Mode', C.WHITE))
        self.Text_list.append(Text((565, 110), 20, '    Not Applied', C.WHITE))
        self.Text_list.append(Text((20, 150), 30, 'KEY CONTROL', C.WHITE))
        self.Text_list.append(Text((40, 200), 20, 'Up', C.WHITE))
        self.Text_list.append(Text((40, 240), 20, 'Left', C.WHITE))
        self.Text_list.append(Text((40, 280), 20, 'Down', C.WHITE))
        self.Text_list.append(Text((40, 320), 20, 'Right', C.WHITE))
        self.Text_list.append(Text((40, 360), 20, 'Return', C.WHITE))
        self.Text_list.append(Text((40, 400), 20, 'Escape', C.WHITE))
        self.Text_list.append(Text((440, 200), 20, 'Red', C.WHITE))
        self.Text_list.append(Text((440, 240), 20, 'Green', C.WHITE))
        self.Text_list.append(Text((440, 280), 20, 'Blue', C.WHITE))
        self.Text_list.append(Text((440, 320), 20, 'Yellow', C.WHITE))
        self.Text_list.append(Text((440, 360), 20, 'Draw', C.WHITE))
        self.Text_list.append(Text((20, 440), 30, 'SOUND', C.WHITE))
        self.Text_list.append(Text((40, 490), 20, 'Master Volume', C.WHITE))
        self.Text_list.append(Text((40, 530), 20, 'Music Volume', C.WHITE))
        self.Text_list.append(Text((40, 570), 20, 'Effect Volume', C.WHITE))
        self.Slider_list = []
        self.Slider_list.append(Slider(350, 493, 200, 20, 0.5))
        self.Slider_list.append(Slider(350, 533, 200, 20, 0.5))
        self.Slider_list.append(Slider(350, 573, 200, 20, 0.5))
        self.key_set = False
        self.dragging = False
        self.slider_idx = 0
        self.index = 0
        self.active = [False, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

        # Load Setting
        for i in range(11):
            self.Button_list[i+4].change_text(pg.key.name(Data.data.KEY_Settings[i]))
        Display.display_idx = Data.data.Resolution
        self.Text_list[2].change_text(C.DISPLAY_SIZE_STR[Display.display_idx])
        if Display.display_idx == 1:
            self.active[0] = True
        elif Display.display_idx == 2:
            self.active[0] = True
            self.active[1] = False
        Display.colorblind_idx = Data.data.Color
        if Display.colorblind_idx == 0 or Display.colorblind_idx == 1:
            self.active[2] = True
            self.Text_list[4].change_text(C.COLORBLINDMODE_STR[Display.colorblind_idx])
        elif Display.colorblind_idx == 2:
            self.active[2] = True
            self.active[3] = False
            self.Text_list[4].change_text(C.COLORBLINDMODE_STR[Display.colorblind_idx])
        self.Slider_list[0].s = Data.data.Master_Volume
        self.Slider_list[1].s = Data.data.Music_Volume
        self.Slider_list[2].s = Data.data.Effect_Volume

        
    def next_screen(self, not_use, running):
        self.mode[C.NEXT_SCREEN] = self.mode[C.PREV_SCREEN]
        self.key_set = False

    def button_setting(self, idx, not_use):
        self.key_set = True
        self.index = idx

    def default_setting(self, not_use, not_use_):
        Data.default()
        for i in range(10):
            self.Button_list[i+4].change_text(pg.key.name(Data.data.KEY_Settings[i]))
        Display.display_idx = Data.data.Resolution
        Display.colorblind_idx = Data.data.Color
        self.Slider_list[0].s = Data.data.Master_Volume
        Music.master_volume(0.5)
        self.Slider_list[1].s = Data.data.Music_Volume
        Music.bg_volume(0.5)
        self.Slider_list[2].s = Data.data.Effect_Volume
        Music.ef_volume(0.5)
        self.active[0] = False
        self.active[1] = True
        self.active[2] = False
        self.active[3] = True
        self.screen = pg.display.set_mode(C.DISPLAY_SIZE[Display.display_idx])
        self.Text_list[2].change_text(C.DISPLAY_SIZE_STR[Display.display_idx])
        self.Text_list[4].change_text("    Not Applied")
        self.key_set = False

    def update_screen(self, mouse_pos):
        pg.draw.line(self.screen, C.WHITE, [int(160*C.WEIGHT[Display.display_idx]), int(35*C.WEIGHT[Display.display_idx])], [int(780*C.WEIGHT[Display.display_idx]), int(35*C.WEIGHT[Display.display_idx])], 3)
        pg.draw.line(self.screen, C.WHITE, [int(250*C.WEIGHT[Display.display_idx]), int(165*C.WEIGHT[Display.display_idx])], [int(780*C.WEIGHT[Display.display_idx]), int(165*C.WEIGHT[Display.display_idx])], 3)
        pg.draw.line(self.screen, C.WHITE, [int(140*C.WEIGHT[Display.display_idx]), int(455*C.WEIGHT[Display.display_idx])], [int(780*C.WEIGHT[Display.display_idx]), int(455*C.WEIGHT[Display.display_idx])], 3)
        for item in self.Slider_list:
            item.change_size(Display.display_idx)
            item.draw(self.screen)
        for idx, item in enumerate(self.Button_list):
            if self.active[idx]:
                item.change_size(Display.display_idx)
                item.update(mouse_pos)
                item.draw(self.screen)
        for item in self.Text_list:
            item.change_size(Display.display_idx)
            item.draw(self.screen)
        if Display.colorblind_idx != -1:
            self.color()
        pg.display.update()

    def screen_size_change(self, idx, not_use):
        if idx == 0:
            Display.display_idx -= 1
            if Display.display_idx == 0:
                self.active[0] = False
            elif Display.display_idx == 1:
                self.active[1] = True
        else:
            Display.display_idx += 1
            if Display.display_idx == 2:
                self.active[1] = False
            elif Display.display_idx == 1:
                self.active[0] = True
        self.screen = pg.display.set_mode(C.DISPLAY_SIZE[Display.display_idx])
        self.Text_list[2].change_text(C.DISPLAY_SIZE_STR[Display.display_idx])
        Data.save_resolution(Display.display_idx)
        self.key_set = False

    def colorblind_control(self, idx, not_use):
        if idx == 2:
            Display.colorblind_idx -= 1
            if Display.colorblind_idx == -1:
                self.active[2] = False
            elif Display.colorblind_idx == 1:
                self.active[3] = True
        else:
            Display.colorblind_idx += 1
            if Display.colorblind_idx == 2:
                self.active[3] = False
            elif Display.colorblind_idx == 0:
                self.active[2] = True
        if Display.colorblind_idx == -1:
            self.Text_list[4].change_text("    Not Applied")
        else:
            self.Text_list[4].change_text(C.COLORBLINDMODE_STR[Display.colorblind_idx])
        Data.save_color(Display.colorblind_idx)
        self.key_set = False
        
    def volume_control(self, idx, v):
        print(v)
        if idx == 0:
            #v = Data.data.Master_Volume
            Music.master_volume(v)
        if idx == 1:
            #v = Data.data.Music_Volume
            Music.bg_volume(v)
        if idx == 2:
            #v = Data.data.Music_volume
            Music.ef_volume(v)

    def main_loop(self, running):
        self.screen.fill((0, 0, 0))
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                for idx, item in enumerate(self.Slider_list):
                    handle_rect = pg.Rect(item.hx, item.hy, item.h, item.h)
                    if handle_rect.collidepoint(event.pos):
                        self.dragging = True
                        self.slider_idx = idx
                for idx, item in enumerate(self.Button_list):
                    if item.above and self.active[idx]:
                        item.click((idx, running))
                        break
                    else:
                        if(self.key_set):
                            self.key_set = False
            elif event.type == pg.MOUSEBUTTONUP:
                if self.dragging:
                    self.dragging = False
                    Data.save_sound(self.slider_idx, max(0, min(1, (event.pos[0] - self.Slider_list[self.slider_idx].x) / self.Slider_list[self.slider_idx].w)))
                    self.volume_control(self.slider_idx, max(0, min(1, (event.pos[0] - self.Slider_list[self.slider_idx].x) / self.Slider_list[self.slider_idx].w)))
            elif event.type == pg.MOUSEMOTION:
                if self.dragging:
                    self.Slider_list[self.slider_idx].s = max(0, min(1, (event.pos[0] - self.Slider_list[self.slider_idx].x) / self.Slider_list[self.slider_idx].w))
            if self.key_set:
                if event.type == pg.KEYUP:
                    if event.key not in Data.data.KEY_Settings:
                        self.Button_list[self.index].change_text(pg.key.name(event.key))
                        Data.save_key(self.index-4, event.key)
                        self.key_set = False
                    else:
                        warning = Button((400, 300), (300, 60), 'The key is already in use', color=C.RED)
                        warning.draw(self.screen)
                        pg.display.update()
                        pg.time.wait(1500)