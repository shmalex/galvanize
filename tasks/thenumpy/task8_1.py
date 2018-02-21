import numpy as np
import time
import sys

SIZE = 10000000


r1 = [1, 2, 3, 4, 5, 6]
r2 = [2, 3, 4, 5, 6, 2]
ar = np.array([r1, r2], dtype=type(int))
l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# python list
start = time.time()
result = [(x + y) for x, y in zip(l1, l2)]
print("python list took:", (time.time() - start) * 1000)

start = time.time()
result = a1 + a2
print("numpy list took:", (time.time() - start) * 1000)

print(ar[0, 0])
print(ar)
print(ar.dtype)
