from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.Button_Class import Button
from uno.Text_Class import Text
from uno.KeySettings import Data
'''
- djqwjr 배열 사용 위해서 Data 임포트하기
from KeySettings import Data

- djqwjr 배열에서 값 가져오기
first_value = Data.data.djqwjr[0]

- djqwjr 배열의 값 수정하기
Data.data.djqwjr[0] = new_value
'''

class AchievementInfo:
    def __init__(self, name, index):
        self.name = name
        self.index = index

'''
AchievementInfo('First Win in Single Mode', 'Win your first game in single player mode'),
            AchievementInfo('Story Mode Area1 Clear', 'Win your Area1 game in story mode'),
            AchievementInfo('Story Mode Area2 Clear', 'Win your Area2 game in story mode'),
            AchievementInfo('Story Mode Area3 Clear', 'Win your Area3 game in story mode'),
            AchievementInfo('Story Mode Area4 Clear', 'Win your Area4 game in story mode'),
            AchievementInfo('Win in 10 Turns', 'Win in 10 Truns'),
            AchievementInfo('With No Active Card', 'Win with no active card'),
            AchievementInfo('other people said Uno', 'Win with other people said Uno'),
            AchievementInfo('Bonus1', 'Bonus1'),
            AchievementInfo('Bonus2', 'Bonus2'),
            AchievementInfo('Bonus3', 'Bonus3'),'''
