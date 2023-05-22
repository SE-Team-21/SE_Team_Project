from uno.game.Card import UnoCard

class UnoPlayer:
    def __init__(self, cards, player_id=None):
        if not all(isinstance(card, UnoCard) for card in cards):
            raise ValueError(
                'Invalid player: cards must all be UnoCard objects'
            )
        self.hand = cards
        self.player_id = player_id
        self.uno_state = False
        self.sock = None
        self.name = ""
        self.is_computer = False

    def __repr__(self):
        if self.player_id is not None:
            return '<UnoPlayer object: player {}>'.format(self.player_id)
        else:
            return '<UnoPlayer object>'

    def __str__(self):
        if self.player_id is not None:
            return str(self.player_id)
        else:
            return repr(self)

    def can_play(self, current_card):
        return any(current_card.playable(card) for card in self.hand)

