'''You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is positive.'''

import math  # so the sqrt function can be used
sq = 120
print(sq**0.5)

# .......... Su Solution ..........


def find_next_square(sq):
    sqrt = sq ** (0.5)  # get square root
    # if the modulo of the result after casting to int is 0, then it's an int.
    if (sqrt % (int(sqrt)) == 0):
        return (sqrt + 1) ** 2  # return the next square
    return -1  # otherwise -1:


def find_next_square(sq):
    if sq % sq**0.5 == 0:  # seeing if the square root in an integer
        return ((sq**0.5)+1)**2  # if it is return the next square
    else:
        return: -1  # if not


def find_next_square(sq):
    return [-1, int(sq**.5+1)**2][math.sqrt(sq).is_integer()]
    # first [] are the 2 answers
    # second [] is the question ( is the sqrt of the number an integer)