class Achievement(Display):
    def __init__(self):
        super().__init__()
        
        # 도전과제 정보를 저장하는 리스트
        self.achievement_info_list = [
            AchievementInfo('First Win in Single Mode', '0'),
            AchievementInfo('Story Mode Area1 Clear', '1'),
            AchievementInfo('Story Mode Area2 Clear', '2'),
            AchievementInfo('Story Mode Area3 Clear', '3'),
            AchievementInfo('Story Mode Area4 Clear', '4'),
            AchievementInfo('Win in 10 Turns', '5'),
            AchievementInfo('With No Active Card', '6'),
            AchievementInfo('other people said Uno', '7'),
            AchievementInfo('Bonus1', '8'),
            AchievementInfo('Bonus2', '9'),
            AchievementInfo('Bonus3', '10'),
        ]
        
        # 도전과제 버튼 생성
        for idx, info in enumerate(self.achievement_info_list):
            if(idx < 6):
                self.Button_list.append(Button((200, 50 + 30 * idx), (200, 30), info.name, function=self.show_info, color=C.BLACK))
                
            else:
                self.Button_list.append(Button((400, 50 + 30 * (idx-6)), (200, 30), info.name, function=self.show_info, color=C.BLACK))
                
        # 뒤로가기 버튼 생성
        self.Button_list.append(Button((400, 550), (120, 60), 'Back', self.next_screen))
        
        # 현재 선택된 도전과제 정보를 저장하는 변수
        self.selected_achievement_info = None

    def show_info(self, button):
        for info in self.achievement_info_list:
            if info.name == button.button_text:
                self.selected_achievement_info = info
                break

    #def next_screen(self):
    #    self.mode[C.NEXT_SCREEN] = self.mode[C.PREV_SCREEN]

    def next_screen(self, _=None): # '_'는 파이썬에서 관습적으로 사용되는 더미 변수입니다.
        self.mode[C.NEXT_SCREEN] = self.mode[C.PREV_SCREEN]

    def main_loop(self, running):
        self.screen.fill(C.BLACK)
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                for idx, item in enumerate(self.Button_list):
                    if item.above:
                        item.click((item, ))

        # 선택된 도전과제 정보 표시
        if self.selected_achievement_info is not None:
            font = pg.font.SysFont(C.FONT, C.DEFAULT_SIZE)
            if self.selected_achievement_info.index == '0':
                if Data.data.djqwjr[0] == 0:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/notyet.png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render('Date : Notyet', True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                elif Data.data.djqwjr[0] == 1:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/a" + self.selected_achievement_info.index + ".png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render("Date : " + str(Data.data.djqwjr_date[8]), True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                info_text = font.render('First Win in Single Mode', True, C.WHITE)
                self.screen.blit(info_text, (100, 470))

            elif self.selected_achievement_info.index == '1':
                if Data.data.djqwjr[1] == 0:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/notyet.png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render('Date : Notyet', True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                elif Data.data.djqwjr[1] == 1:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/a" + self.selected_achievement_info.index + ".png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render("Date : " + str(Data.data.djqwjr_date[8]), True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                info_text = font.render('Story Mode Area1 Clear', True, C.WHITE)
                self.screen.blit(info_text, (100, 470))
            
            elif self.selected_achievement_info.index == '2':
                if Data.data.djqwjr[2] == 0:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/notyet.png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render('Date : Notyet', True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                elif Data.data.djqwjr[2] == 1:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/a" + self.selected_achievement_info.index + ".png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render("Date : " + str(Data.data.djqwjr_date[8]), True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                info_text = font.render('Story Mode Area2 Clear', True, C.WHITE)
                self.screen.blit(info_text, (100, 470))
            
            elif self.selected_achievement_info.index == '3':
                if Data.data.djqwjr[3] == 0:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/notyet.png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render('Date : Notyet', True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                elif Data.data.djqwjr[3] == 1:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/a" + self.selected_achievement_info.index + ".png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render("Date : " + str(Data.data.djqwjr_date[8]), True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                info_text = font.render('Story Mode Area3 Clear', True, C.WHITE)
                self.screen.blit(info_text, (100, 470))

            elif self.selected_achievement_info.index == '4':
                if Data.data.djqwjr[4] == 0:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/notyet.png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render('Date : Notyet', True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                elif Data.data.djqwjr[4] == 1:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/a" + self.selected_achievement_info.index + ".png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render("Date : " + str(Data.data.djqwjr_date[8]), True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                info_text = font.render('Story Mode Area4 Clear', True, C.WHITE)
                self.screen.blit(info_text, (100, 470))

            elif self.selected_achievement_info.index == '5':
                if Data.data.djqwjr[5] == 0:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/notyet.png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render('Date : Notyet', True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                elif Data.data.djqwjr[5] == 1:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/a" + self.selected_achievement_info.index + ".png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render("Date : " + str(Data.data.djqwjr_date[8]), True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                info_text = font.render('Win in 10 Turns', True, C.WHITE)
                self.screen.blit(info_text, (100, 470))
            
            elif self.selected_achievement_info.index == '6':
                if Data.data.djqwjr[6] == 0:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/notyet.png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render('Date : Notyet', True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                elif Data.data.djqwjr[6] == 1:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/a" + self.selected_achievement_info.index + ".png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render("Date : " + str(Data.data.djqwjr_date[8]), True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                info_text = font.render('With No Active Card', True, C.WHITE)
                self.screen.blit(info_text, (100, 470))
            
            elif self.selected_achievement_info.index == '7':
                if Data.data.djqwjr[7] == 0:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/notyet.png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render('Date : Notyet', True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                elif Data.data.djqwjr[7] == 1:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/a" + self.selected_achievement_info.index + ".png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render("Date : " + str(Data.data.djqwjr_date[8]), True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                info_text = font.render('other people said Uno', True, C.WHITE)
                self.screen.blit(info_text, (100, 470))

            elif self.selected_achievement_info.index == '8':
                if Data.data.djqwjr[8] == 0:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/notyet.png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render('Date : Notyet', True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                elif Data.data.djqwjr[8] == 1:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/a" + self.selected_achievement_info.index + ".png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render("Date : " + str(Data.data.djqwjr_date[8]), True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                info_text = font.render('Hello, World!', True, C.WHITE)
                self.screen.blit(info_text, (100, 470))
            
            elif self.selected_achievement_info.index == '9':
                if Data.data.djqwjr[9] == 0:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/notyet.png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render('Date : Notyet', True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                elif Data.data.djqwjr[9] == 1:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/a" + self.selected_achievement_info.index + ".png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render("Date : " + str(Data.data.djqwjr_date[8]), True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                info_text = font.render('Bonus2', True, C.WHITE)
                self.screen.blit(info_text, (100, 470))
            
            elif self.selected_achievement_info.index == '10':
                if Data.data.djqwjr[10] == 0:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/notyet.png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render('Date : Notyet', True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                elif Data.data.djqwjr[10] == 1:
                    info_image = pg.transform.scale(pg.image.load("./assets/images/a" + self.selected_achievement_info.index + ".png"), (int(100*C.WEIGHT[Display.display_idx]), int(100*C.WEIGHT[Display.display_idx])))
                    self.screen.blit(info_image, (100, 350))
                    info_text = font.render("Date : " + str(Data.data.djqwjr_date[8]), True, C.WHITE)
                    self.screen.blit(info_text, (100, 450))
                info_text = font.render('Bonus3', True, C.WHITE)
                self.screen.blit(info_text, (100, 470))


            
            

        pg.display.flip()

    def update_screen(self, mouse_pos):
        for item in self.Button_list:
            item.update(mouse_pos)
            item.draw(self.screen)