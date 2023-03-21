from uno.game.AI import AIUnoGame
from uno.game.Card import UnoCard
from uno.game.Game import UnoGame
from uno.game.Player import UnoPlayer
from uno.game.ReversibleCycle import ReversibleCycle
from uno.Constants import COLORS
import random

game = UnoGame(5)

while game.is_active:
    player = game.current_player
    player_id = player.player_id
    if player.can_play(game.current_card):
        for i, card in enumerate(player.hand):
            if game.current_card.playable(card):
                if card.color == 'black':
                    new_color = random.choice(COLORS)
                else:
                    new_color = None
                print("Player {} played {}".format(player, card))
                game.play(player=player_id, card=i, new_color=new_color)
                break
    else:
        print("Player {} picked up".format(player))
        game.play(player=player_id, card=None)
