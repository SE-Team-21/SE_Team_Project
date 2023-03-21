import pygame as pg
import uno.Draw_Start_Display as Draw_Start_Display
import uno.Draw_Setting_Display as Draw_Setting_Display
import uno.Draw_Playing_Display as Draw_Playing_Display
import uno.Draw_Stop_Display as Draw_Stop_Display
import uno.onstants as C
import uno.KeySettings as K

def uno_mainloop():
    pg.init()
    pg.display.set_caption("UNO Game") # 실행 창 제목
    screen = pg.display.set_mode((800,600))
    K.load_settings()
    for idx in range(5): # load 해온 값으로 설정 창에 있는 버튼 다시 그려주기
        Draw_Setting_Display.Button_list[idx+4].change_text(pg.key.name(K.KEY_Settings[idx])) #Draw_Setting에 있는 Button의 index가 4~8이라서 idx+4해줌
    running = [True]
    mode = [C.START, C.START] # mode[0] = 다음 화면, mode[1] = 이전 화면
    while running[0]:
        if mode[C.NEXT_SCREEN] == C.START:
            Draw_Start_Display.draw(screen, mode, running)
        elif mode[C.NEXT_SCREEN] == C.SETTING:
            Draw_Setting_Display.draw(screen, mode, running)
        elif mode[C.NEXT_SCREEN] == C.PLAYING:
            Draw_Playing_Display.draw(screen, mode, running)
        elif mode[C.NEXT_SCREEN] == C.STOP:
            Draw_Stop_Display.draw(screen, mode, running)
        else:
            pass
        pg.display.update()
    pg.quit()

if __name__ == "__main__":
    uno_mainloop()
