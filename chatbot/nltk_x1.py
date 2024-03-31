import nltk  
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer 
import numpy as np 

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    """
    examples  
    sentence = ["hello", "how", "are", "you"]
    words = ["hello", "how", "are", "you"]
    bag = [1, 1, 1, 1]


    """        

    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for index, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[index] =    1.0


    return bag

# sentence = ["hello", "how", "are", "you"]
# words = ["helo", "how", "nothing", "you"]
# bag = bag_of_words(sentence, words)
# actual bag of words example 

# print(bag)




# a= "How long does shipping take?"
# print(a)
# a=tokenize(a)
# print(a)

# words = ["organize", "organizes", "organizing"]
# stemmed_words = [stem(w) for w in words]
# print(stemmed_words)
