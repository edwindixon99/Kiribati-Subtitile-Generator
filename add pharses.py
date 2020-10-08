import collections
import itertools
import string
import json
import random
import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.corpus import wordnet



they_pronouns = {'their','him', 'its', 'her', 'his', 'she', 'herself', 'they', 'he', 'itself', 'himself', 'them', 'it'}

we_pronouns = {'we','our','us'}

you_pronouns = {'you','your''ya''yourself'}

i_pronouns = {'myself', 'me', 'my', 'i'}

def remove_pronouns(phrase):
    phrase = phrase.split()
    for i in range(len(phrase)):
        if phrase[i] in i_pronouns:
            phrase[i] = '{me}'
        elif phrase[i] in you_pronouns:
            phrase[i] = '{you}'
        elif phrase[i] in we_pronouns:
            phrase[i] = '{our}'
        elif phrase[i] in they_pronouns:
            phrase[i] = '{they}' 
    return ' '.join(phrase)
    
    

def get_eng_phrases(filename):
    dict1 = get_dict('dictionary.txt')
    dict2 = get_dict("new phrases.txt")  
    phrases = []
    f = open(filename, 'r')
    lines = f.read().lower().split('\n\n')
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
                    phrase = remove_pronouns(phrase)
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
                        print(phrase)
                        phrases.append(phrase)
    #print(len(phrases))
    set1 = set(phrases)
    print(len(set1))
    f.close()  
    return phrases
    
#from nltk.corpus import wordnet as wn

#def collect_nouns(filename):
    #phrases = get_eng_phrases(filename)
    #Tokens = []
    #for Sent in phrases:
        #Tokens.append(nltk.word_tokenize(Sent)) 
    #Words_List = [nltk.pos_tag(Token) for Token in Tokens]
    ##print(Words_List)
    #Nouns_List = []
    #pronouns = set()
    
    #for List in Words_List:
        #for Word in List:
            ##if Word[0] == 'Dance':
                ##print(Word)
            ##if Word[1] == 'NN':
                ##Nouns_List.append(Word[0])
            #if re.match('PRP', Word[1]):
                #pronouns.add(Word[0].lower())
    #print(pronouns)
    
    #Names = set()
    #for Nouns in Nouns_List:
        #if Nouns[0].isupper() and wordnet.synsets(Nouns):
            #Names.add(Nouns)
    
    #print (Names)  
    #for i in Names:
        #print(i)
    #return Names
    return pronouns


    
        

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
#nouns = collect_nouns(filename)
#print(nouns)