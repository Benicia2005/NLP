import nltk
nltk.download('punkt')
nltk.download('average_perceptron_tagger')
text="The cats are playing in the garden."
tokens=nltk.word_tokenize(text)
tagged=nltk.pos_tag(tokens)
print(tagged)
