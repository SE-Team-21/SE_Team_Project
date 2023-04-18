import pygame as pg

# Color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 211, 67)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
ABOVE_COLOR = (234, 236, 240)
INACTIVE_COLOR = (215, 215, 215)

# Text and Button Font
FONT = 'arial'

# Game Mode Flag
START = 1
SETTING = 2
PLAYING = 3
STOP = 4  
MODE = 5
STORY = 6
IS_GAME_END = False
NEXT_SCREEN = 0
PREV_SCREEN = 1
game_mode = 0
# Default Size of Button and Text
DEFAULT_SIZE = 20

# Object Size Control
WEIGHT = [1, 1.1, 1.2]

# Display Size
DISPLAY_SIZE = [(800, 600), (880, 660), (960, 720)]
DISPLAY_SIZE_STR = ['800x600', '880x660', '960x720']

# game
COLORS = ['red', 'yellow', 'green', 'blue']
ALL_COLORS = COLORS + ['black']
NUMBERS = list(range(10)) + list(range(1, 10))
SPECIAL_CARD_TYPES = ['skip', 'reverse', '+2']
COLOR_CARD_TYPES = NUMBERS + SPECIAL_CARD_TYPES * 2
BLACK_CARD_TYPES = ['wildcard', '+4']
ARBITRARY_BLACK_CARD_TYPES = ['wildcard_fuck', 'wildcard+10']
ARBITRARY_COLOR_CARD_TYPES = ['all+1']
CARD_TYPES = NUMBERS + SPECIAL_CARD_TYPES + BLACK_CARD_TYPES
TECH_CARD_TYPES = SPECIAL_CARD_TYPES + BLACK_CARD_TYPES + ARBITRARY_BLACK_CARD_TYPES + ARBITRARY_COLOR_CARD_TYPES

# Colorblind Mode
PROTANOPIA_MATRIX = [[0.45, 0.35, 0.20], [0.43, 0.35, 0.22], [0.01, 0.40, 0.59]]
DEUTERANOPIA_MATRIX = [[0.55, 0.30, 0.15], [0.65, 0.25, 0.10], [0.01, 0.25, 0.74]]
TRITANOPIA_MATRIX = [[0.96, 0.04, 0], [0, 0.73, 0.27], [0, 0.13,  0.87]]
COLORBLINDMODE_STR = ['  PROTANOPIA', 'DEUTERANOPIA', '   TRITANOPIA']

# Card List 
ALL_CARDS = {"blue0": pg.image.load("./assets/images/blue0.png"),
             "blue1": pg.image.load("./assets/images/blue1.png"),
             "blue2": pg.image.load("./assets/images/blue2.png"),
             "blue3": pg.image.load("./assets/images/blue3.png"),
             "blue4": pg.image.load("./assets/images/blue4.png"),
             "blue5": pg.image.load("./assets/images/blue5.png"),
             "blue6": pg.image.load("./assets/images/blue6.png"),
             "blue7": pg.image.load("./assets/images/blue7.png"),
             "blue8": pg.image.load("./assets/images/blue8.png"),
             "blue9": pg.image.load("./assets/images/blue9.png"),
             "blueall+1": pg.image.load("./assets/images/blueall+1.png"),
             "bluereverse": pg.image.load("./assets/images/bluereverse.png"),
             "blueskip": pg.image.load("./assets/images/blueskip.png"),
             "blue+2": pg.image.load("./assets/images/blue+2.png"),
             "red0": pg.image.load("./assets/images/red0.png"),
             "red1": pg.image.load("./assets/images/red1.png"),
             "red2": pg.image.load("./assets/images/red2.png"),
             "red3": pg.image.load("./assets/images/red3.png"),
             "red4": pg.image.load("./assets/images/red4.png"),
             "red5": pg.image.load("./assets/images/red5.png"),
             "red6": pg.image.load("./assets/images/red6.png"),
             "red7": pg.image.load("./assets/images/red7.png"),
             "red8": pg.image.load("./assets/images/red8.png"),
             "red9": pg.image.load("./assets/images/red9.png"),
             "redall+1": pg.image.load("./assets/images/redall+1.png"),
             "redreverse": pg.image.load("./assets/images/redreverse.png"),
             "redskip": pg.image.load("./assets/images/redskip.png"),
             "red+2": pg.image.load("./assets/images/red+2.png"),
             "yellow0": pg.image.load("./assets/images/yellow0.png"),
             "yellow1": pg.image.load("./assets/images/yellow1.png"),
             "yellow2": pg.image.load("./assets/images/yellow2.png"),
             "yellow3": pg.image.load("./assets/images/yellow3.png"),
             "yellow4": pg.image.load("./assets/images/yellow4.png"),
             "yellow5": pg.image.load("./assets/images/yellow5.png"),
             "yellow6": pg.image.load("./assets/images/yellow6.png"),
             "yellow7": pg.image.load("./assets/images/yellow7.png"),
             "yellow8": pg.image.load("./assets/images/yellow8.png"),
             "yellow9": pg.image.load("./assets/images/yellow9.png"),
             "yellowall+1": pg.image.load("./assets/images/yellowall+1.png"),
             "yellowreverse": pg.image.load("./assets/images/yellowreverse.png"),
             "yellowskip": pg.image.load("./assets/images/yellowskip.png"),
             "yellow+2": pg.image.load("./assets/images/yellow+2.png"),
             "green0": pg.image.load("./assets/images/green0.png"),
             "green1": pg.image.load("./assets/images/green1.png"),
             "green2": pg.image.load("./assets/images/green2.png"),
             "green3": pg.image.load("./assets/images/green3.png"),
             "green4": pg.image.load("./assets/images/green4.png"),
             "green5": pg.image.load("./assets/images/green5.png"),
             "green6": pg.image.load("./assets/images/green6.png"),
             "green7": pg.image.load("./assets/images/green7.png"),
             "green8": pg.image.load("./assets/images/green8.png"),
             "green9": pg.image.load("./assets/images/green9.png"),
             "greenall+1": pg.image.load("./assets/images/greenall+1.png"),
             "greenreverse": pg.image.load("./assets/images/greenreverse.png"),
             "greenskip": pg.image.load("./assets/images/greenskip.png"),
             "green+2": pg.image.load("./assets/images/green+2.png"),
             "black+4": pg.image.load("./assets/images/black+4.png"),
             "blackwildcard": pg.image.load("./assets/images/blackwildcard.png"),
             "blackwildcard_fuck": pg.image.load("./assets/images/blackwildcard_fuck.png"),
             "blackwildcard+10": pg.image.load("./assets/images/blackwildcard+10.png"),
             "Back": pg.image.load("./assets/images/Back.png"),
             }
