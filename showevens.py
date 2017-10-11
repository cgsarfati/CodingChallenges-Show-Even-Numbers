"""Given list of ints, return list of *indices* of even numbers in list.

For example::

    >>> show_evens([])
    []

    >>> show_evens([2])
    [0]

    >>> show_evens([1, 2, 3, 4])
    [1, 3]

"""


def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    # make new lst to store indices
    # loop, use enumerate to access index, value
    # if value is even, append index to new lst
    # return new lst

    evens = []

    for i, j in enumerate(nums):
        if j % 2 == 0:
            evens.append(i)

    return evens


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EVENLY HANDLED!\n"
