from uno.game.Card import UnoCard
from uno.game.Player import UnoPlayer
from uno.game.ReversibleCycle import ReversibleCycle
from random import shuffle, random
from itertools import product, repeat, chain
from uno.Constants import COLORS, COLOR_CARD_TYPES, BLACK_CARD_TYPES, ARBITRARY_BLACK_CARD_TYPES, ARBITRARY_COLOR_CARD_TYPES, TECH_CARD_TYPES
import copy

class UnoGame:
    def __init__(self, players, probability=-1, init_deal_cnt= 7, unit_test_deck=None, random=True):
        self.tmp = True
        self.init_deal_cnt = init_deal_cnt
        self.probability = probability
        if not isinstance(players, int):
            raise ValueError('Invalid game: players must be integer')
        elif unit_test_deck is None and not 2 <= players <= 15:
            raise ValueError('Invalid game: must be between 2 and 15 players')
        if unit_test_deck is None:
            self.deck = self._create_deck(random)
            print(self.deck[-1 * init_deal_cnt * players - 1].color)
            while self.deck[-1 * init_deal_cnt * players - 1].color == "black":
                self.deck = self._create_deck(random)
                print(self.deck[-1 * init_deal_cnt * players - 1].color)
        else:
            self.deck = unit_test_deck
            self.deck_full = copy.deepcopy(self.deck)

        self.all_card_cnt = len(self.deck_full)
        self.tech_card_cnt = 0
        for i in self.deck_full:
            if any(card_type in str(i.card_type) for card_type in TECH_CARD_TYPES):
                self.tech_card_cnt += 1
        self.num_card_cnt = self.all_card_cnt - self.tech_card_cnt
        if (probability != -1):
            tech = (1 + self.probability / 100) * self.tech_card_cnt
            tot = 1 * self.num_card_cnt + tech
            self.tech_prob = tech / tot
        self.players = [
            UnoPlayer(self._deal_hand(), n) for n in range(players)
        ]
        self._player_cycle = ReversibleCycle(self.players)
        self._current_player = next(self._player_cycle)
        self._winner = None

    def __next__(self):
        self._current_player = next(self._player_cycle)

    def _create_deck(self, random):
        color_cards = product(COLORS, COLOR_CARD_TYPES)
        black_cards = product(repeat('black', 4), BLACK_CARD_TYPES)
        # 임의
        Arbitrary_cards = chain(product(repeat('black', 2), ARBITRARY_BLACK_CARD_TYPES),
                                product(COLORS, ARBITRARY_COLOR_CARD_TYPES))
        all_cards = chain(color_cards, black_cards, Arbitrary_cards)
        deck = [UnoCard(color, card_type) for color, card_type in all_cards]
        self.deck_full = copy.deepcopy(deck)
        if random:
            shuffle(deck)
            return deck
        else:
            return list(reversed(deck))

    def _deal_prob(self, n):
        ret = list()
        for i in range(n):
            if random() <= self.tech_prob:
                for j, card in enumerate(self.deck):
                    if any(card_type in str(card.card_type) for card_type in TECH_CARD_TYPES):
                        ret.append(self.deck.pop(j))
                        break
            else:
                for j, card in enumerate(self.deck):
                    if not any(card_type in str(card.card_type) for card_type in TECH_CARD_TYPES):
                        ret.append(self.deck.pop(j))
                        break
        return ret

    def _deal_hand(self):
        if self.probability == -1:
            return [self.deck.pop() for i in range(self.init_deal_cnt)]
        else:
            return self._deal_prob(self.init_deal_cnt)

    @property
    def current_card(self):
        return self.deck[-1]

    @property
    def is_active(self):
        return all(len(player.hand) > 0 for player in self.players) and self.tmp

    @property
    def current_player(self):
        return self._current_player

    @property
    def winner(self):
        return self._winner

    def play(self, player, card=None, new_color=None):
        if not isinstance(player, int):
            raise ValueError('Invalid player: should be the index number')
        if not 0 <= player < len(self.players):
            raise ValueError('Invalid player: index out of range')
        _player = self.players[player]
        if self.current_player != _player:
            raise ValueError('Invalid player: not their turn')
        if card is None:
            self._pick_up(_player, 1)
            next(self)
            return
        _card = _player.hand[card]
        if not self.current_card.playable(_card):
            raise ValueError(
                'Invalid card: {} not playable on {}'.format(
                    _card, self.current_card
                )
            )
        if _card.color == 'black':
            if new_color not in COLORS:
                raise ValueError(
                    'Invalid new_color: must be red, yellow, green or blue'
                )
        if not self.is_active:
            pass
            #raise ValueError('Game is over')

        played_card = _player.hand.pop(card)
        self.deck.append(played_card)

        card_color = played_card.color
        card_type = played_card.card_type
        if card_color == 'black':
            self.current_card.temp_color = new_color
            if card_type == '+4':
                next(self)
                self._pick_up(self.current_player, 4)
            if card_type == 'wildcard_fuck':
                if random() < 0.05:
                    _player.hand.clear()
                next(self)
            if card_type == 'wildcard+10':
                next(self)
                self._pick_up(self.current_player, 10)
        elif card_type == 'all+1':
            player_now = self.current_player
            for n in self.players:
                next(self)
                if(player_now != self.current_player):
                    self._pick_up(self.current_player, 1)
        elif card_type == 'reverse':
            self._player_cycle.reverse()
        elif card_type == 'skip':
            next(self)
        elif card_type == '+2':
            next(self)
            self._pick_up(self.current_player, 2)

        if self.is_active:
            next(self)
        else:
            self._winner = _player
            self._print_winner()

    def _print_winner(self):
        if self.winner.player_id:
            winner_name = self.winner.player_id
        else:
            winner_name = self.players.index(self.winner)
        print("Player {} wins!".format(winner_name))
        self.tmp = True

    def _pick_up(self, player, n):
        player.uno_state = False
        if self.probability == -1:
            penalty_cards = [self.deck.pop(0) for i in range(n)]
            player.hand.extend(penalty_cards)
        else:
            penalty_cards = self._deal_prob(self.init_deal_cnt)
            player.hand.extend(penalty_cards)
            

