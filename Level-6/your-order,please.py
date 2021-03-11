'''Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.'''

# .......... S solution..........

s = "is2 Thi1s T4est 3a"


def order(s):
    s = s.split()  # Turning the string into a list
    # making a new list full of 0's (the amount is the same as s numbers)
    d = [0]*len(s)
    for i in s:  # Start loop looking for each word is the s list
        for j in i:  # start loop looking for each character in each word
            if j.isdigit():  # if the character is a digit move on if a character go to next character
                # d (reference d list)[indexing the number as an integer - 1 for correct location]
                d[int(j)-1] = i
                # make all that equal i (the word in the sentence)
                break  # Come out of the character check loop and search another word
    return ' '.join(d)  # Make the list a string


print(order(s))

# .......... Random solution (learning lambda)..........
'''
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
  # First bit joins the list to a string for output
  # making the string alist (words.split())
  # 

def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
  # First bit joins the list to a string for output
  # making the string alist (words.split())
'''
print(sorted(order(s,)))
