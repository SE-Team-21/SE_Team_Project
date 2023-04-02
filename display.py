import pygame as pg
from abc import *
from pygame.locals import *
import uno.Constants as C
from uno.KeySettings import Data
from uno.Button_Class import Button
from uno.Text_Class import Text
from uno.Slider_Class import Slider
import os
import numpy as np
import torch
from uno.CardButton_Class import CardButton
from uno.game.Game import UnoGame
from uno.Music import Background_Music as bgm
import random

class Display(metaclass=ABCMeta):
    # Static Variable
    mode = [C.START, C.START]
    display_idx = 0
    key_idx = -1
    colorblind_idx = -1
    COLORBLIND_MATRIX = [torch.tensor(C.PROTANOPIA_MATRIX), torch.tensor(C.DEUTERANOPIA_MATRIX), torch.tensor(C.TRITANOPIA_MATRIX)]

    def __init__(self):
        self.Button_list = []
        self.Text_list = []
        self.screen = pg.display.set_mode(C.DISPLAY_SIZE[Display.display_idx])

    def draw_card(self, card, x, y):
        card_image = pg.image.load(os.path.join('assets', f'{card}.png'))
        self.screen.blit(card_image, (x, y))

    def color(self):
        array = pg.surfarray.array3d(self.screen)
        rgb_tensor = torch.from_numpy(np.transpose(array[:, :, :3], (2, 0, 1))).float()
        filtered_rgb_tensor = torch.matmul(Display.COLORBLIND_MATRIX[Display.colorblind_idx], rgb_tensor.view(3, -1)).view(rgb_tensor.shape)
        filtered_array = np.transpose(filtered_rgb_tensor.numpy(), (1,2,0))
        filtered_img = pg.surfarray.make_surface(filtered_array.astype('uint8'))        
        self.screen.blit(filtered_img, (0, 0))

    def update_screen(self, mouse_pos): # 현재 화면 업데이트
        for item in self.Button_list:
            item.change_size(Display.display_idx)
            item.update(mouse_pos)
            item.draw(self.screen)
        for item in self.Text_list:
            item.change_size(Display.display_idx)
            item.draw(self.screen)
        if Display.colorblind_idx != -1:
            self.color()
        pg.display.update()

    #def background_music(self, display_idx):     # 배경음악 실행
        #bgm1 = bgm(self, display_idx)
        #bgm1.play()


    @abstractmethod
    def next_screen(self): # 버튼 클릭시 다음 화면으로 전환
        pass

    @abstractmethod
    def main_loop(self):
        pass

