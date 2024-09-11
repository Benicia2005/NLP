import nltk
from nltk import word_tokenize
def coherence(text1, text2):
    words1 = set(word_tokenize(text1.lower()))
    words2 = set(word_tokenize(text2.lower()))
    return len(words1 & words2) / len(words1 | words2)
print(coherence("The cat sat on the mat.", "The cat sat on the rug."))
