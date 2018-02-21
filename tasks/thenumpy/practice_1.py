"""
    Day 9 
"""
# from . import

import numpy as np

a = np.arange(25)

print(a)

c = a.reshape(5, 5)

print(c)

mask2 = (a % 3) == 0
print(mask2)
print(a[mask2])

b = np.arange(-2, 7.4, 0.17)

print(b.shape)
print(b)

e = np.empty(10, dtype='float32')
print(e)


a = np.array([[1, 2, 3], [4, 5, 600]])

%timeit a.sum()
print(a.sum())

print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=-1))
print(a.shape)

dir(a)


def func():
    """Return a new matrix of given shape and type, without initializing entries.
    Parameters
    ----------
    shape : int or tuple of int
        Shape of the empty matrix.
    dtype : data-type, optional
        Desired output data-type.
    order : {'C', 'F'}, optional
        Whether to store multi-dimensional data in row-major
        (C-style) or column-major (Fortran-style) order in
        memory.
    See Also
    --------
    empty_like, zeros
    Notes
    -----
    `empty`, unlike `zeros`, does not set the matrix values to zero,
    and may therefore be marginally faster.  On the other hand, it requires
    the user to manually set all the values in the array, and should be
    used with caution.
    Examples
    --------
    >>> import numpy.matlib
    >>> np.matlib.empty((2, 2))    # filled with random data
    matrix([[  6.76425276e-320,   9.79033856e-307],
            [  7.39337286e-309,   3.22135945e-309]])        #random
    >>> np.matlib.empty((2, 2), dtype=int)
    matrix([[ 6600475,        0],
            [ 6586976, 22740995]])                          #random
    """
    return 0


# sinstance()

multiarray.

.copyto(a, 1, casting='unsafe')
