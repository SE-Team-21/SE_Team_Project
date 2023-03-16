import pygame as pg
from Color import *

class Button:
    def __init__(self, pos, size, name, color = BLACK): # pos = 버튼 중앙 좌표, size = (가로, 세로), name = 내용
        pg.font.init()
        self.default_pos = pos
        self.pos = pos
        self.size = size
        self.name = name
        self.text_color = color
        self.FONT = pg.font.SysFont('arial', 20)
        self.text = self.FONT.render(name, True, color)
        self.text_rect = self.text.get_rect(center=pos)
        self.rect = pg.Rect(0, 0, *size)
        self.rect.center = pos
        self.color = INACTIVE_COLOR
    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, self.text_rect)
    def above(self):
        self.color = ABOVE_COLOR
    def active(self):
        self.color = ACTIVE_COLOR
    def inactive(self):
        self.color = INACTIVE_COLOR
    def change_size(self, size):
        if size==1:
            self.FONT = pg.font.SysFont('arial', 20)
            self.rect = pg.Rect(0, 0, *self.size)
            self.pos = self.default_pos
        elif size==2:
            self.FONT = pg.font.SysFont('arial', int(20*1.1))
            self.rect = pg.Rect(0, 0, *tuple(int(item*1.1) for item in self.size))
            self.pos = tuple(int(item*1.1) for item in self.default_pos)
        else:
            self.FONT = pg.font.SysFont('arial', int(20*1.2))
            self.rect = pg.Rect(0, 0, *tuple(int(item*1.2) for item in self.size))
            self.pos = tuple(int(item*1.2) for item in self.default_pos)
        self.text = self.FONT.render(self.name, True, self.text_color)
        self.text_rect = self.text.get_rect(center=self.pos)
        self.rect.center = self.pos