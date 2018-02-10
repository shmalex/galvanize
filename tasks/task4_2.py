import timer
import random as rn
import threading

response = None
score = [0, 0]
x = 0


def tick(t=5):
    t -= 1
    print(t)


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 1
    return True


assert is_prime(7) == True
assert is_prime(81197) == True
assert is_prime(95191) == True
assert is_prime(95633) == True
assert is_prime(173) == True
assert is_prime(179) == True
assert is_prime(181) == True
assert is_prime(191) == True
assert is_prime(193) == True
assert is_prime(17) == True


def user_input():
    global response
    r = input(f"in 5 seconds tell if {x} is prime? [y/n]? ")
    r = r.strip().lower()
    while(True):
        if (r == 'y'):
            response = True
            break
        elif r == 'n':
            response = False
            break
        else:
            print('Sorry i didn\'t get that')


def propose():
    print(
        'Score [{0} : {1}] \n Would like to play again? y/n'.format(score[0], score[1]))
    while True:
        y = input()
        if (y == 'y'):
            return True
        elif y == 'n':
            return False
        else:
            print('Sorry i didn\'t get that')


timer_id = 0
while True:
    x = rn.randint(0, 1000000)

    # timer_id = timer.set_timer(1000, tick)
    user = threading.Thread(target=user_input)
    user.daemon = True
    user.start()
    user.join(5)
    # timer.kill_timer(timer_id)
    if response is None:
        print('Times out!')
        score[1] += 1
    else:
        if response == is_prime(x):
            print('You are right!')
            score[0] += 1
        else:
            print('Nope!')
            score[1] += 1
    if not propose():
        break