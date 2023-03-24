import pygame as pg
from pygame.locals import *
import os

COLORBLIND_MODE = False
COLORBLIND_COLORS = {
    'red': (255, 100, 100),
    'green': (100, 255, 100),
    'blue': (100, 100, 255),
    'yellow': (255, 255, 100),
}

REGULAR_COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
}

class Display:
    def __init__(self, width, height, title, colorblind_mode=False):
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.colorblind_mode = colorblind_mode

    def draw_card(self, card, x, y):
        card_image = pg.image.load(os.path.join('assets', f'{card}.png'))
        
        self.screen.blit(card_image, (x, y))

    def get_color(self, color_name):
        if self.colorblind_mode:
            return COLORBLIND_COLORS.get(color_name, (255, 255, 255))
        else:
            return REGULAR_COLORS.get(color_name, (255, 255, 255))

    def update_display(self):
        pg.display.update()

    def main_loop(self, game_logic):
        running = True
        while running:
            self.screen.fill((0, 0, 0))

            for event in pg.event.get():
                if event.type == QUIT:
                    running = False

            self.update_display()
            self.clock.tick(60)

        pg.quit()

display = Display(800, 600, 'Uno Game', colorblind_mode=COLORBLIND_MODE)

#이런식으로 대충