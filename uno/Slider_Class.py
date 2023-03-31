import pygame as pg
import uno.Constants as C

class Slider:
    def __init__(self, x, y, width, height, sound_level):
        pg.font.init()
        self.slider_x = x
        self.slider_y = y
        self.slider_width = width
        self.slider_height = height
        self.sound_level = sound_level
        self.font = pg.font.SysFont(None, 30)

    def draw(self, screen, weight_idx):
        self.font = pg.font.SysFont(None, int(30*C.WEIGHT[weight_idx]))
        pg.draw.rect(screen, (128, 128, 128), (int(self.slider_x*C.WEIGHT[weight_idx]), int(self.slider_y*C.WEIGHT[weight_idx]), int(self.slider_width*C.WEIGHT[weight_idx]), int(self.slider_height*C.WEIGHT[weight_idx])))
        handle_size = int(self.slider_height*C.WEIGHT[weight_idx])
        handle_x = int(self.slider_x*C.WEIGHT[weight_idx]) + int(self.sound_level * self.slider_width*C.WEIGHT[weight_idx]) - handle_size/2
        handle_y = int(self.slider_y*C.WEIGHT[weight_idx])
        pg.draw.rect(screen, C.WHITE, (handle_x, handle_y, handle_size, handle_size))
        label = self.font.render("{:.0%}".format(self.sound_level), True, C.WHITE)
        label_rect = label.get_rect(center=(int(self.slider_x*C.WEIGHT[weight_idx]) - int(40*C.WEIGHT[weight_idx]), int(self.slider_y*C.WEIGHT[weight_idx]) + int(self.slider_height*C.WEIGHT[weight_idx] // 2)))
        screen.blit(label, label_rect)