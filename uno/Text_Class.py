import pygame as pg
import uno.Constants as C

class Text:
    def __init__(self, pos, size, text, color = C.BLACK): # pos = 좌상단 모서리 좌표, size = 글씨 크기, text = 내용
        pg.font.init()
        self.default_pos = pos
        self.pos = pos
        self.size = size
        self.color = color
        self.text = text
        self.FONT = pg.font.SysFont(C.FONT, self.size)
        self.ren = self.FONT.render(text, True, color)
        
    def draw(self, screen):
        screen.blit(self.ren, self.pos)
        
    def change_size(self, weight_idx):
        self.FONT = pg.font.SysFont(C.FONT, int(self.size*C.WEIGHT[weight_idx]))
        self.pos = tuple(int(item*C.WEIGHT[weight_idx]) for item in self.default_pos)
        self.ren = self.FONT.render(self.text, True, self.color)

    def change_text(self, text):
        self.text = text
        self.ren = self.FONT.render(self.text, True, self.color)
