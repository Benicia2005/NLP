from nltk.corpus import wordnet
word = 'bank'
synsets = wordnet.synsets(word)
for syn in synsets:
    print(syn.name(), syn.definition())
