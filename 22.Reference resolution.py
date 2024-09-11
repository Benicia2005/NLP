import nltk
from nltk import word_tokenize, pos_tag
def find_pronouns(text):
    words = word_tokenize(text)
    tagged = pos_tag(words)
    return [word for word, tag in tagged if tag in ('PRP', 'PRP$')]
print(find_pronouns("He went to the store. She bought some milk."))
