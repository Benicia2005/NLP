import nltk
from nltk import CFG
grammar = CFG.fromstring("""
  S -> NP VP
  NP -> 'he' | 'they'
  VP -> 'runs' | 'run'
""")
parser = nltk.ChartParser(grammar)
sentence = "he runs".split()
for tree in parser.parse(sentence):
    print(tree)
