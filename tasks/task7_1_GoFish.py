"""
Using your Card and Deck class (and any other classyou care to implement), make a game of Go Fish playable by two human players.
(Obviously, this is not ideal, because the two players will be able to see each others cards! Still, we will push on..)
The rules:
Four cards of the same face value are known as a "book"
Five cards are dealt from a standard 52-card deck to each player. The remaining cards are kept in a pile referred to as the "ocean" or "pool"
The player whose turn it is to play asks another player for his or her cards of a particular face value.
For example Alice may ask, "Bob, do you have any threes?" Alice must have at least one card of the rank she requested.
Bob must hand over all cards of that rank if he has any.
If he has none, Bob tells Alice to "go fish" and Alice draws a card from the pool and places it in her own hand, ending her turn. Then it is the next player's turn
When any player at any time has all four cards of one face value, it forms a book, and the cards must be placed face up in front of that player.
When all sets of cards have been laid down in books, the game ends. The player with the most books wins

If you run out of cards and there are still cards left, you get five free cards.
"""

import task6_deck as d
import asks as ask


def clear(): return os.system('cls')


class Player():

    def __init__(self, name):
        self.__name = name
        self.__cards = []
        self.__table_cards = []

    @property
    def name(self):
        return self.__name

    @property
    def hand_cards_str(self):
        return ' '.join([str(c) for c in self.__cards])

    @property
    def table_cards_str(self):
        return ' '.join([str(c) for c in self.__table_cards])

    @property
    def table_card_count(self):
        return len(self.__table_cards)

    # add cards to players hasds
    def take_card(self, cards):
        if type(cards) is d.Card:
            self.__cards.append(cards)
            return
        for c in cards:
            self.__cards.append(c)

    # return from hands cards of the value
    def give_cards_of_value(self, value):
        ret = [card for card in self.__cards if card.value == value]
        self.__cards = [card for card in self.__cards if card.value != value]
        return ret

    def AskForCard(self):
        v = set()
        for card in self.__cards:
            v.add(card. value)
        print(self.name + "'s hands", self.hand_cards_str)

        return ask.ask_one_othe(v, pre_msg='Ask next player for card:')

    def DoesYouHave(self, value):
        while True:
            yn = ask.ask_yes_no(self.__name + ":Do you have " +
                                value + " in " + self.hand_cards_str)
            v = value in self.__cards
            if (value in self.__cards) == yn:
                return yn
            print(self.name, 'are you sure?')

    def count_table_cards(self):
        return len(self.__table_cards)

    def are_you_a_winner(self):
        for card in self.__cards:
            print(card)
        return ask.ask_yes_no(self.__name + ": Are you a winner?")

    def has_card_on_hands(self):
        return len(self.__cards) > 0

    # checks if player has books,
    # return True, False
    def check_books(self):
        if len(self.__cards) == 0:
            return None
        values = []
        d = {}
        for card in self.__cards:
            if (card.value in d):
                d[card.value] += 1
                if d[card.value] == 4:
                    values.append(card.value)
            else:
                d[card.value] = 1
        new_cards = []
        ret = []
        ret = [card for card in self.__cards if card.value in values]
        new_cards = [card for card in self.__cards if not card.value in values]
        self.__cards = new_cards
        return ret

    def put_on_table(self, cards):
        tmp = self.table_cards_str

        for c in cards:
            self.__table_cards.append(c)
        if (len(tmp) > 0):
            print(self.name, 'place cards on table:',
                  ' '.join([str(c) for c in cards]))
            print(self.name, "'s table looks like:", self.table_cards_str)
        else:
            print(self.name, "put cards on table:", self.table_cards_str)


