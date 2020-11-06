import collections
import itertools
import string
import json


def translate(words, num):
    words = list(itertools.islice(words, 0, num))
    while num > 1:
        sub_words = list(itertools.islice(words, 0, num))
        #print(words)
        num_words = ' '.join(sub_words)
        try:
            if dictionp[num_words]:
                try:
                    if words[2] in ['it', 'he', 'she', 'that']:
                        return num + 1, dictionp[num_words]
                except IndexError:
                    pass
            return num, dictionp[num_words]
        except KeyError:
            pass
        try:
            return num, diction[num_words]
        except KeyError:
            num -= 1 
            
            
    word1 = words[0]
    try:
        if dictionp[word1]:
            try:
                if words[1] in ['it', 'he', 'she', 'that']:
                    return num + 1, dictionp[word1]
            except IndexError:
                pass
        return num, dictionp[word1]
    except KeyError:
        pass    
    try:
        
        #print(diction[word1])
        return 1, diction[word1]
    except KeyError:
        try:
            wordsingle = remove_plural(word1)
            return 1, diction[wordsingle]
        except KeyError:        
            pass
    return 1, word1      


def pre_adjust(word):
    f = word[0]
    r = word[len(word) -1]
    tup = [False, False]
    if f in ['-']:
        word = word.replace(f, '')
        tup[0] = f
    if r in ['?', '!', ',', '.']:
        word = word.replace(r, '')
        tup[1] = r
    return tup, word

def post_adjust(tup, word):
    f = tup[0]
    r = tup[1]
    if f:
        word =  f + word
    if r:
        word = word + r
    
    return word    
    
    
#def strip_word(word):
    #word = word.replace('<i>', '')
    #word = word.replace('</i>', '')
    #word = word.strip('-?!.,') 
    ##word = word.strip() 
    #return word

def remove_plural(word):
    word = word.rstrip('s')
    word = word.rstrip("'")
    return word

def get_dict():
    diction = {}
    alpha = list(string.ascii_lowercase)
    f = open("dictionary.txt", encoding = "ISO-8859-1")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip().split(':')
        if len(line) >= 2:
        
            
            #print(line)
            eng_word = line[0].strip()
            kir_word = line[1].strip()
            diction[eng_word] = kir_word
            
    f.close()   
    return diction


diction = get_dict()


dictionp = {"where is": "e ngaa","who is": "antai", "how's": "e uara", "how is": "e uara", "why is": "Bukin tera bwa e", "what's up with" : "??????????"}


def translate_file_attempt(title3, filename, film):
    try:
        translate_file(filename, film)
        title3.set("Finsihed!!")
    except:
        title3.set("Something went wrong!?! Maybe wrong filename")
        

    
def translate_file(filename, film):
    words = collections.deque()
    f_r = collections.deque()
    f = open(filename, 'r')
    lines = f.read().lower().split('\n\n')
    for j in range(len(lines)):
        line1 = lines[j].split()
        #print(line1)
        line = line1[4:]
        #print(line)
        skips = 1
        i = 0
        for word in line:
            #print(line)
            #print(word, i)
            f_r_tup, word1 = pre_adjust(word)
            words.append(word1)
            f_r.append(f_r_tup)
        while 0 < len(words):
            if skips > 1:
                line[i] = ''
                skips -= 1
                words.popleft()
                f_r.popleft()
            else:
                num = len(words)
                skips, word = translate(words, num)
                tup = f_r.popleft()
                word = post_adjust(tup, word)
                #print(word)
                line[i] = word
                words.popleft()
                #f_r.popleft()
            i += 1
            
        #print(line)
        try:
            start = line1[0] + '\n' + line1[1] + ' '+ line1[2] + ' ' + line1[3] + '\n' 
            if '' in line:
                line.remove('')            
            line = ' '.join(line)
            line = start + line
            #print(line)
            lines[j] = line
        except IndexError:
            pass
    string = '\n\n'.join(lines)
    
    #print(string)
    f.close()   
    
    
    file = "{}-Kiribati.srt".format(film)
    w = open(file, 'w')
    w.write(string)
    w.close()


if __name__ == '__main__':
    #translate_file("Twins.1988.1080p.BluRay.x264-[YTS.MX]-English.srt", "king")
    from tkinter import *
    from tkinter.ttk import *  
    window = Tk()
    frame = Frame(window,width=600,height=400)
    frame.pack(expand=YES)
    filename = StringVar()
    title = StringVar()
    title.set("Enter english subtitle filename:")
    filename.set("")
    label = Label(frame, textvariable=title, width=100)
    label.pack()
    entry = Entry(frame, textvariable=filename, width=100)
    entry.pack()
    
    film_name = StringVar()
    title2 = StringVar()
    title2.set("Enter film name")
    film_name.set("")
    label2 = Label(frame, textvariable=title2, width=100)
    label2.pack()
    entry2 = Entry(frame, textvariable=film_name, width=100)
    entry2.pack()
    
    title3 = StringVar()
    title3.set("")
    label3 = Label(frame, textvariable=title3, width=100)
    label3.pack()
    
    
    clear = Button(frame, text="Enter", width=100, command=lambda: translate_file_attempt(title3, filename.get(), film_name.get()))
    clear.pack()
    
    window.mainloop()
