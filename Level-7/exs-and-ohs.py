''' Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. The string can contain any char.'''

# .......... S solution ..........


def xo(s):
    s = s.lower()  # Making sure it is case sensitive (making things lower)
    # count x's and o's and see if they are =
    return s.count('x') == s.count('o')

# .......... D failed attempt (needs capitilzation test)..........


def xo(s):
    x_list = []
    o_list = []
    for y in s:
        if y == "x":
            x_list.append(y)
        elif y == "o":
            o_list.append(y)
    if len(x_list) == len(o_list):
        return True
    else:
        return False
