import pygame as pg
import uno.Draw_Start_Display as Draw_Start_Display
import uno.Draw_Setting_Display as Draw_Setting_Display
import uno.Draw_Playing_Display as Draw_Playing_Display
import uno.Draw_Stop_Display as Draw_Stop_Display
import uno.Constants as C


def uno_mainloop():
    pg.init()
    pg.display.set_caption("UNO Game")
    screen = pg.display.set_mode((800,600))
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
        pg.time.wait(100)
    pg.quit()

if __name__ == "__main__":
    uno_mainloop()



