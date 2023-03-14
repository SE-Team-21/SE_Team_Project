import pygame as pg
from Color import *

class Button:
    def __init__(self,pos, size, name, color = BLACK): # pos = 버튼 중앙 좌표, size = (가로, 세로), name = 내용
        pg.font.init()
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