import numpy as np # pip install numpy
import nltk # pip install nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()


# h e l l o  b r o, hello bhai, bhai hello, hello brother, hey

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return Stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,words):
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words),dtype= np.float32)

    for idx, w in enumerate(words):
        if w in sentence_word:
            bag[idx] = 1

    return bag
    


