from collections import defaultdict
import string
import re

def def_value():
    return 0

croatianBigrams=defaultdict(def_value)
filename='HR_Txt-624.txt'

def ReadAll():
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            word=line.split()[0]
            for index, char in enumerate(word):
                if index+1==len(word):
                    break
                bigram=(char+word[index+1]).lower()
                croatianBigrams[bigram]+=1

def LimitedRead():
    alphabet=list(string.ascii_lowercase)
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            word=line.split()[0]
            for index, char in enumerate(word):
                if index+1==len(word):
                    break
                nextChar=word[index+1]
                char=OptimizeDiacrtic(char)
                nextChar=OptimizeDiacrtic(nextChar)
                if(char in alphabet and nextChar in alphabet):
                    bigram=char+nextChar
                    croatianBigrams[bigram]+=1

def SortAndWrite(file):
    sortedCroatianBigrams={key: val for key, val in sorted(croatianBigrams.items(), key=lambda ele:ele[1], reverse=True)}

    with open(file, 'w', encoding='UTF-8') as f:
        string=""
        for bigram, occurances in sortedCroatianBigrams.items():
            string+=f"{bigram} {occurances}\n"
        f.write(string)

def OptimizeDiacrtic(char):
    if(char=='č' or char=='ć'):
        return 'c'
    if(char=='š'):
        return 's'
    if(char=='đ'):
        return 'd'
    if(char=='ž'):
        return 'z'
    return char.lower()

def DeleteDuplicateCharacters():
    keysToRemove=[]
    for key in croatianBigrams:
        if key[0]==key[1]:
            keysToRemove.append(key)
    for key in keysToRemove:
        croatianBigrams.pop(key)

def GenerateAll():
    ReadAll()
    SortAndWrite('croatianBigramsAll.txt')

def GenerateLimited():
    LimitedRead()
    DeleteDuplicateCharacters()
    SortAndWrite('croatianBigramsLimited.txt')

def Main():
    print('1 - Generate with every possible character\n2 - Generate with limited character')
    option=input()
    if option=='1':
        GenerateAll()
    if option=='2':
        GenerateLimited()

if __name__=="__main__":
    Main()