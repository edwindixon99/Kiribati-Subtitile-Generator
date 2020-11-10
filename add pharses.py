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
from nltk.corpus import wordnet as wn

filename = "WALL E.srt"

contractions = { 
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so is",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have"
}


they_pronouns = {'their','him', 'its', 'her', 'his', 'she', 'herself', 'they', 'he', 'itself', 'himself', 'them', 'it'}

we_pronouns = {'we','our','us'}

you_pronouns = {'you','your''ya''yourself'}

i_pronouns = {'myself', 'me', 'my', 'i'}


    



    #return pronouns


    
        

def strip_word(word):
    word = word.replace('<i>', '')
    word = word.replace('</i>', '')
    word = word.strip('-?!.,') 
    #word = word.strip() 
    return word

def get_dict(filename):
    diction = {}
    alpha = list(string.ascii_lowercase)
    f = open(filename, 'r')
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



def get_initial_eng_phrases(filename):
    dict1 = get_dict('dictionary.txt')
    dict2 = get_dict("new phrases.txt") 
    dictbl = get_dict("bl phrases.txt") 
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
                res = re.split('[?.,_-]', sentence)
                in_dict = False
                for phrase in res:
                    phrase = phrase.strip()
                    phrase = phrase.strip('!?,-')
                    phrase = phrase.strip()
                    #phrase = remove_pronouns_and_nouns(phrase)
                    

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
                    try:
                        dictbl[phrase]
                        in_dict = True
                    except KeyError:
                        pass                     
                    
                    if not in_dict and phrase != '' and len(phrase.split()) >= 1:
                        
                        #print(phrase)
                        phrases.append(phrase)
    #print(len(phrases))
    #set1 = set(phrases)
    #print(len(set1))
    f.close()  
    return phrases


def collect_nouns(filename, conjuction=False):
    phrases = get_initial_eng_phrases(filename)
    #print(phrases)
    Tokens = []
    for Sent in phrases:
        Tokens.append(nltk.word_tokenize(Sent)) 
    Words_List = [nltk.pos_tag(Token) for Token in Tokens]
    print(Words_List)
    Nouns = set()
    pronouns = set('i')
    conjuction_set = set()
    num = set()
    for List in Words_List:
        for Word in List:
            #print(List)
            if re.match('CC', Word[1]):
                conjuction_set.add(Word[0].lower())

            if re.match('PRP', Word[1]):
                #print('ok')
                pronouns.add(Word[0].lower())            
            
            elif re.match('NUM', Word[1]):
                num.add(Word[0].lower())
                
            elif Word[1] == 'NN' or Word[1] == 'NNS':
                #print('ol')
                Nouns.add(Word[0])
            
                
                        
    #print(pronouns)
    
    #Names = set()
    #for Nouns in Nouns_List:
        ##if Nouns[0].isupper() and wordnet.synsets(Nouns):
            #Names.add(Nouns)
    
    if conjuction:
        return conjuction_set
    return Nouns, pronouns


nouns, pronouns = collect_nouns(filename)

def remove_pronouns_and_nouns(phrase, dict1, dict2, dictbl, phrases):
    phrase = phrase.split()
    r = False
    noun_counter = collections.defaultdict(list)
    pronoun_counter = collections.defaultdict(list)
    n_counter = 0
    pr_counter = 0
    for i in range(len(phrase)):
        word = phrase[i]
        conjuct = False
        try:
            words = contractions[word].split()
            word = words[0]
            conjuct = True
            #print(phrase)
        except KeyError:
            pass
            
        #if word in i_pronouns:
            #word = '{me}'
        #elif word in you_pronouns:
            #word = '{you}'
        #elif word in we_pronouns:
            #word = '{our}'
        #elif word in they_pronouns:
            #word = '{they}' 
        add_to_list = False
        
            
        if word in pronouns:
            pronoun_counter[word].append(pr_counter)
            pr_counter += 1
            subbed_word = word
            word = "__PRONOUN!!!___"
            add_to_list = True
            
            
        elif word in nouns:
            noun_counter[word].append(n_counter)
            n_counter += 1
            subbed_word = word
            word = "__NOUN!!!___"
            add_to_list = True
            
        if conjuct:
            words[0] = word
            word = ' '.join(words)
            r = True
            
                
        phrase[i] = word
        in_dict = False
        if add_to_list:
            try:
                dict1[subbed_word]
                in_dict = True
            except KeyError:
                pass
            try:
                dict2[subbed_word]
                in_dict = True
            except KeyError:
                pass    
            try:
                dictbl[subbed_word]
                in_dict = True
            except KeyError:
                pass             
            if not in_dict and subbed_word != '':
                
                phrases.append(subbed_word)
    phrase = ' '.join(phrase)
    #if r:
        #print(phrase)
    return phrase, phrases
    
    

    

    
    
    
