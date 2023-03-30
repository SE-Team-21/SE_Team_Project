import pygame as pg
import display as D
import uno.Constants as C
from uno.KeySettings import Data

def uno_mainloop():
    pg.init()
    pg.display.set_caption("UNO Game") # 실행 창 제목
    Data.load_settings()
    a = D.Start()
    b = D.Setting()
    c = D.Playing()
    d = D.Pause()
    e = D.Mode()
    f = D.Story()
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
        elif D.Display.mode[C.NEXT_SCREEN] == C.MODE:
            e.main_loop(running)
        elif D.Display.mode[C.NEXT_SCREEN] == C.STORY:
            f.main_loop(running)
    pg.quit()

if __name__ == "__main__":
    uno_mainloop()
