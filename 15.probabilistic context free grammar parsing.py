import nltk
from nltk import PCFG

# Define a simple PCFG
grammar = PCFG.fromstring("""
  S -> 'a' B [0.3]
  S -> 'a' 'b' [0.7]
  B -> 'a' [1.0]
""")

parser = nltk.ViterbiParser(grammar)
sentence = "a b".split()

for tree in parser.parse(sentence):
    print(tree)
