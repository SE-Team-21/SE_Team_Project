import pygame as pg
import uno.Constants as C

class CardButton:
    def __init__(self, card_name, img, function = None): # pos = 버튼 중앙 좌표, size = (가로, 세로), button_text = 내용
        #self.default_pos = pos
        #self.pos = pos
        #self.size = size
        self.function = function
        self.above = False
        self.on_key = False
        self.rect = pg.Rect(0, 0, 0, 0)
        self.img = pg.transform.scale(img, (45,90))
        self.card_name = card_name

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.above = True
        else:
            self.above = False

    def draw(self, screen, x, y): # 왼쪽 위 모서리 좌표
        self.rect = pg.Rect(x, y, 45, 90)
        screen.blit(self.img, (x,y))
        if self.above or self.on_key:
            pg.draw.rect(screen, (191,255,0), [x, y, 45, 90], 3)

    def click(self, params = None):
        print(self.card_name)
        
        '''if self.function:
            if params:
                self.function(*params)
            else:
                self.function()'''

    def change_size(self, weight_idx):
        self.FONT = pg.font.SysFont(C.FONT, int(C.DEFAULT_SIZE*C.WEIGHT[weight_idx]))
        self.rect = pg.Rect(0, 0, *tuple(int(item*C.WEIGHT[weight_idx]) for item in self.size))
        self.pos = tuple(int(item*C.WEIGHT[weight_idx]) for item in self.default_pos)