'''In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.

If you can, try writing it in one line of code.'''


# .......... D First solution..........
'''
two lists of 3 numbers
always positive
'''




from numpy import prod # Improt the prod function from the numpy library
def find_difference(a, b):
    # multiply all (a,b) list numbers together. Subratct the products. Absolute the results
    return abs(prod(a)-prod(b))


# .......... Alternative..........
# It is a comment so saving the file doesn't move the import around
'''
import numpy as np # Different way to import nympy (refer as any variable)
def find_difference(a,b):
    return abs(prod(a)-prod(b))
'''
