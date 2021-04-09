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
    try:
        filename = "dic_{}1.htm".format(i)
        #print(filename)
        f = open(filename, 'r')
        lines = f.readlines()
        count = 0
        for j in range(len(lines)):
            line = lines[j].rstrip()
            #if line.startswith('   <TD><IMG SRC="empty10.gif" WIDTH=60 HEIGHT=10>ex</TD>'):
                #nextline = lines[j+1].rstrip()
                ##print(lines[j+1].rstrip())
                ##final.append(str(count) + ' : ' + eng_word)
                #translation = h.handle(nextline).strip('|\n')
                ##print(translation)
                ##count += 1
                #translist = translation.split(":")
                #if len(translist) == 2:
                    #count += 1
                    ##diction[eng_word] = kir_word 
                    #[kir_word, eng_word] = translist
                    #if eng_word != "":
                        #final.append(eng_word + " : " + kir_word)
                        
            if line.startswith('   <TD><IMG SRC="empty10.gif" WIDTH=60 HEIGHT=10>idiom</TD>'):
                nextline = lines[j+1].rstrip()
                #print(lines[j+1].rstrip())
                #final.append(str(count) + ' : ' + eng_word)
                translation = h.handle(nextline).strip('|\n')
                #print(translation)
                #count += 1
                translist = translation.split(":")
                if len(translist) == 1:
                    count += 1
                    #diction[eng_word] = kir_word 
                    #[kir_word, eng_word] = translist
                    #if eng_word != "":
                        #final.append(eng_word + " : " + kir_word)            
                    final.append(translation)
        #print(translist)
            #if line.startswith("<FONT COLOR=darkred><B>"):
                #count += 1
                #kir_word = h.handle(line).strip('.\n')
                #kir_word = re.sub(r'\d+', '', kir_word)
                #kdef = h.handle(lines[j+1]).strip('.\n')
        print(count)
                
        
            
        
        f.close() 
    except FileNotFoundError:
        pass
        #print("fail")
    
    
    
    #lines = f.readlines()
    #count = 0
    #for j in range(len(lines)):
        #line = lines[j].rstrip()
        #if line.startswith("<FONT COLOR=darkblue SIZE=+1><B>"):
            #final.append(str(count) + ' : ' + eng_word)
            #eng_word = h.handle(line).strip('|\n')
            ##print(eng_word)
            #count = 0
        #if line.startswith("<FONT COLOR=darkred><B>"):
            #count += 1
            #kir_word = h.handle(line).strip('.\n')
            #kir_word = re.sub(r'\d+', '', kir_word)
            #kdef = h.handle(lines[j+1]).strip('.\n')
            
            
  
        
    
    #f.close() 

final = sorted(final)
    
final = '\n\n'.join(final)
w = open("dictionarynumbidiom1.txt", 'w')
j = json.dumps(diction)
w.write(final)
w.close()
#print(diction)
