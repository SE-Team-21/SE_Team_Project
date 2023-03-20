import pygame as pg
import uno.Color as COLOR
import uno.constants as C

class Button:
    def __init__(self, pos, size, button_text, color = COLOR.BLACK): # pos = 버튼 중앙 좌표, size = (가로, 세로), button_text = 내용
        pg.font.init()
        self.default_pos = pos
        self.pos = pos
        self.size = size
        self.button_text = button_text
        self.text_color = color
        self.FONT = pg.font.SysFont(COLOR.FONT, C.DEFAULT_SIZE)
        self.text = self.FONT.render(button_text, True, color)
        self.text_rect = self.text.get_rect(center=pos)
        self.rect = pg.Rect(0, 0, *size)
        self.rect.center = pos
        self.color = COLOR.INACTIVE_COLOR
        
    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, self.text_rect)
        
    def above(self):
        self.color = COLOR.ABOVE_COLOR
        
    def active(self):
        self.color = COLOR.BLUE
        
    def inactive(self):
        self.color = COLOR.INACTIVE_COLOR
        
    def change_size(self, weight_idx):
        self.FONT = pg.font.SysFont(COLOR.FONT, int(C.DEFAULT_SIZE*C.WEIGHT[weight_idx]))
        self.rect = pg.Rect(0, 0, *tuple(int(item*C.WEIGHT[weight_idx]) for item in self.size))
        self.pos = tuple(int(item*C.WEIGHT[weight_idx]) for item in self.default_pos)
        self.text = self.FONT.render(self.button_text, True, self.text_color)
        self.text_rect = self.text.get_rect(center=self.pos)
        self.rect.center = self.pos