import collections
import itertools
import string
import json
import random



def strip_word(word):
    word = word.replace('<i>', '')
    word = word.replace('</i>', '')
    word = word.strip('-?!.,') 
    #word = word.strip() 
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
            kir_word = ':'.join(line[1:])
            diction[eng_word] = kir_word
            
    f.close()   
    return diction


def get_random_word(words, e, k, note):
    eng, kir = random.choice(list(words.items()))
    e.set(eng)
    k.set(kir)
    note.set('')

        
def add_to_file(correct, e, k, note):
    text_file = open("rand words.txt", "a")
    if correct:
        text_file.write('YES : ' + e.get() + ' : ' + k.get() + "\n" + "note :" + note.get() +"\n\n")
    else:
        text_file.write('NO : ' + e.get() + ' : ' + k.get() + "\n" + "note :" + note.get() +"\n")
    text_file.close()
    get_random_word(words, e, k, note)



words = get_dict()

#translate_file("Jaws-English.srt", "Jaws")
from tkinter import *
from tkinter.ttk import *


window = Tk()
e = StringVar()
e.set("")  
k = StringVar()
k.set('')
note = StringVar()
get_random_word(words, e, k, note)
frame = Frame(window,width=600,height=400)
frame.pack(expand=YES)

label = Label(frame, textvariable=e, width=100)
label.config(font=("Arial", 40))
label.pack()

klabel = Label(frame, textvariable=k, width=100, wraplength=1000)
klabel.config(font=("Arial", 40))
klabel.pack()


label2 = Label(frame, text='note :', width=100)
label2.config(font=("Arial", 20))
label2.pack()
entry2 = Entry(frame, text=note, width=100)
entry2.pack()

frame2 = Frame(window)
frame2.pack(side='bottom')


##clear = Button(frame2, text="Enter", width=100, command=lambda: translate_file_attempt(title3, filename.get(), film_name.get()))
##clear.pack(side='left')

clear = Button(frame2, text="Correct", width=20, command=lambda: add_to_file(True, e, k, note))
clear.pack(side='left')

new = Button(frame2, text="New Word", width=20, command=lambda: get_random_word(words, e, k, note))
new.pack(side='left')

clear2 = Button(frame2, text="Wrong", width=20, command=lambda: add_to_file(False, e, k, note))
clear2.pack(side='right')

window.mainloop()
