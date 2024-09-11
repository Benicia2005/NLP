from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
sentence = "I went to the bank to fish."
word = "bank"
sense = lesk(word_tokenize(sentence), word)
print(sense, sense.definition())
