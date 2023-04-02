from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.Button_Class import Button
from uno.play import Playing
from uno.game.Game import UnoGame

class Story(Display):
    def __init__(self):
        super().__init__()
        self.Area_list = []
        self.Area_list.append(Button((162, 112), (150, 150), '', lambda x,y: self.next_screen_2(x,y)))
        self.Area_list.append(Button((302, 321), (150, 150), '', lambda x,y: self.next_screen_2(x,y)))
        self.Area_list.append(Button((567, 112), (150, 150), '', lambda x,y: self.next_screen_2(x,y)))
        self.Area_list.append(Button((666, 357), (150, 150), '', lambda x,y: self.next_screen_2(x,y)))
        self.Button_list.append(Button((400, 500), (120, 60), 'Back', lambda x,y: self.next_screen(x,y)))
        self.backgroundimg = pg.transform.scale(pg.image.load("./assets/images/story_map.png"), C.DISPLAY_SIZE[Display.display_idx])
        self.cloudimg = pg.transform.scale(pg.image.load("./assets/images/cloud.png"), (int(444*C.WEIGHT[Display.display_idx]), int(300*C.WEIGHT[Display.display_idx])))
        self.active = [True, False, False, False]

    def next_screen(self, idx, running):
        if idx==0:
            self.mode[C.NEXT_SCREEN] = C.START

    def next_screen_2(self, idx, running):
        if Playing.game == None:
                Playing.game = UnoGame(5) # game inst
        if idx==0:
            self.mode[C.NEXT_SCREEN] = C.PLAYING
        if idx==1:
            self.mode[C.NEXT_SCREEN] = C.PLAYING
        if idx==2:
            self.mode[C.NEXT_SCREEN] = C.PLAYING
        if idx==3:
            self.mode[C.NEXT_SCREEN] = C.PLAYING

    def update_area(self, mouse_pos):	
        for item in self.Area_list:	
            item.change_size(Display.display_idx)	
            item.update(mouse_pos)	
            item.draw(self.screen)

    def main_loop(self, running):
        self.screen.fill((255, 255, 255))
        self.update_area(pg.mouse.get_pos())
        self.backgroundimg = pg.transform.scale(self.backgroundimg, C.DISPLAY_SIZE[Display.display_idx])
        self.screen.blit(self.backgroundimg, (0, 0))
        self.screen.blit(self.cloudimg, (int(50*C.WEIGHT[Display.display_idx]), int(160*C.WEIGHT[Display.display_idx])))
        self.screen.blit(self.cloudimg, (int(370*C.WEIGHT[Display.display_idx]), int(170*C.WEIGHT[Display.display_idx])))
        self.screen.blit(self.cloudimg, (int(310*C.WEIGHT[Display.display_idx]), 0))
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                for idx, item in enumerate(self.Button_list):
                    if item.above:
                        item.click((idx, running))
                for idx, item in enumerate(self.Area_list):	
                    if item.above:	
                        item.click((idx, running))