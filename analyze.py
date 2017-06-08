import nltk
from nltk import word_tokenize

tokenized_texts = []
for text in texts:
    tokenized_texts.append(word_tokenize(text))

for tokenized_text in tokenized_texts:
    print('=====')
    print(len(tokenized_text))
    print(tokenized_text[0:20])
