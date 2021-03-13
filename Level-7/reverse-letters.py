'''Given a string str, reverse it omitting all non-alphabetic characters.'''

# ..........D solution..........


def reverse_letter(string):
    return "".join([x for x in string if x.isalpha()][::-1])
    # Join the list to an empty string to make the output a string
    # check each number in the list using a loop
    # if the character is a number keep it if not remove it
    # reverse the list order before joining it with the string

# ..........D solution..........
# Longer version


def reverse_letter(string):
    l1 = []  # Make a list
    for x in string:  # Check all the characters in the list
        if x.isalpha():  # See if the characters are part of the alphabet
            l1.append(x)  # if true add them to the list
    return "".join(l1[::-1])  # combine the reversed list with the empty string
