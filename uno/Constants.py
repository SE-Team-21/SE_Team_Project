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
MODE = 5
STORY = 6

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
             "blueall+1": CardButton("blueall+1"), 
             "bluereverse": CardButton("bluereverse"), 
             "blueskip": CardButton("blueskip"), 
             "blue+2": CardButton("blue+2"), 
             "red0": CardButton("red0"), 
             "red1": CardButton("red1"), 
             "red2": CardButton("red2"), 
             "red3": CardButton("red3"), 
             "red4": CardButton("red4"), 
             "red5": CardButton("red5"), 
             "red6": CardButton("red6"), 
             "red7": CardButton("red7"), 
             "red8": CardButton("red8"), 
             "red9": CardButton("red9"),
             "redall+1": CardButton("redall+1"), 
             "redreverse": CardButton("redreverse"), 
             "redskip": CardButton("redskip"), 
             "red+2": CardButton("red+2"), 
             "yellow0": CardButton("yellow0"), 
             "yellow1": CardButton("yellow1"), 
             "yellow2": CardButton("yellow2"), 
             "yellow3": CardButton("yellow3"), 
             "yellow4": CardButton("yellow4"), 
             "yellow5": CardButton("yellow5"), 
             "yellow6": CardButton("yellow6"), 
             "yellow7": CardButton("yellow7"), 
             "yellow8": CardButton("yellow8"), 
             "yellow9": CardButton("yellow9"),
             "yellowall+1": CardButton("yellowall+1"), 
             "yellowreverse": CardButton("yellowreverse"), 
             "yellowskip": CardButton("yellowskip"), 
             "yellow+2": CardButton("yellow+2"), 
             "green0": CardButton("green0"), 
             "green1": CardButton("green1"), 
             "green2": CardButton("green2"), 
             "green3": CardButton("green3"), 
             "green4": CardButton("green4"), 
             "green5": CardButton("green5"), 
             "green6": CardButton("green6"), 
             "green7": CardButton("green7"), 
             "green8": CardButton("green8"), 
             "green9": CardButton("green9"),
             "greenall+1": CardButton("greenall+1"), 
             "greenreverse": CardButton("greenreverse"), 
             "greenskip": CardButton("greenskip"), 
             "green+2": CardButton("green+2"), 
             "black+4": CardButton("black+4"), 
             "black+10": CardButton("black+10"), 
             "blackwild": CardButton("blackwild"), 
             "blackwildfuck": CardButton("blackwildfuck"), 
             }
