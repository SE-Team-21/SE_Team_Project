import pygame as pg
from uno.display import Display
from uno.start import Start
from uno.setting import Setting
from uno.pause import Pause
from uno.story import Story
from uno.mode import Mode
from uno.play import Playing
import uno.Constants as C
from uno.KeySettings import Data

def uno_mainloop():
    pg.init()
    pg.display.set_caption("UNO Game") # 실행 창 제목
    Data.load_settings()
    Game = [Start(), Setting(), Playing(), Pause(), Mode(), Story()]
    running = [True]
    while running[0]:
        Game[Display.mode[C.NEXT_SCREEN]-1].main_loop(running)
    pg.quit()

if __name__ == "__main__":
    uno_mainloop()