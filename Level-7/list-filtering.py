'''In this kata you will create a function that takes a list of non-negative 
integers and strings and returns a new list with the strings filtered out.
'''

# ..........D solution..........


def filter_list(l):
    new_list = []  # Make new listj
    for x in l:  # Make loop to check through the list
        if type(x) is int:  # Check the type of value
            new_list.append(x)  # If true add to new list
    return new_list  # return list

# ..........S solution..........


def filter_list(l):
    return [x for x in l if type(x) is int]
