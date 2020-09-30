import html2text
import re
import string
import json



h = html2text.HTML2Text()
# Ignore converting links from HTML
h.ignore_links = True
h.ignore_emphasis = True


diction = {}

alpha = list(string.ascii_lowercase)

for i in alpha:
    #print(i)
    filename = "find_{}.htm".format(i)
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        if line.startswith("<FONT COLOR=darkblue SIZE=+1><B>"):
            eng_word = h.handle(line).strip('|\n')
            kir_word_final = '*' * 50
            #print(eng_word)
        if line.startswith("<FONT COLOR=darkred><B>"):
            kir_word = h.handle(line).strip('.\n')
            kir_word = re.sub(r'\d+', '', kir_word)
            if len(kir_word) < len(kir_word_final):
                kir_word_final = kir_word
                diction[eng_word] = kir_word   
        
    
    f.close() 
    
    
w = open("dictionary.txt", 'w')
j = json.dumps(diction)
w.write(j)
w.close()
#print(diction)



