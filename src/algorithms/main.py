from simple_test import *
from markov_test import *

print("Tweet generated with next word chosen by frequence:")
simple_higher_freq()
print("\nTweet generated with next word chosen randomly:")
simple_rand()
print("\nTweet generated with Markov's Chains(state_size = 1):")
markov_chain(1)
print("\nTweet generated with Markov's Chains(state_size = 3):")
markov_chain(3)
print("\nTweet generated with Markov's Chains(state_size = 5):")
markov_chain(5)