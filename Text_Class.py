import pygame as pg
from Color import *

class Text:
    def __init__(self, pos, size, text, color = BLACK): # pos = 좌상단 모서리 좌표, size = 글씨 크기, text = 내용
        pg.font.init()
        self.FONT = pg.font.SysFont('arial', size)
        self.text = self.FONT.render(text, True, color)
        self.pos = pos
    def draw(self, screen):
        screen.blit(self.text, self.pos)