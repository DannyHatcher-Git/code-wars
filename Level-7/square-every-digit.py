'''Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer'''

# ..........N Solution..........


def square_digits(num):
    ret = ""  # A blank list to put the answers in
    for x in str(num):  # A loop to search through the (num) list
        # Add after = to the ret list (answers list). str because ret is a string list
        ret += str(int(x)**2)
    return int(ret)

# ..........V Solution..........


def square_digits(x):
    l1 = []  # Create list
    for i in str(x):  # Started a search loop
        l1.append(str(int(i)*int(i)))  # Add the squared number to l1 list
    le = len(l1)  # Length of the new list - called it le
    m = 1  # Making m = 1
    z = l1[0]  # z = first number in the list (string)
    while m < le:  # Is the length of le (l1) smaller than 1
        # replace z varialbe with z(first number) +l1[m](second number and growing because m changes)
        z = z+l1[m]
        m = m+1    # adding 1 to the m variable to prevenet an infinate loop
    return int(z)  # retrun the list of z as an integer

# ..........V Solution D adjust..........
# took out le and used len(l1) in the while loop


def square_digits(x):
    l1 = []  # Create list
    for i in str(x):  # Started a search loop
        l1.append(str(int(i)*int(i)))  # Add the squared number to l1 list
    m = 1  # Making m = 1
    z = l1[0]  # z = first number in the list (string)
    while m < len(l1):  # Is the length of le (l1) smaller than 1
        # replace z varialbe with z(first number) +l1[m](second number and growing because m changes)
        z = z+l1[m]
        m = m+1    # adding 1 to the m variable to prevenet an infinate loop
    return int(z)  # retrun the list of z as an integer
