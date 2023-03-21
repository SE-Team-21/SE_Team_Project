import pygame as pg
import uno.Constants as COLOR
import uno.Constants as C

class Text:
    def __init__(self, pos, size, text, color = COLOR.BLACK): # pos = 좌상단 모서리 좌표, size = 글씨 크기, text = 내용
        pg.font.init()
        self.default_pos = pos
        self.pos = pos
        self.size = size
        self.color = color
        self.text = text
        self.FONT = pg.font.SysFont(COLOR.FONT, C.DEFAULT_SIZE)
        self.ren = self.FONT.render(text, True, color)
        
    def draw(self, screen):
        screen.blit(self.ren, self.pos)
        
    def change_size(self, weight_idx):
        self.FONT = pg.font.SysFont(COLOR.FONT, int(C.DEFAULT_SIZE*C.WEIGHT[weight_idx]))
        self.pos = tuple(int(item*C.WEIGHT[weight_idx]) for item in self.default_pos)
        self.ren = self.FONT.render(self.text, True, self.color)