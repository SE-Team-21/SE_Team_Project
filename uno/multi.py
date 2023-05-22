from socket import *
import encryption as E
from datetime import datetime
from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.KeySettings import Data
from uno.Button_Class import Button
from uno.CardButton_Class import CardButton
from uno.Text_Class import Text

class Multi(Display):
    def __init__(self):
        super().__init__()
        self.button_create_game = Button((100, 150), (120, 60), 'Create Game', color=C.WHITE, inactive_color=(0, 255, 128), above_color=(0, 229, 115), bold=True)
        self.button_reload = Button((300, 150), (60, 52), '', color=C.WHITE, inactive_color=(4, 149, 205), above_color=(119, 199, 230), bold=True)
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
        self.my_name = ''
        self.text_top_create = Text((300, 120), 30, 'Creating Game')
        self.text_top_join = Text((350, 120), 30, 'Join Game')
        self.text_host_ip = Text((220, 200), 20, 'Host IP : ')
        self.text_password = Text((220, 300), 20, 'Password : ')
        self.text_caution = Text((220, 360), 20, '6 ~ 12 char : Alphabet or Number')
        self.text_ip = Button((450, 214), (240, 40), '')
        self.target_address = None
        self.target_port = None

        # 대기실
        self.start_button = Button((100, 100), (60, 60), 'Game Start', lambda: self.game_start())
        self.is_computer_activated = [False, False, False, False, False]
        self.Player_list = []
        self.Player_list.append(Button((710, 160), (160, 80), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 250), (160, 80), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 340), (160, 80), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 430), (160, 80), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.Player_list.append(Button((710, 520), (160, 80), 'empty', lambda x, y: self.computer_add_remove(x, y)))
        self.name_input_box = Button((710, 70), (160, 80), 'You', )
        self.name_infor = Text((140, 256), 20, 'Only Alphabet up to 7 char and Enter', C.BLACK)
        self.input_active1 = False
        self.num_of_players = 1
        self.win = False

        # 인게임
        self.Card_list = []
        self.my_turn = False
        # Load Setting
        self.my_name = Data.data.name
    
    ### 송신
    def connect(self):
        self.clientSock = socket(AF_INET, SOCK_STREAM)
        #self.clientSock.connect(('13.210.238.200', 10123))
        self.clientSock.connect(('127.0.0.1', 10123))
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

    def game_start(self):
        self.clientSock.send(E.Encrypt_A({"Type": "game_start"}))

    ### 수신
    def hand_out(self):
        print(self.data)
        if self.host:
            self.my_turn = True
        self.is_game_start = True
        for i in range(self.data["Num"]):
            self.Card_list.append(CardButton(self.data[str(i)][0] + str(self.data[str(i)][1]), C.ALL_CARDS[self.data[str(i)][0] + str(self.data[str(i)][1])]))
        self.data = None

    def next_screen(self, idx, running):
        pass

    def update_screen1(self, mouse_pos): # 대기실 화면 업데이트
        self.name_input_box.change_text(self.my_name)
        self.name_input_box.change_size(Display.display_idx)
        self.name_input_box.update(mouse_pos)
        self.name_input_box.draw(self.screen)
        if self.input_active1:
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
        self.start_button.change_size(Display.display_idx)
        self.start_button.update(mouse_pos)
        pg.display.update()

    def main_loop(self, running):
        pg.time.Clock().tick(60)
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
                        print(self.data["Type"])
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
                    self.update_screen(pg.mouse.get_pos())
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
                    self.screen.fill((255, 255, 255))
                    self.x = 0
                    self.y = 300
                    for item in self.Card_list:
                        item.draw(self.screen, self.x, self.y)
                        self.x += 50
                        if self.x >= 500:
                            self.x = 0
                            self.y += 100
                    pg.display.update()
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            running[0] = False
                            self.disconnect()
                            return
                else: # 게임 대기실 화면
                    if self.host: # 방장일 때
                        if self.data is not None:
                            if self.data["Type"] == "add": # 방에 새로운 사람이 들어오거나 컴퓨터 추가
                                self.data = None
                            elif self.data["Type"] == "remove": # 방에서 나가거나 컴퓨터 삭제
                                self.data = None
                            elif self.data["Type"] == "game_start":
                                self.hand_out()
                                
                        self.screen.fill((255, 255, 255))
                        pg.draw.rect(self.screen, C.BLACK, (int(620*C.WEIGHT[Display.display_idx]), 0, 
                                                            int(180*C.WEIGHT[Display.display_idx]), int(600*C.WEIGHT[Display.display_idx])))
                        self.start_button.draw(self.screen)
                        self.update_screen1(pg.mouse.get_pos())
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                running[0] = False
                                self.disconnect()
                                return
                            elif (event.type == pg.MOUSEBUTTONDOWN) and not self.input_active1:
                                for idx, item in enumerate(self.Player_list):
                                    if item.above:
                                        item.click((idx, item))
                                if self.start_button.above and self.num_of_players>=1:
                                    self.start_button.click()
                                    
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
                            if self.data["Type"] == "add":
                                pass
                            if self.data["Type"] == "game_start":
                                self.hand_out()
                        self.screen.fill((255, 255, 255))
                        pg.draw.rect(self.screen, C.BLACK, (int(620*C.WEIGHT[Display.display_idx]), 0, 
                                                            int(180*C.WEIGHT[Display.display_idx]), int(600*C.WEIGHT[Display.display_idx])))
                        self.start_button.draw(self.screen)
                        self.update_screen1(pg.mouse.get_pos())
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                running[0] = False
                                self.disconnect()
                                return
                            elif (event.type == pg.MOUSEBUTTONDOWN) and not self.input_active1:
                                for idx, item in enumerate(self.Player_list):
                                    if item.above:
                                        item.click((idx, item))
                                if self.start_button.above and self.num_of_players>=1:
                                    self.start_button.click()
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
                except:
                    pass
