import pygame as pg
import uno.Constants as C

class CardButton:
    def __init__(self, card_name, function = None): # pos = 버튼 중앙 좌표, size = (가로, 세로), button_text = 내용
        #self.default_pos = pos
        #self.pos = pos
        #self.size = size
        
        self.color = C.INACTIVE_COLOR
        self.function = function
        self.above = False
        self.on_key = False
        self.img = pg.transform.scale(pg.image.load("./assets/images/"+ card_name + ".png"), (60,120))

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.above = True
        else:
            self.above = False

    def draw(self, screen):
        if self.above or self.on_key:
            self.color = C.ABOVE_COLOR
        else:
            self.color = C.INACTIVE_COLOR
        # pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.img, (10,10))

    def click(self, params = None):
        if self.function:
            if params:
                self.function(*params)
            else:
                self.function()
'''
    def change_size(self, weight_idx):
        self.FONT = pg.font.SysFont(C.FONT, int(C.DEFAULT_SIZE*C.WEIGHT[weight_idx]))
        self.rect = pg.Rect(0, 0, *tuple(int(item*C.WEIGHT[weight_idx]) for item in self.size))
        self.pos = tuple(int(item*C.WEIGHT[weight_idx]) for item in self.default_pos)
        self.text = self.FONT.render(self.button_text, True, self.text_color)
        self.text_rect = self.text.get_rect(center=self.pos)
        self.rect.center = self.pos
        
    def change_text(self, text):
        self.button_text=text
        self.text = self.FONT.render(text, True, C.BLACK)
        self.text_rect = self.text.get_rect(center=self.pos)
        '''
