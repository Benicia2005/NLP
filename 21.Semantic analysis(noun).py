import nltk
from nltk import pos_tag, word_tokenize
def get_noun_phrases(sentence):
    words = word_tokenize(sentence)
    tagged = pos_tag(words)
    return [word for word, tag in tagged if tag in ('NN', 'NNS')]
print(get_noun_phrases("The quick brown fox jumps over the lazy dog."))
