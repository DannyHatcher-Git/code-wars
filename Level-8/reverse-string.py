# Complete the solution so that it reverses the string passed into it.

# .......... S help solution ..........
def solution(string):
    # index from start to end (::) -1 go from the end backwards 1
    return string[::-1]

# ..........D exceptiong ..........


def solution(string):
    return string[5:-6:-1]  # Will work for strings shorter than 5
