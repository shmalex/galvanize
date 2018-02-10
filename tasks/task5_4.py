import random
import math
import threading
import os
import sys
from multiprocessing import Process, Value, Array, Pool
from threading import Thread
from time import sleep


rnd = random.SystemRandom()


def GenString(size):
    ret = ''
    for i in range(0, size):
        ret += rnd.choice('abcdefghijklmnopqrstuvwxyz ')
    return ret


def scoreNum(a, b):
    if len(a) != len(b):
        raise ValueError('string should be equal length')
    d = dict(zip(a, b))
    ret = 0
    for x, y in d.items():
        if x == y:
            ret += 1
    return ret


def score(a, b):
    if len(a) != len(b):
        raise ValueError('string should be equal length')
    d = dict(zip(a, b))
    ret = 1
    for x, y in d.items():
        ret *= ord(x) / ord(y)
    return ret


def max(target, max_tries, max_sc, t_id, sync):
    print(t_id + ' started')
    target = target.lower()
    size = len(target)
    print(size)
    best_score = 0
    best_str = ''
    for i in range(max_tries):
        gen_str = GenString(size)
        score = scoreNum(target, gen_str)
        if (best_score < score):
            print((t_id + ' ' + gen_str + ' ' + str(score) + ' ' + str(i) + '\r'))
            best_score = score
            best_str = gen_str
            if (best_score == size):
                print(t_id + ' ' + str(i) + ' found!!!')
                max_sc.value = best_score
                break

        if (i % sync == 0):
            if max_sc.value < best_score:
                print(t_id + ' beaten best ' +
                      str(max_sc.value) + '<' + str(best_score)+' ' + str(i))
                max_sc.value = best_score
            else:
                if max_sc.value == size:
                    print(t_id + ' some one else found :( ' + str(i))
                    return
    if best_score != size:
        print(t_id + ' gave up with\n ')


max_score = Value('i', 0)
ps = []
ps_tostart = 5
target_string = 'helol'
max_tries = int(math.pow(10, 9))
sync_mod = 10000

if __name__ == '__main__':
    for x in range(ps_tostart):
        p = Process(
            target=max,
            args=(target_string, max_tries, max_score, str(x), sync_mod))
        ps.append(p)
        p.start()

for x in ps:
    x.join()