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
MODE = 5

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

# Colorblind Mode
PROTANOPIA_MATRIX = [[0.567, 0.433, 0], [0.558, 0.442, 0], [0, 0.242, 0.758]]
DEUTERANOPIA_MATRIX = [[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.3, 0.7]]
TRITANOPIA_MATRIX = [[0.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, 0.525]]
COLORBLINDMODE_STR = ['  PROTANOPIA', 'DEUTERANOPIA', '   TRITANOPIA']
