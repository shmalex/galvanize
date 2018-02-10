import random as rn
from enum import Enum, unique, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(name, start, count, last_values)
        return count  # fot no reason


@unique
class GameDict(AutoName):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            if self.value == other.value:
                return False
            if self.value == 0:
                return other.value == 1
            if self. value == 1:
                return other.value == 2
            if self.value == 2:
                return other.value == 0
        return NotImplemented


# self test
assert GameDict.PAPER < GameDict.SCISSORS
assert GameDict.ROCK > GameDict.SCISSORS
assert GameDict.ROCK < GameDict.PAPER

print(GameDict(0))
score = [0, 0, 0]


game_dict = {
    '0': 'Rock',
    '1': 'Paper',
    '2': 'Scissors'
}

game_inv_dict = {
    'Rock': '0',
    'Paper': '1',
    'Scissors': '2'
}


def lose(a, b):
    score[1] += 1
    print("Sorry you lost :( {0} beats {1}".format(a, b))


def win(a, b):
    score[0] += 1
    print("you win! :) {0} beats {1}".format(a, b))


def draw(a, b):
    score[2] += 1
    print("we both are lucky the {0} is {1}".format(a, b))


case_dict = {
    '00': draw,
    '01': lose,
    '02': win,
    '10': win,
    '11': draw,
    '12': lose,
    '20': lose,
    '21': win,
    '22': draw
}


def show(a, b):
    print("Player's {0} vs AI's {1}".format(a, b))


def validate(inp):
    if len(inp) == 1 and (inp in ['0', '1', '2']):
        return GameDict(int(inp))
    print('Possible inputs are 0:Rock, 1:Papar, 2:Scissors.')
    return None


def propose():
    print('Score [{0} : {1}] draw {2} \n Would like to play again? y/n'.format(
        score[0], score[1], score[2]))
    while True:
        y = input()
        if (y == 'y'):
            return True
        elif y == 'n':
            return False
        else:
            print('Sorry i didn\'t get that')


def game(p):
    ai = (rn.random() * 3) // 1
    ai = GameDict(ai)
    show(ai, p)
    if (ai == p):
        draw(ai, p)
    elif ai < p:
        lose(ai, p)
    else:
        win(ai, p)


while True:
    validate('')
    inp = input()
    valid = validate(inp)
    if valid == None:
        continue
    game(valid)
    if (not propose()):
        break