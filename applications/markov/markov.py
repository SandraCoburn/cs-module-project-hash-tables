import random
import numpy as np

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here


def markov(l):
    cache = {}
    # #print(l)
    ind_words = l.split()
    #print(ind_words)
    for i in range(len(ind_words) - 1):
        yield (ind_words[i], ind_words[i + 1])
        pairs = markov(ind_words)
        for word1, word2 in pairs:
            if word1 in cache.keys():
                cache[word1].append(word2)
            else:
                cache[word1] = [word2]
    #Randonly pick the firt word
    first_word = np.random.choice(ind_words)
    while first_word.islower():
        chain = [first_word]
        print(chain)
        #Initialize the number of stimulated words
        n_words = 10
        for i in range(n_words):
            chain.append(np.random.choice(cache[chain[-1]]))
            #Join returns the chain as a string
    print(" ".join(chain))
    # for i in range(len(ind_words)-1):
    #     if ind_words[i] in cache:
    #         cache[ind_words[i]].append(ind_words[i+1])
    #     else:
    #         cache[ind_words[i]] = [ind_words[i+1]]
    # return cache  


# TODO: construct 5 random sentences
def random_sent(text):
    pass
    # cache = markov(text)
    # random_w = random.choice(text.split())
    # stop_word = ['.', '?', '!','."']

    # curr = cache[random_w]
    # sentence = random_w
    # while curr[-1] not in stop_word or curr[-2:] not in stop_word:
    #     print(sentence = sentence + " " + curr)

markov(words)
random_sent(words)