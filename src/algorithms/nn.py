import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
import random as rand
import gensim
import pandas as pd
import numpy as np
import sys

def tokenisation(line):
    #supressing links
    for f in re.findall('http+[^\s]+[\w]+[^\s]', line):
        line = line.replace(f, '')
    #suppressing #
    for f in re.findall('#+[^\s]+[\w]', line):
        line = line.replace(f, '')
    #suppressing special characters and ponctuation
    line = re.sub('[^A-Za-z0-9Ü-ü]+', ' ', line)
    #to lowercase
    return line.lower().split()

def get_data_from_text(text, vectors, vocabulary):
    datas = []
    k = 0
    for tweet in text:
        line = []
        for i in range(0, len(tweet)):
            temp = {}
            word = tweet[i]
            if word in vectors:
                vect = vectors[word]
                temp = {i:vect[i] for i in range(0,len(vect))}
                if i < len(tweet) - 1:
                    if tweet[i+1] in vocabulary:
                        next_word = vocabulary.index(tweet[i+1])
                else:
                    next_word = -1
                temp['next'] = next_word
            line = line + [temp]
        datas = datas + line
        k += 1
    return pd.DataFrame(datas)

def toVec(text):
    model = gensim.models.Word2Vec(
        window=5,
        min_count=1,
        workers=4
    )
    model.build_vocab(text, progress_per=1000)
    model.train(text, total_examples=model.corpus_count, epochs=model.epochs)
    vocabulary = model.wv.index_to_key
    vectors = model.wv
    data = get_data_from_text(text, vectors, vocabulary)
    data.dropna(inplace=True)
    return (vocabulary, vectors, data)

def train_model(data, vect_dim, epochs):
    y = data['next']
    X = data.drop(columns=['next'])

    nn = keras.Sequential([
                layers.Dense(512, activation='relu', input_shape=[vect_dim]),
                layers.Dense(512, activation='relu'),    
                layers.Dense(512, activation='relu'),
                layers.Dense(1),
            ])
    nn.compile(
        optimizer="adam",
        loss="mae",
    )
    X_train, X_valid, y_train, y_valid = train_test_split(X, y)
    history = nn.fit(
        X_train, y_train,
        validation_data=(X_valid, y_valid),
        batch_size=128,
        epochs=epochs
    )
    history_df = pd.DataFrame(history.history)
    history_df['loss'].plot();
    return nn

def embedding_in_nn(epochs):
    print("launch")
    file = pd.read_csv("./src/data/tweets.csv")
    tweets = np.array(file[file.columns[0]])
    tweets_size = len(tweets)
    for i in range(0, tweets_size):
        tweets[i] = tokenisation(tweets[i])
    df = pd.DataFrame(tweets)
    print("data loaded")
    df.replace("", np.nan, inplace=True)
    tweets = df.dropna()
    text = np.array(tweets[0])
    vocabulary, vectors, data = toVec(text)
    print("training model")
    nn = train_model(data, len(vectors[0]), int(epochs))
    index = rand.randint(0, len(vocabulary))
    print("generating")
    phrase = ""
    i = 0
    while (index != -1) & (i < 50):
        word = vocabulary[index]
        phrase = phrase + " " + word
        vect = vectors[word]
        next_vect = np.array([vect[i] for i in range(0,len(vect))])
        next_vect = np.reshape(next_vect, (1,100))
        index = int(nn.predict(next_vect))
        i+=1
    return phrase

res = embedding_in_nn(sys.argv[1])
res = res[1].upper() + res[1:] + '.'
print("res=", res)
