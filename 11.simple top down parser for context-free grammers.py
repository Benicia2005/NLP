import nltk
from nltk import CFG
parser = nltk.ChartParser(CFG.fromstring("S -> 'a' S 'b' | 'a' 'b'"))
for sentence in ["a b", "a a b b", "a b a b"]:
    print("Valid" if list(parser.parse(sentence.split())) else "Invalid")
