"""
Task 8 - Mean, Median, and Mode (Computed From Scratch)
1) Write a function that, given an arbitrary list of numbers (or a range, or a tuple of numbers) computes the mean.
2) Write a function that, given an arbitrary list of numbers (or a range of numbers, or a tuple of numbers) computes the median.
3) Write a function that, given an arbitrary list of numbers (or a range, or a tuple of numbers) computes the mode.
see docstring below for examples

list1 == [2,3,4]
assert mean(list1) == 3
assert median(list1) == 3
assert mode(list1) == None
list2 == [10,1,4,3,2,10]
assert mean(list2) == 5
assert median(list2) == 3.5
assert mode(list2) == 10
range1 == range(2,5)
assert mean(range1) == 3
assert median(range1) == 3
assert mode(range1) == None
range2 == range(1,101)
assert mean(range2) == 5050
assert median(range2) == 50.5
assert mode(range2) == None
tuple1 == (10,4,6,8,2)
assert mean(tuple1) == 6
assert median(range1) == 6
assert mode(range1) == None
tuple2 == (10,4,6,8,2,10000,4)
assert mean(tuple1) == 1433.4 
assert median(range1) == 6
assert mode(range1) == 4
"""


def mean(l):
    r = 0
    for i in l:
        r += i
    ret = r / len(l)
    return ret


def median(l):
    ls = sorted(l)
    size = len(ls)
    if (size % 2 == 1):
        return ls[(size // 2 + 1) - 1]
    else:
        a = ls[(size // 2) - 1]
        b = ls[(size // 2 + 1) - 1]
        return (a + b) / 2


def mode(l):
    if len(l) == 1:
        return l[0]

    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    k = d.keys()
    v = d.values()
    sv = sorted(v, reverse=True)

    if sv[0] == sv[1]:
        return None

    max_k = 0
    max_v = 0

    for itm in d.items():
        if (max_v < itm[1]):
            max_v = itm[1]
            max_k = itm[0]
    return max_k


list1 = [2, 3, 4]
assert mean(list1) == 3
assert median(list1) == 3
assert mode(list1) == None
list2 = [10, 1, 4, 3, 2, 10]
assert mean(list2) == 5
assert median(list2) == 3.5
assert mode(list2) == 10
range1 = range(2, 5)
assert mean(range1) == 3
assert median(range1) == 3
assert mode(range1) == None
range2 = range(1, 101)
assert mean(range2) == 50.5  # 50
assert median(range2) == 50.5
assert mode(range2) == None
tuple1 = (10, 4, 6, 8, 2)
assert mean(tuple1) == 6
assert median(tuple1) == 6
assert mode(range1) == None
tuple2 = (10, 4, 6, 8, 2, 10000, 4)
assert (mean(tuple2) - 1433.4) <= 0.1
assert median(tuple2) == 6
assert mode(tuple2) == 4

tuple3 = [17]
assert mean(tuple3) == 17
assert median(tuple3) == 17
assert mode(tuple3) == 17
