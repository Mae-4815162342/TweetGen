from sklearn.feature_extraction.text import CountVectorizer
from tensorflow import keras

import numpy

import torch
import torch.nn as nn
import torch.optim as optim

def log_loss(prediction, expected):
    if expected == 1:
        return -numpy.log(prediction)
    return -numpy.log(1 - prediction)

def vectorisation(text, min_df):
    vect = CountVectorized(min_df = min_df)
    vect.feat(text)
    return vect.vocabulary_

class Discriminator(nn.Module):
    error = 0
    def __init__(self, txt_dim):
        super().__init__()
        self.disc = nn.Sequential(
            nn.Linear(txt_dim, 128),
            nn.LinearRelU(0.1),
            #only one output for true or false
            nn.Linear(128, 1)
            #to make sure the last output is between 0 and 1
            nn.Sigmoid()
        )


    def forward(self, sentence):
        #vectorise sentence

        #feat into model
         return self.disc(sentence)


class Generator(nn.Module):
    #random initialisation
    def __init__(self, z_dim, txt_dim, min_df):
        super().__init__()
        self.gen = nn.Sequential(
            nn.Linear(z_dim, 128),
            nn.LinearRelU(0.1),
            nn.Linear(128, txt_dim)

        )

    def forward(self, sentence):
        #vectorise sentence

        #feat into model
         return self.disc(sentence)


device = "cuda" if torch.cuda.is_available() else "cpu"
lr = 3e-4
z_dim = 64
txt_dim = 50
batch_size = 32
num_epochs = 50
min_df = 3

disc = Discriminator(txt_dim).to(device)
gen = Generator(z_dim, txt_dim, min_df).to(device)
fixed_noise = torch.randn((batch_size, z_dim)).to(device)
transforms = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5,),(0.5,))]
)
#datas
dataset = 

opt_disc = optim.Adam(disc.parameters(), lr= lr)
opt_gen = optim.Adam(gen.parameters(), lr = lr)
criterion = nn.BCEloss()
fakedata = #
truedata = #

for epoch in range(num_epochs):
    
    # train discriminator 
    
def gans(nbOfRound):
    #get datas
        #vocabulary
    #initialise weight randomly in nn


    for in in range(0, nbOfRound):
        #

        #train generator

    #return generator.generate



print(gans())