'''Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).'''


# ..........D solution..........
def odd_or_even(arr):
    if sum(arr) % 2 == 0:  # Adds all the numbers in the arrayj
        return("even")  # If the check is true
    else:
        return("odd")  # If the check is false
# .......... D second solution ..........


def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

# .......... S solution..........


def odd_or_even(arr):
    # the & 1 is looking for the last binary of the sum(arr) if it is a 1 it is odd etc.
    return ['even', 'odd'][sum(arr) & 1]
