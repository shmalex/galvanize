import random as rn

score = [0, 0, 0]

game_dict = {
    '0': 'Rock',
    '1': 'Paper',
    '2': 'Scissors'
}

game_inv_dict = {
    'Rock': '0',
    'Paper': '1',
    'Scissors': '2',
    '0': '0',
    '1': '1',
    '2': '2'
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
    cap_str = str(inp).capitalize()
    if(cap_str in game_inv_dict):
        return game_inv_dict[cap_str]
    print('Possible inputs are Rock,0,Papar,1,Scissors,2.')
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
    ai, case = str(ai)[0], str(p) + str(ai)[0]
    ai_p = game_dict[ai]
    p_p = game_dict[p]
    show(ai_p, p_p)
    case_dict[case](ai_p, p_p)


while True:
    validate('')
    inp = input()
    valid = validate(inp)
    if valid == None:
        continue
    game(valid)
    if (not propose()):
        break
