''' Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.'''

# ..........D solution..........


def friend(x):
    new_list = []  # new list
    for i in x:  # start loop to search the list x
        if len(i) == 4:  # check length of name is = 4
            new_list.append(i)  # if name length = 4 add to list
    return new_list  # return the list

# ..........S solution..........


def friend(x):


return [i for i in x if len(i) == 4]
