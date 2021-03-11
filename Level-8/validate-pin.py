'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
'''


# ..........D First solution..........

def validate_pin(pin):
    if pin.isdigit():  # Check to see if the pin is all digits
        if len(pin) == 4 or len(pin) == 6:  # Check to see if the length is 4 or 6
            return True  # If it is 4 or 6
        else:
            return False  # If it is not 4 or 6
    else:
        return False  # If they are not all digits

# ..........V solution with aid..........
# Can probably get rid of the >= 0 check as .isdigit will return false


def validate_pin(x):
    if x.isdigit() == True:  # Checking for all digits in the pin
        if int(x) >= 0:  # is the x integer bigger than or equal to 0
            if len(x) == 4:  # is the length of x = to 4
                return True  # if length = 4 put true
            elif len(x) == 6:  # is length of x = 6
                return True  # if length is =6 put true
            else:
                return False  # if length is not 4 or 6 put false
        else:
            return False  # if length is not bigger or = to 0 put false
    else:
        return False  # if the pin is not all digits put false
