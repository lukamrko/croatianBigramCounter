from collections import defaultdict

#croatianLetters=['a', 'b', 'c', 'č', 'ć', 'd', 'đ', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 'š', 't', 'u', 'v', 'z', 'ž']
def def_value():
    return 0
croatianBigrams=defaultdict(def_value)

with open('HR_Txt-624.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        word=line.split()[0]
        for index, char in enumerate(word):
            if index+1==len(word):
                break
            bigram=(char+word[index+1]).lower()
            croatianBigrams[bigram]+=1

sortedCroatianBigrams={key: val for key, val in sorted(croatianBigrams.items(), key=lambda ele:ele[1], reverse=True)}

with open('croatianBigrams.txt', 'w', encoding='UTF-8') as f:
    string=""
    for bigram, occurances in sortedCroatianBigrams.items():
        string+=f"{bigram} {occurances}\n"
    f.write(string)