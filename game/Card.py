from uno.Constants import COLORS, ALL_COLORS, COLOR_CARD_TYPES, BLACK_CARD_TYPES, ARBITRARY_BLACK_CARD_TYPES, ARBITRARY_COLOR_CARD_TYPES

class UnoCard:
    def __init__(self, color, card_type):
        self._validate(color, card_type)
        self.color = color
        self.card_type = card_type
        self.temp_color = None

    def __repr__(self):
        return '<UnoCard object: {} {}>'.format(self.color, self.card_type)

    def __str__(self):
        return '{}{}'.format(self.color_short, self.card_type_short)

    def __eq__(self, other):
        return self.color == other.color and self.card_type == other.card_type

    def _validate(self, color, card_type):
        if color not in ALL_COLORS:
            raise ValueError('Invalid color')
        if color == 'black' and not (card_type in BLACK_CARD_TYPES 
                                 or card_type in ARBITRARY_BLACK_CARD_TYPES):
            raise ValueError('Invalid card type')
        if color != 'black' and not (card_type in COLOR_CARD_TYPES 
                                 or card_type in ARBITRARY_COLOR_CARD_TYPES):
            raise ValueError('Invalid card type')

    @property
    def color_short(self):
        return self.color[0].upper()

    @property
    def card_type_short(self):
        if self.card_type in ('skip', 'reverse', 'wildcard'):
            return self.card_type[0].upper()
        else:
            return self.card_type

    @property
    def _color(self):
        return self.temp_color if self.temp_color else self.color

    @property
    def temp_color(self):
        return self._temp_color

    @temp_color.setter
    def temp_color(self, color):
        if color is not None:
            if color not in COLORS:
                raise ValueError('Invalid color')
        self._temp_color = color

    def playable(self, other):
        return (
            self._color == other.color or
            self.card_type == other.card_type or
            other.color == 'black'
        )