def get_eng_phrases(filename):
    conjuncted = collect_nouns(filename, True)
    conjuncts = '[?!.,_-]'
    #print(conjuncted)
    if len(conjuncted) > 0:
        con = '|'.join(conjuncted)
        #print(con)
        conjuncts = conjuncts + '|' + con
    #print(conjuncted)       
    dict1 = get_dict('dictionary.txt')
    dict2 = get_dict("new phrases.txt")  
    dictbl = get_dict("bl phrases.txt")  
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
                
                res = re.split(conjuncts, sentence)
                
                in_dict = False
                for phrase in res:
                    phrase = phrase.strip()
                    phrase = phrase.strip('!?,-')
                    phrase = phrase.strip()
                    #phrase = remove_pronouns_and_nouns(phrase)
                    

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
                    try:
                        dictbl[phrase]
                        in_dict = True
                    except KeyError:
                        pass                     
                    
                    if not in_dict and phrase != '' and len(phrase.split()) > 0:
                        new_phrase, phrases = remove_pronouns_and_nouns(phrase, dict1, dict2, dictbl, phrases)
                        if new_phrase == phrase:
                            phrases.append(phrase)
                        else:
                            in_dict2 = False
                            try:
                                dict1[new_phrase]
                                in_dict2 = True
                            except KeyError:
                                pass
                            try:
                                dict2[new_phrase]
                                in_dict2 = True
                            except KeyError:
                                pass 
                            try:
                                dictbl[new_phrase]
                                in_dict2 = True
                            except KeyError:
                                pass                             
                            if not in_dict2:
                                print(new_phrase)
                                phrases.append(new_phrase)
                                
    #print(len(phrases))
    set1 = set(phrases)
    #print(len(set1))
    #print(set1)
    f.close()  
    return phrases



def get_new_eng_pharse():
    eng = get_eng_phrases(filename)[0]
    e.set(eng)
    note.set('')
    
def print_new_eng_pharse2():
    print(len(set(get_eng_phrases(filename))))
    print(len(set(get_initial_eng_phrases(filename))))


        
def add_to_file():
    if not len(note.get()) == 0:
        text_file = open("new phrases.txt", "a")
        text_file.write(e.get() + ' : ' + note.get() + "\n\n")
        text_file.close()
        get_new_eng_pharse()
        
        
def add_to_blacklist():
    #if not len(note.get()) == 0:
    text_file = open("bl phrases.txt", "a")
    text_file.write(e.get() + ' : ' + 'nothin' + "\n\n")
    text_file.close()
    get_new_eng_pharse()    


#filename = "Twins.1988.1080p.BluRay.x264-[YTS.MX]-English.srt"

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

label = Label(frame, textvariable=e, width=100, wraplength=1000)
label.config(font=("Arial", 60))
label.pack()

klabel = Label(frame, textvariable=note, width=100, wraplength=1000)
klabel.config(font=("Arial", 60))
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

clear = Button(frame2, text="Blacklist", width=10, command=add_to_blacklist)
clear.pack(side='right')

    
window.bind("<Return>", (lambda event: add_to_file()))
    

#new = Button(frame2, text="New Word", width=20, command=lambda: get_random_word(words, e, k, note))
#new.pack(side='left')

#clear2 = Button(frame2, text="Wrong", width=20, command=lambda: add_to_file(False, e, k, note))
#clear2.pack(side='right')

window.mainloop()






#phrases = phrases = get_eng_phrases(filename)
#nouns = collect_nouns(filename)
#print(nouns)

print_new_eng_pharse2()