class Start(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((100, 150), (120, 60), 'Play', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((100, 300), (120, 60), 'Options', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((100, 450), (120, 60), 'Quit', lambda x,y: self.next_screen(x,y)))
        self.backgroundimg = pg.transform.scale(pg.image.load("./assets/images/Main.png"), C.DISPLAY_SIZE[Display.display_idx])

    def next_screen(self, idx, running):
        if idx == 0:                            
            self.mode[C.NEXT_SCREEN] = C.MODE
        elif idx == 1:
            self.mode[C.NEXT_SCREEN] = C.SETTING
            self.mode[C.PREV_SCREEN] = C.START
        elif idx == 2:
            running[0] = False
    
    def main_loop(self, running):
        self.screen.fill((255, 255, 255))
        self.backgroundimg = pg.transform.scale(self.backgroundimg, C.DISPLAY_SIZE[Display.display_idx])
        self.screen.blit(self.backgroundimg, (0, 0))
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.Button_list[Display.key_idx].on_key = False
                Display.key_idx = -1
                for idx, item in enumerate(self.Button_list):
                    if item.above:
                        item.click((idx, running))
            elif event.type == pg.KEYUP:
                for idx, item in enumerate(Data.data.KEY_Settings):
                    if event.key == item:
                        if idx == 0 or idx == 1: # Up and Left Key
                            if Display.key_idx == 0:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx = len(self.Button_list)-1
                            elif Display.key_idx == -1:
                                Display.key_idx = 0
                            else:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx -= 1
                            self.Button_list[Display.key_idx].on_key = True
                        elif idx == 2 or idx == 3: # Right and Down Key
                            if Display.key_idx == len(self.Button_list)-1:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx = 0
                            elif Display.key_idx == -1:
                                Display.key_idx = 0
                            else:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx += 1
                            self.Button_list[Display.key_idx].on_key = True
                        elif idx == 4: # Return Key
                            if Display.key_idx != -1:
                                self.Button_list[Display.key_idx].on_key = False
                                self.next_screen(Display.key_idx, running)
                                Display.key_idx = -1
                
    

class Setting(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((540, 80), (20, 20), '<', lambda idx, running: self.screen_size_change(idx, running)))
        self.Button_list.append(Button((740, 80), (20, 20), '>', lambda idx, running: self.screen_size_change(idx, running)))
        self.Button_list.append(Button((540, 120), (20, 20), '<', lambda idx, running: self.colorblind_control(idx, running)))
        self.Button_list.append(Button((740, 120), (20, 20), '>', lambda idx, running: self.colorblind_control(idx, running)))
        self.Button_list.append(Button((320, 210), (120, 30), 'UP', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((320, 250), (120, 30), 'DOWN', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((320, 290), (120, 30), 'RIGHT', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((320, 330), (120, 30), 'LEFT', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((320, 370), (120, 30), 'RETURN', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((320, 410), (120, 30), 'ESCAPE', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((680, 210), (120, 30), '1', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((680, 250), (120, 30), '2', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((680, 290), (120, 30), '3', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((680, 330), (120, 30), '4', lambda idx, running: self.button_setting(idx, running)))
        self.Button_list.append(Button((700, 510), (140, 40), 'Default Options', lambda idx, running: self.default_setting(idx, running)))
        self.Button_list.append(Button((700, 570), (140, 40), 'Back', lambda idx, running: self.next_screen(idx, running)))
        self.Text_list.append(Text((20, 20), 30, 'DISPLAY', C.WHITE))
        self.Text_list.append(Text((40, 70), 20, 'Resolution', C.WHITE))
        self.Text_list.append(Text((605, 70), 20, '800x600', C.WHITE))
        self.Text_list.append(Text((40, 110), 20, 'Colorblind Mode', C.WHITE))
        self.Text_list.append(Text((565, 110), 20, '    Not Applied', C.WHITE))
        self.Text_list.append(Text((20, 150), 30, 'KEY CONTROL', C.WHITE))
        self.Text_list.append(Text((40, 200), 20, 'Up', C.WHITE))
        self.Text_list.append(Text((40, 240), 20, 'Left', C.WHITE))
        self.Text_list.append(Text((40, 280), 20, 'Down', C.WHITE))
        self.Text_list.append(Text((40, 320), 20, 'Right', C.WHITE))
        self.Text_list.append(Text((40, 360), 20, 'Return', C.WHITE))
        self.Text_list.append(Text((40, 400), 20, 'Escape', C.WHITE))
        self.Text_list.append(Text((440, 200), 20, 'Red', C.WHITE))
        self.Text_list.append(Text((440, 240), 20, 'Green', C.WHITE))
        self.Text_list.append(Text((440, 280), 20, 'Blue', C.WHITE))
        self.Text_list.append(Text((440, 320), 20, 'Yellow', C.WHITE))
        self.Text_list.append(Text((20, 440), 30, 'SOUND', C.WHITE))
        self.Text_list.append(Text((40, 490), 20, 'Master Volume', C.WHITE))
        self.Text_list.append(Text((40, 530), 20, 'Music Volume', C.WHITE))
        self.Text_list.append(Text((40, 570), 20, 'Effect Volume', C.WHITE))
        self.Slider_list = []
        self.Slider_list.append(Slider(350, 493, 200, 20, 0.5))
        self.Slider_list.append(Slider(350, 533, 200, 20, 0.5))
        self.Slider_list.append(Slider(350, 573, 200, 20, 0.5))
        self.key_set = False
        self.dragging = False
        self.slider_idx = 0
        self.index = 0
        self.active = [False, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True]

        # Load Setting
        for i in range(10):
            self.Button_list[i+4].change_text(pg.key.name(Data.data.KEY_Settings[i]))
        Display.display_idx = Data.data.Resolution
        self.Text_list[2].change_text(C.DISPLAY_SIZE_STR[Display.display_idx])
        if Display.display_idx == 1:
            self.active[0] = True
        elif Display.display_idx == 2:
            self.active[0] = True
            self.active[1] = False
        Display.colorblind_idx = Data.data.Color
        if Display.colorblind_idx == 0 or Display.colorblind_idx == 1:
            self.active[2] = True
            self.Text_list[4].change_text(C.COLORBLINDMODE_STR[Display.colorblind_idx])
        elif Display.colorblind_idx == 2:
            self.active[2] = True
            self.active[3] = False
            self.Text_list[4].change_text(C.COLORBLINDMODE_STR[Display.colorblind_idx])
        self.Slider_list[0].s = Data.data.Master_Volume
        self.Slider_list[1].s = Data.data.Music_Volume
        self.Slider_list[2].s = Data.data.Effect_Volume

        
    def next_screen(self, not_use, running):
        if self.mode[C.PREV_SCREEN] == C.START:
            self.mode[C.NEXT_SCREEN] = C.START
        elif self.mode[C.PREV_SCREEN] == C.STOP:
            self.mode[C.NEXT_SCREEN] = C.STOP
        self.key_set = False

    def button_setting(self, idx, not_use):
        self.key_set = True
        self.index = idx

    def default_setting(self, not_use, not_use_):
        Data.default()
        for i in range(10):
            self.Button_list[i+4].change_text(pg.key.name(Data.data.KEY_Settings[i]))
        Display.display_idx = Data.data.Resolution
        Display.colorblind_idx = Data.data.Color
        self.Slider_list[0].s = Data.data.Master_Volume
        self.Slider_list[1].s = Data.data.Music_Volume
        self.Slider_list[2].s = Data.data.Effect_Volume
        self.active[0] = False
        self.active[1] = True
        self.active[2] = False
        self.active[3] = True
        self.screen = pg.display.set_mode(C.DISPLAY_SIZE[Display.display_idx])
        self.Text_list[2].change_text(C.DISPLAY_SIZE_STR[Display.display_idx])
        self.Text_list[4].change_text("    Not Applied")
        self.key_set = False

    def update_screen(self, mouse_pos):
        pg.draw.line(self.screen, C.WHITE, [int(160*C.WEIGHT[Display.display_idx]), int(35*C.WEIGHT[Display.display_idx])], [int(780*C.WEIGHT[Display.display_idx]), int(35*C.WEIGHT[Display.display_idx])], 3)
        pg.draw.line(self.screen, C.WHITE, [int(250*C.WEIGHT[Display.display_idx]), int(165*C.WEIGHT[Display.display_idx])], [int(780*C.WEIGHT[Display.display_idx]), int(165*C.WEIGHT[Display.display_idx])], 3)
        pg.draw.line(self.screen, C.WHITE, [int(140*C.WEIGHT[Display.display_idx]), int(455*C.WEIGHT[Display.display_idx])], [int(780*C.WEIGHT[Display.display_idx]), int(455*C.WEIGHT[Display.display_idx])], 3)
        for item in self.Slider_list:
            item.change_size(Display.display_idx)
            item.draw(self.screen)
        for idx, item in enumerate(self.Button_list):
            if self.active[idx]:
                item.change_size(Display.display_idx)
                item.update(mouse_pos)
                item.draw(self.screen)
        for item in self.Text_list:
            item.change_size(Display.display_idx)
            item.draw(self.screen)
        if Display.colorblind_idx != -1:
            self.color()
        pg.display.update()

    def screen_size_change(self, idx, not_use):
        if idx == 0:
            Display.display_idx -= 1
            if Display.display_idx == 0:
                self.active[0] = False
            elif Display.display_idx == 1:
                self.active[1] = True
        else:
            Display.display_idx += 1
            if Display.display_idx == 2:
                self.active[1] = False
            elif Display.display_idx == 1:
                self.active[0] = True
        self.screen = pg.display.set_mode(C.DISPLAY_SIZE[Display.display_idx])
        self.Text_list[2].change_text(C.DISPLAY_SIZE_STR[Display.display_idx])
        Data.save_resolution(Display.display_idx)
        self.key_set = False

    def colorblind_control(self, idx, not_use):
        if idx == 2:
            Display.colorblind_idx -= 1
            if Display.colorblind_idx == -1:
                self.active[2] = False
            elif Display.colorblind_idx == 1:
                self.active[3] = True
        else:
            Display.colorblind_idx += 1
            if Display.colorblind_idx == 2:
                self.active[3] = False
            elif Display.colorblind_idx == 0:
                self.active[2] = True
        if Display.colorblind_idx == -1:
            self.Text_list[4].change_text("    Not Applied")
        else:
            self.Text_list[4].change_text(C.COLORBLINDMODE_STR[Display.colorblind_idx])
        Data.save_color(Display.colorblind_idx)
        self.key_set = False

    def main_loop(self, running):
        self.screen.fill((0, 0, 0))
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                for idx, item in enumerate(self.Slider_list):
                    handle_rect = pg.Rect(item.hx, item.hy, item.h, item.h)
                    if handle_rect.collidepoint(event.pos):
                        self.dragging = True
                        self.slider_idx = idx
                for idx, item in enumerate(self.Button_list):
                    if item.above and self.active[idx]:
                        item.click((idx, running))
                        break
                    else:
                        if(self.key_set):
                            self.key_set = False
            elif event.type == pg.MOUSEBUTTONUP:
                if self.dragging:
                    self.dragging = False
                    Data.save_sound(self.slider_idx, max(0, min(1, (event.pos[0] - self.Slider_list[self.slider_idx].x) / self.Slider_list[self.slider_idx].w)))
            elif event.type == pg.MOUSEMOTION:
                if self.dragging:
                    self.Slider_list[self.slider_idx].s = max(0, min(1, (event.pos[0] - self.Slider_list[self.slider_idx].x) / self.Slider_list[self.slider_idx].w))
            if self.key_set:
                if event.type == pg.KEYUP:
                    if event.key not in Data.data.KEY_Settings:
                        self.Button_list[self.index].change_text(pg.key.name(event.key))
                        Data.save_key(self.index-4, event.key)
                        self.key_set = False
                    else:
                        warning = Button((400, 300), (300, 60), 'The key is already in use', color=C.RED)
                        warning.draw(self.screen)
                        pg.display.update()
                        pg.time.wait(1500)


class Playing(Display):
    game = None
    game_mode = 0
    def __init__(self):
        super().__init__()
        self.Card_list = []
        self.x = 0
        self.y = 0
        self.stage = 0
        self.num_of_players = 1
        self.is_game_start = False
        self.is_computer_activated = [False, False, False, False, False]
        self.Player_list = []
        self.Player_list.append(Button((600, 100), (80, 80), 'Computer1 ', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((600, 200), (80, 80), 'Computer2 ', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((600, 300), (80, 80), 'Computer3 ', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((600, 400), (80, 80), 'Computer4 ', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((600, 500), (80, 80), 'Computer5 ', lambda x, y: self.computer_add_remove(x, y)))
        self.start_button = Button((100, 100), (60, 60), 'Game Start', lambda: self.game_start())

        self.choice_card_idx = None

    def computer_add_remove(self, idx, item):
        if self.is_computer_activated[idx]:
            self.is_computer_activated[idx] = False
            self.num_of_players -= 1
        else:
            self.is_computer_activated[idx] = True
            self.num_of_players += 1

    def update_screen(self, mouse_pos): # 현재 화면 업데이트
        for item in self.Card_list:
            item.update(mouse_pos)
        for item in self.Player_list:
            item.update(mouse_pos)
        self.start_button.update(mouse_pos)
        
    def next_screen(self):
        pass
    
    def game_start(self):
        self.is_game_start = True

    def player_action(self, running):
        player = self.game.current_player
        player_id = player.player_id
        if player.can_play(self.game.current_card):
            
            # if self.top.card_color == myCard.card_color or self.top.card_type == myCard.card_type or myCard.card_color == "black":
            if self.choice_card_idx is not None:
                card = Playing.game.players[0].hand[self.choice_card_idx]
                if self.game.current_card.playable(card):
                    if card.color == 'black':
                        new_color = random.choice(C.COLORS)
                    else:
                        new_color = None
                    print("Player {} played {}".format(player, card))
                    self.game.play(player=player_id, card=self.choice_card_idx, new_color=new_color)
                    
                self.choice_card_idx = None
        
        else:
            print("Player {} picked up".format(player))
            self.game.play(player=player_id, card=None)
            pg.time.wait(200)

    def game_handler(self, running):
        if Playing.game == None:
            Playing.game = UnoGame(self.num_of_players)
        self.top = C.ALL_CARDS[str(Playing.game.current_card.color) + str(Playing.game.current_card.card_type)]
        for i in Playing.game.players[0].hand:
            myCard = C.ALL_CARDS[str(i.color) + str(i.card_type)]
            self.Card_list.append(myCard)
            '''
                if self.top.card_color == myCard.card_color or self.top.card_type == myCard.card_type or myCard.card_color == "black":
                    self.Card_list.append(myCard)
                    self.screen.blit(myCard.img, (self.x, self.y))
                self.x += 50
            '''
            myCard.draw(self.screen, self.x, self.y)
            self.x += 50
            self.screen.blit(self.top.img, (150,100))
            self.backCard = C.ALL_CARDS["Back"]
            self.screen.blit(self.backCard.img, (100, 100))

            player = self.game.current_player
            player_id = player.player_id
            if player_id == 0:
                self.player_action(running)
            else:
                if player.can_play(self.game.current_card):
                    for i, card in enumerate(player.hand):
                        if self.game.current_card.playable(card):
                            if card.color == 'black':
                                new_color = random.choice(C.COLORS)
                            else:
                                new_color = None
                            print("Computer {} played {}".format(player, card))
                            self.game.play(player=player_id, card=i, new_color=new_color)
                            break
                else:
                    print("Computer {} picked up".format(player))
                    self.game.play(player=player_id, card=None)
                    pg.time.wait(200)

    def single_mode(self, running):
        self.screen.fill((255, 255, 255))
        self.Card_list = []
        self.x = 0
        self.y = 300

        if self.is_game_start:
            self.game_handler(running)
        else:
            self.start_button.draw(self.screen)

        for idx, item in enumerate(self.Player_list):
            if self.is_computer_activated[idx]:
                item.change_text(item.button_text.replace(" ", "_activated"))
                item.draw(self.screen)
            else:
                item.change_text(item.button_text.replace("_activated", " "))
                item.draw(self.screen)
        '''
        self.x_ = 0
        self.y_ = 0
        for player in Playing.game.players:
            self.screen.blit(self.backCard.img, (self.x_, self.y_))
            self.y_ = self.y_ + 100
        '''
            
        self.update_screen(pg.mouse.get_pos())
        pg.display.update()
        for event in pg.event.get():
            self.tmp_event = event
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.mode[C.NEXT_SCREEN] = C.STOP
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.tmp_event.type == pg.QUIT:
                    running[0] = False
                    return
                elif self.tmp_event.type == pg.KEYUP:
                    if self.tmp_event.key == pg.K_ESCAPE:
                        self.mode[C.NEXT_SCREEN] = C.STOP
                elif self.tmp_event.type == pg.MOUSEBUTTONDOWN:
                    if Playing.game:
                        for idx, item in enumerate(self.Card_list):
                            if item.above:
                                print(idx)
                                self.choice_card_idx = idx
                                break
                for idx, item in enumerate(self.Player_list):
                    if item.above and not self.is_game_start:
                        item.click((idx, item))
                if self.start_button.above and not self.is_game_start:
                    self.start_button.click()

    def story_mode(self, stage, running):
        pass

    def main_loop(self, running):
        # # game inst
        if Playing.game_mode == 0:
            self.single_mode(running)
        elif Playing.game_mode == 1:
            self.story_mode(self.stage, running)
        

class Pause(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((400, 200), (100, 50), 'RESUME', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((400, 300), (100, 50), 'OPTIONS', lambda x,y: self.next_screen(x,y)))
        self.Button_list.append(Button((400, 400), (100, 50), 'GAME QUIT', lambda x,y: self.next_screen(x,y)))

    def next_screen(self, idx, running):
        if idx==0:
            self.mode[C.NEXT_SCREEN] = C.PLAYING
        elif idx==1:
            self.mode[C.NEXT_SCREEN] = C.SETTING
            self.mode[C.PREV_SCREEN] = C.STOP
        elif idx==2:
            self.mode[C.NEXT_SCREEN] = C.START
            Playing.game = None

    def main_loop(self, running):
        self.screen.fill((255, 255, 255))
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                for idx, item in enumerate(self.Button_list):
                    if item.above:
                        item.click((idx, running))

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
class Mode(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((100, 150), (120, 60), 'Story Mode', lambda x,y: self.next_screen(x,y)))  #스토리모드 선택
        self.Button_list.append(Button((100, 300), (120, 60), 'Single Mode', lambda x,y: self.next_screen(x,y)))  #싱글모드 선택
        self.Button_list.append(Button((100, 450), (120, 60), 'Back', lambda x,y: self.next_screen(x,y)))  #시작 화면 되돌아가기
        self.backgroundimg = pg.transform.scale(pg.image.load("./assets/images/Main.png"), C.DISPLAY_SIZE[Display.display_idx])

    def next_screen(self, idx, running):
        if idx == 0:
            self.mode[C.NEXT_SCREEN] = C.STORY
            Playing.game_mode = 1
        elif idx == 1:
            self.mode[C.NEXT_SCREEN] = C.PLAYING
            Playing.game_mode = 0
        elif idx == 2:
            self.mode[C.NEXT_SCREEN] = C.START
    
    def main_loop(self, running):
        self.screen.fill((255, 255, 255))
        self.backgroundimg = pg.transform.scale(self.backgroundimg, C.DISPLAY_SIZE[Display.display_idx])
        self.screen.blit(self.backgroundimg, (0, 0))
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.Button_list[Display.key_idx].on_key = False
                Display.key_idx = -1
                for idx, item in enumerate(self.Button_list):
                    if item.above:
                        item.click((idx, running))
            elif event.type == pg.KEYUP:
                for idx, item in enumerate(Data.data.KEY_Settings):
                    if event.key == item:
                        if idx == 0 or idx == 1: # Up and Left Key
                            if Display.key_idx == 0:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx = len(self.Button_list)-1
                            elif Display.key_idx == -1:
                                Display.key_idx = 0
                            else:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx -= 1
                            self.Button_list[Display.key_idx].on_key = True
                        elif idx == 2 or idx == 3: # Right and Down Key
                            if Display.key_idx == len(self.Button_list)-1:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx = 0
                            elif Display.key_idx == -1:
                                Display.key_idx = 0
                            else:
                                self.Button_list[Display.key_idx].on_key = False
                                Display.key_idx += 1
                            self.Button_list[Display.key_idx].on_key = True
                        elif idx == 4: # Return Key
                            if Display.key_idx != -1:
                                self.Button_list[Display.key_idx].on_key = False
                                self.next_screen(Display.key_idx, running)
                                Display.key_idx = -1
