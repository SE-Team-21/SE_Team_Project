from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.Button_Class import Button
from uno.game.Game import UnoGame
from uno.Text_Class import Text
import random
from socket import *
import encryption as E
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

        ## Multi
        self.start_button_m = Button((100, 100), (60, 60), 'Game Start', lambda: self.game_start_m())
        self.button_create_game = Button((100, 150), (120, 60), 'Create Game', color=C.WHITE, inactive_color=(0, 255, 128), above_color=(0, 229, 115), bold=True)
        self.button_reload = Button((300, 150), (60, 52), '', color=C.WHITE, inactive_color=(4, 149, 205), above_color=(119, 199, 230), bold=True)
        self.button_area = []
        self.button_area.append(Button((280, 300), (60, 60), 'A'))
        self.button_area.append(Button((360, 300), (60, 60), 'B'))
        self.button_area.append(Button((440, 300), (60, 60), 'C'))
        self.button_area.append(Button((520, 300), (60, 60), 'D'))
        
        self.reload_img = pg.transform.scale(pg.image.load("./assets/images/reload.png"), (int(60*C.WEIGHT[Display.display_idx]), int(52*C.WEIGHT[Display.display_idx])))
        self.Room_list = []
        self.Room_data = []
        self.connection = False
        self.clientSock = None
        self.password = ''
        self.input_active = False
        self.pw_input_box = Button((450, 314), (240, 40), self.password)
        self.button_create = Button((300, 450), (120, 60), 'Create')
        self.button_cancel = Button((500, 450), (120, 60), 'Cancel')
        self.button_join = Button((300, 450), (120, 60), 'Join')
        self.pw_type = None
        self.start_tick = 239
        self.start_text = Text((200, 200), 40, 'Connecting to server.', C.BLACK)
        self.connect_fail = False
        self.host = False
        self.data = None
        self.lobby = True
        self.is_game_start = False
        self.text_top_create = Text((300, 120), 30, 'Creating Game')
        self.text_top_join = Text((350, 120), 30, 'Join Game')
        self.text_host_ip = Text((220, 200), 20, 'Host IP : ')
        self.text_password = Text((220, 300), 20, 'Password : ')
        self.text_caution = Text((220, 360), 20, '6 ~ 12 char : Alphabet or Number')
        self.text_ip = Button((450, 214), (240, 40), '')
        self.target_address = None
        self.target_port = None
        self.input_active1 = False
        self.select = False
        self.where = 0
        
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

    ###################################### 멀티
    def connect(self):
        self.clientSock = socket(AF_INET, SOCK_STREAM)
        self.clientSock.connect(('13.210.238.200', 10123))
        #self.clientSock.connect(('127.0.0.1', 10123))
        self.clientSock.setblocking(False)
        print('연결 확인 됐습니다.')
        self.get_my_address()
    
    def disconnect(self): # 서버에 연결 끊음 요청
        self.clientSock.send(E.Encrypt_A({"Type": "exit"}))
        self.clientSock = None

    def send_password(self, password, host_ip, host_port): # 방 Password 전송 / 입장용
        self.clientSock.send(E.Encrypt_A({"Type": "pw", "Password": E.Encrypt_S(password), "Host_IP": host_ip, "Host_PORT": host_port}))

    def make_room(self, password): # 방 생성
        self.clientSock.send(E.Encrypt_A({"Type": "mkr", "Password": E.Encrypt_S(password)}))
        self.host = True
    
    def get_room_state(self): # 대기실 상태 요청
        self.clientSock.send(E.Encrypt_A({"Type": "grs"}))
    
    def get_game_state(self): # 게임 진행 상태 요청
        self.clientSock.send(E.Encrypt_A({"Type": "ggs"}))
    
    def get_my_address(self): # 내 IP 주소 요청
        self.clientSock.send(E.Encrypt_A({"Type": "gma"}))

    def quit_room(self): # 방에서 퇴장
        self.clientSock.send(E.Encrypt_A({"Type": "qr"}))
        self.host = False
        
    def send_name(self): # 내 이름을 서버에 전송
        self.clientSock.send(E.Encrypt_A({"Type": "sn", "Name": self.my_name}))
        
    def card_click(self):
        self.clientSock.send(E.Encrypt_A({"Type": "card_click", "Num": self.key_locate}))
    
    def add_computer(self, idx, area):
        self.clientSock.send(E.Encrypt_A({"Type": "add_computer", "Index": idx, "Area": area}))

    def remove_computer(self, idx):
        self.clientSock.send(E.Encrypt_A({"Type": "remove_computer", "Index": idx}))

    def ban_player(self, idx):
        self.clientSock.send(E.Encrypt_A({"Type": "ban_player", "Index": idx}))
        
    def game_start_m(self):
        self.clientSock.send(E.Encrypt_A({"Type": "game_start"}))

    ### 수신
    def hand_out(self):
        print(self.data)
        if self.host:
            self.my_turn = True
        self.is_game_start = True
        for i in range(self.data["Num"]):
            self.Card_list.append(CardButton(self.data[str(i)][0] + str(self.data[str(i)][1]), C.ALL_CARDS[self.data[str(i)][0] + str(self.data[str(i)][1])]))
        self.top = CardButton(self.data["top"][0] + self.data["top"][1], C.ALL_CARDS[self.data["top"][0] + self.data["top"][1]])
        self.data = None


    #################################################
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
        fps = 60
        target_x = 150
        target_y = 100
        if self.game.is_active:
            print(self.game.is_active)
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
        fps = 60
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
                pass
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
                if len(player.hand) > 1 or (len(player.hand) == 1):
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
                            if self.game.tmp == False:
                                    self.is_game_start = False
                                    self.win = True
                                    self.key_locate = None
                                    print("win")
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
            if C.game_mode == 0:
                self.game = UnoGame(self.num_of_players, -1, 4)
            else:
                if C.INDEX == 0: # 지역 A 나포함 2명 50% 증가 / 기술 콤보
                    self.game = UnoGame(2, -1, 2)
                elif C.INDEX == 1:#지역 B 나포함 4명 첫 카드 빼고 다 나눠 주기
                    self.game = UnoGame(4, -1, 25)
                elif C.INDEX == 2:# 지역 C 나포함3명 5턴마다 필드위 색상 바꾸기
                    self.game = UnoGame(3, -1, 7)
                elif C.INDEX == 3:# 지역 나포함 3명 상대 50% 증가 / 기술 콤보 / 매 턴마다 색상 바뀜
                    self.game = UnoGame(3, 50, 15)
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
            self.game.turn += 1
            self.player_action(running)
            # here
        else: # ai
            if player.can_play(self.game.current_card) and self.game.is_active:
                # 30 - random
                if 1800 - self.time < 60*random.uniform(1, 3):
                    pass
                else:
                    for i, card in enumerate(player.hand):
                        if self.game.current_card.playable(card):
                            if len(player.hand) > 1 or (len(player.hand) == 1):
                                if card.color == 'black':
                                    new_color = random.choice(C.COLORS)
                                else:
                                    new_color = None
                                print("Computer {} played {}".format(player, card))
                                self.card_motion(player_id)
                                self.game.play(player=player_id, card=i, new_color=new_color)
                                self.time = 1800
                                if self.game.tmp == False:
                                    self.is_game_start = False
                                    self.win = True
                                    self.key_locate = None
                                    print("win")
                                    break
                                break
                    if 1800 -self.time < 60*random.uniform(0.8, 1):
                        if len(player.hand) == 1:
                            self.click_uno(player_id)
            elif self.game.is_active:
                print("Computer {} picked up".format(player))
                self.pick_up_motion(player_id)
                self.game.play(player=player_id, card=None)
                self.time = 1800

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
            if self.key_locate is not None:
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
                            if idx == 0 and self.key_locate is not None: # up
                                if self.key_locate-10 >= 0:
                                    self.Card_list[self.key_locate].on_key = False
                                    self.key_locate -= 10
                                    self.Card_list[self.key_locate].on_key = True
                            elif idx == 1 and self.key_locate is not None: # left
                                if self.key_locate%10 != 0:
                                    self.Card_list[self.key_locate].on_key = False
                                    self.key_locate -= 1
                                    self.Card_list[self.key_locate].on_key = True
                            elif idx == 2 and self.key_locate is not None: # down
                                if self.key_locate+10<=len(self.Card_list)-1:
                                    self.Card_list[self.key_locate].on_key = False
                                    self.key_locate += 10
                                    self.Card_list[self.key_locate].on_key = True
                            elif idx == 3 and self.key_locate is not None: # right
                                if (self.key_locate != len(self.Card_list)-1) and ((self.key_locate+1)%10 != 0):
                                    self.Card_list[self.key_locate].on_key = False
                                    self.key_locate += 1
                                    self.Card_list[self.key_locate].on_key = True
                            elif idx == 4 and self.key_locate is not None: # return
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
                if Data.data.djqwjr[0] == 0:
                    Data.save_djqwjr(0, 1)
                if C.game_mode == 0 and Data.data.djqwjr[2] == 0 and self.game.turn <= 10:
                    Data.save_djqwjr(2, 1)
                self.screen.fill((255, 255, 255))
                self.winner.change_size(Display.display_idx)
                #self.winner.change_text(self.game._winner)
                self.winner.change_text(str(self.game.current_player.player_id)+'th player win')
                self.winner.draw(self.screen)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running[0] = False
                        return
                    elif event.type == pg.MOUSEBUTTONDOWN or event.type == pg.KEYUP:
                        self.mode[C.NEXT_SCREEN] = C.START
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
                        if self.start_button.above and self.num_of_players>=2:
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
                    


    def multi_mode(self, running):
        if not self.connection: # 서버 연결
            if not self.connect_fail:
                if self.start_tick == 0:
                    self.screen.fill((255, 255, 255))
                    self.start_text.draw(self.screen)
                    pg.display.update()
                elif self.start_tick == 60:
                    self.screen.fill((255, 255, 255))
                    self.start_text.change_text('Connecting to server..')
                    self.start_text.draw(self.screen)
                    pg.display.update()
                elif self.start_tick == 120:
                    self.screen.fill((255, 255, 255))
                    self.start_text.change_text('Connecting to server...')
                    self.start_text.draw(self.screen)
                    pg.display.update()
                elif self.start_tick == 180:
                    self.screen.fill((255, 255, 255))
                    self.start_text.change_text('Connecting to server.')
                    self.start_text.draw(self.screen)
                    pg.display.update()
                elif self.start_tick == 240:
                    try:
                        self.connect()
                        self.connection = True
                    except:
                        self.connect_fail = True
                self.start_tick += 1
                if self.connection or self.connect_fail:
                    self.start_tick = 0
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running[0] = False
                        self.disconnect()
                        return
            else: # 서버 연결 실패시 예외처리
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running[0] = False
                        self.disconnect()
                        return
        else:
            if self.lobby: # 로비 화면
                if self.input_active: # 로비 - 패스워드 입력 화면
                    if self.pw_type == 1: # 패스워드 - 방 생성 / 호스트
                        pg.draw.rect(self.screen, C.GRAY, (200, 100, 400, 400))
                        self.text_host_ip.draw(self.screen)
                        self.text_password.draw(self.screen)
                        self.text_caution.draw(self.screen)
                        self.text_top_create.draw(self.screen)
                        self.button_create.update(pg.mouse.get_pos())
                        self.button_create.draw(self.screen)
                        self.button_cancel.update(pg.mouse.get_pos())
                        self.button_cancel.draw(self.screen)
                        self.pw_input_box.update(pg.mouse.get_pos())
                        self.pw_input_box.draw(self.screen)
                        self.text_ip.draw(self.screen)
                        pg.display.update()
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                running[0] = False
                                self.disconnect()
                                return
                            elif event.type == pg.MOUSEBUTTONDOWN:
                                if self.button_create.above and len(self.password)>=6:
                                    self.input_active = False
                                    self.make_room(self.password)
                                    print(self.password)
                                    self.password = ''
                                    self.pw_input_box.change_text(self.password)
                                    self.lobby = False
                                    self.input_active = False
                                    return
                                if self.button_cancel.above:
                                    self.pw_type = None
                                    self.input_active = False
                                    self.password = ''
                                    self.pw_input_box.change_text(self.password)
                            elif event.type == pg.KEYUP:
                                if event.key == pg.K_BACKSPACE:
                                        self.password = self.password[:-1]
                                        temp = ''
                                        for i in self.password:
                                            temp+='*'
                                        self.pw_input_box.change_text(temp)
                                elif event.key == pg.K_RETURN and len(self.password)>=6:
                                    self.input_active = False
                                    self.make_room(self.password)
                                    print(self.password)
                                    self.password = ''
                                    self.pw_input_box.change_text(self.password)
                                    self.lobby = False
                                    self.input_active = False
                                    return
                                elif (event.unicode.isalpha() or event.unicode.isdigit()) and len(self.password)<=12:
                                    self.password += event.unicode
                                    temp = ''
                                    for i in self.password:
                                        temp+='*'
                                    self.pw_input_box.change_text(temp)
                    else: # 패스워드 - 방 입장 / 클라이언트
                        pg.draw.rect(self.screen, C.GRAY, (200, 100, 400, 400))
                        self.text_host_ip.draw(self.screen)
                        self.text_password.draw(self.screen)
                        self.text_caution.draw(self.screen)
                        self.text_top_join.draw(self.screen)
                        self.button_join.update(pg.mouse.get_pos())
                        self.button_join.draw(self.screen)
                        self.button_cancel.update(pg.mouse.get_pos())
                        self.button_cancel.draw(self.screen)
                        self.pw_input_box.update(pg.mouse.get_pos())
                        self.pw_input_box.draw(self.screen)
                        self.text_ip.draw(self.screen)
                        pg.display.update()
                        if self.data is not None:
                            if self.data["Type"] == "Correct":
                                self.data = None
                                self.input_active = False
                                self.lobby = False
                                self.password = ''
                                self.pw_input_box.change_text(self.password)
                            elif self.data["Type"] == "Incorrect":
                                self.data = None
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                running[0] = False
                                self.disconnect()
                                return
                            elif event.type == pg.MOUSEBUTTONDOWN:
                                if self.button_join.above and len(self.password)>=6:
                                    self.send_password(self.password, self.target_address, self.target_port)
                                if self.button_cancel.above:
                                    self.pw_type = None
                                    self.input_active = False
                                    self.password = ''
                                    self.pw_input_box.change_text(self.password)
                            elif event.type == pg.KEYUP:
                                if event.key == pg.K_BACKSPACE:
                                        self.password = self.password[:-1]
                                        temp = ''
                                        for i in self.password:
                                            temp+='*'
                                        self.pw_input_box.change_text(temp)
                                elif event.key == pg.K_RETURN and len(self.password)>=6:
                                    self.send_password(self.password, self.target_address, self.target_port)
                                elif (event.unicode.isalpha() or event.unicode.isdigit()) and len(self.password)<=12:
                                    self.password += event.unicode
                                    temp = ''
                                    for i in self.password:
                                        temp+='*'
                                    self.pw_input_box.change_text(temp)
                else: # 로비 - 대기
                    self.screen.fill((59, 174, 218))
                    self.button_reload.update(pg.mouse.get_pos())
                    self.button_reload.draw(self.screen)
                    self.button_create_game.update(pg.mouse.get_pos())
                    self.button_create_game.draw(self.screen)
                    for room in self.Room_list:
                        room.update(pg.mouse.get_pos())
                        room.draw(self.screen)
                    if self.data is not None:
                        if self.data["Type"] == "rs":
                            self.Room_list = []
                            x = 100
                            y = 300
                            for i in range(self.data["Num"]):
                                self.Room_list.append(Button((x, y), (200, 60), self.data[str(i)][0]+'  '+str(self.data[str(i)][1])+'/6', color=C.WHITE, inactive_color=(0, 255, 128), above_color=(0, 229, 115), bold=True))
                                self.Room_data.append([self.data[str(i)][0], self.data[str(i)][2]]) # [address, port]
                                y += 90
                            for room in self.Room_list:
                                room.update(pg.mouse.get_pos())
                                room.draw(self.screen)
                            self.data = None
                        elif self.data["Type"] == "ip":
                            print("Host's IP Address : ", self.data["address"])
                            self.data = None
                        elif self.data["Type"] == "myip":
                            self.text_ip.change_text(self.data["address"])
                            self.data = None
                    self.screen.blit(pg.transform.scale(self.reload_img, (int(60*C.WEIGHT[Display.display_idx]), int(52*C.WEIGHT[Display.display_idx]))), (int(270*C.WEIGHT[Display.display_idx]), int(124*C.WEIGHT[Display.display_idx])))
                    pg.display.update()
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            running[0] = False
                            self.disconnect()
                            return
                        elif event.type == pg.MOUSEBUTTONDOWN:
                            if self.button_create_game.above:
                                self.input_active = True
                                self.pw_type = 1
                            if self.button_reload.above:
                                self.get_room_state()
                            for idx, room in enumerate(self.Room_list):
                                if room.above:
                                    self.target_address = self.Room_data[idx][0]
                                    self.target_port = self.Room_data[idx][1]
                                    self.input_active = True
                                    self.pw_type = 2
                                    break

            else:
                if self.is_game_start: # 게임 시작 후 화면
                    self.win = False
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
                    #self.draw_computer_back()
                    #self.draw_arrow()
                    #self.draw_color_selection()
                    self.top.draw(self.screen, 150, 100)
                    self.backCard = CardButton("Back", C.ALL_CARDS["Back"])
                    self.backCard.draw(self.screen, 100, 100)
                    self.Uno_Button.draw(self.screen)
                    if self.key_locate is not None:
                        self.Card_list[self.key_locate].on_key = True
                    if self.Color_active:
                        for item in self.Color_list:
                            item.update(pg.mouse.get_pos())
                            item.draw(self.screen)
                    pg.display.update()
                    for event in pg.event.get():
                        self.tmp_event = event
                        if event.type == pg.QUIT:
                            running[0] = False
                            self.disconnect()
                            return
                        elif event.type == pg.KEYUP:
                            for idx, item in enumerate(Data.data.KEY_Settings):
                                if event.key == item:
                                    if idx == 0 and self.key_locate is not None: # up
                                        if self.key_locate-10 >= 0:
                                            self.Card_list[self.key_locate].on_key = False
                                            self.key_locate -= 10
                                            self.Card_list[self.key_locate].on_key = True
                                    elif idx == 1 and self.key_locate is not None: # left
                                        if self.key_locate%10 != 0:
                                            self.Card_list[self.key_locate].on_key = False
                                            self.key_locate -= 1
                                            self.Card_list[self.key_locate].on_key = True
                                    elif idx == 2 and self.key_locate is not None: # down
                                        if self.key_locate+10<=len(self.Card_list)-1:
                                            self.Card_list[self.key_locate].on_key = False
                                            self.key_locate += 10
                                            self.Card_list[self.key_locate].on_key = True
                                    elif idx == 3 and self.key_locate is not None: # right
                                        if (self.key_locate != len(self.Card_list)-1) and ((self.key_locate+1)%10 != 0):
                                            self.Card_list[self.key_locate].on_key = False
                                            self.key_locate += 1
                                            self.Card_list[self.key_locate].on_key = True
                                    elif idx == 4 and self.key_locate is not None: # return
                                        if self.my_turn:
                                            self.card_click()
                                        '''if self.game.current_card.playable(self.game.players[0].hand[self.key_locate]): #여기
                                            x = self.key_locate
                                            self.key_locaself.choice_card_idte = 0'''
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
                                self.disconnect()
                                return
                            elif self.tmp_event.type == pg.KEYUP:
                                if self.tmp_event.key == pg.K_ESCAPE:
                                    self.mode[C.NEXT_SCREEN] = C.STOP
                            elif self.tmp_event.type == pg.MOUSEBUTTONDOWN:
                                if self.game: #여기
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
                else: # 게임 대기실 화면
                    if self.host: # 방장일 때
                        if self.data is not None:
                            if self.data["Type"] == "update": # 방에 새로운 사람이 들어오거나 컴퓨터 추가
                                pass
                                self.data = None
                            elif self.data["Type"] == "remove": # 방에서 나가거나 컴퓨터 삭제
                                self.data = None
                            elif self.data["Type"] == "game_start":
                                self.hand_out()
                                
                        self.screen.fill((255, 255, 255))
                        pg.draw.rect(self.screen, C.BLACK, (int(620*C.WEIGHT[Display.display_idx]), 0, 
                                                            int(180*C.WEIGHT[Display.display_idx]), int(600*C.WEIGHT[Display.display_idx])))
                        self.start_button_m.draw(self.screen)
                        self.update_screen(pg.mouse.get_pos())
                        if self.select:
                            for idx, item in enumerate(self.button_area):
                                item.update(pg.mouse.get_pos())
                                item.draw(self.screen)
                        pg.display.update()
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                running[0] = False
                                self.disconnect()
                                return
                            elif (event.type == pg.MOUSEBUTTONDOWN) and not self.input_active1:
                                if self.select:
                                    for idx, item in enumerate(self.button_area):
                                        if item.above:
                                            self.add_computer(self.where, idx)
                                            self.select = False
                                else:
                                    for idx, item in enumerate(self.Player_list):
                                        if item.above:
                                            if self.is_computer_activated[idx]:
                                                self.remove_computer(idx)
                                            else:
                                                self.select = True
                                                self.where = idx
                                    if self.start_button_m.above and self.num_of_players>=1:
                                        self.start_button_m.click()
                                    if self.name_input_box.above:
                                        self.input_active1 = True
                            elif event.type == pg.KEYUP:
                                if self.input_active1:
                                    if event.key == pg.K_BACKSPACE:
                                        self.my_name = self.my_name[:-1]
                                    elif event.key == pg.K_RETURN:
                                        Data.save_name(self.my_name)
                                        self.input_active1 = False
                                        self.send_name()
                                    elif event.unicode.isalpha() and len(self.my_name)<=6:
                                        self.my_name += event.unicode
                                else:
                                    if event.key == Data.data.KEY_Settings[5]:
                                        self.mode[C.NEXT_SCREEN] = C.STOP
                    else: # 클라이언트일 때
                        if self.data is not None:
                            if self.data["Type"] == "update":
                                pass# 새로운 유저 들어왔을 때
                                self.data = None
                            if self.data["Type"] == "game_start":
                                self.hand_out()
                                self.data = None
                        self.screen.fill((255, 255, 255))
                        pg.draw.rect(self.screen, C.BLACK, (int(620*C.WEIGHT[Display.display_idx]), 0, 
                                                            int(180*C.WEIGHT[Display.display_idx]), int(600*C.WEIGHT[Display.display_idx])))
                        self.update_screen(pg.mouse.get_pos())
                        pg.display.update()
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                running[0] = False
                                self.disconnect()
                                return
                            elif (event.type == pg.MOUSEBUTTONDOWN) and not self.input_active1:
                                if self.name_input_box.above:
                                    self.input_active1 = True
                            elif event.type == pg.KEYUP:
                                if self.input_active1:
                                    if event.key == pg.K_BACKSPACE:
                                        self.my_name = self.my_name[:-1]
                                    elif event.key == pg.K_RETURN:
                                        Data.save_name(self.my_name)
                                        self.input_active1 = False
                                    elif event.unicode.isalpha() and len(self.my_name)<=6:
                                        self.my_name += event.unicode
                                else:
                                    if event.key == Data.data.KEY_Settings[5]:
                                        self.mode[C.NEXT_SCREEN] = C.STOP
                    

            if self.clientSock is not None:
                try:
                    self.data = E.Decrypt_A(self.clientSock.recv(1024))
                    print('받은 데이터 : ', self.data)
                    if self.data['Type'] == 'action':
                        self.current_card_color = self.data['current_card_color']
                        self.current_card_card_type = self.data['current_card_card_type']
                        # wild card +10
                        for i in range(self.data['Num']): # 각 플레이어의 핸드 개수
                            pass

                        # 1. 누가 먹었는지 보내주기 vs 2. 매턴마다 모든 플레이어의 카드 보여주기
                        # 내 턴이면
                        self.my_turn = True
                        self.data = None
                    elif self.data['Type'] == '':
                        pass
                except:
                    pass



    def story_mode(self, stage, running):
        if self.is_game_start == False:
            if stage == 0: # 지역 A 나포함 2명 50% 증가 / 기술 콤보
                self.num_of_players += 1
                self.is_computer_activated[0] = True
            elif stage == 1: #지역 B 나포함 4명 첫 카드 빼고 다 나눠 주기
                self.num_of_players += 3
                self.is_computer_activated[0] = True
                self.is_computer_activated[1] = True
                self.is_computer_activated[2] = True
            elif stage == 2: # 지역 C 나포함3명 5턴마다 필드위 색상 바꾸기
                self.num_of_players += 2
                self.is_computer_activated[0] = True
                self.is_computer_activated[1] = True
            elif stage == 3: # 지역 나포함 3명 상대 50% 증가 / 기술 콤보 / 매 턴마다 색상 바뀜
                self.num_of_players += 2
                self.is_computer_activated[0] = True
                self.is_computer_activated[1] = True
            self.is_game_start = True
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
        if self.key_locate is not None:
            self.Card_list[self.key_locate].on_key = True
        if self.Color_active:
            for item in self.Color_list:
                item.update(pg.mouse.get_pos())
                item.draw(self.screen)
        if self.win: # 승리 화면 마우스를 클릭하거나 키를 누르면 시작 메뉴로 돌아감 여기서 저장해야됨
            self.screen.fill((255, 255, 255))
            self.winner.change_size(Display.display_idx)
            #self.winner.change_text(self.game._winner)
            self.winner.change_text(str(self.game.current_player.player_id)+'th player win')
            self.winner.draw(self.screen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running[0] = False
                    return
                elif event.type == pg.MOUSEBUTTONDOWN or event.type == pg.KEYUP:
                    self.mode[C.NEXT_SCREEN] = C.START
                    Data.save_story(Data.data.Story+1)
        else:
            for event in pg.event.get():
                self.tmp_event = event
                if event.type == pg.QUIT:
                    running[0] = False
                    return
                elif event.type == pg.KEYUP:
                    for idx, item in enumerate(Data.data.KEY_Settings):
                        if event.key == item:
                            if idx == 0 and self.key_locate is not None: # up
                                if self.key_locate-10 >= 0:
                                    self.Card_list[self.key_locate].on_key = False
                                    self.key_locate -= 10
                                    self.Card_list[self.key_locate].on_key = True
                            elif idx == 1 and self.key_locate is not None: # left
                                if self.key_locate%10 != 0:
                                    self.Card_list[self.key_locate].on_key = False
                                    self.key_locate -= 1
                                    self.Card_list[self.key_locate].on_key = True
                            elif idx == 2 and self.key_locate is not None: # down
                                if self.key_locate+10<=len(self.Card_list)-1:
                                    self.Card_list[self.key_locate].on_key = False
                                    self.key_locate += 10
                                    self.Card_list[self.key_locate].on_key = True
                            elif idx == 3 and self.key_locate is not None: # right
                                if (self.key_locate != len(self.Card_list)-1) and ((self.key_locate+1)%10 != 0):
                                    self.Card_list[self.key_locate].on_key = False
                                    self.key_locate += 1
                                    self.Card_list[self.key_locate].on_key = True
                            elif idx == 4 and self.key_locate is not None: # return
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

    def main_loop(self, running):
        # game inst
        pg.time.Clock().tick(60)
        if self.is_game_start:
            if self.time <= 0:
                self.game.play(self.game.current_player.player_id)
                self.time = 1800
            else:
                self.time -= 1
        if C.game_mode == 0:
            self.single_mode(running)
        elif C.game_mode == 1:
            self.story_mode(C.INDEX, running)
        elif C.game_mode == 2:
            self.multi_mode(running)
        if Display.colorblind_idx != -1:
            self.color()
        pg.display.update()
