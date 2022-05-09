import markovify
import pandas as pd
import sys

def markov_chain(state_size):
    file = pd.read_csv("./src/data/tweets.csv")
    tweets = '\n'.join(file['content'])

    model = markovify.Text(tweets, state_size = int(state_size))
    sentence = None
    while not sentence:
        sentence = model.make_short_sentence(10000)
    return sentence

print(markov_chain(sys.argv[1]))