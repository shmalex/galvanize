"""
Task #9 for beginning of Monday's class.

Design a Python class called Card, and then  a Python class called Deck that represents a deck of cards.
The cards should have four suits (hearts spades clubs and diamonds) and go from 2 to Ace like normal playing cards.

Make a list of attributes and methods that your Card and Deck classes should have, and implement them as time permits.
"""

import random


class CardException(Exception):
    pass


class DeckEmptyException(Exception):
    pass


class Card():
    SUITS = {
        'heart': '♥',
        'spade': '♠',
        'club': '♣',
        'diamond': '♦'
    }

    RANKS = ['2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suite, value):
        self.__suite = suite
        self.__value = value

    def __eq__(self, card):
        if (type(card) is Card):
            return self.__suite == card.__suite and self.__value == card.__value

        if (type(card) is str):
            if (card in Card.RANKS):
                return self.__value == card
            return self.__suite == card

    def __repr__(self):
        return f"Card('{self.value}', '{self.suite}')"

    def __str__(self):
        h = Card.SUITS[self.__suite]
        return f'{self.value}{h}'

    @property
    def suite(self):
        return self.__suite

    @property
    def value(self):
        return self.__value


class Deck():
    def __init__(self):
        self.__cards = [Card(suite, value)
                        for value in Card.RANKS
                        for suite in Card.SUITS]

    def __iter__(self):
        if len(self.__cards) == 0:
            return None
        self.current = 0
        return self

    def __next__(self):
        if self.current >= len(self.__cards):
            raise StopIteration()

        ret = self.__cards[self.current]
        self.current += 1
        return ret

    def __len__(self):
        return len(self.__cards)

    def __delitem__(self, card_or_index):
        raise NotImplementedError()

    def is_empty(self):
        return len(self.__cards) == 0

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

    def pick_from_top(self):
        if (len(self.__cards) == 0):
            raise DeckEmptyException()
        return self.__cards.pop()


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


if __name__ == '__main__':
    main()
