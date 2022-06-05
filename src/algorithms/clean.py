from asyncio.windows_events import NULL
import pandas as pd
import numpy as np
import re
import sys

def regex(line):
    #supressing links
    for f in re.findall('http+[^\s]+[\w]+[^\s]', line):
        line = line.replace(f, '')
    #suppressing #
    for f in re.findall('#+[^\s]+[\w]', line):
        line = line.replace(f, '')
    #suppressing special characters and ponctuation
    line = re.sub('[^A-Za-z0-9]+', ' ', line)
    #to lowercase
    return line.lower()

def clean(name):
    datas = pd.read_csv("./src/data/tweets.csv")
    table = np.array(datas[datas.columns[0]])
    for i in range(0, (table.size -1)):
        table[i] = regex(table[i])
    #removing empty data
    df = pd.DataFrame(table)
    df.replace("", np.nan, inplace=True)
    df_new = df.dropna()
    df_new.to_csv('./src/data/cleaned.csv')
    return name

print(clean(sys.argv[1]))