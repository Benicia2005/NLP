import nltk
nltk.download('punkt');
nltk.download('averaged_perceptron_tagger')
tokens = nltk.word_tokenize("This is an example.")
tags = nltk.pos_tag(tokens)
print(tags)
