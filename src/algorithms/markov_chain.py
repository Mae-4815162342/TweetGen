import markovify
import pandas as pd
import sys

def markov_chain(state_size):
    datas = pd.read_csv("./src/data/tweets.csv")
    tweets = '\n'.join(datas[datas.columns[0]])

    model = markovify.Text(tweets, state_size = int(state_size))
    sentence = None
    while not sentence:
        sentence = model.make_short_sentence(10000)
    return sentence

res = markov_chain(sys.argv[1])
res = res[0].upper() + res[1:] + '.'
print("res=",res)