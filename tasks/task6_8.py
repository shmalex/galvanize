"""
Task 8 - Mean, Median, and Mode (Computed From Scratch)
1) Write a function that, given an arbitrary list of numbers (or a range, or a tuple of numbers) computes the mean.
2) Write a function that, given an arbitrary list of numbers (or a range of numbers, or a tuple of numbers) computes the median.
3) Write a function that, given an arbitrary list of numbers (or a range, or a tuple of numbers) computes the mode.
4) MAKE A CLASS that has the exact same methods as the functions described above.
see docstring below for examples
list1 = [2,3,4]
>>> mean(list1) = 3
>>> median(list1) = 3
>>> mode(list1) = None
list2 = [10,1,4,3,2,10]
>>> mean(list2) = 5
>>> median(list2) = 3.5
>>> mode(list2) = 10
range1 = range(2,5)
>>> mean(range1) = 3
>>> median(range1) = 3
>>> mode(range1) = None
range2 = range(1,101)
>>> mean(range2) = 50.5
>>> median(range2) = 50.5
>>> mode(range2) = None
tuple1 = (10,4,6,8,2)
>>> mean(tuple1) = 6
>>> median(range1) = 6
>>> mode(range1) = None
tuple2 = (10,4,6,8,2,10000,4)
>>> mean(tuple1) = 1433.4
>>> median(range1) = 6
>>> mode(range1) = 4
***One way that #4 could be done
(mean, median, mode as a class)***
class StatsInfo():
    def __init__(self,iterable=None):
        self.interable = iterable
        self.mean_ = None
        self.median_ = None
        self.mode_ = None
        self.std_ = None

    def fit(self):
        ''' compute all statistics '''
        self.mean()
        self.median()

        pass
    def mean(self):
        self.mean_ = #calculated value
        return self.mean_

    def median(self)
        self.median_ = #calculated value

    etc..

Usage:
nums = [1,3,5,7,8,11]
stats = StatsInfo(nums) # makes a new object
stats.fit() # calculates mean, median, and mode
"""
import math


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


class StatsInfo():
    def __init__(self, iterable=None):
        self.interable = iterable
        self.mean_ = None
        self.median_ = None
        self.mode_ = None
        self.std_ = None
        self.normalized_ = None
        self.__fitted = False

    def fit(self):
        ''' compute all statistics '''
        self.mean()
        self.median()
        self.std()
        pass

    def mean(self):
        if (self.mean_ != None):
            return self.mean_
        r = 0
        for i in self.interable:
            r += i
        self.mean_ = r / len(self.interable)
        return self.mean_

    def mode(self):
        if self.mode_ != None:
            return self.mode_

        l = self.interable
        if len(l) == 1:
            self.mode_ = l[0]
            return self.mode_

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
        self.mode_ = max_k

    def median(self):
        if (self.median_ != None):
            return self.median_

        l = self.interable
        ls = sorted(l)
        size = len(ls)
        if (size % 2 == 1):
            result = ls[(size // 2 + 1) - 1]
        else:
            a = ls[(size // 2) - 1]
            b = ls[(size // 2 + 1) - 1]
            result = (a + b) / 2
        self.median_ = result
        return self.median_

    def std(self):
        if (self.mean_ == None):
            self.mean_ = self.mean()

        if (self.std_ != None):
            return self.std_

        l = self.interable
        count = len(l)
        ret = 0
        for x in l:
            r += (x - mean) ^ 2
        variance = r / l
        std = math.sqrt(variance)
        self.std_ = std
        self.variance_ = variance
        return self.std_

    def variance(self):
        if(self.variance_ != None):
            return self.variance_
        self.std()
        return self.variance_


list1 = [2, 3, 4]
si = StatsInfo(list1)
assert mean(list1) == si.mean()
assert median(list1) == si.median()
assert mode(list1) == si.mode()

list2 = [10, 1, 4, 3, 2, 10]
si = StatsInfo(list2)
assert mean(list2) == si.mean()
assert median(list2) == si.median()
assert mode(list2) == si.mode()

range1 = range(2, 5)
si = StatsInfo(range1)
assert mean(range1) == si.mean()
assert median(range1) == si.median()
assert mode(range1) == si.mode()

range2 = range(1, 101)
si = StatsInfo(range2)
assert mean(range2) == si.mean()
assert median(range2) == si.median()
assert mode(range2) == si.mode()

tuple1 = (10, 4, 6, 8, 2)
si = StatsInfo(tuple1)
assert mean(tuple1) == si.mean()
assert median(tuple1) == si.median()
assert mode(tuple1) == si.mode()

tuple2 = (10, 4, 6, 8, 2, 10000, 4)
si = StatsInfo(tuple2)
assert (si.mean() - 1433.4) <= 0.1
assert median(tuple2) == si.median()
assert mode(tuple2) == si.mode()

tuple3 = [17]
si = StatsInfo(tuple3)
assert mean(tuple3) == si.mean()
assert median(tuple3) == si.median()
assert mode(tuple3) == si.mode()
