import pygame as pg
from uno.Color import *

class Text:
    def __init__(self, pos, size, text, color = BLACK): # pos = 좌상단 모서리 좌표, size = 글씨 크기, text = 내용
        pg.font.init()
        self.default_pos = pos
        self.pos = pos
        self.size = size
        self.color = color
        self.text = text
        self.FONT = pg.font.SysFont('arial', 20)
        self.ren = self.FONT.render(text, True, color)
    def draw(self, screen):
        screen.blit(self.ren, self.pos)
    def change_size(self, size):
        if size==1:
            self.FONT = pg.font.SysFont('arial', 20)
            self.pos = self.default_pos
        elif size==2:
            self.FONT = pg.font.SysFont('arial', int(20*1.1))
            self.pos = tuple(int(item*1.1) for item in self.default_pos)
        else:
            self.FONT = pg.font.SysFont('arial', int(20*1.2))
            self.pos = tuple(int(item*1.2) for item in self.default_pos)
        self.ren = self.FONT.render(self.text, True, self.color)
