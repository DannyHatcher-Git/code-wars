'''Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.'''


def bool_to_word(boolean):
    if boolean is True:
        # Using print only gives a string output. Return makes the result usable elsewhere
        return("Yes")
    else:
        return("No")
