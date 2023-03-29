from uno.game.Card import UnoCard
from uno.game.Game import UnoGame
from uno.game.Player import UnoPlayer
from uno.game.ReversibleCycle import ReversibleCycle
import uno.Constants as C
from random import shuffle, random
from itertools import product, repeat, chain

number_of_num_cards = 500
number_of_skill_cards = 500
skill_cards_deal_W = 50

number_of_total_cards = number_of_num_cards + number_of_skill_cards

num_cards = repeat(['red', 1], number_of_num_cards)
skill_cards = repeat(['black', 'wildcard'], number_of_skill_cards)
all_cards = chain(num_cards, skill_cards)
deck = [UnoCard(color, card_type) for color, card_type in all_cards]
shuffle(deck)

game = UnoGame(1, skill_cards_deal_W, 10, deck)
print(game.players[0].hand)