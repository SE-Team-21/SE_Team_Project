from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.Button_Class import Button
from uno.game.Game import UnoGame
from uno.Text_Class import Text
import random
from uno.CardButton_Class import CardButton
from uno.KeySettings import Data

class Playing(Display):
    game = None
    is_game_start = False
    game_mode = 0
    is_computer_activated = [False, False, False, False, False]
    num_of_players = 1
    Color_active = False
    Color_idx = None
    is_color_choice = False
    choice_card_idx = None
    time = 1800
    key_locate = 0
    x = 0
    y = 0

    @staticmethod
    def reset():
        Playing.game = None
        Playing.is_game_start = False
        Playing.game_mode = 0
        Playing.is_computer_activated = [False, False, False, False, False]
        Playing.num_of_players = 1
        Playing.Color_active = False
        Playing.Color_idx = None
        Playing.is_color_choice = False
        Playing.choice_card_idx = None
        Playing.time = 1800
        Playing.key_locate = 0
        Playing.x = 0
        Playing.y = 0
        
    def __init__(self):
        super().__init__()
        self.Card_list = []
        self.stage = 0
        self.Player_list = []
        self.Player_list.append(Button((710, 60), (160, 100), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 178), (160, 100), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 296), (160, 100), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 414), (160, 100), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 532), (160, 100), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Text_list.append(Text((690, 60), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 178), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 296), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 414), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 532), 20, '', C.BLACK))
        self.start_button = Button((100, 100), (60, 60), 'Game Start', lambda: self.game_start())
        self.Color_list = []
        self.Color_list.append(Button((380, 120), (40, 40), 'RED', lambda x: self.choice_color(x)))
        self.Color_list.append(Button((420, 120), (40, 40), 'YELLOW', lambda x: self.choice_color(x)))
        self.Color_list.append(Button((380, 160), (40, 40), 'GREEN', lambda x: self.choice_color(x)))
        self.Color_list.append(Button((420, 160), (40, 40), 'BLUE', lambda x: self.choice_color(x)))
        self.Color_list[0].INACTIVE_COLOR = C.RED
        self.Color_list[1].INACTIVE_COLOR = C.YELLOW
        self.Color_list[2].INACTIVE_COLOR = C.GREEN
        self.Color_list[3].INACTIVE_COLOR = C.BLUE
        self.Uno_Button = Button((120, 220), (40, 40), 'UNO', lambda x: self.click_uno(x))
        self.Timer = Text((240, 120), 20, '', C.BLACK)
    '''
    아무나 카드가 한 장일 때, 누구든 누를 수 있음.
        나보다 상대가 먼저 눌렀으면 카드 뽑기.
    그 한장에 대해 우노를 안누른 상태라면 낼 수 없음.

    내 턴에 2장이었다가 한장 내고 우노를 누름
    1. 상대 턴 돌면서 나한테 카드 먹여서 2장이 넘어감
    2. 내 턴 다시 돌아왔는데 낼 카드가 없어서 드로우 -> 2장이 됨
    
    1. 마지막 한장  카드를 내려면, 우노를 누른 상태여야만 함.
        우노 누른 상태


    '''

    def click_uno(self, who):
        print("click uno button, player ", who)
        valid = 0
        game = Playing.game
        for player in game.players:
            if (len(player.hand) == 1):
                valid += 1
                
        if valid:
            if self.game.current_player.player_id != who: # who가 아닌 사람이 uno일 때 who가 누른 경우
                self.game._pick_up(self.game.current_player, 1)
            else: # 내꺼 내가누름
                self.game.current_player.uno_state = True
        else: 
            pass

    def choice_color(self, n):
        self.Color_idx = n
        
    def computer_add_remove(self, idx, item):
        if self.is_computer_activated[idx]:
            self.is_computer_activated[idx] = False
            self.num_of_players -= 1
        else:
            self.is_computer_activated[idx] = True
            self.num_of_players += 1

    def update_screen(self, mouse_pos): # 현재 화면 업데이트
        self.Timer.change_text(str(self.time//60))
        self.Timer.draw(self.screen)
        for idx, item in enumerate(self.Player_list):
            if self.is_computer_activated[idx]:
                item.INACTIVE_COLOR = C.GRAY
                item.locate = True
                item.change_text('Computer'+str(idx+1))
            else:
                item.INACTIVE_COLOR = C.WHITE
                item.locate = False
                item.change_text('empty')
            item.update(mouse_pos)
            item.draw(self.screen)
            item.change_size(Display.display_idx)
        for item in self.Card_list:
            item.update(mouse_pos)
        self.start_button.update(mouse_pos)
        self.Uno_Button.update(mouse_pos)
        
    def next_screen(self):
        pass
    
    def game_start(self):
        self.is_game_start = True

    def player_action(self, running):
        player = self.game.current_player
        player_id = player.player_id
        if player.can_play(self.game.current_card):
            
            # if self.top.card_color == myCard.card_color or self.top.card_type == myCard.card_type or myCard.card_color == "black":
            if  self.is_color_choice and self.Color_idx != None:                           
                new_color = C.COLORS[self.Color_idx]
                self.Color_active = False
                self.Color_idx = None
                #print("Player {} played {}".format(player, card))
                self.game.play(player=player_id, card=self.choice_card_idx, new_color=new_color)
                self.time = 1800
                self.is_color_choice = False
                self.choice_card_idx = None
                
            if self.choice_card_idx is not None:
                if len(player.hand) > 1 or (len(player.hand) == 1 and player.uno_state):
                    card = Playing.game.players[0].hand[self.choice_card_idx]
                    if self.game.current_card.playable(card):
                        if card.color == 'black':
                            if self.Color_idx == None:
                                self.Color_active = True
                                self.is_color_choice = True

                        else:
                            new_color = None
                            print("Player {} played {}".format(player, card))
                            self.game.play(player=player_id, card=self.choice_card_idx, new_color=new_color)
                            self.choice_card_idx = None
                            self.time = 1800
        
        else:
            print("Player {} picked up".format(player))
            self.game.play(player=player_id, card=None)
            pg.time.wait(200)
            self.time = 1800


    def game_handler(self, running): # main
        if Playing.game == None:
            Playing.game = UnoGame(self.num_of_players)
        self.top = CardButton(str(Playing.game.current_card.color) + str(Playing.game.current_card.card_type), 
                              C.ALL_CARDS[str(Playing.game.current_card.color) + str(Playing.game.current_card.card_type)])
        for i in Playing.game.players[0].hand:
            myCard = CardButton(str(i.color) + str(i.card_type), C.ALL_CARDS[str(i.color) + str(i.card_type)])
            self.Card_list.append(myCard)
            '''
                if self.top.card_color == myCard.card_color or self.top.card_type == myCard.card_type or myCard.card_color == "black":
                    self.Card_list.append(myCard)
                    self.screen.blit(myCard.img, (self.x, self.y))
                self.x += 50
            '''
        self.top.draw(self.screen, 150, 100)
        self.backCard = CardButton("Back", C.ALL_CARDS["Back"])
        self.backCard.draw(self.screen, 100, 100)

        player = self.game.current_player
        player_id = player.player_id
        if player_id == 0: # 나
            self.player_action(running)
        else: # ai
            if player.can_play(self.game.current_card):
                # 30 - random 
                if 1800 - self.time < 60*random.uniform(0.1, 0.2):
                    pass
                else:
                    if len(player.hand) == 1:
                        self.click_uno(player_id)
                    for i, card in enumerate(player.hand):
                        if self.game.current_card.playable(card):
                            if len(player.hand) > 1 or (len(player.hand) == 1 and player.uno_state):
                                if card.color == 'black':
                                    new_color = random.choice(C.COLORS)
                                else:
                                    new_color = None
                                print("Computer {} played {}".format(player, card))
                                self.game.play(player=player_id, card=i, new_color=new_color)
                                self.time = 1800
                                break
            else:
                print("Computer {} picked up".format(player))
                self.game.play(player=player_id, card=None)
                self.time = 1800

    def single_mode(self, running):
        self.screen.fill((255, 255, 255))
        pg.draw.rect(self.screen, C.BLACK, (int(620*C.WEIGHT[Display.display_idx]), 0, 
                                            int(180*C.WEIGHT[Display.display_idx]), int(600*C.WEIGHT[Display.display_idx])))
        self.Card_list = []
        self.x = 0
        self.y = 300

        if self.is_game_start:
            self.game_handler(running)
        else:
            self.start_button.draw(self.screen)

        if self.is_game_start:
            for item in self.Card_list:
                item.draw(self.screen, self.x, self.y)
                self.x += 50
                if self.x >= 500:
                    self.x = 0
                    self.y += 100
    
        self.update_screen(pg.mouse.get_pos())

        if self.is_game_start:
            self.x = 0
            self.y = 300
            for item in self.Card_list:
                item.draw(self.screen, self.x, self.y)
                self.x += 50
                if self.x >= 500:
                    self.x = 0
                    self.y += 100

        if self.is_game_start:
            x_ = 640
            y_ = 40
            index = 0
            for idx in range(5):
                if self.is_computer_activated[idx]:
                    self.screen.blit(pg.transform.scale(C.ALL_CARDS["Back"], (30,60)), (x_, y_))
                    self.Text_list[idx].change_text(str(len(Playing.game.players[index + 1].hand)) + " Card(s) in hand")
                    self.Text_list[idx].draw(self.screen)
                    index += 1
                y_ += 118

            if self.game.current_card.color == 'red': # 현재 색깔 표시
                pg.draw.rect(self.screen, C.RED, (100, 50, 50, 50))
            elif self.game.current_card.color == 'green':
                pg.draw.rect(self.screen, C.GREEN, (100, 50, 50, 50))
            elif self.game.current_card.color == 'yellow':
                pg.draw.rect(self.screen, C.YELLOW, (100, 50, 50, 50))
            elif self.game.current_card.color == 'blue':
                pg.draw.rect(self.screen, C.BLUE, (100, 50, 50, 50))
            elif self.game.current_card.color == 'black':
                if self.game.current_card.temp_color == 'red':
                    pg.draw.rect(self.screen, C.RED, (100, 50, 50, 50))
                elif self.game.current_card.temp_color == 'green':
                    pg.draw.rect(self.screen, C.GREEN, (100, 50, 50, 50))
                elif self.game.current_card.temp_color == 'yellow':
                    pg.draw.rect(self.screen, C.YELLOW, (100, 50, 50, 50))
                elif self.game.current_card.temp_color == 'blue':
                    pg.draw.rect(self.screen, C.BLUE, (100, 50, 50, 50))

        if self.is_game_start:
            self.Uno_Button.draw(self.screen)
            self.Card_list[self.key_locate].on_key = True

        if self.Color_active:
            for item in self.Color_list:
                item.update(pg.mouse.get_pos())
                item.draw(self.screen)

        for event in pg.event.get():
            self.tmp_event = event
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.KEYUP:
                for idx, item in enumerate(Data.data.KEY_Settings):
                    if event.key == item:
                        if idx == 0: # up
                            if self.key_locate-10 >= 0:
                                self.Card_list[self.key_locate].on_key = False
                                self.key_locate -= 10
                                self.Card_list[self.key_locate].on_key = True
                        elif idx == 1: # left
                            if self.key_locate%10 != 0:
                                self.Card_list[self.key_locate].on_key = False
                                self.key_locate -= 1
                                self.Card_list[self.key_locate].on_key = True
                        elif idx == 2: # down
                            if self.key_locate+10<=len(self.Card_list)-1:
                                self.Card_list[self.key_locate].on_key = False
                                self.key_locate += 10
                                self.Card_list[self.key_locate].on_key = True
                        elif idx == 3: # right
                            if (self.key_locate != len(self.Card_list)-1) and ((self.key_locate+1)%10 != 0):
                                self.Card_list[self.key_locate].on_key = False
                                self.key_locate += 1
                                self.Card_list[self.key_locate].on_key = True
                        elif idx == 4: # return
                            if self.game.current_card.playable(Playing.game.players[0].hand[self.key_locate]):
                                '''if "black" in self.Card_list[self.key_locate].card_name:
                                    new_color = random.choice(C.COLORS)
                                else:
                                    new_color = None
                                self.game.play(player=0, card=self.key_locate, new_color=new_color)'''
                                self.choice_card_idx = self.key_locate
                                self.key_locate = 0
                        elif idx == 5: # escape
                            self.mode[C.NEXT_SCREEN] = C.STOP
                        else:
                            if self.Color_active:
                                if idx == 6:
                                    self.Color_idx = 0
                                elif idx == 7:
                                    self.Color_idx = 1
                                elif idx == 8:
                                    self.Color_idx = 2
                                elif idx == 9:
                                    self.Color_idx = 3
                                print(self.Color_idx)
                                self.Color_active = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.tmp_event.type == pg.QUIT:
                    running[0] = False
                    return
                elif self.tmp_event.type == pg.KEYUP:
                    if self.tmp_event.key == pg.K_ESCAPE:
                        self.mode[C.NEXT_SCREEN] = C.STOP
                elif self.tmp_event.type == pg.MOUSEBUTTONDOWN:
                    if Playing.game:
                        if self.Color_active:
                            print(2)
                            for idx, item in enumerate(self.Color_list):
                                if item.above:
                                    self.Color_idx = idx
                        else:
                            for idx, item in enumerate(self.Card_list):
                                if item.above:
                                    print(item.card_name)
                                    self.choice_card_idx = idx
                                    break
                            if self.Uno_Button.above:
                                self.Uno_Button.click((0, ))

                for idx, item in enumerate(self.Player_list):
                    if item.above and not self.is_game_start:
                        item.click((idx, item))
                if self.start_button.above and not self.is_game_start:
                    self.start_button.click()
        if self.is_game_start:
            self.x = 0
            self.y = 300
            for item in self.Card_list:
                item.draw(self.screen, self.x, self.y)
                self.x += 50
                if self.x >= 500:
                    self.x = 0
                    self.y += 100
        pg.display.update()

    def story_mode(self, stage, running):
        pass

    def main_loop(self, running):
        # game inst
        pg.time.Clock().tick(60)
        if self.is_game_start:
            if self.time <= 0:
                self.time = 1800
            else:
                self.time -= 1
        if Playing.game_mode == 0:
            self.single_mode(running)
        elif Playing.game_mode == 1:
            self.story_mode(self.stage, running)
