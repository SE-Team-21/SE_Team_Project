from uno.Button_Class import Button
from uno.Text_Class import Text
from uno.KeySettings import *
import pygame as pg
import uno.constants as C
import pickle

Button_list = []
Button_list.append(Button((400, 200), (100, 50), 'SINGLE PLAYER'))
Button_list.append(Button((400, 300), (100, 50), 'OPTIONS'))
Button_list.append(Button((400, 400), (100, 50), 'QUIT'))

Text_list = []
Text_list.append(Text((320, 60), 40, 'UNO Game'))

KEY = [UpKey, LeftKey, DownKey, RightKey, ReturnKey, EnterKey]

load_settings()
KEY_Settings['UpKey'] = pg.K_a
# 수정할 입력 키보드 내용은 여기서 수정
save_settings()
KEY = []
for v in KEY_Settings.values():
    KEY.append(v)
# 키 업데이트 하는거 방법 생각해야 함

def screen_change(idx, mode, running): # idx = 어떤 버튼인지
    if idx == 0:
        mode[C.NEXT_SCREEN] = C.PLAYING
    elif idx == 1:
        mode[C.NEXT_SCREEN] = C.SETTING
        mode[C.PREV_SCREEN] = C.START
    elif idx == 2:
        running[0] = False

def on_draw(index):
    for idx, item in enumerate(Button_list):
         
        if idx==index:
            item.above()
        else:
            item.inactive()
            
def on_button(pos):
    for idx, item in enumerate(Button_list): # 마우스가 버튼 위에 놓여 있는가?
        if item.rect.collidepoint(pos):
            return True, idx
    return False, 0

def draw(screen, mode, running):
    for event in pg.event.get():
        mouse_pos = pg.mouse.get_pos()
        flag, index = on_button(mouse_pos)
        if event.type == pg.QUIT: # 종료 버튼을 눌렀는가?
            running[0] = False
            return
        if(flag):
            if event.type == pg.MOUSEBUTTONDOWN:
                Button_list[index].active()
                screen_change(index, mode, running)
            else:
                C.mouse_focus = index
        else: # 마우스가 버튼 위에 있지 않는 경우
            for item in Button_list:
                C.mouse_focus = -1
        if event.type == pg.KEYUP and C.mouse_focus == -1: # 키보드를 눌렀는가?
            for idx, item in enumerate(KEY):
                if event.key == item:
                    if idx==0 or idx==1:
                        if C.POS==0:
                            C.POS=len(Button_list)-1    
                        else:
                            C.POS-=1
                        C.key_focus = C.POS
                        C.mouse_focus=-1
                    elif idx==2 or idx==3:
                        if C.POS==len(Button_list)-1:
                            C.POS=0             
                        else:
                            C.POS+=1
                        C.key_focus = C.POS
                        C.mouse_focus=-1
                    else:
                        screen_change(C.POS, mode, running)
        if C.mouse_focus==-1:
            on_draw(C.key_focus)
        else:
            on_draw(C.mouse_focus)
    screen.fill((255, 255, 255))
    for item in Button_list:
        item.draw(screen)
    for item in Text_list:
        item.draw(screen)
