'''Complete the function that accepts a string parameter,
and reverses each word in the string. All spaces in the string should be retained.'''

# When printing make sure you reference the def and the (in brackets)

text = "The quick brown fox jumps over the lazy dog."

# .......... D solution


def reverse_words(text):
    # making string into list (split makes it a list automatically)
    my_list = list(text.split(" "))
    answer_list = []  # making blank list
    for x in my_list:  # creating loop to check list
        answer_list.append(x[::-1])  # adding reversed word to list
    return " ".join(answer_list)


# .......... S S Solution ..........
def reverse_words(text):
    return " ".join(x[::-1]for x in text.split(" "))
