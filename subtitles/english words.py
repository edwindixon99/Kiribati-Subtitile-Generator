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
        if d.check(word) and not word.isdigit():
            try:
                dictx[word] += 1
            except KeyError:
                dictx[word] = 1
                
                
print(dictx)


#def print_most_frequent(ngrams, num=30):
    #for n in sorted(ngrams):
        #print('----- {} most common {}-grams -----'.format(num, n))
        #for gram, count in ngrams[n].most_common(num):
            #print('{0}: {1}'.format(' '.join(gram), count))
        #print('')


start_time = time.time()

    

