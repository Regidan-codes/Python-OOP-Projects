class Card:
    SPECIAL_CARDS = {11: 'Jack', 12: 'Queen', 13: 'King', 14: "Ace"}

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def show(self):
        card_value = self._value
        card_suit = self._suit
        suit_symbol = self._suit._description.capitalize()

    def is_special(self):
        return self._value >= 11