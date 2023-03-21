# Color
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 211, 67)
GREEN = (0, 255, 0)
ABOVE_COLOR = (234, 236, 240)
ACTIVE_COLOR = (144, 144, 144)
INACTIVE_COLOR = (215, 215, 215)

# Text and Button Font
FONT = 'arial'

#game
COLORS = ['red', 'yellow', 'green', 'blue']
ALL_COLORS = COLORS + ['black']
NUMBERS = list(range(10)) + list(range(1, 10))
SPECIAL_CARD_TYPES = ['skip', 'reverse', '+2']
COLOR_CARD_TYPES = NUMBERS + SPECIAL_CARD_TYPES * 2
BLACK_CARD_TYPES = ['wildcard', '+4']
ARBITRARY_BLACK_CARD_TYPES = ['wildcard_fuck', 'wildcard+10']
ARBITRARY_COLOR_CARD_TYPES = ['all+1']
CARD_TYPES = NUMBERS + SPECIAL_CARD_TYPES + BLACK_CARD_TYPES

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

#Start Display On Keyboard And Mouse
POS = 0
mouse_focus = -1
key_focus = -1
