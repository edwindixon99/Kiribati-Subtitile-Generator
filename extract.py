import html2text
import re
import string
import json



h = html2text.HTML2Text()
# Ignore converting links from HTML
h.ignore_links = True
h.ignore_emphasis = True


diction = {}
final = []
alpha = list(string.ascii_lowercase)

for i in alpha:
    #print(i)
    filename = "find_{}.htm".format(i)
    f = open(filename, 'r')
    lines = f.readlines()
    for j in range(len(lines)):
        line = lines[j].rstrip()
        if line.startswith("<FONT COLOR=darkblue SIZE=+1><B>"):
            eng_word = h.handle(line).strip('|\n')
            #print(eng_word)
        if line.startswith("<FONT COLOR=darkred><B>"):
            kir_word = h.handle(line).strip('.\n')
            kir_word = re.sub(r'\d+', '', kir_word)
            kdef = h.handle(lines[j+1]).strip('.\n')
            final.append(eng_word + ' : ' + kir_word + ' : ' + kdef)
            
  
        
    
    f.close() 
    
final = '\n\n'.join(final)
w = open("dictionary.txt", 'w')
j = json.dumps(diction)
w.write(final)
w.close()
#print(diction)



