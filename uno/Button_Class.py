import pygame as pg
import uno.Constants as C

class Button:
    def __init__(self, pos, size, button_text, function = None, color = C.BLACK, locate = False, inactive_color = C.INACTIVE_COLOR, above_color = C.ABOVE_COLOR, bold = False): # pos = 버튼 중앙 좌표, size = (가로, 세로), button_text = 내용
        pg.font.init()
        self.default_pos = pos
        self.pos = pos
        self.size = size
        self.button_text = button_text
        self.text_color = color
        self.FONT = pg.font.SysFont(C.FONT, C.DEFAULT_SIZE, bold)
        self.text = self.FONT.render(button_text, True, self.text_color)
        self.text_rect = self.text.get_rect(center=pos)
        self.rect = pg.Rect(0, 0, *size)
        self.rect.center = pos
        self.color = inactive_color
        self.function = function
        self.above = False
        self.on_key = False
        self.INACTIVE_COLOR = inactive_color
        self.ABOVE_COLOR = above_color
        self.locate = locate
    
    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.above = True
        else:
            self.above = False

    def draw(self, screen):
        if self.above or self.on_key:
            self.color = self.ABOVE_COLOR
        else:
            self.color = self.INACTIVE_COLOR
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, self.text_rect)

    def click(self, params = None):
        if self.function:
            if params:
                self.function(*params)
            else:
                self.function()

    def location(self):
        if self.locate:
            self.text_rect = self.text.get_rect(topleft=(self.pos[0]-self.size[0]//2, self.pos[1]-self.size[1]//2))
        else:
             self.text_rect = self.text.get_rect(center=self.pos)

    def change_size(self, weight_idx):
        self.FONT = pg.font.SysFont(C.FONT, int(C.DEFAULT_SIZE*C.WEIGHT[weight_idx]))
        self.rect = pg.Rect(0, 0, *tuple(int(item*C.WEIGHT[weight_idx]) for item in self.size))
        self.pos = tuple(int(item*C.WEIGHT[weight_idx]) for item in self.default_pos)
        self.text = self.FONT.render(self.button_text, True, self.text_color)
        self.location()
        self.rect.center = self.pos
        
    def change_text(self, text):
        self.button_text=text
        self.text = self.FONT.render(text, True, C.BLACK)
        self.location()
