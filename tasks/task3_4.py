import os
import random as rn


def clear(): return os.system('cls')


lines = [x.replace('\n', '') for x in tuple(open('words.txt', 'r'))]

clear()
words = lines
char_set = set()
word = ''
word_set = set(word)
word_len = len(word)
trie = 6
score = [0, 0]


def reset():
    x = rn.randint(0, len(words) - 1)
    global word, trie, char_set, word_set, word_len
    word = words[x]
    char_set = set()
    word_set = set(word)
    word_len = len(word)
    trie = 6


reset()


def propose():
    print('Score [{0} : {1}]\n Would like to play again? y/n'.format(
        score[0], score[1]))
    while True:
        y = input()
        if (y == 'y'):
            return True
        elif y == 'n':
            return False
        else:
            print('Sorry i didn\'t get that')


def ask_for_letter():
    print("Enter letter?")
    while True:
        c = input()
        if (len(c) > 0):
            break

    if c in char_set:
        print('you allready tried that letter')
    else:
        char_set.add(c)
    return c


def check(c):
    if (c not in word_set):
        global trie
        trie -= 1
    if (char_set & word_set) == word_set:
        return True
    return False


def print_word():
    print('You tried: ' + ''.join([(c + ' ') for c in char_set][::-1]))
    print('Tries left:',  trie)
    print(
        ''.join([(c + ' ') if c in char_set else chr(167) + ' ' for c in word]))


print('wellcome to hang man')
print_word()

while True:
    c = ask_for_letter()
    if check(c):
        clear()
        print('You win')
        print_word()
        score[0] += 1
        if (not propose()):
            break
        else:
            reset()
    if trie == 0:
        print('You dead')
        score[1] += 1
        if (not propose()):
            break
        else:
            reset()
    clear()
    print_word()
