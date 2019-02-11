import random

def punc(s):
        #s = "a,p."
        li = [',','.','!',';']
        for symbol in s:
                if symbol in li:
                        return ''.join(map(str, symbol))
#x = punc(".ap.,")


'''def shuffle_string(string):
        return ''.join(e for e in string if e.isalnum())
print(shuffle_string())'''

def shuffle_string(string):

        st = ''.join(e for e in string if e.isalnum())        
        chars = list(string)
        random.shuffle(chars)
        return ''.join(chars)

def scramble(word):

        if len(word) <= 3:
                return word
        else:        
                first, mid, last = word[0], word[1:-1], word[-1]

                y = str(punc(mid))

                x = first + shuffle_string(mid) + last 

                return x + y

def final(sentence):
        words = sentence.split(' ')
        return ' '.join(map(scramble, words))

#print(final("infosy,s"))


f = open(r"E:\Git Folders\Infosyscc\word_scrambling\scramble.txt", "r")
a = f.read()

scr = final(a)

nf = open(r"E:\Git Folders\Infosyscc\word_scrambling\after_scramble.txt", "w")
nf.write(scr)

'''file_name = input('Enter file name:')
with open(file_name) as f:
        x = f.read()
        print(x)
        word = scramble(x)
new_file=open(r"E:\Git Folders\Infosyscc\word_scrambling\after_scramble", "w")
new_file.write(word)'''


