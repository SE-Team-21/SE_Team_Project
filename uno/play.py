from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.Button_Class import Button
from uno.game.Game import UnoGame
from uno.Text_Class import Text
import random
from uno.CardButton_Class import CardButton
from uno.KeySettings import Data
import uno.Music as Music

class Playing(Display):
    def __init__(self):    
        super().__init__()
        self.game = None
        self.game_mode = 0
        self.win = False
        self.Card_list = []
        self.time = 1800
        self.key_locate = 0
        self.x = 0
        self.y = 0
        self.stage = 0
        self.num_of_players = 1
        self.is_game_start = False
        self.is_computer_activated = [False, False, False, False, False]
        self.Player_list = []
        self.Player_list.append(Button((710, 160), (160, 80), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 250), (160, 80), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 340), (160, 80), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 430), (160, 80), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 520), (160, 80), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Text_list.append(Text((690, 160), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 250), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 340), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 430), 20, '', C.BLACK))
        self.Text_list.append(Text((690, 520), 20, '', C.BLACK))
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
        self.Color_active = False
        self.Color_idx = None
        self.is_color_choice = False
        self.Timer = Text((240, 120), 20, '', C.BLACK)
        self.choice_card_idx = None
        self.name_input_box = Button((710, 70), (160, 80), 'You', )
        self.name_infor = Text((140, 256), 20, 'Only Alphabet up to 7 char and Enter', C.BLACK)
        self.my_name = 'You'
        self.input_active = False
        self.up_arrow = pg.transform.scale(pg.image.load("./assets/images/up_arrow.png"), (int(42*C.WEIGHT[Display.display_idx]), int(500*C.WEIGHT[Display.display_idx])))
        self.down_arrow = pg.transform.scale(pg.image.load("./assets/images/down_arrow.png"), (int(42*C.WEIGHT[Display.display_idx]), int(500*C.WEIGHT[Display.display_idx])))
        self.right_arrow = pg.transform.scale(pg.image.load("./assets/images/right_arrow.png"), (int(30*C.WEIGHT[Display.display_idx]), int(14*C.WEIGHT[Display.display_idx])))
        self.winner = Text((300, 300), 60, '', C.BLACK)
        self.circle = pg.transform.scale(pg.image.load("./assets/images/circle.png"), (int(200*C.WEIGHT[Display.display_idx]), int(200*C.WEIGHT[Display.display_idx])))
        self.uncircle = pg.transform.scale(pg.image.load("./assets/images/uncircle.png"), (int(200*C.WEIGHT[Display.display_idx]), int(200*C.WEIGHT[Display.display_idx])))
        # Load Setting
        self.name_input_box.change_text(Data.data.name)
        self.my_name = Data.data.name
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
    def draw_circle(self):
        if self.game._player_cycle._reverse:
            self.screen.blit(pg.transform.scale(self.circle, (int(200*C.WEIGHT[Display.display_idx]), int(200*C.WEIGHT[Display.display_idx]))), (int(300*C.WEIGHT[Display.display_idx]), int(200*C.WEIGHT[Display.display_idx])))
        else:
            self.screen.blit(pg.transform.scale(self.uncircle, (int(200*C.WEIGHT[Display.display_idx]), int(200*C.WEIGHT[Display.display_idx]))), (int(300*C.WEIGHT[Display.display_idx]), int(200*C.WEIGHT[Display.display_idx])))
        pg.display.update()
        pg.time.wait(3000)

    def draw_arrow(self):
        if self.game._player_cycle._reverse: # 화살표 위로
            self.screen.blit(pg.transform.scale(self.up_arrow, (int(42*C.WEIGHT[Display.display_idx]), int(500*C.WEIGHT[Display.display_idx]))), (int(550*C.WEIGHT[Display.display_idx]), int(40*C.WEIGHT[Display.display_idx])))
        else: # 화살표 아래로
            self.screen.blit(pg.transform.scale(self.down_arrow, (int(42*C.WEIGHT[Display.display_idx]), int(500*C.WEIGHT[Display.display_idx]))), (int(550*C.WEIGHT[Display.display_idx]), int(40*C.WEIGHT[Display.display_idx])))
        id = self.game.current_player.player_id
        if id == 0:
            self.screen.blit(pg.transform.scale(self.right_arrow, (int(30*C.WEIGHT[Display.display_idx]), int(14*C.WEIGHT[Display.display_idx]))), (int(580*C.WEIGHT[Display.display_idx]), int(60*C.WEIGHT[Display.display_idx])))
        else:
            idx = 0
            for i in self.is_computer_activated:
                if i:
                    id -= 1
                    idx += 1
                else:
                    idx += 1
                if id == 0:
                    break
            self.screen.blit(pg.transform.scale(self.right_arrow, (int(30*C.WEIGHT[Display.display_idx]), int(14*C.WEIGHT[Display.display_idx]))), (int(580*C.WEIGHT[Display.display_idx]), int((60+90*idx)*C.WEIGHT[Display.display_idx])))

    def draw_color_selection(self):
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
    
    def draw_computer_back(self):
        x_ = int(640*C.WEIGHT[Display.display_idx])
        y_ = int(140*C.WEIGHT[Display.display_idx])
        index = 0
        for idx in range(5):
            if self.is_computer_activated[idx]:
                self.screen.blit(pg.transform.scale(C.ALL_CARDS["Back"], (int(30*C.WEIGHT[Display.display_idx]),int(60*C.WEIGHT[Display.display_idx]))), (x_, y_))
                self.Text_list[idx].change_text(str(len(self.game.players[index + 1].hand)) + " Card(s) in hand")
                self.Text_list[idx].change_size(Display.display_idx)
                self.Text_list[idx].draw(self.screen)
                index += 1
            y_ += int(90*C.WEIGHT[Display.display_idx])

    def temp(self):
        self.screen.fill((255, 255, 255))
        pg.draw.rect(self.screen, C.BLACK, (int(620*C.WEIGHT[Display.display_idx]), 0, 
                                            int(180*C.WEIGHT[Display.display_idx]), int(600*C.WEIGHT[Display.display_idx])))
        self.x = 0
        self.y = 300
        for item in self.Card_list:
            item.draw(self.screen, self.x, self.y)
            self.x += 50
            if self.x >= 500:
                self.x = 0
                self.y += 100
        self.update_screen(pg.mouse.get_pos())
        self.draw_computer_back()
        self.draw_arrow()
        self.Uno_Button.draw(self.screen)
        self.top.draw(self.screen, 150, 100)
        self.backCard = CardButton("Back", C.ALL_CARDS["Back"])
        self.backCard.draw(self.screen, 100, 100)
        self.draw_color_selection()

    def card_motion(self, idx): # 카드 내는거
        fps = 120
        target_x = 150
        target_y = 100
        Music.ef_music_set.play()
        if idx == 0:
            locate = self.choice_card_idx
            start_x = 50*(locate%10)
            start_y = 300 + (locate//10)*100
            current_x = start_x
            current_y = start_y
            for i in range(fps):
                self.temp()
                self.screen.blit(pg.transform.scale(C.ALL_CARDS[str(self.game.players[0].hand[self.choice_card_idx].color) + str(self.game.players[0].hand[self.choice_card_idx].card_type)], (45,90)), (current_x, current_y))
                current_x -= (start_x - target_x)/fps
                current_y -= (start_y - target_y)/fps
                pg.display.update()
        else:
            id = self.game.current_player.player_id
            index = 0
            for i in self.is_computer_activated:
                if i:
                    id -= 1
                    index += 1
                else:
                    index += 1
                if id == 0:
                    break
            start_x = 640
            start_y = 50 + 90*index
            current_x = start_x
            current_y = start_y
            for i in range(fps):
                self.temp()
                self.screen.blit(pg.transform.scale(C.ALL_CARDS["Back"], (45,90)), (current_x, current_y))
                current_x -= (start_x - target_x)/fps
                current_y -= (start_y - target_y)/fps
                pg.display.update()

    def pick_up_motion(self, idx): # 카드 뽑는거
        fps = 120
        start_x = 100
        start_y = 100
        current_x = start_x
        current_y = start_y
        Music.ef_music_draw.play()
        
        if idx == 0: # 내가 뽑을 때
            locate = len(self.Card_list)
            target_x = 50*(locate%10)
            target_y = 300 + (locate//10)*100
            for i in range(fps):
                self.temp()
                self.screen.blit(pg.transform.scale(C.ALL_CARDS["Back"], (30,60)), (current_x, current_y))
                current_x -= (start_x - target_x)/fps
                current_y -= (start_y - target_y)/fps
                pg.display.update()
        else: # 컴퓨터가 뽑을 때
            id = self.game.current_player.player_id
            index = 0
            for i in self.is_computer_activated:
                if i:
                    id -= 1
                    index += 1
                else:
                    index += 1
                if id == 0:
                    break
            target_x = 640
            target_y = 50 + 90*index
            for i in range(fps):
                self.temp()
                self.screen.blit(pg.transform.scale(C.ALL_CARDS["Back"], (30,60)), (current_x, current_y))
                current_x -= (start_x - target_x)/fps
                current_y -= (start_y - target_y)/fps
                pg.display.update()

    def click_uno(self, who):
        print("click uno button, player ", who)
        valid = -1
        game = self.game
        for player in game.players:
            if (len(player.hand) == 1): # 1장인 사람이 여려명이면
                valid = player.player_id
                break
                
        if valid != -1:
            if valid != who: # who가 아닌 사람이 uno일 때 who가 누른 경우
                self.game._pick_up(valid, 1)
            else: # 내꺼 내가누름
                self.game.players[valid].uno_state = True
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
        self.Timer.change_size(Display.display_idx)
        self.Timer.draw(self.screen)
        self.name_input_box.change_text(self.my_name)
        self.name_input_box.change_size(Display.display_idx)
        self.name_input_box.update(mouse_pos)
        self.name_input_box.draw(self.screen)
        if self.input_active:
            self.name_infor.change_size(Display.display_idx)
            self.name_infor.draw(self.screen)
        for idx, item in enumerate(self.Player_list):
            if self.is_computer_activated[idx]:
                item.INACTIVE_COLOR = C.GRAY
                item.locate = True
                item.change_text('Computer'+str(idx+1))
            else:
                item.INACTIVE_COLOR = C.WHITE
                item.locate = False
                item.change_text('empty')
            item.change_size(Display.display_idx)
            item.update(mouse_pos)
            item.draw(self.screen)
        for item in self.Card_list:
            item.update(mouse_pos)
        self.start_button.change_size(Display.display_idx)
        self.start_button.update(mouse_pos)
        self.Uno_Button.change_size(Display.display_idx)
        self.Uno_Button.update(mouse_pos)
        
    def next_screen(self):
        pass
    
    def game_start(self):
        self.is_game_start = True
        C.IS_GAME_END = False

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
                    card = self.game.players[0].hand[self.choice_card_idx]
                    if self.game.current_card.playable(card):
                        if card.color == 'black':
                            if self.Color_idx == None:
                                self.Color_active = True
                                self.is_color_choice = True

                        else:
                            new_color = None
                            print("Player {} played {}".format(player, card))
                            self.card_motion(0)
                            self.game.play(player=player_id, card=self.choice_card_idx, new_color=new_color)
                            if card.card_type == 'reverse':
                                self.draw_circle()
                            self.choice_card_idx = None
                            self.time = 1800
                            
        
        else:
            print("Player {} picked up".format(player))
            self.game.play(player=player_id, card=None)
            self.pick_up_motion(0)
            self.time = 1800

    def game_handler(self, running): # main
        if self.game == None:
            self.game = UnoGame(self.num_of_players)
        self.top = CardButton(str(self.game.current_card.color) + str(self.game.current_card.card_type), 
                              C.ALL_CARDS[str(self.game.current_card.color) + str(self.game.current_card.card_type)])
        for i in self.game.players[0].hand:
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
            # here
        else: # ai
            if player.can_play(self.game.current_card) and self.game.is_active:
                # 30 - random
                if 1800 - self.time < 60*random.uniform(0.1, 0.2):
                    pass
                else:
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
                                self.card_motion(player_id)
                                if self.game.is_active == False:
                                    self.is_game_start = False
                                    self.win = True
                                    break
                                break
                    if 1800 -self.time < 60*random.uniform(0.8, 1):
                        if len(player.hand) == 1:
                            self.click_uno(player_id)
            elif self.game.is_active:
                print("Computer {} picked up".format(player))
                self.game.play(player=player_id, card=None)
                self.time = 1800
                self.pick_up_motion(player_id)

    def single_mode(self, running):
        if self.is_game_start: # 인게임화면
            self.win = False
            self.screen.fill((255, 255, 255))
            pg.draw.rect(self.screen, C.BLACK, (int(620*C.WEIGHT[Display.display_idx]), 0, 
                                                int(180*C.WEIGHT[Display.display_idx]), int(600*C.WEIGHT[Display.display_idx])))
            self.Card_list = []
            self.x = 0
            self.y = 300
            self.game_handler(running)
            for item in self.Card_list:
                item.draw(self.screen, self.x, self.y)
                self.x += 50
                if self.x >= 500:
                    self.x = 0
                    self.y += 100
            self.update_screen(pg.mouse.get_pos())
            self.x = 0
            self.y = 300
            for item in self.Card_list:
                item.draw(self.screen, self.x, self.y)
                self.x += 50
                if self.x >= 500:
                    self.x = 0
                    self.y += 100
            self.draw_computer_back()
            self.draw_arrow()
            self.draw_color_selection()
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
                                if self.game.current_card.playable(self.game.players[0].hand[self.key_locate]):
                                    self.choice_card_idx = self.key_locate
                                    self.key_locate = 0
                            elif idx == 5: # escape
                                self.mode[C.NEXT_SCREEN] = C.STOP
                                #self.is_game_start = False
                                #self.win = True
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
                        if self.game:
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
            self.x = 0
            self.y = 300
            for item in self.Card_list:
                item.draw(self.screen, self.x, self.y)
                self.x += 50
                if self.x >= 500:
                    self.x = 0
                    self.y += 100
        else:
            if self.win: # 승리 화면 마우스를 클릭하거나 키를 누르면 시작 메뉴로 돌아감
                self.screen.fill((255, 255, 255))
                self.winner.change_size(Display.display_idx)
                #self.winner.change_text(self.game._winner)
                self.winner.change_text(str(self.game.current_player.player_id)+'th player win')
                self.winner.draw(self.screen)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running[0] = False
                        return
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        print("END")
                    elif event.type == pg.KEYUP:
                        print("END")
            else: # 대기실
                self.screen.fill((255, 255, 255))
                pg.draw.rect(self.screen, C.BLACK, (int(620*C.WEIGHT[Display.display_idx]), 0, 
                                                    int(180*C.WEIGHT[Display.display_idx]), int(600*C.WEIGHT[Display.display_idx])))
                self.start_button.draw(self.screen)
                self.update_screen(pg.mouse.get_pos())
                if self.win:
                    pass
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running[0] = False
                        return
                    elif (event.type == pg.MOUSEBUTTONDOWN) and not self.input_active:
                        for idx, item in enumerate(self.Player_list):
                            if item.above:
                                item.click((idx, item))
                        if self.start_button.above:
                            self.start_button.click()
                        if self.name_input_box.above:
                            self.input_active = True
                    elif event.type == pg.KEYUP:
                        if self.input_active:
                            if event.key == pg.K_BACKSPACE:
                                self.my_name = self.my_name[:-1]
                            elif event.key == pg.K_RETURN:
                                Data.save_name(self.my_name)
                                self.input_active = False
                            elif event.unicode.isalpha() and len(self.my_name)<=6:
                                self.my_name += event.unicode
                        else:
                            if event.key == Data.data.KEY_Settings[5]:
                                self.mode[C.NEXT_SCREEN] = C.STOP
                    




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
        if self.game_mode == 0:
            self.single_mode(running)
        elif self.game_mode == 1:
            self.story_mode(self.stage, running)
        if Display.colorblind_idx != -1:
            self.color()
        pg.display.update()
