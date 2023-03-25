import pygame as pg
import display as D
import uno.Constants as C
import uno.KeySettings as K

def uno_mainloop():
    pg.init()
    pg.display.set_caption("UNO Game") # 실행 창 제목
    K.load_settings()
    a = D.Start()
    b = D.Setting()
    c = D.Playing()
    d = D.Pause()
    for idx in range(5): # load 해온 값으로 설정 창에 있는 버튼 다시 그려주기
        b.Button_list[idx+4].change_text(pg.key.name(K.KEY_Settings[idx])) #Draw_Setting에 있는 Button의 index가 4~8이라서 idx+4해줌
    running = [True]
    while running[0]:
        if D.Display.mode[C.NEXT_SCREEN] == C.START:
            a.main_loop(running)
        elif D.Display.mode[C.NEXT_SCREEN] == C.SETTING:
            b.main_loop(running)
        elif D.Display.mode[C.NEXT_SCREEN] == C.PLAYING:
            c.main_loop(running)
        elif D.Display.mode[C.NEXT_SCREEN] == C.STOP:
            d.main_loop(running)
    pg.quit()

if __name__ == "__main__":
    uno_mainloop()
