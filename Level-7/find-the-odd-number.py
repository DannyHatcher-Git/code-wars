'''You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)'''


def stray(arr):
    for x in arr:  # open loop to check the list
        if arr.count(x) == 1:  # check if the count of the number is 1
            return x  # When true
