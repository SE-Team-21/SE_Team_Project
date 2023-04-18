from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.Button_Class import Button
from uno.Text_Class import Text
from uno.play import Playing
from uno.game.Game import UnoGame
from uno.KeySettings import Data

class Story(Display):
    def __init__(self):
        super().__init__()
        self.Area_list = []
        self.Area_list.append(Button((162, 112), (150, 150), ''))
        self.Area_list.append(Button((302, 321), (150, 150), ''))
        self.Area_list.append(Button((567, 112), (150, 150), ''))
        self.Area_list.append(Button((666, 357), (150, 150), ''))
        self.Checked_list = []
        self.Checked_list.append(Text((120, 84), 40, 'Clear', C.BLACK))
        self.Checked_list.append(Text((260, 296), 40, 'Clear', C.BLACK))
        self.Checked_list.append(Text((530, 84), 40, 'Clear', C.BLACK))
        self.Checked_list.append(Text((625, 334), 40, 'Clear', C.BLACK))
        self.Button_list.append(Button((700, 500), (120, 60), 'Back', lambda x,y: self.next_screen(x,y)))
        self.backgroundimg_d = pg.transform.scale(pg.image.load("./assets/images/story_map.png"), C.DISPLAY_SIZE[Display.display_idx])
        self.cloudimg_d = pg.transform.scale(pg.image.load("./assets/images/cloud.png"), (int(444*C.WEIGHT[Display.display_idx]), int(300*C.WEIGHT[Display.display_idx])))
        self.area1_d = pg.transform.scale(pg.image.load("./assets/images/area1.png"), (int(180*C.WEIGHT[Display.display_idx]), int(341*C.WEIGHT[Display.display_idx])))
        self.area2_d = pg.transform.scale(pg.image.load("./assets/images/area2.png"), (int(180*C.WEIGHT[Display.display_idx]), int(351*C.WEIGHT[Display.display_idx])))
        self.area3_d = pg.transform.scale(pg.image.load("./assets/images/area3.png"), (int(180*C.WEIGHT[Display.display_idx]), int(330*C.WEIGHT[Display.display_idx])))
        self.area4_d = pg.transform.scale(pg.image.load("./assets/images/area4.png"), (int(360*C.WEIGHT[Display.display_idx]), int(250*C.WEIGHT[Display.display_idx])))
        self.backgroundimg = pg.transform.scale(pg.image.load("./assets/images/story_map.png"), C.DISPLAY_SIZE[Display.display_idx])
        self.cloudimg = pg.transform.scale(pg.image.load("./assets/images/cloud.png"), (int(444*C.WEIGHT[Display.display_idx]), int(300*C.WEIGHT[Display.display_idx])))
        self.area1 = pg.transform.scale(pg.image.load("./assets/images/area1.png"), (int(180*C.WEIGHT[Display.display_idx]), int(341*C.WEIGHT[Display.display_idx])))
        self.area2 = pg.transform.scale(pg.image.load("./assets/images/area2.png"), (int(180*C.WEIGHT[Display.display_idx]), int(351*C.WEIGHT[Display.display_idx])))
        self.area3 = pg.transform.scale(pg.image.load("./assets/images/area3.png"), (int(180*C.WEIGHT[Display.display_idx]), int(330*C.WEIGHT[Display.display_idx])))
        self.area4 = pg.transform.scale(pg.image.load("./assets/images/area4.png"), (int(360*C.WEIGHT[Display.display_idx]), int(250*C.WEIGHT[Display.display_idx])))
        self.yes_button = Button((340, 300), (100, 50), 'Game Start')
        self.no_button = Button((460, 300), (100, 50), 'Cancel')
        self.active = [True, False, False, False]
        self.clear = [False, False, False, False]
        self.phase = 1

        #Load Setting
        for i in range(Data.data.Story):
            self.active[i]=True
            self.clear[i]=True
        if Data.data.Clear:
            self.clear[3]=True
        self.active[Data.data.Story] = True


    def next_screen(self, idx, running): # Return to Main Menu
        if idx==0:
            self.mode[C.NEXT_SCREEN] = C.START

    def next_screen_2(self):
        self.mode[C.NEXT_SCREEN] = C.PLAYING

    def update_area(self, mouse_pos):	
        for item in self.Area_list:	
            item.change_size(Display.display_idx)	
            item.update(mouse_pos)
            item.draw(self.screen)

    def main_loop(self, running):
        if self.phase == 1:
            self.screen.fill((255, 255, 255))
            self.update_area(pg.mouse.get_pos())
            self.backgroundimg = pg.transform.scale(self.backgroundimg_d, C.DISPLAY_SIZE[Display.display_idx])
            self.cloudimg = pg.transform.scale(self.cloudimg_d, (int(444*C.WEIGHT[Display.display_idx]), int(300*C.WEIGHT[Display.display_idx])))
            self.area1 = pg.transform.scale(self.area1_d, (int(180*C.WEIGHT[Display.display_idx]), int(341*C.WEIGHT[Display.display_idx])))
            self.area2 = pg.transform.scale(self.area2_d, (int(180*C.WEIGHT[Display.display_idx]), int(351*C.WEIGHT[Display.display_idx])))
            self.area3 = pg.transform.scale(self.area3_d, (int(180*C.WEIGHT[Display.display_idx]), int(330*C.WEIGHT[Display.display_idx])))
            self.area4 = pg.transform.scale(self.area4_d, (int(360*C.WEIGHT[Display.display_idx]), int(250*C.WEIGHT[Display.display_idx])))
            self.screen.blit(self.backgroundimg, (0, 0))
            if Data.data.Story == 0:
                self.screen.blit(self.cloudimg, (int(50*C.WEIGHT[Display.display_idx]), int(160*C.WEIGHT[Display.display_idx])))
                self.screen.blit(self.cloudimg, (int(370*C.WEIGHT[Display.display_idx]), int(170*C.WEIGHT[Display.display_idx])))
                self.screen.blit(self.cloudimg, (int(310*C.WEIGHT[Display.display_idx]), 0))
            elif Data.data.Story == 1:
                self.screen.blit(self.cloudimg, (int(370*C.WEIGHT[Display.display_idx]), int(170*C.WEIGHT[Display.display_idx])))
                self.screen.blit(self.cloudimg, (int(310*C.WEIGHT[Display.display_idx]), 0))
            elif Data.data.Story == 2:
                self.screen.blit(self.cloudimg, (int(370*C.WEIGHT[Display.display_idx]), int(170*C.WEIGHT[Display.display_idx])))
            for idx, item in enumerate(self.Area_list):	
                if (item.above or item.on_key) and self.active[idx]:
                    if idx == 0:
                        self.screen.blit(self.area1, (int(71*C.WEIGHT[Display.display_idx]), int(56*C.WEIGHT[Display.display_idx])))
                    elif idx == 1:
                        self.screen.blit(self.area2, (int(215*C.WEIGHT[Display.display_idx]), int(260*C.WEIGHT[Display.display_idx])))
                    elif idx == 2:
                        self.screen.blit(self.area3, (int(478*C.WEIGHT[Display.display_idx]), int(56*C.WEIGHT[Display.display_idx])))
                    elif idx == 3:
                        self.screen.blit(self.area4, (int(365*C.WEIGHT[Display.display_idx]), int(235*C.WEIGHT[Display.display_idx])))
            for idx, item in enumerate(self.Checked_list):
                if self.clear[idx]:
                    item.change_size(Display.display_idx)
                    item.draw(self.screen)
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
                        if item.above and self.active[idx]:
                            self.index = idx
                            item.on_key = True
                            self.phase = 2
        else:
            self.yes_button.change_size(Display.display_idx)
            self.yes_button.update(pg.mouse.get_pos())
            self.yes_button.draw(self.screen)
            self.no_button.change_size(Display.display_idx)
            self.no_button.update(pg.mouse.get_pos())
            self.no_button.draw(self.screen)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running[0] = False
                    return
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.yes_button.above:
                        self.phase = 1
                        C.game_mode = 1
                        C.INDEX = self.index
                        self.next_screen_2()
                        '''if Data.data.Story<=2 and (self.index == Data.data.Story):
                            self.clear[Data.data.Story] = True
                            Data.save_story(Data.data.Story+1)
                        elif self.index == 3:
                            self.clear[Data.data.Story] = True
                            Data.save_clear()
                        for i in range(Data.data.Story+1):
                            self.active[i]=True'''
                    elif self.no_button.above:
                        self.phase = 1
                        self.index = None
                    for item in self.Area_list:
                        item.on_key = False
