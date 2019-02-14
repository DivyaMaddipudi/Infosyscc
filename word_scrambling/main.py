import random
import re
 

def scramble_word(word):
    if len(word) <= 3:
        return word

    first, *mid, last = word[0] + word[1:-1] + word[-1]
    random.shuffle(mid)
    return first + "".join(mid) + last

def scramble_text(text):
    for i in text:
        return re.sub(r"\w+", lambda match: scramble_word(match.group()),text)

def scramble_file(input_filename):
    with open(input_filename) as input_file:
        text = input_file.read()

    scrambled_text = scramble_text(text)
    f = open(r"E:\Git Folders\Infosyscc\word_scrambling\after_scramble.txt", "w")
    f.write(scrambled_text)

x = input("enter input file name:")

scramble_file(x)