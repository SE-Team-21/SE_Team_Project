from uno.CardButton_Class import CardButton

# Color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
blue = (0, 0, 255)
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
ALL_CARDS = {"blue0": CardButton("blue0", "blue", "0"), 
             "blue1": CardButton("blue1", "blue", "1"), 
             "blue2": CardButton("blue2", "blue", "2"), 
             "blue3": CardButton("blue3", "blue", "3"), 
             "blue4": CardButton("blue4", "blue", "4"), 
             "blue5": CardButton("blue5", "blue", "5"), 
             "blue6": CardButton("blue6", "blue", "6"), 
             "blue7": CardButton("blue7", "blue", "7"), 
             "blue8": CardButton("blue8", "blue", "8"), 
             "blue9": CardButton("blue9", "blue", "9"),
             "blueall+1": CardButton("blueall+1","blue","all+1"), 
             "bluereverse": CardButton("bluereverse","blue","reverse"), 
             "blueskip": CardButton("blueskip","blue","skip"), 
             "blue+2": CardButton("blue+2","blue","+2"), 
             "red0": CardButton("red0","red", "0"), 
             "red1": CardButton("red1","red", "1"), 
             "red2": CardButton("red2","red", "2"), 
             "red3": CardButton("red3","red", "3"), 
             "red4": CardButton("red4","red", "4"), 
             "red5": CardButton("red5","red", "5"), 
             "red6": CardButton("red6","red", "6"), 
             "red7": CardButton("red7","red", "7"), 
             "red8": CardButton("red8","red", "8"), 
             "red9": CardButton("red9","red", "9"),
             "redall+1": CardButton("redall+1","red", "all+1"), 
             "redreverse": CardButton("redreverse","red", "reverse"), 
             "redskip": CardButton("redskip","red", "skip"), 
             "red+2": CardButton("red+2","red", "+2"), 
             "yellow0": CardButton("yellow0","yellow", "0"), 
             "yellow1": CardButton("yellow1","yellow", "1"), 
             "yellow2": CardButton("yellow2","yellow", "2"), 
             "yellow3": CardButton("yellow3","yellow", "3"), 
             "yellow4": CardButton("yellow4","yellow", "4"), 
             "yellow5": CardButton("yellow5","yellow", "5"), 
             "yellow6": CardButton("yellow6","yellow", "6"), 
             "yellow7": CardButton("yellow7","yellow", "7"), 
             "yellow8": CardButton("yellow8","yellow", "8"), 
             "yellow9": CardButton("yellow9","yellow", "9"),
             "yellowall+1": CardButton("yellowall+1","yellow", "all+1"), 
             "yellowreverse": CardButton("yellowreverse","yellow", "reverse"), 
             "yellowskip": CardButton("yellowskip","yellow", "skip"), 
             "yellow+2": CardButton("yellow+2","yellow", "+2"), 
             "green0": CardButton("green0","green", "0"), 
             "green1": CardButton("green1","green", "1"), 
             "green2": CardButton("green2","green", "2"), 
             "green3": CardButton("green3","green", "3"), 
             "green4": CardButton("green4","green", "4"), 
             "green5": CardButton("green5","green", "5"), 
             "green6": CardButton("green6","green", "6"), 
             "green7": CardButton("green7","green", "7"), 
             "green8": CardButton("green8","green", "8"), 
             "green9": CardButton("green9","green", "9"),
             "greenall+1": CardButton("greenall+1","green", "all+1"), 
             "greenreverse": CardButton("greenreverse","green", "reverse"), 
             "greenskip": CardButton("greenskip","green", "skip"), 
             "green+2": CardButton("green+2","green", "+2"), 
             "black+4": CardButton("black+4","black", "+4"), 
             #"black+10": CardButton("black+10"), 
             "blackwildcard": CardButton("blackwildcard","black", "wildcard"), 
             "blackwildcard_fuck": CardButton("blackwildcard_fuck","black", "wildcard_fuck"), 
             "blackwildcard+10": CardButton("blackwildcard+10","black", "wildcard+10"),
             "Back": CardButton("Back","Ba", "ck"),
             }
