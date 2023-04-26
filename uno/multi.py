from socket import *
import encryption as E
from datetime import datetime
from uno.display import Display
import uno.Constants as C
import pygame as pg
from uno.KeySettings import Data
from uno.Button_Class import Button
from uno.Text_Class import Text

class Multi(Display):
    def __init__(self):
        super().__init__()
        self.Button_list.append(Button((100, 150), (120, 60), 'Make Room', self.connect))
        self.Button_list.append(Button((300, 150), (120, 60), 'Connect Room', self.send))
        self.Button_list.append(Button((500, 150), (120, 60), '3', self.send))
        self.Text_list.append(Text((690, 160), 20, '', C.BLACK))
        self.clientSock = None
        self.password = ''
        self.input_active = False
        self.pw_input_box = Button((710, 70), (160, 80), self.password)

    def connect(self):
        self.clientSock = socket(AF_INET, SOCK_STREAM)
        self.clientSock.connect(('13.210.238.200', 10123))
        self.clientSock.setblocking(False)
        print('연결 확인 됐습니다.')
    
    def disconnect(self): # 서버에 연결 끊음 요청
        self.clientSock.send(E.Encrypt_A({"Type": "exit"}))
        self.clientSock = None

    def send(self, password): # 방 Password 전송
        self.clientSock.send(E.Encrypt_A({"Type": "pw", "Password": E.Encrypt_S(password)}))
    
    def get_room_state(self): # 대기실 상태 요청
        self.clientSock.send(E.Encrypt_A({"Type": "grs"}))
    
    def get_game_state(self): # 게임 진행 상태 요청
        self.clientSock.send(E.Encrypt_A({"Type": "ggs"}))



    def next_screen(self, idx, running):
        pass

    def main_loop(self, running):
        self.screen.fill((255, 255, 255))
        self.pw_input_box.update(pg.mouse.get_pos())
        self.pw_input_box.draw(self.screen)
        self.update_screen(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running[0] = False
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                for idx, item in enumerate(self.Button_list):
                    if item.above:
                        item.click()
                if self.pw_input_box.above:
                            self.input_active = True
            elif event.type == pg.KEYUP:
                    if self.input_active:
                        if event.key == pg.K_BACKSPACE:
                            self.password = self.password[:-1]
                            temp = ''
                            for i in self.password:
                                temp+='*'
                            self.pw_input_box.change_text(temp)
                        elif event.key == pg.K_RETURN and len(self.password)>=6:
                            self.input_active = False
                            self.send(self.password)
                            print(self.password)
                            self.password = ''
                        elif (event.unicode.isalpha() or event.unicode.isdigit()) and len(self.password)<=12:
                            self.password += event.unicode
                            temp = ''
                            for i in self.password:
                                temp+='*'
                            self.pw_input_box.change_text(temp)
        if self.clientSock is not None:
            try:
                data = self.clientSock.recv(1024).decode('utf-8')
                print('받은 데이터 : ', data)
            except:
                pass
