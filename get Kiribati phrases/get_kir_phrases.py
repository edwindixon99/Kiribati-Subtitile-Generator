import re

filename = "dictionarynumb.txt"

lines = open(filename, "r").readlines()

#print(lines)

final = []
c = 0

bl = ["", " ", "etc.", "etc", "...", "etc.)", "etc. (for things)"]
for i in range(len(lines)):
    line = lines[i].rstrip().strip()
    #print(line)
    
    line = line.split(":")
    
    if len(line) == 2:
        c += 1
        #kirs = line[0].split(",")
        #engs = line[1].split(",")
        resk = re.split('[?!,]', line[1])
        rese = re.split('[?!,]', line[0])
        
        #rese = re.split('[?!,]', line[1])
        #resk = re.split('[?!,]', line[0])         
        print(rese)
        if (len(rese) > 1) and len(rese) == len(resk):
            for p in range(len(rese)):
                #print(rese[p])
                #print()
                ef, kf = rese[p].strip(), resk[p].strip()
                if ef not in bl and kf not in bl:
                    final.append("{} : {}".format(ef, kf))                    
                #final.append("{} : {}".format(rese[p].strip(), resk[p].strip()))
        elif len(rese) > 1 or len(resk) > 1:
            for k1 in resk:
                for e1 in rese:
                    ef, kf = e1.strip(), k1.strip()
                    if ef not in bl and kf not in bl:
                        final.append("{} : {}".format(ef, kf))                        
                    #final.append("{} : {}".format(e1.strip(), k1.strip()))
        
        else:
                          
            ef, kf = rese[0].strip(), resk[0].strip()
            
            if ef not in bl and kf not in bl:
                final.append("{} : {}".format(ef, kf))              
            
        #if ef not in bl and kf not in bl:
            #final.append("{} : {}".format(ef, kf))        
        
        #for k in kirs:
            #for e in engs:
                #k = k.strip()
                #e = e.strip()
                
                #rese = re.split('[?!,]', e)
                #resk = re.split('[?!,]', k)
                
                #if (len(rese) > 1) and len(rese) == len(resk):
                    #for p in range(len(rese)):
                        ##print(rese[p])
                        ##print()
                        #ef, kf = rese[p].strip(), resk[p].strip()
                        ##final.append("{} : {}".format(rese[p].strip(), resk[p].strip()))
                #elif len(rese) > 1 or len(resk) > 1:
                    #for k1 in rese:
                        #for e1 in rese:
                            #ef, kf = e1.strip(), k1.strip()
                            ##final.append("{} : {}".format(e1.strip(), k1.strip()))
                
                #else:
                    #ef, kf = e, k
                    
                #if ef not in bl and kf not in bl:
                    #final.append("{} : {}".format(ef, kf))
                
         
    lines[i] = line
#print(c)    
#print(final)
#print(lines)
#print("ok")




final = '\n\n'.join(final)
w = open("dictionaryeng-kir34t43.txt", 'w')
w.write(final)
w.close()