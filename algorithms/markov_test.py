import markovify
import pandas as pd

def markov_chain(state_size):
    file = pd.read_csv("./assets/realdonaldtrump.csv")
    tweets = '\n'.join(file['content'])

    model = markovify.Text(tweets, state_size = state_size)
    sentence = None
    while not sentence:
        sentence = model.make_short_sentence(10000)
    print(sentence)