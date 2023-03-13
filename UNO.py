import pygame as pg

Default_font = 'arial'
screen_width = 800
screen_height = 600
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
ABOVE_COLOR = (234, 236, 240)
ACTIVE_COLOR = (144, 144, 144)
INACTIVE_COLOR = (215, 215, 215)
global screen
screen = pg.display.set_mode((screen_width, screen_height))

class button:
    def __init__(self, pos, size, name, color = BLACK): # pos = 버튼 중앙 좌표, size = (가로, 세로), name = 내용
        self.FONT = pg.font.SysFont(Default_font, 20)
        self.text = self.FONT.render(name, True, color)
        self.text_rect = self.text.get_rect(center=pos)
        self.rect = pg.Rect(0, 0, *size)
        self.rect.center = pos
        self.color = INACTIVE_COLOR
    def draw(self):
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, self.text_rect)
    def above(self):
        self.color = ABOVE_COLOR
    def active(self):
        self.color = ACTIVE_COLOR
    def inactive(self):
        self.color = INACTIVE_COLOR

class Text:
    def __init__(self, pos, size, text, color = BLACK): # pos = 좌상단 모서리 좌표, size = 글씨 크기, text = 내용
        self.FONT = pg.font.SysFont(Default_font, size)
        self.text = self.FONT.render(text, True, color)
        self.pos = pos
    def draw(self):
        screen.blit(self.text, self.pos)


def pygame_mainloop():
    pg.init()
    pg.display.set_caption("UNO Game")
    # Set up the buttons
    start_button = button((400, 200), (100, 50), 'SINGLE PLAYER')
    setting_button = button((400, 300), (100, 50), 'OPTIONS')
    quit_button = button((400, 400), (100, 50), 'QUIT')
    game_name = Text((320, 60), 40, 'UNO Game')
    txt1 = Text((320, 60), 40, 'Display')
    txt2 = Text((320, 120), 40, 'Key Setting')
    txt3 = Text((320, 180), 40, 'color mode')
    txt4 = Text((320, 240), 40, 'Default Options')
    bt1 = button((400, 350), (200, 60), 'Return to Main Menu')
    mode = 1
    global screen
    # Game loop
    running = True
    while running:
        if mode==1:
            for event in pg.event.get():
                mouse_pos = pg.mouse.get_pos()
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    # Check if the mouse click was inside a button
                    if start_button.rect.collidepoint(mouse_pos):
                        start_button.active()
                        print('Single Player')
                    elif setting_button.rect.collidepoint(mouse_pos):
                        setting_button.active()
                        mode=2
                    elif quit_button.rect.collidepoint(mouse_pos):
                        running = False
                elif start_button.rect.collidepoint(mouse_pos):
                    start_button.above()
                elif setting_button.rect.collidepoint(mouse_pos):
                    setting_button.above()
                elif quit_button.rect.collidepoint(mouse_pos):
                    quit_button.above()
                else:
                    start_button.inactive()
                    setting_button.inactive()
                    quit_button.inactive()
            
            # Fill the background color
            screen.fill((255, 255, 255))
            
            # Draw the buttons and text
            start_button.draw()
            setting_button.draw()
            quit_button.draw()
            game_name.draw()
        elif mode==2:
            for event in pg.event.get():
                mouse_pos = pg.mouse.get_pos()
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    # Check if the mouse click was inside a button
                    if bt1.rect.collidepoint(mouse_pos):
                        bt1.active()
                        mode=1
                elif bt1.rect.collidepoint(mouse_pos):
                    bt1.above()
                else:
                    bt1.inactive()    
            
            screen.fill((255, 255, 255))
            txt1.draw()
            txt2.draw()
            txt3.draw()
            txt4.draw()
            bt1.draw()
        else:
            pass
        
        # Update the screen
        pg.display.update()

    # Quit Pygame
    pg.quit()

if __name__ == "__main__":
    pygame_mainloop()