import nltk
from nltk import CFG

# Define the grammar correctly without semicolons
grammar = CFG.fromstring("""
  S -> 'the' N | 'a' N
  N -> 'cat' | 'dog'
""")

parser = nltk.ChartParser(grammar)

for tree in parser.parse("the cat".split()):
    print(tree)
