import json
from nltk_x1 import tokenize
from nltk_x1 import stem
from nltk_x1 import bag_of_words


# Corrected file path
file_path_intents = '/workspaces/Hollow-Technique-Purple/chatbot/intents.json'

with open(file_path_intents, 'r') as f:
    intents = json.load(f)

# print(intents)

all_words = []
tags = []
xy = []
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?', '!', ',', '.']

all_words = [stem(w) for w in all_words if w not in ignore_words]
# print(all_words)
all_words = sorted(set(all_words))
tags = sorted(set(tags))
print(tags)

X_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)
    