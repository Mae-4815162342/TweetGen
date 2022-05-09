#import pandas as pd
from random import randint, random
import random


def creationDic(listString):
    listLen = []
    #ajouter un compteur de longueur
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
                #aug score
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
    print(strFinal)


#file = pd.read_csv("./src/data/tweets.csv")
#tweets = '\n'.join(file['content'])
tweets =  ["They also found stories that quoted spider experts tended to be more accurate than those that quoted medical experts of pest control specialists who don’t receive the same level of training","Negative media portrayals of spiders snakes and other animals that many people tend to dislike hurt efforts to conserve species that play an important role in the ecosystem the study authors say","Media coverage of human encounters with spiders is rife with misinformation, according to a study by more than 60 scientists around the world","They compiled a database of more than 5,300 news articles from 81 countries about these encounters, and found 47% had factual errors and 43% were sensationalistic","The research, posted as a pre-print and currently under peer review, is the product of a massive effort by more than 60 scientists around the world led by ecologist Stefano Mammola of the Italian National Research Council. They compiled a database of 5,348 news articles about human-spider encounters from 81 countries and written in 41 languages","Mammola and his colleagues analyzed each article in the database, recording whether they contained factual errors about spiders and whether they used sensationalistic language and/or images, such as the words “killer,” “terror” and “nightmare,” to describe the encounters. They found the articles were rife with misinformation: nearly half (47%) of the total news articles contained factual errors, and 43% were sensationalistic","Study co-author Catherine Scott, a postdoctoral fellow at the Lyman Entomological Museum at McGill University in Canada, agrees. “People love to hate spiders. They occupy this place in our minds, and I think it has something to do with how different they are from us. They’re almost alien … they have eight legs, they have lots of eyes, they move in an erratic way,” they explained, noting that even some entomologists, scientists who study insects (which have six legs), are afraid of the eight-legged animals","Scott said they empathize with people who fear spiders. As a child and teenager, they were also arachnophobic, to the point that they couldn’t be in the same room with a spider. But their fear turned to curiosity when they had the opportunity to research black widow spider communication as an undergraduate student. After observing the spiders’ sophisticated behaviors and communication systems, Scott “very rapidly switched from being arachnophobic to arachnophilic [spider-loving].” And there is a lot to love about these animals: spiders fill an important ecological role as predators of household and agricultural pests. A 2017 study estimated that the world’s spiders collectively devour 400 million to 800 million metric tons of insects and other tiny prey each year. Today, Scott is a spider scientist who focuses on combating misinformation about these creatures. “It’s a constant frustration for me as an arachnologist to see sensationalized media stories, to see information being spread on the internet that is false,"," they said. Scott even started a Twitter project called #RecluseOrNot to correct misinformation about brown recluse spiders on social media.","A key finding of this new study is that, although factual errors and sensationalism in news media about spiders is widespread, such misinformation was less common when reporters sought commentary from spider experts. This was not the case when reporters consulted pest control or medical experts, who do not receive the same level of training as spider specialists do,","For Mammola, this finding demonstrates how important it is that journalists seek out the right type of expert to comment on scientific stories, not just any expert. Scott said it’s an encouraging finding, because “it means there is an easy fix.” The research group is currently composing guidelines for journalists reporting on spiders. The group also intends to compile a database of spider experts available to speak with the media to make it easier for journalists to find high-quality sources","Because they were a global team, Mammola and his colleagues were also able to construct a network of how information — and misinformation — about spiders flows around the world. They saw how even very specific, local stories could spread worldwide. “A single spider event occurring in a small town in Michigan can be taken up by the global press, which for me was quite amazing,” he said. One reason this happens? “If something is particularly stupid,” Mammola said, recounting a viral story of a man being bitten on the genitals by a spider as an example.","Emily Geest, an ecologist and postdoctoral fellow at Oklahoma State University who was not involved in the study, said she was particularly impressed by its worldwide coverage. “To see those patterns, globally, is really intense,” she said.","Geest has previously published research on the moral depictions of animals in comic books. She said she knows how media portrayals can fan the flames of fear, particularly for animals such as snakes and spiders that people are predisposed to dislike.","These negative media portrayals have real-world repercussions for animals, particularly on conservation efforts. “The ultimate problem is, I think, that we will spend less and less resources to preserve spider species, just because we fear them and we have this societal and political perception about them,” Mammola said.","Geest said she’s also concerned about the effect of misinformation on the public perception of conservation funding, which could disadvantage species that are ecologically important but not beloved. “When you see organizations like zoos and aquariums putting money into trying conserve species that aren’t well-liked, there is this disconnect where the public ","doesn’t see the value in them, she said. And if they don’t see the value in them, they’re not going to support policies around it"]
    
dict = {}   
first_word = {} 
last_word = {}
lenAVG = 7
strFinal = ""

most_likely()

    
                
        
                    
                
        