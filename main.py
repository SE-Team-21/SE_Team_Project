import pygame as pg
from uno.display import Display
from uno.start import Start
from uno.setting import Setting
from uno.pause import Pause
from uno.story import Story
from uno.mode import Mode
from uno.play import Playing
from uno.multi import Multi
from uno.achievement import Achievement
import uno.Constants as C
from uno.KeySettings import Data
from datetime import datetime

def uno_mainloop():
    pg.init()
    pg.display.set_caption("UNO Game") # 실행 창 제목
    Game = [Start(), Setting(), Playing(), Pause(), Mode(), Story(), Achievement(), Multi()]
    running = [True]
    print(Data.data.__dict__)
    #print(datetime.now().date().strftime('%Y-%m-%d'))
    while running[0]:
        Data.data.save_djqwjr(8)
        Data.data.save_djqwjr_date(8)
        Game[Display.mode[C.NEXT_SCREEN]-1].main_loop(running)
        #Game[7].main_loop(running)
        if C.IS_GAME_END:
            Game[2] = Playing()
            C.IS_GAME_END = False
    pg.quit()

if __name__ == "__main__":
    uno_mainloop()