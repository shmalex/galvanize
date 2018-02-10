
def next(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


c = 10
s = 0
while c != 1:
    c = next(c)
    s += 1


d = {}


def search(x):
    if x == 1:
        return 0
    if x in d:
        return d[x]
    l = search(next(x)) + 1
    d[x] = l
    return l


max = (0, 0)
for i in range(1, 1000001):
    a = search(i)
    if a > max[1]:
        max = (i, a)
print(max)
