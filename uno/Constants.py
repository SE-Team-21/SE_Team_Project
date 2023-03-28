from uno.CardButton_Class import CardButton

# Color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 211, 67)
GREEN = (0, 255, 0)
ABOVE_COLOR = (234, 236, 240)
INACTIVE_COLOR = (215, 215, 215)

# Text and Button Font
FONT = 'arial'

# Game Mode Flag
START = 1
SETTING = 2
PLAYING = 3
STOP = 4  

NEXT_SCREEN = 0
PREV_SCREEN = 1

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
ALL_CARDS = {"blue0": CardButton("blue0"), 
             "blue1": CardButton("blue1"), 
             "blue2": CardButton("blue2"), 
             "blue3": CardButton("blue3"), 
             "blue4": CardButton("blue4"), 
             "blue5": CardButton("blue5"), 
             "blue6": CardButton("blue6"), 
             "blue7": CardButton("blue7"), 
             "blue8": CardButton("blue8"), 
             "blue9": CardButton("blue9"), 
             }
