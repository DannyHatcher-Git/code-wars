'''Your task is to make a function that can take any non-negative integer as an 
argument and return it with its digits in descending order. Essentially, rearrange 
the digits to create the highest possible number.
'''
# ..........D First with S help..........


def descending_order(num):
    mylist = []  # Creating an empty list (don't use list as a name)
    for x in str(num):  # Creating a loop to turn num into a list
        mylist.append(x)  # Adding each number from num to mylist
    mylist.sort(reverse=True)  # Sorting my list in reverse order
    # Adding the reversed list as a variable (myReverseString)
    myReverseString = "".join(mylist)
    return int(myReverseString)  # Printing the integer version of the list

# .......... D better solution with S removing loop..........


def descending_order(num):
    # Making the num into a string then list called mylist
    mylist = list(str(num))
    mylist.sort(reverse=True)  # Sorting my list in reverse order
    myReverseList = "".join(mylist)  # Storing the sorted list as myReverseList
    return int(myReverseList)  # Printing myReverseList as integers
