import os
from random import randrange


pl1_score = 0
pl2_score = 0
draw = 0
marker = 1
markers = ['x', 'o']
ZERO = ' o'
X = ' x'
score = [0, 0, 0]
size = [3, 3]
with_ai = False  # 0 players, 1 with AI


def clear(): pass
#def clear(): return os.system('cls')

def game(size):
    players_are_interested = True
    board = make_board(size[0], size[1])
    tos = 0
    while players_are_interested:
        print_score(score, tos)
        print_board(board)
        mover = tos % 2
        while not make_move(board, mover):
            print('nope')
            continue

        winner = check_win(board)
        tos = tos + 1
        can_move = tos != (size[0] * size[1])
        if (winner or not can_move):
            keep_score(mover if winner else 2)
            clear()
            print_score(score, tos)
            print_board(board)
            players_are_interested = exit_or_not(score)
            if(not players_are_interested):
                with_ai = choose_or_die()
                players_are_interested = True
            board = make_board(size[0], size[1])
            tos = 0
            continue
        clear()


def make_move(board, marker):
    print(f'makers {marker}')
    if with_ai and marker % 2 == 1:
        x = randrange(size[0])
        y = randrange(size[1])
        inp = str(x) + str(y)
    else:
        inp = input('make move')  # .split(' ')

    if (len(inp) != 2):
        print('nope len')
        return False
    try:
        x = inp[0]
        y = inp[1]
        x = int(x)
        y = int(y)
    except:
        print(f'nope parse {inp}')
        return False

    if x > size[0] or y > size[1]:
        print('nope (outside)')
        return False
    if board[x][y] == X or board[x][y] == ZERO:
        print('nope ')
        return False
    print(f' x:{x} y:{y}')
    board[x][y] = X if marker == 1 else ZERO
    return True


def keep_score(p_i):
    global score
    score[p_i] += 1


def print_score(score, t):
    w = score[0]
    r = score[1]
    z = score[2]
    print(f'Plr#1 \t{w}\tPlr#2 \t{r}\nDraw\t{z}\tTos\t{t}')


def print_board(board):
    p = ' '
    for x in range(len(board)):
        p += '  ' + str(x)

    print(p)
    x = 0
    for rows in board:
        out = ''
        for i in rows:
            out += ' ' + i
        print(str(x) + out)
        x += 1


def exit_or_not(score):
    cont = input('do you want to continue:[y/n]')
    if cont == 'y':
        return True
    if cont == 'n':
        print("Fine fuck you we didn't want you to play our game anyway asshole")
        return False


def check_win(board):
    print(f'check win{board}')
    # check rows
    for x in board:
        y = x[0]
        p = [i for i in x if i == y]
        if (len(p) == len(x)):
            print(f'rows {y}')
            return y

    size = len(board)
    # check colums
    for x in range(size):
        s = board[0][x]
        c = 0
        for y in range(size):
            if s == board[y][x]:
                c += 1
        if c == size and s != '_':
            print(f'columns c:{c} x:{x}')
            return c

    # check dia/glna
    s = board[0][0]
    c = 0
    for x in range(size):
        if s == board[x][x]:
            c += 1
    if c == size and s != '_':
        print(f'dia/glnac :{c}')

        return s

    # check rl diagnal
    s = board[0][size - 1]
    c = 0
    for x in range(size):
        if s == board[x][size - x - 1]:
            c += 1
    if c == size and s != '_':
        print(f'dia/glnac :{c}')

        return s
    return False


def make_board(x=3, y=3):
    if not x % y == 0:
        print('Make your board a square or rectangle asshole')
        return None
    board = []
    print(x, y)
    for xi in range(x):
        row = []
        for yi in range(y):
            row.append(str(xi) + str(yi))
        board.append(row)
    return board


def choose_or_die():
    global with_ai
    cont = input('do you play with AI:[y/n]')
    if cont == 'y':
        return True
    if cont == 'n':
        print("Fine!")
        return False


clear()
print('Do you want to play the game?!')
print('Tic-Tac-Toy by Directory Alexei Matusevski and some other guy:')
with_ai = choose_or_die()
game(size)
