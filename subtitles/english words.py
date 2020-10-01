import enchant
d = enchant.Dict("en_US")


import collections
import re
import sys
import time


# Convert a string to lowercase and split into words (w/o punctuation)
def tokenize(string):
    return re.findall(r'\w+', string.lower())

f = open('The Terminal-Kiribati.srt', 'r')
lines = f.readlines()

dictx = {} 
    # Loop through all lines and words and add n-grams to dict
for line in lines:
    for word in tokenize(line):
        if not word.isdigit() and len(word) > 1:
            try:
                dictx[word] += 1
            except KeyError:
                dictx[word] = 1
                

                
sorteddict = sorted(dictx.items(), key=lambda x: x[1], reverse=True)                
print(dictx)
final = ''
for i in sorteddict:
    final += str(i[0]) + ' : ' + str(i[1]) +'\n'


w = open("all_count.txt", 'w')
w.write(final)
w.close()

    

