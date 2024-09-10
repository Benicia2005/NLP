import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download necessary NLTK data files
nltk.download('wordnet')
nltk.download('omw-1.4')

# Sample words for morphological analysis
words = ["running", "jumps", "easily", "fairly", "geese", "better", "studies", "studying"]

# 1. Stemming
print("Stemming:")
porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")

for word in words:
    print(f"{word}:")
    print(f"  Porter Stemmer: {porter.stem(word)}")
    print(f"  Lancaster Stemmer: {lancaster.stem(word)}")
    print(f"  Snowball Stemmer: {snowball.stem(word)}")

# 2. Lemmatization
print("\nLemmatization:")
lemmatizer = WordNetLemmatizer()

for word in words:
    # Lemmatize without specifying the POS tag
    lemma = lemmatizer.lemmatize(word)
    print(f"{word} -> Lemma: {lemma}")

# Lemmatizing with POS tagging
print("\nLemmatization with POS tagging:")
for word in words:
    lemma_noun = lemmatizer.lemmatize(word, pos=wordnet.NOUN)
    lemma_verb = lemmatizer.lemmatize(word, pos=wordnet.VERB)
    print(f"{word} -> Lemma (Noun): {lemma_noun}, Lemma (Verb): {lemma_verb}")
