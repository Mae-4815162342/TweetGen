#import pandas as pd
from random import randint, random
import random
import pandas as pd

def creationDic(listString):
    listLen = []
    for string in listString:
        maList = string.split(" ")
        listLen.append(len(maList))
        if (maList[0] in first_word):
            first_word[maList[0]]+=1
        else :
            first_word[maList[0]]=1
        if (maList[-1] in last_word):
            last_word[maList[-1]]+=1
        else :
            last_word[maList[-1]]=1    
        for i in range(len(maList)-1) :
            if ( maList[i] in dict ):
                value= dict[maList[i]]
                if ( maList[i+1] in value):
                    value[maList[i+1]]+=1
                else :
                    value[maList[i+1]]=1
            else :
                value={}
                value[maList[i+1]]=1
                dict[maList[i]]=value
    lenAVG = sum(listLen) / len(listLen)

def wordPred(dic):
    list= []
    for k, v in sorted(dic.items(), key=lambda x: x[1]):
        list.append(k)
    random= randint(int(len(list)*3/4),len(list)-1)
    return list[random]

def most_likely():
    creationDic(tweets)
    word = wordPred(first_word)

    strFinal=word
    for i in range(lenAVG):
        if(i==(lenAVG-1)):
            word= wordPred(last_word) 
            tmpList1=[]
            if word in dict:
                tmpList1=list(dict[word])
            tmpList2=list(last_word)
            intersecList = [value for value in tmpList1 if value in tmpList2]
            if len(intersecList)==0:
                word= wordPred(last_word) 
            else :
                word = random.choice(intersecList)    
        else :    
            if(word in dict) :
                word = wordPred(dict[word])
            else :
                word =  random.choice(list(dict))
                word=wordPred(dict[word])
        strFinal = strFinal + " " + word
    return strFinal

file = pd.read_csv("./src/data/tweets.csv")
tweets = file[file.columns[0]]
    
dict = {}   
first_word = {} 
last_word = {}
lenAVG = 25
strFinal = ""

print(most_likely())
    
                
        
                    
                
        
