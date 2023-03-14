import pygame as pg
import Draw_Start_Display
import Draw_Setting_Display

def pygame_mainloop():
    pg.init()
    pg.display.set_caption("UNO Game") # 실행 창 제목
    screen_width = 800 # 화면 크기 조절시 변경 바람
    screen_height = 600
    screen = pg.display.set_mode((screen_width, screen_height))
    
    running = [True]
    mode = [1]
    while running[0]:
        if mode[0]==1:
            Draw_Start_Display.draw(screen, mode, running)
        elif mode[0]==2:
            Draw_Setting_Display.draw(screen, mode, running)
        else:
            pass
        pg.display.update()
    pg.quit()

if __name__ == "__main__":
    pygame_mainloop()
