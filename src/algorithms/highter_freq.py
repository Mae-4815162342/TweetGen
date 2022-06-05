import pandas as pd

#higher_freq will evaluate from a word which word appears most afterwards in the dataset,
#therefore building a tweet from a statistical approach
def read_file():
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None
    return pd.read_csv("./src/data/tweets.csv")


def get_text_from_data(file):
    return file['content']



def clean_line(text):
    res = text.split("http://")
    res = res[0].split("https://")
    res = res[0].split("@ ")
    res = [c for c in res[0] if (c != '"') & (c != "'") & (c != "-")]
    return "".join(res)


def clean_tab(tab):
    res = []
    for text in tab:
        res.append(clean_line(text))
    return res

def get_clean_text():
    file = read_file()
    tab = get_text_from_data(file)
    return clean_tab(tab)


def get_next_word_naive_impl(word, text, used_words, lim_per_word):
    all_words_in_tab = [t.split(" ") for t in text]
    all_words = []
    words_next = {}
    next_word = False
    for tab in all_words_in_tab:
        all_words.extend(tab)
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
    text = pd.read_csv("./src/data/tweets.csv")
    current_word = "Make"
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
    
print(highter_freq())