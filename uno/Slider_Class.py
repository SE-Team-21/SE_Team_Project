import pygame as pg
import uno.Constants as C

class Slider:
    def __init__(self, x, y, width, height, sound_level):
        pg.font.init()
        self.s = sound_level
        self.dx = x
        self.dy = y
        self.dw = width
        self.dh = height
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.hx = self.x + int(self.s * self.w) - self.h//2
        self.hy = self.y
        self.font = pg.font.SysFont(None, 30)

    def draw(self, screen):
        pg.draw.rect(screen, C.GRAY, (self.x, self.y, self.w, self.h))
        pg.draw.rect(screen, C.WHITE, (self.hx, self.hy, self.h, self.h))
        label = self.font.render("{:.0%}".format(self.s), True, C.WHITE)
        label_rect = label.get_rect(center=(self.x - 40, self.y + self.h // 2))
        screen.blit(label, label_rect)
    
    def change_size(self, idx):
        self.font = pg.font.SysFont(None, 30)
        self.x = int(self.dx * C.WEIGHT[idx])
        self.y = int(self.dy * C.WEIGHT[idx])
        self.w = int(self.dw * C.WEIGHT[idx])
        self.h = int(self.dh * C.WEIGHT[idx])
        self.hx = self.x + int(self.s * self.w) - self.h//2
        self.hy = self.y
