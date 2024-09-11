import nltk
nltk.download('treebank')
train_data = nltk.corpus.treebank.tagged_sents()[:100]
tagger = nltk.DefaultTagger('NN')
tokens = nltk.word_tokenize("The quick fox.")
print(tagger.tag(tokens))
