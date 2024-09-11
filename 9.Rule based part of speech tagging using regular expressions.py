import nltk
patterns = [(r'.*ing$', 'VBG'), (r'.*ed$', 'VBD')]
tagger = nltk.RegexpTagger(patterns)
tokens = nltk.word_tokenize("He is swimming.")
print(tagger.tag(tokens))
