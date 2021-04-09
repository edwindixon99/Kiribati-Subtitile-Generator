filename = "dictionarynumbidiom1.txt"

lines = open(filename, "r").readlines()

print(lines)

final = []

for i in range(len(lines)):
    line = lines[i].rstrip().strip()
    #print(line)
    
    line = line.split(":")
    
    if len(line) == 2:
        kirs = line[0].split(",")
        engs = line[1].split(",")
        
        for k in kirs:
            for e in engs:
                k = k.strip()
                e = e.strip()
                final.append("{} : {}".format(e, k))
         
    lines[i] = line
    

print(final)
print(lines)
print("ok")