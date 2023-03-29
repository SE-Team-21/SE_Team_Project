from uno.game.Card import UnoCard
from uno.game.Game import UnoGame
from uno.game.Player import UnoPlayer
from uno.game.ReversibleCycle import ReversibleCycle
import uno.Constants as C
from itertools import product, repeat, chain

number_of_num_cards = 500
number_of_tech_cards = 500

number_of_total_cards = number_of_num_cards + number_of_tech_cards

num_cards = repeat(['red', 1], number_of_num_cards)
tech_cards = repeat(['black', 'wildcard'], number_of_tech_cards)
all_cards = chain(num_cards, tech_cards)
deck = [UnoCard(color, card_type) for color, card_type in all_cards]
game = UnoGame(2, 50, 500, deck)
print(num_cards)