class GoFishGame():

    def __init__(self, names, given_cards=5):
        if (len(names) > 6):
            raise ValueError('dont play in this game more then 6 players')
        if (len(names) < 2):
            raise ValueError(
                'dont play in this game alone - invite some friends')

        self.__init = False
        self.__players = []
        for name in names:
            self.__players.append(Player(name))

        self.__deck = d.Deck()
        self.__deck.shuffle()
        self.__deck.shuffle()
        self.__deck.shuffle()
        for player in self.__players:
            for x in range(given_cards):
                card = self.__deck.pick_from_top()
                player .take_card(card)
        self.__curr_player = self.__players[0]
        self.__next_player = self.__players[1]

    def start(self):
        self.ask()

    def NextPlayer(self, stack):
        p0 = self.__curr_player
        idx = self.__players.index(p0)
        size = len(self.__players)
        if (idx == (size - 1)):
            p1 = self.__players[0]
            p2 = self.__players[1]
        elif (idx == (size - 2)):
            p1 = self.__players[size - 1]
            p2 = self.__players[0]
        else:
            p1 = self.__players[idx + 1]
            p2 = self.__players[idx + 2]
        self.__curr_player = p1
        stack.append(p2)
        stack.append(p1)
        stack.append(self.ask)

    # end game when deck is emtpy and players has no cards
    def check_game_end(self, stack):
        if not self.__deck.is_empty():
            return False


        for p in self.__players:
            if not p.has_card_on_hands():
                return True

        return False

    def show_table(self):
        for p in self.__players:
            print(p.name, p.table_cards_str)

    def PassCards(self, stack):
        p1 = stack.pop()
        p2 = stack.pop()
        asks = p1.AskForCard()
        cards = p2.take_card(asks)
        p1.add_cards(cards)
        return stack

    def check_books(self, stack):
        p = stack.pop()
        new_books = p.check_books()
        if new_books:
            p.put_on_table(new_books)

        if not p.has_card_on_hands():
            if (self.__deck.is_empty()):
                stack.append(p)
                stack.append(end_game)
                return
            for x in range(5):
                card = self.__deck.pick_from_top()
                p.take_card(card)
                if (self.__deck.is_empty()):
                    break

    def give_card(self, stack):
        p1 = stack.pop()
        p2 = stack.pop()
        card_value = stack.pop()
        cards = p2.give_cards_of_value(card_value)
        p1.take_card(cards)
        print(p2.name + ' sicretly gives card to ' + p1.name)
        stack.append(p1)
        stack.append(self.check_books)

    def take_from_pool(self, stack):
        p1 = stack.pop()
        if (self.__deck.is_empty()):
            print(p.name,'no cards in pool :(')
            return
        card = self.__deck.pick_from_top()
        print(p1.name + ' takes from pool', card,
              '(', len(self.__deck), ' left)')
        p1.take_card(card)
        stack.append(p1)
        stack.append(self.check_books)

    # one players [asks] another player for a [card]
    # if he says Yes move to - pass cards
    # if he say No - move to  - start to

    def ask(self, stack):
        p1 = stack.pop()
        p2 = stack.pop()
        print(p1.name, 'Turn')
        asked_card = p1.AskForCard()
        is_has = p2.DoesYouHave(asked_card)
        if (is_has):
            stack.append(asked_card)
            stack.append(p2)
            stack.append(p1)
            stack.append(self.give_card)
            return stack
        else:
            stack.append(p1)
            stack.append(self.take_from_pool)

    def init(self):
        self.__init = True
        self.__curr_player = self.__players[0]

    def end_game(self, stack):
        p = stack.pop()
        print('End of the game!')

    def find_winner(self):
        players = [p for p in self.__players]
        sorted(players,
               key=lambda player: player.table_card_count, reverse=True)
        print(players[0].name, 'is winner')

    def play(self):
        stack = []
        if not self.__init:
            self.init()

        stack.append(self.__players[1])
        stack.append(self.__players[0])
        stack.append(self.ask)

        while True:
            m = stack.pop()
            m(stack)
            if (len(stack) == 0):
                if (self.check_game_end(stack)):
                    self.find_winner()
                    return
                else:
                    self.NextPlayer(stack)


def main():
    print('wellcome to Go Fish game')
    nbm_p = ask.ask_number("Enter number of player")
    names = [('Player#' + str(x + 1)) for x in range(nbm_p)]
    game = GoFishGame(names)
    game.play()
    print('game end')


def test():
    p1 = Player("1")
    deck = d.Deck()
    p1.take_card(deck.pick_from_top())
    p1.take_card(deck.pick_from_top())
    p1.take_card(deck.pick_from_top())
    p1.take_card(deck.pick_from_top())
    book = p1.check_books()
    assert book[0].value == 'Ace'

    p2 = Player("2")
    book = p2.check_books()
    assert book == None

    names = ['0', '1']
    game = GoFishGame(names)
    game.init()
    stack = []
    game.NextPlayer(stack)
    assert stack[0].name == '0'
    assert stack[1].name == '1'

    stack = []
    game.NextPlayer(stack)
    assert stack[0].name == '1'
    assert stack[1].name == '0'

    # game.find_winner()


test()
main()
