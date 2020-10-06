import collections
import itertools
import string
import json
import random
import re

def get_eng_phrases(filename):
    dict1 = get_dict('dictionary.txt')
    dict2 = get_dict("new phrases.txt")    
    phrases = []
    f = open(filename, 'r')
    lines = f.read().split('\n\n')
    for j in range(len(lines)):
        line1 = lines[j].split()
        #print(line1)
        line = line1[4:]
        #print(line)
        line = " ".join(line)
        
        if not (line.startswith("(") or line.startswith('<')):
            line = line.split('.')
           
            for sentence in line:
                #print(sentence)
                res = re.split(',|_|-|!', sentence)
                in_dict = False
                for phrase in res:
                    phrase = phrase.strip()
                    phrase = phrase.strip('!?,-')
                    phrase = phrase.strip()
                    try:
                        dict1[phrase]
                        in_dict = True
                    except KeyError:
                        pass
                    try:
                        dict2[phrase]
                        in_dict = True
                    except KeyError:
                        pass  
                    
                    if not in_dict and phrase != '':
                        #print(phrase)
                        phrases.append(phrase)
    #print(phrases)
    set1 = set(phrases)
    print(len(set1))
    f.close()  
    return phrases
    


def collect_nouns(phrases):
    
    
     
    
    

    
    for phrase in phrases:
        t = re.findall('([A-Z][a-z]+)', phrase)
        #print(t)
        print(t, phrase)        
        for word in t:
            
            #phrase = phrase.replace(word, '__noun__')
            n_word = word + '\n'
            
            blacklist_file = open('blacklist.txt', 'r')
            names_file = open('names.txt', 'r')
            blacklist = blacklist_file.read()
            names = names_file.read()  
            blacklist_file.close()
            names_file.close()
            
            if n_word not in blacklist and n_word not in names:
                print(word)
                names_file = open("names.txt", "a")
                blacklist_file = open("blacklist.txt", "a")
                if not input('noun? ') == '':
                    names_file.write(n_word)
                else:
                    blacklist_file.write(n_word)
                    
                blacklist_file.close()
                names_file.close()
                
        #words = phrase.split()
    
        

def strip_word(word):
    word = word.replace('<i>', '')
    word = word.replace('</i>', '')
    word = word.strip('-?!.,') 
    #word = word.strip() 
    return word

def get_dict(filename):
    diction = {}
    alpha = list(string.ascii_lowercase)
    f = open(filename, encoding = "ISO-8859-1")
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


def get_new_eng_pharse():
    eng = get_eng_phrases(filename)[0]
    e.set(eng)
    note.set('')

        
def add_to_file():
    if not len(note.get()) == 0:
        text_file = open("new phrases.txt", "a")
        text_file.write(e.get() + ' : ' + note.get() + "\n\n")
        text_file.close()
        get_new_eng_pharse()
    


filename = "A Beautiful Mind 2001 720p BrRip x264 YIFY-English.srt"

#phrases = get_eng_phrases(filename)
#get_new_eng_pharse(phrases)

from tkinter import *
from tkinter.ttk import *


window = Tk()
e = StringVar()
e.set("")  

note = StringVar()
get_new_eng_pharse()
frame = Frame(window,width=600,height=400)
frame.pack(expand=YES)

label = Label(frame, textvariable=e, width=100)
label.config(font=("Arial", 40))
label.pack()

klabel = Label(frame, textvariable=note, width=100, wraplength=1000)
klabel.config(font=("Arial", 40))
klabel.pack()


label2 = Label(frame, text='In Kiribati this means :', width=100)
label2.config(font=("Arial", 20))
label2.pack()
entry2 = Entry(frame, text=note, width=100)
entry2.pack()

frame2 = Frame(window)
frame2.pack(side='bottom')


clear = Button(frame2, text="Correct", width=20, command=add_to_file)
clear.pack(side='left')

    
window.bind("<Return>", (lambda event: add_to_file()))
    

#new = Button(frame2, text="New Word", width=20, command=lambda: get_random_word(words, e, k, note))
#new.pack(side='left')

#clear2 = Button(frame2, text="Wrong", width=20, command=lambda: add_to_file(False, e, k, note))
#clear2.pack(side='right')

window.mainloop()






#phrases = phrases = get_eng_phrases(filename)
#nouns = collect_nouns(phrases)
#print(nouns)