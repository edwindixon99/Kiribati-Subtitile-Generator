import string
import json




diction = {}
final = []
alpha = list(string.ascii_lowercase)
f = open("dictionary.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.rstrip().split(':')
    if len(line) >= 2:
    
        
        #print(line)
        eng_word = line[0].strip()
        kir_word = line[1].strip()
        diction[eng_word] = kir_word
        
f.close() 
    
w = open("dictionary5.txt", 'w')
j = json.dumps(diction)
w.write(j)
w.close()
#print(diction)



