import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
porter_stemmer = PorterStemmer()
words = ["running", "jumps", "easily", "fairly", "studies", "studying", "cats", "caresses", "ponies", "happiness"]
stemmed_words = [porter_stemmer.stem(word) for word in words]
for original, stemmed in zip(words, stemmed_words):
    print(f"Original: {original}, Stemmed: {stemmed}")
