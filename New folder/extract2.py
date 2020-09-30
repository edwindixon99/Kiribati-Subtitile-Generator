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
eng_word = ''
for i in alpha:
    #print(i)
    filename = "find_{}.htm".format(i)
    f = open(filename, 'r')
    lines = f.readlines()
    count = 0
    for j in range(len(lines)):
        line = lines[j].rstrip()
        if line.startswith("<FONT COLOR=darkblue SIZE=+1><B>"):
            final.append(str(count) + ' : ' + eng_word)
            eng_word = h.handle(line).strip('|\n')
            #print(eng_word)
            count = 0
        if line.startswith("<FONT COLOR=darkred><B>"):
            count += 1
            #kir_word = h.handle(line).strip('.\n')
            #kir_word = re.sub(r'\d+', '', kir_word)
            #kdef = h.handle(lines[j+1]).strip('.\n')
            
            
  
        
    
    f.close() 

final = sorted(final)
    
final = '\n\n'.join(final)
w = open("dictionarynumb.txt", 'w')
j = json.dumps(diction)
w.write(final)
w.close()
#print(diction)



