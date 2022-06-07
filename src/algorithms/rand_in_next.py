#rand_in_next choses the next word randomly in the list of the next words
#the tweet is built from a random approach

import pandas as pd
import random
from ponctuation import ponctuation

def get_text_table():
    datas = pd.read_csv("./src/data/cleaned.csv")
    return (' '.join(datas[datas.columns[1]])).split()

def get_next_word_naive_impl(word, all_words, used_words, lim_per_word):
    words_next = []
    next_word = False
    for w in all_words:
        if next_word:
            if next_word not in words_next:
                words_next += [w]
            next_word = False
        if w == word:
            next_word = True
    if len(words_next) == 0:
        return "_"
    if len(words_next) == 1:
        return words_next[0]
    rand = random.randint(0, len(words_next) - 1)
    if words_next[rand] not in used_words:
        return words_next[rand]
    i = 0
    while (used_words[words_next[rand]] >= lim_per_word) & (i < 5):
        rand = random.randint(0, len(words_next) - 1)
        i+=1
        if words_next[rand] not in used_words:
            return words_next[rand]
    return words_next[rand]

def rand_in_next():
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

res = rand_in_next()
res = res[1].upper() + res[1:] + '.'
print("res=",ponctuation(res))