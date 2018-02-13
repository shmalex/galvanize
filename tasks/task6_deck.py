"""
Task #9 for beginning of Monday's class.

Design a Python class called Card, and then  a Python class called Deck that represents a deck of cards.
The cards should have four suits (hearts spades clubs and diamonds) and go from 2 to Ace like normal playing cards.

Make a list of attributes and methods that your Card and Deck classes should have, and implement them as time permits.
"""

import random


class CardException(Exception):
    pass


class Card():
    def __init__(self, suite, value):
        self.__suite = suite
        self.__value = value

    def __eq__(self, card):
        if not (type(card) is Card):
            raise CardException('Only card instances are allowed')
        return self.__suite == card.__suite and self.__value == card.__value

    def __str__(self):
        return f'{self.value} of {self.suite}'

    @property
    def suite(self):
        return self.__suite

    @property
    def value(self):
        return self.__value


class Deck():
    _suites = ['heart', 'spade', 'club', 'diamond']
    _value = ['2', '3', '4', '5', '6', '7', '8',
              '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.__cards = []
        for v in Deck._value:
            for s in Deck._suites:
                self.__cards.append(Card(s, v))

    def __iter__(self):
        if len(self.__cards) == 0:
            return None
        self.current = 0
        return self

    def __next__(self):
        if self.current >= len(self.__cards):
            raise StopIteration()
        else:
            ret = self.__cards[self.current]
            self.current += 1
            return ret

    def __len__(self):
        return len(self.__cards)

    def shuffle(self):
        new_deck = []
        while len(self.__cards) > 0:
            size = len(self) - 1
            x = random.randint(0, size)
            card = self.__cards[x]
            new_deck.append(card)
            self.__cards.remove(card)
        self.__cards = new_deck

    def pick_random(self):
        x = random.randint(0, len(self) - 1)
        card = self.__cards[x]
        self.__cards.remove(card)
        return card


def main():
    dec = Deck()
    print(dec)
    print(len(dec))

    # for card in dec:
    #     print(card.suite, card.value)5
    dec.shuffle()
    for card in dec:
        print(card.suite, card.value)

    card = dec.pick_random()
    print(card)
    print(len(dec))


main()
