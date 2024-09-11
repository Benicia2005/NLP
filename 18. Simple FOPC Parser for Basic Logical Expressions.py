import nltk
from nltk import CFG
grammar = CFG.fromstring("""
  S -> 'P' '(' 'x' ')' '&' 'Q' '(' 'x' ')'
""")
parser = nltk.ChartParser(grammar)
expression = "P(x) & Q(x)"
tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
for tree in parser.parse(tokens):
    print(tree)
