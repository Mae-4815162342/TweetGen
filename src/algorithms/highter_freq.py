import pandas as pd
import numpy as np
import random 
from ponctuation import ponctuation

#higher_freq will evaluate from a word which word appears most afterwards in the dataset,
#therefore building a tweet from a statistical approach

#returns a table with the text
def get_text_table():
    datas = pd.read_csv("./src/data/cleaned.csv")
    return (' '.join(datas[datas.columns[1]])).split()

def get_next_word_naive_impl(word, all_words, used_words, lim_per_word):
    words_next = {}
    next_word = False
    for w in all_words:
        if next_word:
            if w in words_next:
                words_next[w]  = 1 + words_next[w]
            else:
                words_next[w] = 1
            next_word = False
        if w == word:
            next_word = True
    val_temp = 0
    res = "_"
    for w in words_next:
        if(words_next[w] > val_temp):
            if w in used_words:
                if used_words[w] > lim_per_word:
                    continue
            val_temp = words_next[w]
            res = w
    return res


def highter_freq():
    text = get_text_table()
    rand = random.randint(0, len(text) - 1)
    current_word = text[rand]
    res = ""
    i = 0
    used_words = {}
    lim_per_word = 1
    while (len(current_word) > 0) & (current_word != "_") & (i < 50):
        res += " " + current_word
        i += 1
        if current_word in used_words:
            used_words[current_word] += 1
        else:
            used_words[current_word] = 1
        current_word = get_next_word_naive_impl(current_word, text, used_words, lim_per_word)
    return res
    
res = highter_freq()
res = res[0].upper() + res[1:] + '.'
print("res=",ponctuation(res))