import collections
import itertools
import string
import json
import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
import copy



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


pronoun_subs = {"you":"your", "me":"my"}



def sub_nouns(words, num):
    phrase = ' '.join(words)
    Tokens = []
    n_words = copy.deepcopy(words)
    
    Tokens.append(nltk.word_tokenize(phrase)) 
    
    #Tokens = [list(n_words).remove('')]
    #print(Tokens)
    Words_List = [nltk.pos_tag(Token) for Token in Tokens]
    
    changed = {'noun':[], 'pronoun':[], 'number':[]}
    
    i = 0
    pr = "__PRONOUN!!!___"
    noun = "__NOUN!!!___"
    number = "__NUM!!!___"
    tok_count = 0
    for List in Words_List:
        for Word in List:
            #print(List)
            
            #print(n_words)
            #print(i)
            if re.match('PRP', Word[1]) or Word[0] == 'i':
                #print('ok')
                changed['pronoun'].append(Word[0])
                n_words[i] = pr
                         
            
            elif re.match('NUM', Word[1]):
                changed['num'].append(Word[0])
                n_words[i] = num
                
            elif Word[1] == 'NN' or Word[1] == 'NNS':
                changed['noun'].append(Word[0])
                n_words[i] = noun
            #print(i)
            #print(n_words)
            if not (Word[1] == '``' or Word[1] == "''" or Word[1] =='.' or Word[1] == ":" or Word[1] == "," or "'" in Word[0]):
                i += 1
            try:
                #print(List[tok_count+1])
                if Word[0] == 'can' and List[tok_count+1][0] == 'not':
                    i -= 1
            except:
                pass
            try:
                #print(List[tok_count+1])
                if Word[0] == 'wan' and List[tok_count+1][0] == 'na':
                    i -= 1
            except:
                pass
            try:
                #print(List[tok_count+1])
                if Word[0] == 'got' and List[tok_count+1][0] == 'ta':
                    i -= 1
            except:
                pass  
            try:
                #print(List[tok_count+1])
                if Word[0] == 'gon' and List[tok_count+1][0] == 'na':
                    i -= 1
            except:
                pass               
            
            tok_count += 1
    return list(itertools.islice(n_words, 0, num)), changed

                
def resub_nouns(num_A_words, changed):
    #print()
    pr = "__PRONOUN!!!___"
    noun = "__NOUN!!!___"
    number = "__NUM!!!___"    
    pr_count = 0
    noun_count = 0
    num_count = 0
    
    num_A_words = diction[num_A_words]
    #print(num_A_words)
    #print(changed)
    words = num_A_words.split()
    for i in range(len(words)):
        word = words[i]
        itis = False
        #print(word)
        if word == pr:
            word = changed['pronoun'][pr_count]
            #if i > 0:
                #try:
                    #word = pronoun_subs[word]
                #except KeyError:
                    #pass
            pr_count += 1
            itis = True
        elif word == noun:
            word = changed['noun'][noun_count]
            noun_count += 1            
            itis = True
        elif word == number:
            word = changed['num'][num_count]
            num_count += 1            
            itis = True
        if itis:
            #print('ok')
            #print(changed[word])
            new_word = translate([word], 1)[1]
            #print(new_word)
            #print(words[i])
            words[i] = new_word
    #print(' '.join(words))
    return ' '.join(words)
            
            

#nouns, pronouns = collect_nouns(filename)

 

def translate(words, num):
    
    if len(words) == 1:        
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
    
    else: 
        words_alter, changed = sub_nouns(words, num)
        words = list(itertools.islice(words, 0, num))
        
        while num > 1:
            sub_words = list(itertools.islice(words, 0, num))
            sub_A_words = list(itertools.islice(words_alter, 0, num))
            
            num_words = ' '.join(sub_words)
            num_A_words = ' '.join(sub_A_words)
            #print(num_words)
            #print(num_A_words)
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
                if dictionp[num_A_words]:
                    try:
                        if words[2] in ['it', 'he', 'she', 'that']:
                            return num + 1, dictionp[num_A_words]
                    except IndexError:
                        pass
                return num, dictionp[num_A_words]
            
            except KeyError:
                pass
            #############################################################
            try:
                return num, diction[num_words]
            except KeyError:
                pass
            try:
                
                if diction[num_A_words]:
                    #print(num_A_words)
                    num_A_words = resub_nouns(num_A_words, changed)
                    #print()
                    #print(num_A_words)
                return num, num_A_words
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
    
    
def strip_word(word):
    word = word.replace('<i>', '')
    word = word.replace('</i>', '')
    return word


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
        
def contraction(word, words, f_r_tup, f_r):
    try:
        con = contractions[word].split()
        con = post_adjust(f_r_tup, ' '.join(con)).split()
        for i in con:
            tup, i = pre_adjust(i)
            words.append(i)
            f_r.append(tup)
        return words, f_r
        
    except KeyError:
        words.append(word)
        f_r.append(f_r_tup)
        return words, f_r
    
def translate_file(filename, film):
    words = collections.deque()
    f_r = collections.deque()
    f = open(filename, 'r')
    lines = f.read().lower().split('\n\n')
    for j in range(len(lines)):
        line1 = lines[j].split()
        #print(line1[0])
        line = line1[4:]
        #print(line)
        skips = 1
        i = 0
        index = 0
        for word in line:
            
            word = strip_word(word)
            f_r_tup, word1 = pre_adjust(word)
            
            words, f_r = contraction(word1, words, f_r_tup, f_r)
        #print(list(words))
        #print(line)
        #print(words)
        line = list(words)
        #print(line)
            
        while 0 < len(words):
            if skips > 1:
                #print(words, skips)
                if i >= len(line):
                    #print(line[i])
                    line.append('')
                else:
                    #print(line[i])
                    line[i] = ''
                skips -= 1
                words.popleft()
                f_r.popleft()
            else:
                num = len(words)
                
                skips, word = translate(words, num)
                #print(skips, word)
                #print(f_r)
                tup = f_r.popleft()
                word = post_adjust(tup, word)
                #print(word)
                if i >= len(line):
                    line.append(word)
                else:
                    line[i] = word
                words.popleft()
                #f_r.popleft()
            i += 1
        line = line[:i]
            
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

translate_file("Meet.The.Parents.2000.BluRay.720p.x264.DTS-MySiLU.srt", "meet the parents")

#if __name__ == '__main__':
    ##translate_file("Twins.1988.1080p.BluRay.x264-[YTS.MX]-English.srt", "king")
    #from tkinter import *
    #from tkinter.ttk import *  
    #window = Tk()
    #frame = Frame(window,width=600,height=400)
    #frame.pack(expand=YES)
    #filename = StringVar()
    #title = StringVar()
    #title.set("Enter english subtitle filename:")
    #filename.set("")
    #label = Label(frame, textvariable=title, width=100)
    #label.pack()
    #entry = Entry(frame, textvariable=filename, width=100)
    #entry.pack()
    
    #film_name = StringVar()
    #title2 = StringVar()
    #title2.set("Enter film name")
    #film_name.set("")
    #label2 = Label(frame, textvariable=title2, width=100)
    #label2.pack()
    #entry2 = Entry(frame, textvariable=film_name, width=100)
    #entry2.pack()
    
    #title3 = StringVar()
    #title3.set("")
    #label3 = Label(frame, textvariable=title3, width=100)
    #label3.pack()
    
    
    #clear = Button(frame, text="Enter", width=100, command=lambda: translate_file_attempt(title3, filename.get(), film_name.get()))
    #clear.pack()
    
    #window.mainloop()
